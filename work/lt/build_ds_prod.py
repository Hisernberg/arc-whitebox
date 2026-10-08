"""Per-layer local-error dataset. For each dump: X (16,1024,F) features, eps (16,1024) local error, Phi, pred, truth."""
import sys, glob, os, numpy as np
from numpy.random import SeedSequence, default_rng
FE = ['mu_pre','var','alpha','phi','Phi','D3','g4row','d21_abs','d21_sq','d21T_abs','d21_colsum','d21_rowsum','coff_sq','coff_sum','pred','K2v','K3v','K4v','k22row','k21row','k21col','e_b','w1','w2','s3c','g_post']
def W_of(seed):
    r = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    return [(r.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16).astype(np.float32) for _ in range(16)]
OUT = '/home/user/arc-whitebox/work/lt/dsp'; os.makedirs(OUT, exist_ok=True)
files = sorted(glob.glob('/home/user/arc-whitebox/work/feats_prod/*.npz'))
k, n = int(sys.argv[1]), int(sys.argv[2])
for f in files[k::n]:
    o = f'{OUT}/' + os.path.basename(f)
    if os.path.exists(o): continue
    d = np.load(f); W = W_of(d['seed']); P, T = d['pred'], d['truth']
    X = np.zeros((16, 1024, len(FE) + 1), np.float32); Phi = np.stack([d[f'L{l:02d}_Phi'] for l in range(16)])
    for l in range(16):
        for j, nm in enumerate(FE):
            key = f'L{l:02d}_{nm}'
            if key in d: X[l, :, j] = d[key]
        X[l, :, -1] = d[f'L{l:02d}_lam'] if f'L{l:02d}_lam' in d else 0
    dl = T - P; eps = dl.copy()
    for l in range(1, 16): eps[l] = dl[l] - Phi[l] * (dl[l-1] @ W[l])
    np.savez(o, X=X.astype(np.float16) if False else X, eps=eps, Phi=Phi, pred=P, truth=T, seed=d['seed'], name=d['name'])
    print(o, flush=True)
