"""Held-out (53 mini MLPs) ratio of an average of LT models. Usage: ens_eval.py m1.pt [m2.pt ...]"""
import sys, glob, numpy as np, torch
from numpy.random import SeedSequence, default_rng
def tf(X): return np.sign(X) * np.log1p(np.abs(X) * 1e3)
def W_of(seed):
    r = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    return [(r.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16).astype(np.float32) for _ in range(16)]
ms = []
for p in sys.argv[1:]:
    ck = torch.load(p, weights_only=False); F, H = ck['F'], ck['hidden']
    net = torch.nn.Sequential(torch.nn.Linear(F + 16, H), torch.nn.GELU(), torch.nn.Linear(H, H), torch.nn.GELU(), torch.nn.Linear(H, H), torch.nn.GELU(), torch.nn.Linear(H, 1)); net.load_state_dict(ck['net'])
    ms.append((net, ck['mu'], ck['sd'], ck['es'], F))
B = np.zeros(len(ms) + 1); base = 0
for f in sorted(glob.glob('/home/user/arc-whitebox/work/lt/ds/feat_*.npz')):
    d = np.load(f); W = W_of(d['seed']); e = (d['truth'][15] - d['pred'][15]).astype(np.float64); base += (e ** 2).mean()
    cs = []
    for net, mu, sd, es, F in ms:
        Z = (tf(d['X']) - mu) / sd; P = np.concatenate([Z, np.broadcast_to(np.eye(16, dtype=np.float32)[:, None, :], (16, 1024, 16))], -1).astype(np.float32)
        with torch.no_grad(): g = net(torch.from_numpy(P.reshape(-1, F + 16))).numpy().reshape(16, 1024) * es
        c = g[0]
        for l in range(1, 16): c = d['Phi'][l] * (c @ W[l]) + g[l]
        cs.append(c.astype(np.float64))
    for k in range(len(ms)): B[k] += ((e - cs[k]) ** 2).mean()
    B[-1] += ((e - np.mean(cs, 0)) ** 2).mean()
print('single', np.round(B[:-1] / base, 4), 'ensemble', round(B[-1] / base, 4))
