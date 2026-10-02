#!/usr/bin/env python3
"""Learned-corrector feasibility on V29 feature dumps.

Fits per-neuron correctors for the FINAL-layer residual (truth - pred) from the chain's state
features, with MLP-level cross-validation (train on K-1 folds of MLPs, test on the held-out fold).
Reports held-out MSE before/after correction. Usage: corr_analysis.py [feat_dir] [n_folds]
"""
import glob, sys
import numpy as np

FD = sys.argv[1] if len(sys.argv) > 1 else "/home/user/arc-whitebox/work/feats"
NF = int(sys.argv[2]) if len(sys.argv) > 2 else 5
files = sorted(glob.glob(FD + "/feat_*.npz"))
print(f"{len(files)} feature files")

LAST = 15
# feature keys available at the last layer (pre-nonlin state + output) and at layer 14 (post state)
def build(d):
    n = d["pred"].shape[1]
    cols, names = [], []
    def add(k, name=None, fn=None):
        if k in d:
            v = d[k].astype(np.float64)
            if fn is not None:
                v = fn(v)
            cols.append(v); names.append(name or k)
    L = f"L{LAST:02d}_"
    for k in ("mu_pre", "var", "alpha", "phi", "Phi", "D3", "g4row", "pred"):
        add(L + k)
    add(L + "var", "sigma", np.sqrt)
    add(L + "alpha", "abs_alpha", np.abs)
    # layer-14 post state and D21 row stats at the last pre-activation
    for k in ("K2v", "K3v", "K4v", "k22row", "k21row", "k21col", "e_b", "w1", "w2", "s3c", "g_post", "coff_sq", "coff_sum"):
        add(f"L14_{k}")
    for lay in (13, 14):
        for k in ("mu_pre", "var", "D3", "g4row", "pred", "d21_abs", "d21_sq", "d21_rowsum", "d21_colsum", "d21T_abs"):
            add(f"L{lay:02d}_{k}", f"L{lay}_{k}")
    X = np.stack(cols, axis=1)  # (n, F)
    return X, names

Xs, ys, preds, truths = [], [], [], []
for f in files:
    d = np.load(f)
    X, names = build(d)
    y = d["truth"][LAST].astype(np.float64) - d["pred"][LAST].astype(np.float64)
    Xs.append(X); ys.append(y); preds.append(d["pred"][LAST].astype(np.float64)); truths.append(d["truth"][LAST].astype(np.float64))
M = len(Xs)
print("features:", len(names), names[:12], "...")

def feat_expand(X):
    # cheap nonlinear expansion: squares and a few products of the leading (standardized) features
    return np.concatenate([X, X ** 2, X[:, :8, None].reshape(X.shape[0], -1)[:, :0]], axis=1)

def ridge_cv(lam, expand=False):
    folds = [list(range(i, M, NF)) for i in range(NF)]
    base, corr = [], []
    for te in folds:
        tr = [i for i in range(M) if i not in te]
        Xtr = np.concatenate([Xs[i] for i in tr]); ytr = np.concatenate([ys[i] for i in tr])
        if expand:
            Xtr = feat_expand(Xtr)
        mu, sd = Xtr.mean(0), Xtr.std(0) + 1e-12
        Z = (Xtr - mu) / sd
        Z = np.concatenate([Z, np.ones((Z.shape[0], 1))], axis=1)
        A = Z.T @ Z + lam * len(Z) * np.eye(Z.shape[1]); A[-1, -1] -= lam * len(Z)
        beta = np.linalg.solve(A, Z.T @ ytr)
        for i in te:
            Xi = feat_expand(Xs[i]) if expand else Xs[i]
            Zi = np.concatenate([(Xi - mu) / sd, np.ones((Xi.shape[0], 1))], axis=1)
            delta = Zi @ beta
            base.append(np.mean(ys[i] ** 2)); corr.append(np.mean((ys[i] - delta) ** 2))
    return np.mean(base), np.mean(corr)

for lam in (1e-1, 1e-2, 1e-3, 1e-4):
    b, c = ridge_cv(lam)
    print(f"ridge lam={lam:g}: held-out raw {b:.4e} -> corrected {c:.4e}  ratio {c / b:.4f}")
for lam in (1e-2, 1e-3):
    b, c = ridge_cv(lam, expand=True)
    print(f"ridge+sq lam={lam:g}: held-out raw {b:.4e} -> corrected {c:.4e}  ratio {c / b:.4f}")

# in-sample upper bound (all MLPs): how much variance is linearly explainable at all
Xall = np.concatenate(Xs); yall = np.concatenate(ys)
mu, sd = Xall.mean(0), Xall.std(0) + 1e-12
Z = np.concatenate([(Xall - mu) / sd, np.ones((len(Xall), 1))], axis=1)
beta = np.linalg.lstsq(Z, yall, rcond=None)[0]
print(f"in-sample linear R2: {1 - np.mean((yall - Z @ beta) ** 2) / np.mean(yall ** 2):.4f}")
# per-feature correlation with the residual
corrs = [(abs(np.corrcoef(Xall[:, j], yall)[0, 1]), names[j]) for j in range(len(names))]
corrs.sort(reverse=True)
print("top |corr| features:", [(n, round(c, 3)) for c, n in corrs[:12]])
# simple scale-bias check: optimal multiplicative factor on pred
pa = np.concatenate(preds); ta = np.concatenate(truths)
s = (pa * ta).sum() / (pa * pa).sum()
print(f"optimal global scale on pred: {s:.6f}; MSE scaled {np.mean((s * pa - ta) ** 2):.4e} vs raw {np.mean((pa - ta) ** 2):.4e}")
