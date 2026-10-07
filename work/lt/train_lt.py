"""Train a per-(layer, neuron) local-error model eps_l = g(features_l) and evaluate the transported correction
c_0 = g_0, c_l = Phi_l * (c_{l-1} @ W_l) + g_l on held-out nets: final = pred_15 + c_15."""
import sys, glob, os, time, argparse, numpy as np, torch
from numpy.random import SeedSequence, default_rng
ap = argparse.ArgumentParser(); ap.add_argument('--ntest', type=int, default=100); ap.add_argument('--ntrain', type=int, default=100000)
ap.add_argument('--epochs', type=int, default=6); ap.add_argument('--hidden', type=int, default=128); ap.add_argument('--out', default='/home/user/arc-whitebox/work/lt/lt_model.pt')
ap.add_argument('--lin', action='store_true'); ap.add_argument('--x2', action='store_true'); ap.add_argument('--seed', type=int, default=0); ap.add_argument('--evalonly', action='store_true')
a = ap.parse_args(); torch.manual_seed(a.seed); torch.set_num_threads(4)
files = sorted(glob.glob('/home/user/arc-whitebox/work/lt/ds/*.npz'))
test = [f for f in files if '/feat_' in f][:a.ntest]; train = [f for f in files if '/featf_' in f][:a.ntrain]
def getX(f, d):
    X = d['X']
    if a.x2: X = np.concatenate([X, np.load(f.replace('/ds/', '/ds2/'))], -1)
    return X
def load(fs):
    X, E = [], []
    for f in fs:
        d = np.load(f); X.append(getX(f, d)); E.append(d['eps'])
    return np.stack(X), np.stack(E)
t0 = time.time(); Xtr, Etr = load(train); print('loaded', Xtr.shape, time.time() - t0, flush=True)
F = Xtr.shape[-1]
# per-layer per-feature standardisation (signed log for heavy tails)
def tf(X): return np.sign(X) * np.log1p(np.abs(X) * 1e3)
S = np.zeros((16, F)); S2 = np.zeros((16, F))   # streamed (chunked) per-layer moments: same values, less memory
for c in range(0, len(Xtr), 50):
    Zc = tf(Xtr[c:c + 50]).astype(np.float64); S += Zc.sum(axis=(0, 2)); S2 += (Zc ** 2).sum(axis=(0, 2)); del Zc
cnt = len(Xtr) * 1024; mu = (S / cnt)[:, None, :].astype(np.float32); sd = (np.sqrt(np.maximum(S2 / cnt - (S / cnt) ** 2, 0)) + 1e-6)[:, None, :].astype(np.float32)
es = np.sqrt((Etr ** 2).mean(axis=(0, 2)))[:, None]   # per-layer target scale
def prep(X):
    Z = (tf(X) - mu) / sd; L = np.broadcast_to(np.eye(16, dtype=np.float32)[:, None, :], (X.shape[0], 16, 1024, 16)) if X.ndim == 4 else None
    return np.concatenate([Z, L], -1).astype(np.float32)
Ptr = np.empty((len(Xtr), 16, 1024, F + 16), np.float32)
for c in range(0, len(Xtr), 50): Ptr[c:c + 50] = prep(Xtr[c:c + 50])
Ptr = Ptr.reshape(-1, F + 16); Ytr = (Etr / es[None]).reshape(-1).astype(np.float32); del Xtr
if a.lin: net = torch.nn.Linear(F + 16, 1)
else: net = torch.nn.Sequential(torch.nn.Linear(F + 16, a.hidden), torch.nn.GELU(), torch.nn.Linear(a.hidden, a.hidden), torch.nn.GELU(), torch.nn.Linear(a.hidden, a.hidden), torch.nn.GELU(), torch.nn.Linear(a.hidden, 1))
opt = torch.optim.AdamW(net.parameters(), lr=2e-3, weight_decay=1e-4)
Pt, Yt = torch.from_numpy(Ptr), torch.from_numpy(Ytr); N = len(Yt); bs = 8192
steps = a.epochs * (N // bs); sched = torch.optim.lr_scheduler.OneCycleLR(opt, max_lr=2e-3, total_steps=steps)
s = 0
for ep in range(a.epochs):
    perm = torch.randperm(N); tot = 0
    for i in range(N // bs):
        idx = perm[i*bs:(i+1)*bs]; p = net(Pt[idx]).squeeze(-1); loss = ((p - Yt[idx]) ** 2).mean()
        opt.zero_grad(); loss.backward(); opt.step(); sched.step(); tot += loss.item()
    print(f'ep {ep} train nmse {tot / (N // bs):.4f} t={time.time()-t0:.0f}', flush=True)
torch.save({'net': net.state_dict(), 'mu': mu, 'sd': sd, 'es': es, 'F': F, 'hidden': a.hidden, 'lin': a.lin}, a.out)
def W_of(seed):
    r = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    return [(r.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16).astype(np.float32) for _ in range(16)]
base = cor = loc0 = loc1 = 0; per_l = np.zeros((16, 2))
with torch.no_grad():
    for f in test:
        d = np.load(f); g = net(torch.from_numpy(prep(getX(f, d)[None])[0].reshape(-1, F + 16))).numpy().reshape(16, 1024) * es
        per_l[:, 0] += (d['eps'] ** 2).mean(1); per_l[:, 1] += ((d['eps'] - g) ** 2).mean(1)
        W = W_of(d['seed']); c = g[0]
        for l in range(1, 16): c = d['Phi'][l] * (c @ W[l]) + g[l]
        e = d['truth'][15] - d['pred'][15]; base += (e ** 2).mean(); cor += ((e - c) ** 2).mean()
print('local nmse per layer', np.round(per_l[:, 1] / per_l[:, 0], 3))
print(f'held-out {len(test)} nets: raw final MSE {base/len(test):.4e}  transported-corrected {cor/len(test):.4e}  ratio {cor/base:.4f}')
