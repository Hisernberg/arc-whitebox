#!/usr/bin/env python3
"""Ridge fit of the transported-correction model on work/feats/G_*.npz with MLP-level CV.
e15 ~ sum_l G_l beta_l (per-layer coefficients) or sum_l G_l beta (shared).
Usage: fit_corr.py [--shared] [--late L0] [--folds K] [--lams a,b,c] [--feats name1,name2,...]"""
import glob, sys
import numpy as np

args = sys.argv[1:]
shared = "--shared" in args
folds = int(args[args.index("--folds") + 1]) if "--folds" in args else 5
late = int(args[args.index("--late") + 1]) if "--late" in args else 0
lams = [float(x) for x in args[args.index("--lams") + 1].split(",")] if "--lams" in args else [1e-4, 1e-3, 1e-2, 1e-1, 1, 10]
sel = args[args.index("--feats") + 1].split(",") if "--feats" in args else None

files = sorted(glob.glob("/home/user/arc-whitebox/work/feats/G_*.npz"))
Xs, ys, mses = [], [], []
names = None
for f in files:
    d = np.load(f)
    G = d["G"].astype(np.float64)  # (16, n, F)
    if names is None:
        names = list(d["names"])
        idx = [names.index(s) for s in sel] if sel else list(range(len(names)))
    G = G[:, :, idx]
    if late:
        G = G[late:]
    X = np.transpose(G, (1, 0, 2)).reshape(G.shape[1], -1) if not shared else G.sum(0)
    Xs.append(X); ys.append(d["e15"].astype(np.float64)); mses.append(float(d["mse"]))
nm = len(Xs)
print(f"{nm} MLPs, {Xs[0].shape[1]} columns, baseline raw MSE {np.mean(mses):.4e}")
rng = np.random.default_rng(0)
perm = rng.permutation(nm)
fold_of = np.zeros(nm, int)
for k in range(folds):
    fold_of[perm[k::folds]] = k

def fit(Xtr, ytr, lam, mu, sd):
    Z = (Xtr - mu) / sd
    A = Z.T @ Z + lam * len(ytr) * np.eye(Z.shape[1])
    b = Z.T @ ytr
    return np.linalg.solve(A, b)

res = {lam: [] for lam in lams}
ins = {lam: [] for lam in lams}
for k in range(folds):
    tr = [i for i in range(nm) if fold_of[i] != k]
    te = [i for i in range(nm) if fold_of[i] == k]
    Xtr = np.concatenate([Xs[i] for i in tr]); ytr = np.concatenate([ys[i] for i in tr])
    mu = Xtr.mean(0); sd = Xtr.std(0) + 1e-30
    for lam in lams:
        beta = fit(Xtr, ytr, lam, mu, sd)
        for i in te:
            p = ((Xs[i] - mu) / sd) @ beta
            res[lam].append((np.mean((ys[i] - p) ** 2), np.mean(ys[i] ** 2)))
        for i in tr[:20]:
            p = ((Xs[i] - mu) / sd) @ beta
            ins[lam].append((np.mean((ys[i] - p) ** 2), np.mean(ys[i] ** 2)))
for lam in lams:
    r = np.array(res[lam]); s = np.array(ins[lam])
    print(f"lam={lam:<8g} CV: corrected {r[:, 0].mean():.4e} vs base {r[:, 1].mean():.4e} ratio {r[:, 0].mean() / r[:, 1].mean():.3f} "
          f"(per-MLP ratio median {np.median(r[:, 0] / r[:, 1]):.3f}, worst {np.max(r[:, 0] / r[:, 1]):.3f}) | in-sample ratio {s[:, 0].mean() / s[:, 1].mean():.3f}")
