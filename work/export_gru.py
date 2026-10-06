#!/usr/bin/env python3
"""Convert a trained gru_model.npz (from gru_corr.py) into gru_model.json for the estimator."""
import json, sys, numpy as np
argv = sys.argv[1:]
alpha = 1.0
if "--alpha" in argv:
    i = argv.index("--alpha"); alpha = float(argv[i + 1]); del argv[i:i + 2]   # scales every member's correction
srcs, dst = argv[:-1], argv[-1]
outs = []
for src in srcs:
  d = np.load(src, allow_pickle=False)
  out = {"H": int(d["H"]), "sig_mu": float(d["sig_mu"]) * alpha, "feats": [str(x) for x in d["feats"]], "act": (str(d["act"]) if "act" in d.files else "tanh"), "resid": (bool(d["resid"]) if "resid" in d.files else False), "hprop": (bool(d["hprop"]) if "hprop" in d.files else False),
       "mu_f": d["mu_f"].astype(np.float32).tolist(), "sd_f": d["sd_f"].astype(np.float32).tolist(),
       "Wih": d["cell.weight_ih"].tolist(), "Whh": d["cell.weight_hh"].tolist(),
       "bih": d["cell.bias_ih"].tolist(), "bhh": d["cell.bias_hh"].tolist(),
       "W1": d["ro.0.weight"].tolist(), "b1": d["ro.0.bias"].tolist(),
       "W2": d["ro.2.weight"].tolist(), "b2": d["ro.2.bias"].tolist()}
  outs.append(out)
json.dump(outs[0] if len(outs) == 1 else outs, open(dst, "w"))
print("wrote", dst, "models", len(outs), "bytes", len(open(dst).read()))
