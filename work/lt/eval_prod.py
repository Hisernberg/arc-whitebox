"""Held-out ratio of an LT checkpoint on a dataset dir (default: production-config dumps, mini split)."""
import sys, glob, numpy as np, torch
from numpy.random import SeedSequence, default_rng
ck = torch.load(sys.argv[1], weights_only=False); D = sys.argv[2] if len(sys.argv) > 2 else 'dsp'
F, Hh, mu, sd, es = ck['F'], ck['hidden'], ck['mu'], ck['sd'], ck['es']
net = torch.nn.Sequential(torch.nn.Linear(F + 16, Hh), torch.nn.GELU(), torch.nn.Linear(Hh, Hh), torch.nn.GELU(), torch.nn.Linear(Hh, Hh), torch.nn.GELU(), torch.nn.Linear(Hh, 1)); net.load_state_dict(ck['net'])
def tf(X): return np.sign(X) * np.log1p(np.abs(X) * 1e3)
def W_of(seed):
    r = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    return [(r.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16).astype(np.float32) for _ in range(16)]
B = C = 0
for f in sorted(glob.glob(f'/home/user/arc-whitebox/work/lt/{D}/feat_*.npz')):
    d = np.load(f); X = d['X']
    if F > X.shape[-1]: X = np.concatenate([X, np.load(f.replace(f'/{D}/', f'/{D}2/'))], -1)
    Z = (tf(X) - mu) / sd; P = np.concatenate([Z, np.broadcast_to(np.eye(16, dtype=np.float32)[:, None, :], (16, 1024, 16))], -1).astype(np.float32)
    with torch.no_grad(): g = net(torch.from_numpy(P.reshape(-1, F + 16))).numpy().reshape(16, 1024) * es
    W = W_of(d['seed']); c = g[0]
    for l in range(1, 16): c = d['Phi'][l] * (c @ W[l]) + g[l]
    e = (d['truth'][15] - d['pred'][15]).astype(np.float64); B += (e ** 2).mean(); C += ((e - c) ** 2).mean()
print(sys.argv[1], D, 'raw %.4e corrected %.4e ratio %.4f' % (B / 53, C / 53, C / B))
