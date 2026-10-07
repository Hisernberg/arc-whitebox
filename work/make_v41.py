#!/usr/bin/env python3
"""V41: replace the GRU corrector by the per-layer local-error corrector (LT): at every layer an MLP
predicts the layer's local mean error from that layer's per-neuron features, and the correction is
carried forward through the weights, c_l = Phi_l * (W_l c_{l-1}) + g_l. Reuses the V31 corrector hook
(the model dict carries kind="lt"). Usage: make_v41.py <src.py> <lt.json> <dst.py>"""
import re, sys
src, ltj, dst = sys.argv[1:4]
s = open(src).read()
lt = open(ltj).read().strip()
# 1. embedded model: the LT JSON replaces the GRU JSON literal
m = re.search(r'^GRU_JSON = r""".*?"""', s, flags=re.M)
assert m, "GRU_JSON literal not found"
s = s[:m.start()] + 'GRU_JSON = r"""' + lt + '"""' + s[m.end():]
# 2. loader dispatch + LT feature list
a = "def _gru_from_dict(d):\n"
assert s.count(a) == 1
s = s.replace(a, '''LT_FE = ["mu_pre", "var", "alpha", "phi", "Phi", "D3", "g4row", "d21_abs", "d21_sq", "d21T_abs", "d21_colsum",
         "d21_rowsum", "coff_sq", "coff_sum", "pred", "K2v", "K3v", "K4v", "k22row", "k21row", "k21col", "e_b", "w1",
         "w2", "s3c", "g_post"]


def _lt_from_dict(d):
    """V41: per-layer local-error corrector parameters (MLP F -> H -> H -> H -> 1, exact GELU)."""
    f32 = fnp.float32
    assert int(d["F"]) == len(LT_FE) + 1, "LT feature count mismatch"
    g = {"kind": "lt", "sig_mu": 1.0}
    g["mu"] = fnp.asarray(d["mu"], dtype=f32); g["sd"] = fnp.asarray(d["sd"], dtype=f32)
    g["es"] = [float(x) for x in d["es"]]
    g["W1T"] = fnp.asarray(d["W1T"], dtype=f32); g["b1L"] = fnp.asarray(d["b1L"], dtype=f32)
    g["W2T"] = fnp.asarray(d["W2T"], dtype=f32); g["b2"] = fnp.asarray(d["b2"], dtype=f32)
    g["W3T"] = fnp.asarray(d["W3T"], dtype=f32); g["b3"] = fnp.asarray(d["b3"], dtype=f32)
    g["w4"] = fnp.asarray(d["w4"], dtype=f32); g["b4"] = float(d["b4"])
    return g


def _gru_from_dict(d):
            if d.get("kind") == "lt":
                return _lt_from_dict(d)
''')
# 3. step dispatch + LT step
a = '''    def _gru_step1(self, g, li, fd, W, gst, n):
        """One GRU corrector step on layer li's per-neuron features fd (dict of (n,) fnp arrays)."""
'''
assert s.count(a) == 1
s = s.replace(a, '''    def _lt_step1(self, g, li, fd, W, gst, n):
        """V41: local-error MLP on layer li's features; gst["u"] = Phi * (W @ u_prev) + g_li (activation units)."""
        f32 = fnp.float32
        cols = []
        for k in LT_FE:
            v = fd.get(k)
            cols.append(fnp.zeros(n, dtype=f32) if v is None else v)
        lam = fd.get("lam")
        cols.append(fnp.zeros(n, dtype=f32) + float(lam) if lam is not None else fnp.zeros(n, dtype=f32))
        X = fnp.stack(cols, axis=1)                                               # (n, F)
        Z = fnp.sign(X) * fnp.log1p(fnp.abs(X) * 1e3)
        Z = (Z - g["mu"][li][None, :]) / g["sd"][li][None, :]
        cdf = flops.stats.norm.cdf
        a = Z @ g["W1T"] + g["b1L"][li][None, :]
        a = a * cdf(a).astype(f32)
        a = a @ g["W2T"] + g["b2"][None, :]
        a = a * cdf(a).astype(f32)
        a = a @ g["W3T"] + g["b3"][None, :]
        a = a * cdf(a).astype(f32)
        c = (a @ g["w4"] + g["b4"]) * g["es"][li]
        if gst["u"] is not None:
            c = fd["Phi"] * (W @ gst["u"]) + c
        gst["u"] = c

''' + a + '''        if g.get("kind") == "lt":
            return self._lt_step1(g, li, fd, W, gst, n)
''')
open(dst, "w").write(s)
print("V41 written", dst)
