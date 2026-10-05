#!/usr/bin/env python3
"""Per-layer predictability of the born error b_m = e_m - T_m e_{m-1} from the layer-m features
(ridge, MLP-level CV). No transport needed. Reports held-out R^2 per layer and which features matter."""
import glob, sys
import numpy as np
sys.path.insert(0, "/home/user/arc-whitebox/work")
from fit_prep import features
FE = "/home/user/arc-whitebox/work/feats"
lam = float(sys.argv[1]) if len(sys.argv) > 1 else 1e-2
ids = [int(f.split("G_")[1][:4]) for f in sorted(glob.glob(f"{FE}/G_*.npz"))]
H = {m: [] for m in range(16)}; B = {m: [] for m in range(16)}; E15 = []
names = None
for i in ids:
    d = np.load(f"{FE}/feat_{i:04d}.npz"); g = np.load(f"{FE}/G_{i:04d}.npz")
    born = g["born"].astype(np.float64)
    k4names = list(g["k4m_names"]); k4arr = g["k4m"].astype(np.float64)
    k4m = {m: {k4names[q]: k4arr[m, :, q] for q in range(len(k4names))} for m in range(16)}
    for m in range(16):
        F = features(d, m, k4m)
        if names is None:
            names = list(F.keys())
        H[m].append(np.stack([F[k] for k in names], 1)); B[m].append(born[m])
nm = len(ids); folds = 5
rng = np.random.default_rng(0); perm = rng.permutation(nm); fold_of = np.zeros(nm, int)
for k in range(folds): fold_of[perm[k::folds]] = k
print(f"{nm} MLPs, {len(names)} features, lam={lam}")
tot_b = 0; tot_r = 0
for m in range(16):
    r2s = []; base = np.mean(np.concatenate(B[m]) ** 2)
    ho = []; 
    for k in range(folds):
        tr = [i for i in range(nm) if fold_of[i] != k]; te = [i for i in range(nm) if fold_of[i] == k]
        X = np.concatenate([H[m][i] for i in tr]); y = np.concatenate([B[m][i] for i in tr])
        mu, sd = X.mean(0), X.std(0) + 1e-30; Z = (X - mu) / sd
        beta = np.linalg.solve(Z.T @ Z + lam * len(y) * np.eye(Z.shape[1]), Z.T @ y)
        for i in te:
            p = ((H[m][i] - mu) / sd) @ beta
            ho.append((np.mean((B[m][i] - p) ** 2), np.mean(B[m][i] ** 2)))
    ho = np.array(ho)
    # top features by |standardized coef| from the full fit
    X = np.concatenate(H[m]); y = np.concatenate(B[m]); mu, sd = X.mean(0), X.std(0) + 1e-30; Z = (X - mu) / sd
    beta = np.linalg.solve(Z.T @ Z + lam * len(y) * np.eye(Z.shape[1]), Z.T @ y)
    top = np.argsort(-np.abs(beta))[:4]
    print(f"L{m:02d} born mse {base:.3e}  held-out residual/base {ho[:, 0].sum() / ho[:, 1].sum():.3f}   top: " + ", ".join(f"{names[t]}" for t in top))
