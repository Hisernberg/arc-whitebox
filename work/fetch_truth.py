#!/usr/bin/env python3
"""Fetch names, seeds and all-layer ground-truth means of every MLP of the public dataset
(mini + full splits) by column-selective remote parquet reads; save work/truth_all.npz."""
import time, glob, os, numpy as np, pyarrow.parquet as pq
from huggingface_hub import HfFileSystem
fs = HfFileSystem()
REPO = "datasets/aicrowd/arc-whestbench-public-2026/data/"
files = sorted(f["name"] for f in fs.ls(REPO, detail=True) if f["name"].endswith(".parquet"))
names, seeds, truths, finals, splits = [], [], [], [], []
t0 = time.time()
for k, fn in enumerate(files):
    for attempt in range(4):
        try:
            with fs.open(fn, "rb") as f:
                t = pq.ParquetFile(f).read(columns=["mlp_name", "mlp_seed", "all_layer_means", "final_means"])
            break
        except Exception as e:
            print("retry", fn, repr(e)[:100], flush=True); time.sleep(5)
    for row in t.to_pylist():
        names.append(row["mlp_name"]); seeds.append(int(row["mlp_seed"]))
        truths.append(np.asarray(row["all_layer_means"], dtype=np.float32).reshape(16, 1024))
        finals.append(np.asarray(row["final_means"], dtype=np.float32))
        splits.append("mini" if "mini-" in fn else "full")
    print(f"[{k + 1}/{len(files)}] {os.path.basename(fn)} rows {t.num_rows} total {len(names)} t={time.time() - t0:.0f}s", flush=True)
np.savez_compressed("/home/user/arc-whitebox/work/truth_all.npz", names=np.array(names), seeds=np.array(seeds, dtype=np.int64),
                    truth=np.stack(truths), final=np.stack(finals), split=np.array(splits))
print("saved", len(names), "MLPs; distinct names", len(set(names)))
