"""Track A: fine-tune an LT checkpoint end-to-end on the FINAL-layer error after transport
(c_0 = g_0, c_l = Phi_l * (c_{l-1} @ W_l) + g_l; loss = mean((e_15 - c_15)^2)). Weights regenerated per MLP.
Usage: train_e2e.py <init.pt> <out.pt> [epochs] [lr] [ntrain]"""
import sys, glob, time, numpy as np, torch
from numpy.random import SeedSequence, default_rng
init, out = sys.argv[1], sys.argv[2]
EP = int(sys.argv[3]) if len(sys.argv) > 3 else 2; LR = float(sys.argv[4]) if len(sys.argv) > 4 else 3e-4
NTR = int(sys.argv[5]) if len(sys.argv) > 5 else 100000
torch.set_num_threads(4); torch.manual_seed(0)
ck = torch.load(init, weights_only=False); F, Hh, mu, sd, es = ck['F'], ck['hidden'], ck['mu'], ck['sd'], ck['es']
net = torch.nn.Sequential(torch.nn.Linear(F + 16, Hh), torch.nn.GELU(), torch.nn.Linear(Hh, Hh), torch.nn.GELU(), torch.nn.Linear(Hh, Hh), torch.nn.GELU(), torch.nn.Linear(Hh, 1)); net.load_state_dict(ck['net'])
def tf(X): return np.sign(X) * np.log1p(np.abs(X) * 1e3)
def W_of(seed):
    r = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    return np.stack([(r.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16).astype(np.float32) for _ in range(16)])
OH = np.broadcast_to(np.eye(16, dtype=np.float32)[:, None, :], (16, 1024, 16))
def load(f):
    d = np.load(f); X = d['X']
    if F > X.shape[-1]: X = np.concatenate([X, np.load(f.replace('/ds/', '/ds2/'))], -1)
    P = np.concatenate([(tf(X) - mu) / sd, OH], -1).astype(np.float32).reshape(-1, F + 16)
    e = (d['truth'][15] - d['pred'][15]).astype(np.float32)
    return torch.from_numpy(P), torch.from_numpy(d['Phi'].astype(np.float32)), torch.from_numpy(e), int(d['seed'])
def corr(P, Phi, W):
    g = net(P).reshape(16, 1024) * torch.from_numpy(es.astype(np.float32))
    c = g[0]
    for l in range(1, 16): c = Phi[l] * (c @ W[l]) + g[l]
    return c
files = sorted(glob.glob('/home/user/arc-whitebox/work/lt/ds/*.npz'))
test = [f for f in files if '/feat_' in f]; train = [f for f in files if '/featf_' in f][:NTR]
def evaluate():
    B = C = 0
    with torch.no_grad():
        for f in test:
            P, Phi, e, s = load(f); c = corr(P, Phi, torch.from_numpy(W_of(s)))
            B += float((e.double() ** 2).mean()); C += float(((e - c).double() ** 2).mean())
    return C / B
best = evaluate(); print('init held-out ratio %.4f' % best, flush=True)
opt = torch.optim.Adam(net.parameters(), lr=LR); sc = float(np.mean([1.0]))
t0 = time.time(); rng = np.random.default_rng(0)
for ep in range(EP):
    tot = 0
    for k, i in enumerate(rng.permutation(len(train))):
        P, Phi, e, s = load(train[i]); W = torch.from_numpy(W_of(s))
        c = corr(P, Phi, W); loss = ((e - c) ** 2).mean() / float((e ** 2).mean() + 1e-30)
        opt.zero_grad(); loss.backward(); opt.step(); tot += loss.item()
        if (k + 1) % 200 == 0: print(f'ep {ep} step {k+1} mean nloss {tot/(k+1):.4f} t={time.time()-t0:.0f}', flush=True)
    r = evaluate(); print(f'ep {ep} held-out ratio {r:.4f} t={time.time()-t0:.0f}', flush=True)
    if r < best:
        best = r; torch.save(dict(ck, net=net.state_dict()), out); print('  saved best', flush=True)
