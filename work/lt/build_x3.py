"""Cross-neuron features for LT v2: previous layer's per-neuron features carried through W_l and W_l^2
(x_{l-1} @ W_l, x_{l-1} @ W_l**2 in the simulator's convention). Saves (16, 1024, 2*len(XF)) per MLP."""
import sys, glob, os, numpy as np
from numpy.random import SeedSequence, default_rng
XF = ['mu_pre','alpha','D3','g4row','d21_abs','d21_sq','d21T_abs','d21_colsum','d21_rowsum','coff_sq','coff_sum','K2v','k22row','k21row','k21col','w1','w2','s3c']
def W_of(seed):
    r = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    return [(r.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16).astype(np.float32) for _ in range(16)]
OUT = '/home/user/arc-whitebox/work/lt/ds3'; os.makedirs(OUT, exist_ok=True)
files = sorted(glob.glob('/home/user/arc-whitebox/work/feats_all/*.npz'))
k, n = int(sys.argv[1]), int(sys.argv[2])
for f in files[k::n]:
    o = f'{OUT}/' + os.path.basename(f)
    if os.path.exists(o): continue
    d = np.load(f); W = W_of(d['seed'])
    X2 = np.zeros((16, 1024, len(XF)), np.float32)
    for l in range(1, 16):
        pass
        for j, nm in enumerate(XF):
            key = f'L{l-1:02d}_{nm}'
            if key not in d: continue
            v = d[key]
            X2[l, :, j] = v @ W[l]
    np.save(o[:-4] + '.npy', X2); os.rename(o[:-4] + '.npy', o)
    print(o, flush=True)
