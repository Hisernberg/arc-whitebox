#!/usr/bin/env python3
"""Per-MLP cost/raw/residual of local Strassen runs vs the V29 feature-dump reference."""
import json, sys, glob, numpy as np
ref = {str(np.load(f)["name"]): float(np.load(f)["mse"]) for f in sorted(glob.glob("/home/user/arc-whitebox/work/feats/feat_*.npz"))[:8]}
for fn in sys.argv[1:]:
    try:
        r = json.load(open(fn))["results"]
    except Exception:
        print(fn.split("/")[-1], "not ready"); continue
    for m in r["per_mlp"]:
        print(f"{fn.split('/')[-1][5:-5]:40s} {m['mlp_name'][:16]:16s} C/B {m['flops_used'] / 2 ** 41:.5f} raw {m['final_layer_mse']:.5e} (ref {ref.get(m['mlp_name'], float('nan')):.5e}) resid {m.get('residual_wall_time_s', 0):.3f} wall {m.get('wall_time_s', 0):.0f}s")
