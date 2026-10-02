#!/usr/bin/env python3
"""Convert a trained gru_model.npz (from gru_corr.py) into gru_model.json for the estimator."""
import json, sys, numpy as np
src, dst = sys.argv[1], sys.argv[2]
d = np.load(src, allow_pickle=False)
out = {"H": int(d["H"]), "sig_mu": float(d["sig_mu"]), "feats": [str(x) for x in d["feats"]], "act": (str(d["act"]) if "act" in d.files else "tanh"),
       "mu_f": d["mu_f"].astype(np.float32).tolist(), "sd_f": d["sd_f"].astype(np.float32).tolist(),
       "Wih": d["cell.weight_ih"].tolist(), "Whh": d["cell.weight_hh"].tolist(),
       "bih": d["cell.bias_ih"].tolist(), "bhh": d["cell.bias_hh"].tolist(),
       "W1": d["ro.0.weight"].tolist(), "b1": d["ro.0.bias"].tolist(),
       "W2": d["ro.2.weight"].tolist(), "b2": d["ro.2.bias"].tolist()}
json.dump(out, open(dst, "w"))
print("wrote", dst, "bytes", len(open(dst).read()))
