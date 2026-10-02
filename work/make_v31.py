#!/usr/bin/env python3
"""Generate work/estimator_v31.py = V29 (instrumented copy) + a GRU corrector step per layer.
The corrector's parameters are read from gru_model.json next to the estimator (pure stdlib json
+ flopscope arrays; no numpy). If the file is missing the estimator is V29 verbatim."""
import ast, re
src = open('/home/user/arc-whitebox/work/estimator_v29_feat.py').read()

def rep(old, new, count=1):
    global src
    assert src.count(old) == count, (src.count(old), old[:80])
    src = src.replace(old, new)

# 1. no numpy: the hooks keep fnp references (all recorded arrays are fresh per layer)
rep('''FEAT = []  # feature dump: per-layer dict of per-neuron numpy arrays (feat_dump harness)
import numpy as _np
def _f(x):
    return _np.asarray(x, dtype=_np.float32).copy()
''', '''FEAT = []  # per-layer dict of per-neuron fnp arrays consumed by the GRU corrector step (V31)
import json as _json


def _f(x):
    return x


GRU_FEATS = ["mu_pre", "var", "alpha", "phi", "Phi", "D3", "g4row", "K2v", "K3v", "K4v", "k22row", "k21row",
             "k21col", "e_b", "w1", "w2", "s3c", "g_post", "coff_sq", "coff_sum", "d21_abs", "d21_sq",
             "d21T_abs", "d21_colsum", "d21_rowsum", "pred"]
GRU_OFF = _os.environ.get("V31_GRU_OFF", "0") == "1"


def _load_gru(ctx):
    """gru_model.json next to this file (or in ctx.submission_dir): weights as nested lists."""
    cands = []
    sd = getattr(ctx, "submission_dir", None)
    if sd:
        cands.append(_os.path.join(str(sd), "gru_model.json"))
    cands.append(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "gru_model.json"))
    for p in cands:
        if _os.path.exists(p):
            with open(p) as fh:
                d = _json.load(fh)
            f32 = fnp.float32
            g = {k: fnp.asarray(d[k], dtype=f32) for k in ("bih", "bhh", "b1", "b2", "mu_f", "sd_f")}
            g["H"] = int(d["H"]); g["sig_mu"] = float(d["sig_mu"]); g["feats"] = list(d["feats"])
            assert g["feats"] == GRU_FEATS, "feature list mismatch"
            # transposed (in, out) layouts built host-side in pure Python, uploaded once
            for k in ("Wih", "Whh", "W1", "W2"):
                g[k + "T"] = fnp.asarray([list(col) for col in zip(*d[k])], dtype=f32)
            return g
    return None
''')

# 2. load in setup
rep('''    def setup(self, ctx: SetupContext) -> None:
        self._setup_rng = fnp.random.default_rng(ctx.seed)
''', '''    def setup(self, ctx: SetupContext) -> None:
        self._setup_rng = fnp.random.default_rng(ctx.seed)
        self._gru = None if GRU_OFF else _load_gru(ctx)
''')

# 3. the GRU step method, inserted before _dslices
rep('''    def _dslices(self, A_st, P_st, Z_st, L_st, w2b_list, s_list, e_list,''',
'''    def _gru_step(self, li, fd, W, gst, n):
        """One GRU corrector step on layer li's per-neuron features fd (dict of (n,) fnp arrays).
        gst holds u (normalized mean correction), q (aux) and h (hidden) of the previous layer."""
        g = self._gru
        f32 = fnp.float32
        def zeros():
            return fnp.zeros(n, dtype=f32)   # a fresh array per use: never the same operand twice in one op
        var = fd["var"]
        sig = fnp.sqrt(fnp.maximum(var, 1e-12))
        cols = []
        for k in GRU_FEATS:
            v = fd.get(k)
            cols.append(zeros() if v is None else v)
        cols.append(sig * fd["phi"])                                              # chi
        cols.append(fd["D3"] / (sig * sig * sig) if fd.get("D3") is not None else zeros())   # skew
        cols.append(fd["g4row"] / (var * var) if fd.get("g4row") is not None else zeros())  # kurt (g4row / sig^4)
        lam = fd.get("lam")
        cols.append(zeros() + float(lam) if lam is not None else zeros())
        if gst["u"] is None:
            cols.append(zeros())
            cols.append(zeros())
        else:
            cols.append(fd["Phi"] * (W @ gst["u"]))      # transported previous correction
            cols.append((W * W) @ gst["q"])              # transported auxiliary state
        cols.append(zeros() + float(li / 15.0))
        inp = fnp.stack(cols, axis=1)                                             # (n, F+3)
        nf = g["mu_f"].shape[1]
        X = (inp[:, :nf] - g["mu_f"][li][None, :]) / g["sd_f"][li][None, :]
        inp = fnp.concatenate([X, inp[:, nf:]], axis=1)
        H = g["H"]
        h_prev = gst["h"] if gst["h"] is not None else fnp.zeros((n, H), dtype=f32)
        gi = inp @ g["WihT"] + g["bih"][None, :]
        gh = h_prev @ g["WhhT"] + g["bhh"][None, :]
        r = 0.5 + 0.5 * fnp.tanh(0.5 * (gi[:, :H] + gh[:, :H]))                   # sigmoid via tanh
        z = 0.5 + 0.5 * fnp.tanh(0.5 * (gi[:, H:2 * H] + gh[:, H:2 * H]))
        nn_ = fnp.tanh(gi[:, 2 * H:] + r * gh[:, 2 * H:])
        h = (1.0 - z) * nn_ + z * h_prev
        a = h @ g["W1T"] + g["b1"][None, :]
        a = 0.5 * a * (1.0 + fnp.tanh(0.7978845608028654 * (a + 0.044715 * a * a * a)))   # tanh-GELU
        y = a @ g["W2T"] + g["b2"][None, :]
        gst["u"] = y[:, 0]
        gst["q"] = y[:, 1]
        gst["h"] = h

    def _dslices(self, A_st, P_st, Z_st, L_st, w2b_list, s_list, e_list,''')

# 4. state init at predict start
rep('''        rows = []

        w1_prev = None  # wick w(1) of the previous layer, folded into WD
''', '''        rows = []
        FEAT.clear()
        gst = {"u": None, "q": None, "h": None}

        w1_prev = None  # wick w(1) of the previous layer, folded into WD
''')

# 5. final layer: GRU step + correction
rep('''            if last:
                FEAT[-1].update(pred=_f(pk1v))
            if last:
                rows.append(pk1v if delta is None else pk1v + delta)
                break
''', '''            if last:
                FEAT[-1].update(pred=_f(pk1v))
            if last:
                if self._gru is not None:
                    self._gru_step(li, FEAT[-1], W, gst, n)
                    pk1v = pk1v + gst["u"] * float(self._gru["sig_mu"])
                rows.append(pk1v if delta is None else pk1v + delta)
                break
''')

# 6. end of a non-final layer: GRU step
rep('''            if riders:
                K4_vec = (K4v * float(st["k4_c4"])
                          + (K22 @ ones_n) * float(st["k4_c22"])) * float(n * st["P2"])
            rows.append(mu)
''', '''            if riders:
                K4_vec = (K4v * float(st["k4_c4"])
                          + (K22 @ ones_n) * float(st["k4_c22"])) * float(n * st["P2"])
            if self._gru is not None:
                self._gru_step(li, FEAT[-1], W, gst, n)
            rows.append(mu)
''')
assert "import numpy" not in src and "_np." not in src
ast.parse(src)
open('/home/user/arc-whitebox/work/estimator_v31.py', 'w').write(src)
print("wrote estimator_v31.py", len(src.splitlines()), "lines")
