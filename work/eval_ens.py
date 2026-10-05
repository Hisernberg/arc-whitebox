#!/usr/bin/env python3
"""Score GRU checkpoints and ensembles on the 100 held-out mini MLPs (final layer only).
Per checkpoint the final-layer correction (activation units) is cached in work/evalcache/<name>.npy.
Usage: eval_ens.py --models a.npz,b.npz,... [--combos "a+b;a+b+c"]   (combo entries = checkpoint basenames w/o .npz)
Prints per-model ratio, per-combo ratio at scale 1 and at the optimal scale alpha*."""
import glob, os, sys, numpy as np, torch, torch.nn as nn
FE = "/home/user/arc-whitebox/work/feats"; CACHE = "/home/user/arc-whitebox/work/evalcache"; n = 1024
args = sys.argv[1:]
def arg(k, d): return args[args.index(k) + 1] if k in args else d
torch.set_num_threads(1)
FEATS = ["mu_pre", "var", "alpha", "phi", "Phi", "D3", "g4row", "K2v", "K3v", "K4v", "k22row", "k21row", "k21col",
         "e_b", "w1", "w2", "s3c", "g_post", "coff_sq", "coff_sum", "d21_abs", "d21_sq", "d21T_abs", "d21_colsum", "d21_rowsum", "pred"]
T = np.load("/home/user/arc-whitebox/work/truth_all.npz"); SEED_OF = {str(a): int(b) for a, b in zip(T["names"], T["seeds"])}
def load(i):
    d = np.load(f"{FE}/feat_{i:04d}.npz")
    X = np.zeros((16, n, len(FEATS) + 4), np.float32)
    for m in range(16):
        for q, k in enumerate(FEATS):
            kk = f"L{m:02d}_{k}"
            if kk in d.files: X[m, :, q] = d[kk]
        sig = np.sqrt(np.maximum(d[f"L{m:02d}_var"], 1e-12))
        X[m, :, len(FEATS)] = sig * d[f"L{m:02d}_phi"]
        X[m, :, len(FEATS) + 1] = (d[f"L{m:02d}_D3"] / sig ** 3) if f"L{m:02d}_D3" in d.files else 0
        X[m, :, len(FEATS) + 2] = (d[f"L{m:02d}_g4row"] / sig ** 4) if f"L{m:02d}_g4row" in d.files else 0
        X[m, :, len(FEATS) + 3] = float(d[f"L{m:02d}_lam"]) if f"L{m:02d}_lam" in d.files else 0.0
    e15 = (d["truth"][15].astype(np.float64) - d["pred"][15].astype(np.float64))
    return X, e15, SEED_OF[str(d["name"])]
def regen(seed):
    from numpy.random import SeedSequence, default_rng
    rng = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    return np.stack([(rng.standard_normal((n, n)) * np.sqrt(2.0 / n)).astype(np.float32) for _ in range(16)])
def cdf(x): return 0.5 * (1.0 + torch.erf(x / 1.4142135623730951))
def run_model(ck, X, W):
    H = int(ck["H"]); act = str(ck["act"]) if "act" in ck.files else "tanh"
    P = {k: torch.tensor(ck[k]) for k in ck.files if k.startswith("cell.") or k.startswith("ro.")}
    mu_f, sd_f = torch.tensor(ck["mu_f"]), torch.tensor(ck["sd_f"])
    Xs = (torch.tensor(X) - mu_f[:, None, :]) / sd_f[:, None, :]
    h = torch.zeros(n, H); u = torch.zeros(n); q = torch.zeros(n); iP = FEATS.index("Phi")
    for m in range(16):
        Phi = torch.tensor(X[m, :, iP])
        pmu = Phi * (u @ W[m]) if m > 0 else torch.zeros(n)
        pq = (q @ (W[m] * W[m])) if m > 0 else torch.zeros(n)
        x = torch.cat([Xs[m], pmu[:, None], pq[:, None], torch.full((n, 1), m / 15.0)], 1)
        gi = x @ P["cell.weight_ih"].T + P["cell.bias_ih"]; gh = h @ P["cell.weight_hh"].T + P["cell.bias_hh"]
        if act == "cdf":
            r = cdf(gi[:, :H] + gh[:, :H]); z = cdf(gi[:, H:2 * H] + gh[:, H:2 * H]); c = 2 * cdf(gi[:, 2 * H:] + r * gh[:, 2 * H:]) - 1
            h = (1 - z) * c + z * h; a = h @ P["ro.0.weight"].T + P["ro.0.bias"]; a = a * cdf(a)
        else:
            r = torch.sigmoid(gi[:, :H] + gh[:, :H]); z = torch.sigmoid(gi[:, H:2 * H] + gh[:, H:2 * H]); c = torch.tanh(gi[:, 2 * H:] + r * gh[:, 2 * H:])
            h = (1 - z) * c + z * h; a = h @ P["ro.0.weight"].T + P["ro.0.bias"]; a = torch.nn.functional.gelu(a, approximate="tanh")
        y = a @ P["ro.2.weight"].T + P["ro.2.bias"]; u, q = y[:, 0], y[:, 1]
    return u.numpy().astype(np.float64) * float(ck["sig_mu"])
models = [m for m in arg("--models", "").split(",") if m]
ids = list(range(100)); need = [m for m in models if not os.path.exists(f"{CACHE}/{os.path.basename(m)[:-4]}.npy")]
E = None
if need or not os.path.exists(f"{CACHE}/_e15.npy"):
    data = [load(i) for i in ids]; E = np.stack([d[1] for d in data]); np.save(f"{CACHE}/_e15.npy", E)
    cks = {m: np.load(m, allow_pickle=False) for m in need}; out = {m: np.zeros((100, n)) for m in need}
    with torch.no_grad():
        for j, (X, e, seed) in enumerate(data):
            W = torch.tensor(regen(seed)) if need else None
            for m in need: out[m][j] = run_model(cks[m], X, W)
    for m in need: np.save(f"{CACHE}/{os.path.basename(m)[:-4]}.npy", out[m])
E = np.load(f"{CACHE}/_e15.npy"); base = float((E ** 2).sum())
C = {os.path.basename(m)[:-4]: np.load(f"{CACHE}/{os.path.basename(m)[:-4]}.npy") for m in models}
def score(keys):
    c = sum(C[k] for k in keys) / len(keys); a = float((E * c).sum() / (c * c).sum())
    return float(((E - c) ** 2).sum()) / base, a, float(((E - a * c) ** 2).sum()) / base
for k in C: r1, a, ra = score([k]); print(f"{k:22s} ratio {r1:.4f}  alpha* {a:.3f} -> {ra:.4f}")
for combo in [c for c in arg("--combos", "").split(";") if c]:
    keys = combo.split("+"); r1, a, ra = score(keys); print(f"COMBO {combo:40s} ratio {r1:.4f}  alpha* {a:.3f} -> {ra:.4f}")
