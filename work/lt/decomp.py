"""Layer-transport error decomposition: delta_l = truth_l - pred_l; local eps_l = delta_l - Phi_l*(delta_{l-1} @ W_l)."""
import sys, glob, numpy as np
from numpy.random import SeedSequence, default_rng
def W_of(seed):
    r = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    return [(r.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16).astype(np.float32) for _ in range(16)]
files = sorted(glob.glob('/home/user/arc-whitebox/work/feats_all/feat_*.npz'))[:int(sys.argv[1])]
acc = np.zeros((16, 3))
for f in files:
    d = np.load(f); W = W_of(d['seed']); P, T = d['pred'], d['truth']
    # check pre-mean linearity
    mp = P[0] @ W[1]; chk = np.abs(mp - d['L01_mu_pre']).max() / np.abs(d['L01_mu_pre']).max()
    dl = T - P
    for l in range(16):
        prop = d[f'L{l:02d}_Phi'] * (dl[l-1] @ W[l]) if l else 0 * dl[0]
        eps = dl[l] - prop
        acc[l] += [np.mean(dl[l]**2), np.mean(eps**2), np.mean(np.asarray(prop)**2)]
print('chk pre-mean rel err', chk)
acc /= len(files)
for l in range(16): print(l, '%.3e total  %.3e local  %.3e propagated  local/total %.2f' % (acc[l,0], acc[l,1], acc[l,2], acc[l,1]/acc[l,0]))
