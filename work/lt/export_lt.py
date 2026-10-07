"""Export the LT model (work/lt/lt_model.pt) to JSON for make_v41.py."""
import sys, json, torch, numpy as np
ck = torch.load(sys.argv[1], weights_only=False); sd = ck['net']; F = ck['F']
lin = [k[:-7] for k in sd if k.endswith('.weight')]
Ws = [sd[k + '.weight'].numpy().astype(np.float64) for k in lin]; bs = [sd[k + '.bias'].numpy().astype(np.float64) for k in lin]
W1 = Ws[0]   # (H, F+16)
out = {"kind": "lt", "F": F, "H": int(ck['hidden']),
       "mu": ck['mu'][:, 0, :].tolist(), "sd": ck['sd'][:, 0, :].tolist(), "es": ck['es'][:, 0].tolist(),
       "W1T": W1[:, :F].T.tolist(),                                  # (F, H)
       "b1L": [(bs[0] + W1[:, F + l]).tolist() for l in range(16)],   # per-layer bias incl. one-hot column
       "W2T": Ws[1].T.tolist(), "b2": bs[1].tolist(), "W3T": Ws[2].T.tolist(), "b3": bs[2].tolist(),
       "w4": Ws[3][0].tolist(), "b4": float(bs[3][0])}
json.dump(out, open(sys.argv[2], 'w')); print('exported', sys.argv[2], 'F', F, 'H', out['H'])
