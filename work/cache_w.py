#!/usr/bin/env python3
"""Cache the weights of mini-split MLPs that have a feature dump as float16 .npy (16, n, n) in
work/feats/W_XXXX.npy (for the corrector training's mean-transport messages)."""
import glob, os, sys
import numpy as np, pyarrow.parquet as pq
FE = "/home/user/arc-whitebox/work/feats"
shards = sorted(glob.glob(os.path.expanduser(
    "~/.cache/huggingface/hub/datasets--aicrowd--arc-whestbench-public-2026/snapshots/*/data/mini-*.parquet")))
i = 0
for sh in shards:
    pf = pq.ParquetFile(sh)
    for batch in pf.iter_batches(batch_size=1, columns=["mlp_name", "weights"]):
        out = f"{FE}/W_{i:04d}.npy"
        if os.path.exists(f"{FE}/feat_{i:04d}.npz") and not os.path.exists(out):
            row = batch.to_pylist()[0]
            name = str(np.load(f"{FE}/feat_{i:04d}.npz")["name"])
            assert name == row["mlp_name"], (i, name, row["mlp_name"])
            np.save(out, np.asarray(row["weights"], dtype=np.float32).reshape(16, 1024, 1024).astype(np.float16))
            print("cached", i, name, flush=True)
        i += 1
