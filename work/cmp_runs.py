#!/usr/bin/env python3
"""Compare local whest-run JSON reports (dense) against the V29 per-MLP reference from work/feats."""
import json, sys, glob, numpy as np
ref = {}
for f in sorted(glob.glob('/home/user/arc-whitebox/work/feats/feat_*.npz')):
    d = np.load(f); ref[str(d['name'])] = float(d['mse'])
for fn in sys.argv[1:]:
    try:
        r = json.load(open(fn))['results']
    except Exception:
        print(fn, 'not ready'); continue
    pm = r['per_mlp']
    ratios = [m['final_layer_mse'] / ref[m['mlp_name']] for m in pm if m['mlp_name'] in ref]
    print(f"{fn.split('/')[-1][:-5]:50s} raw {r['final_layer_mse']:.4e} dense C/B {r['mean_compute_utilization']:.4f} "
          f"ratio-vs-V29 mean {np.mean(ratios):.3f} per-MLP {' '.join(f'{x:.3f}' for x in ratios)} failed {r['n_failed_mlps']}")
