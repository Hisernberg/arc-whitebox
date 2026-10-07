#!/usr/bin/env python3
"""GRU corrector on V29's per-neuron layer trajectories (mliston-style).
Per MLP: features per layer from work/feats/feat_i.npz, weights from W_i.npy (float16), targets
e_m = truth_m - pred_m at every layer. Recurrent messages: p_mu = Phi_m * (u_{m-1} @ W_m),
p_q = q_{m-1} @ (W_m*W_m).  Output 0 = normalized mean correction u_m, output 1 = aux q_m.
Usage: gru_corr.py [--hidden 64] [--epochs 150] [--holdout 20] [--lr 1e-3] [--out model.npz] [--seed 0]"""
import glob, sys, time, json
import numpy as np, torch, torch.nn as nn

FE = "/home/user/arc-whitebox/work/feats"
import sys as _sys
if "--fe" in _sys.argv: FE = _sys.argv[_sys.argv.index("--fe") + 1]   # dump directory (e.g. work/feats33)
args = sys.argv[1:]
def arg(name, default, typ=float):
    return typ(args[args.index(name) + 1]) if name in args else default
H = arg("--hidden", 64, int); EPOCHS = arg("--epochs", 150, int); HOLD = arg("--holdout", 20, int)
LR = arg("--lr", 5e-4); OUT = arg("--out", "/home/user/arc-whitebox/work/gru_model.npz", str); SEED = arg("--seed", 0, int)
WD = arg("--wd", 1e-5)
NMAX = arg("--nmax", 1000, int)
torch.manual_seed(SEED); np.random.seed(SEED); torch.set_num_threads(2)

FEATS = ["mu_pre", "var", "alpha", "phi", "Phi", "D3", "g4row", "K2v", "K3v", "K4v", "k22row", "k21row", "k21col",
         "e_b", "w1", "w2", "s3c", "g_post", "coff_sq", "coff_sum", "d21_abs", "d21_sq", "d21T_abs", "d21_colsum",
         "d21_rowsum", "pred"]
n = 1024

def regen_weights(seed):
    from numpy.random import SeedSequence, default_rng
    rng = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    return np.stack([(rng.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16) for _ in range(16)])

_T = np.load("/home/user/arc-whitebox/work/truth_all.npz") if __import__("os").path.exists("/home/user/arc-whitebox/work/truth_all.npz") else None
SEED_OF = {str(n): int(s) for n, s in zip(_T["names"], _T["seeds"])} if _T is not None else {}
MINI_NAMES = set(str(n) for n, sp in zip(_T["names"], _T["split"]) if sp == "mini") if _T is not None else set()

def feat_path(i):
    return f"{FE}/feat_{i:04d}.npz" if isinstance(i, int) else f"{FE}/{i}.npz"

def load_mlp(i):
    d = np.load(feat_path(i))
    X = np.zeros((16, n, len(FEATS) + 4), np.float32)
    for m in range(16):
        for q, k in enumerate(FEATS):
            kk = f"L{m:02d}_{k}"
            if kk in d.files:
                X[m, :, q] = d[kk]
        sig = np.sqrt(np.maximum(d[f"L{m:02d}_var"], 1e-12))
        X[m, :, len(FEATS)] = sig * d[f"L{m:02d}_phi"]                         # chi
        X[m, :, len(FEATS) + 1] = (d[f"L{m:02d}_D3"] / sig ** 3) if f"L{m:02d}_D3" in d.files else 0  # skew
        X[m, :, len(FEATS) + 2] = (d[f"L{m:02d}_g4row"] / sig ** 4) if f"L{m:02d}_g4row" in d.files else 0  # kurt
        X[m, :, len(FEATS) + 3] = float(d[f"L{m:02d}_lam"]) if f"L{m:02d}_lam" in d.files else 0.0
    e = (d["truth"].astype(np.float64) - d["pred"].astype(np.float64)).astype(np.float32)   # (16, n)
    wf = f"{FE}/W_{i:04d}.npy" if isinstance(i, int) else ""
    if wf and __import__("os").path.exists(wf):
        Wref = ("file", wf)
    else:
        Wref = ("seed", int(d["seed"]) if "seed" in d.files else SEED_OF[str(d["name"])])
    return X, e, Wref, str(d["name"]), float(d["mse"])


def get_W(Wref):
    if Wref[0] == "file":
        return np.load(Wref[1], mmap_mode="r")
    from numpy.random import SeedSequence, default_rng
    rng = default_rng(SeedSequence(int(Wref[1])).spawn(3)[0])
    return np.stack([(rng.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float32) for _ in range(16)])

ids = sorted(int(f.split("feat_")[1][:4]) for f in glob.glob(f"{FE}/feat_*.npz"))
FULL = "--full" in args          # also use the full-split dumps (featf_*.npz), named by file stem
if FULL:
    ids = ids + sorted(f.split("/")[-1][:-4] for f in glob.glob(f"{FE}/featf_*.npz"))
ids = ids[:NMAX]
HOLD_MINI = "--hold-mini" in args   # holdout = the mini-split MLPs (never trained on): clean LB-like estimate
SPLIT_SEED = arg("--split-seed", SEED, int)   # holdout split seed (keep fixed across ensemble members)
rng = np.random.default_rng(SPLIT_SEED); perm = rng.permutation(len(ids))
if HOLD_MINI:
    hold = [i for i in ids if isinstance(i, int)]; train = [i for i in ids if not isinstance(i, int)]
else:
    hold = sorted((ids[k] for k in perm[:HOLD]), key=str); train = sorted((ids[k] for k in perm[HOLD:]), key=str)
print(f"{len(ids)} MLPs: train {len(train)} holdout {len(hold)}", flush=True)
data = {i: load_mlp(i) for i in ids}
F = data[ids[0]][0].shape[2]
# per-layer feature standardization from the training set
Xall = np.stack([data[i][0] for i in train])          # (N, 16, n, F)
mu_f = Xall.mean(axis=(0, 2)); sd_f = Xall.std(axis=(0, 2)) + 1e-12   # (16, F)
sd_f[np.abs(sd_f) < 1e-20] = 1.0
sig_mu = float(np.sqrt(np.mean(np.stack([data[i][1][8:] for i in train]) ** 2)))   # target scale
print(f"F={F} sig_mu={sig_mu:.3e}", flush=True)
del Xall
FINAL_W = arg("--final-w", 4.0)   # loss weight of the scored (final) layer
layer_w = torch.tensor([0.25] * 4 + [1.0] * 4 + [2.0] * 7 + [FINAL_W], dtype=torch.float32)

ACT = arg("--act", "tanh", str)
RESID = "--resid" in args
HPROP = "--hprop" in args   # V40: hidden state transported through W   # V39: residual connection u = Phi*(u_prev @ W) + net output   # tanh: standard GRU (sigmoid/tanh, tanh-GELU); cdf: normal-CDF gates, 2*CDF-1 candidate, exact GELU

def _cdf(x):
    return 0.5 * (1.0 + torch.erf(x / 1.4142135623730951))

class CdfGRUCell(nn.Module):
    """GRU cell whose squashing functions are the normal CDF (gates) and 2*CDF-1 (candidate)."""
    def __init__(self, fin, h):
        super().__init__()
        self.weight_ih = nn.Parameter(torch.randn(3 * h, fin) / fin ** 0.5)
        self.weight_hh = nn.Parameter(torch.randn(3 * h, h) / h ** 0.5)
        self.bias_ih = nn.Parameter(torch.zeros(3 * h)); self.bias_hh = nn.Parameter(torch.zeros(3 * h))
        self.h = h
    def forward(self, x, hp):
        gi = x @ self.weight_ih.T + self.bias_ih; gh = hp @ self.weight_hh.T + self.bias_hh
        H_ = self.h
        r = _cdf(gi[:, :H_] + gh[:, :H_]); z = _cdf(gi[:, H_:2 * H_] + gh[:, H_:2 * H_])
        n_ = 2.0 * _cdf(gi[:, 2 * H_:] + r * gh[:, 2 * H_:]) - 1.0
        return (1.0 - z) * n_ + z * hp

class Model(nn.Module):
    def __init__(self, hid=None):
        super().__init__()
        hid = H if hid is None else hid
        self.hid = hid
        self.cell = nn.GRUCell(F + 3, hid) if ACT == "tanh" else CdfGRUCell(F + 3, hid)
        self.ro = nn.Sequential(nn.Linear(hid, 2 * hid), nn.GELU(approximate="tanh") if ACT == "tanh" else nn.GELU(), nn.Linear(2 * hid, 2))
    def forward(self, X, W):
        # X (16, n, F) standardized; W (16, n, n) float32 tensor
        h = torch.zeros(n, self.hid); u = torch.zeros(n); q = torch.zeros(n)
        us = []
        for m in range(16):
            Phi = X[m, :, FEATS.index("Phi")] * sd_f_t[m, FEATS.index("Phi")] + mu_f_t[m, FEATS.index("Phi")]
            pmu = Phi * (u @ W[m]) if m > 0 else torch.zeros(n)
            pq = (q @ (W[m] * W[m])) if m > 0 else torch.zeros(n)
            inp = torch.cat([X[m], pmu[:, None], pq[:, None], torch.full((n, 1), m / 15.0)], 1)
            if HPROP and m > 0:
                h = W[m].t() @ h   # V40: carry the hidden state through the weights (neuron i at layer m-1 is not neuron i at m)
            h = self.cell(inp, h)
            out = self.ro(h)
            u, q = out[:, 0], out[:, 1]
            if RESID:
                u = u + pmu   # V39: linear error propagation hard-coded; the net learns the local term
            us.append(u)
        return torch.stack(us)   # (16, n)

mu_f_t = torch.tensor(mu_f); sd_f_t = torch.tensor(sd_f)
def tens(i):
    X, e, Wref, _, _ = data[i]
    Xs = torch.tensor((X - mu_f[:, None, :]) / sd_f[:, None, :]); E = torch.tensor(e / sig_mu); Wt = torch.tensor(np.asarray(get_W(Wref), dtype=np.float32))
    return Xs, E, Wt
model = Model()
INIT = arg("--init", "", str)   # fine-tune: start from this checkpoint and keep its normalization
if INIT:
    _ck = np.load(INIT, allow_pickle=False)
    mu_f, sd_f, sig_mu = _ck["mu_f"], _ck["sd_f"], float(_ck["sig_mu"])
    mu_f_t = torch.tensor(mu_f); sd_f_t = torch.tensor(sd_f)
    model = Model(int(_ck["H"]))
    model.load_state_dict({k: torch.tensor(_ck[k]) for k in model.state_dict().keys()})
    H = int(_ck["H"])
    print(f"init from {INIT} (best_ratio {float(_ck['best_ratio']) if 'best_ratio' in _ck.files else float('nan'):.4f})", flush=True)
EVAL = arg("--eval", "", str)
if EVAL:
    cks = [np.load(f, allow_pickle=False) for f in EVAL.split(",")]
    ids_eval = [(int(x) if x.isdigit() else x) for x in arg("--ids", ",".join(str(i) for i in (hold if hold else ids)), str).split(",")]   # default: held-out MLPs only
    corrs = {i: None for i in ids_eval}
    for ck in cks:
        mu_f, sd_f, sig_mu = ck["mu_f"], ck["sd_f"], float(ck["sig_mu"])
        mu_f_t = torch.tensor(mu_f); sd_f_t = torch.tensor(sd_f)
        model = Model(int(ck["H"]))
        model.load_state_dict({k: torch.tensor(ck[k]) for k in model.state_dict().keys()})
        model.eval()
        with torch.no_grad():
            for i in ids_eval:
                Xs, E, Wt = tens(i); U = model(Xs, Wt)
                c = U[15].numpy() * sig_mu / len(cks)
                corrs[i] = c if corrs[i] is None else corrs[i] + c
    if __import__('os').environ.get('GRU_CORR_OUT'):
        np.savez(__import__('os').environ['GRU_CORR_OUT'], **{str(data[i][3]): corrs[i] for i in ids_eval})
    rows = []
    for i in ids_eval:
        e15 = data[i][1][15].astype(np.float64)
        base = float(np.mean(e15 ** 2)); corr = float(np.mean((e15 - corrs[i]) ** 2))
        rows.append((base, corr, i in hold)); _ec = globals().setdefault('_EC', []); _ec.append((float(np.mean(e15 * corrs[i])), float(np.mean(corrs[i] ** 2)), base, i in hold))
        print(f"[{str(i):>10s}] {data[i][3]:20s} V29 {base:.4e} corrected {corr:.4e} ratio {corr / base:.3f} ({'holdout' if i in hold else 'train'})")
    for name, flag in (("holdout", True), ("train", False)):
        r = [(b, c) for b, c, h in rows if h == flag]
        if r:
            print(f"ENSEMBLE {name}: n={len(r)} mean ratio {sum(c for _, c in r) / sum(b for b, _ in r):.4f}")
            q = [(a, c, b) for a, c, b, h in _EC if h == flag]; A = sum(a for a, _, _ in q); Cc = sum(c for _, c, _ in q); B = sum(b for _, _, b in q)
            al = A / Cc; print(f"ENSEMBLE {name}: alpha* {al:.3f} -> ratio {(B - 2 * al * A + al * al * Cc) / B:.4f}")
    sys.exit(0)
opt = torch.optim.Adam(model.parameters(), lr=LR, weight_decay=WD)
sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=EPOCHS * len(train) * arg("--inner", 1, int))
def evaluate(idx):
    model.eval(); rows = []
    with torch.no_grad():
        for i in idx:
            Xs, E, Wt = tens(i); U = model(Xs, Wt)
            base = float((E[15] ** 2).mean()); corr = float(((E[15] - U[15]) ** 2).mean())
            rows.append((base, corr))
    model.train(); r = np.array(rows)
    return r[:, 1].mean() / r[:, 0].mean(), np.median(r[:, 1] / r[:, 0]), r[:, 1].max() / r[:, 0].max()
t0 = time.time()
best = (float("inf"), -1, None)
INNER = arg("--inner", 1, int)   # gradient steps per MLP visit (amortizes the weight regeneration)
for ep in range(EPOCHS):
    order = [train[k] for k in rng.permutation(len(train))]; tot = 0.0   # keep int/str ids intact
    for i in order:
        Xs, E, Wt = tens(i)
        for _ in range(INNER):
            U = model(Xs, Wt)
            loss = (layer_w[:, None] * (U - E) ** 2).mean()
            opt.zero_grad(); loss.backward(); nn.utils.clip_grad_norm_(model.parameters(), 1.0); opt.step(); sched.step()
        tot += float(loss)
    if ep % (1 if EPOCHS <= 12 else 5) == 0 or ep == EPOCHS - 1:
        tr = evaluate(train[:10]); ho = evaluate(hold) if hold else (float('nan'),) * 3
        if hold and ho[0] < best[0]:
            best = (ho[0], ep, {k: v.detach().clone() for k, v in model.state_dict().items()})
            # checkpoint on every improvement (a killed run keeps its best model)
            np.savez(OUT, mu_f=mu_f, sd_f=sd_f, sig_mu=sig_mu, feats=np.array(FEATS), H=H, act=ACT, resid=RESID, hprop=HPROP, best_ratio=best[0], best_epoch=best[1],
                     **{k: v.numpy() for k, v in best[2].items()})
        print(f"ep {ep:3d} loss {tot / len(train):.4f}  final-layer MSE ratio train {tr[0]:.3f}  holdout {ho[0]:.3f} (median {ho[1]:.3f})  best {best[0]:.3f}@{best[1]}  t={time.time() - t0:.0f}s", flush=True)
if best[2] is not None:
    model.load_state_dict(best[2])
    print(f"BEST holdout ratio {best[0]:.4f} at epoch {best[1]} (saved)")
# save weights + normalization for deployment
sd = {k: v.detach().numpy() for k, v in model.state_dict().items()}
np.savez(OUT, mu_f=mu_f, sd_f=sd_f, sig_mu=sig_mu, feats=np.array(FEATS), H=H, act=ACT, resid=RESID, hprop=HPROP, **sd)
print("saved", OUT, "params", sum(p.numel() for p in model.parameters()))
