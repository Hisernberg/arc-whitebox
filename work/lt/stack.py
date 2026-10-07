"""Blend LT (per-layer transported) and GRU corrections on the 53 held-out MLPs; leave-one-out fit of (a, b)."""
import glob, numpy as np, torch
from numpy.random import SeedSequence, default_rng
ck = torch.load('/home/user/arc-whitebox/work/lt/lt_model.pt', weights_only=False)
F, Hh = ck['F'], ck['hidden']; mu, sd, es = ck['mu'], ck['sd'], ck['es']
net = torch.nn.Sequential(torch.nn.Linear(F + 16, Hh), torch.nn.GELU(), torch.nn.Linear(Hh, Hh), torch.nn.GELU(), torch.nn.Linear(Hh, Hh), torch.nn.GELU(), torch.nn.Linear(Hh, 1)); net.load_state_dict(ck['net'])
G = np.load('/home/user/arc-whitebox/work/lt/gru_corr_held.npz')
def tf(X): return np.sign(X) * np.log1p(np.abs(X) * 1e3)
def W_of(seed):
    r = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    return [(r.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16).astype(np.float32) for _ in range(16)]
rows = []
for f in sorted(glob.glob('/home/user/arc-whitebox/work/lt/ds/feat_*.npz')):
    d = np.load(f); Z = (tf(d['X']) - mu) / sd; P = np.concatenate([Z, np.broadcast_to(np.eye(16, dtype=np.float32)[:, None, :], (16, 1024, 16))], -1).astype(np.float32)
    with torch.no_grad(): g = net(torch.from_numpy(P.reshape(-1, F + 16))).numpy().reshape(16, 1024) * es
    W = W_of(d['seed']); c = g[0]
    for l in range(1, 16): c = d['Phi'][l] * (c @ W[l]) + g[l]
    e = (d['truth'][15] - d['pred'][15]).astype(np.float64); r = G[str(d['name'])].astype(np.float64)
    rows.append((e, c.astype(np.float64), r))
B = sum((e ** 2).mean() for e, _, _ in rows)
def ratio(a, b, idx): return sum(((rows[k][0] - a * rows[k][1] - b * rows[k][2]) ** 2).mean() for k in idx) / sum((rows[k][0] ** 2).mean() for k in idx)
def fit(idx):
    A = np.zeros((2, 2)); y = np.zeros(2)
    for k in idx:
        e, c, r = rows[k]; X = np.stack([c, r]); A += X @ X.T; y += X @ e
    return np.linalg.solve(A, y)
allk = list(range(len(rows)))
print('LT only', ratio(1, 0, allk), ' GRU only', ratio(0, 1, allk), ' LT+GRU', ratio(1, 1, allk), ' 0.5/0.5', ratio(.5, .5, allk))
a, b = fit(allk); print('in-sample fit a=%.3f b=%.3f ratio %.4f' % (a, b, ratio(a, b, allk)))
num = sum(((rows[k][0] - np.dot(fit([j for j in allk if j != k]), [rows[k][1], rows[k][2]][0:1] + [0]) ) ** 2).mean() for k in []) if False else 0
loo = 0
for k in allk:
    a_, b_ = fit([j for j in allk if j != k]); loo += ((rows[k][0] - a_ * rows[k][1] - b_ * rows[k][2]) ** 2).mean()
print('leave-one-out blend ratio %.4f' % (loo / B))
