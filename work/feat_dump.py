#!/usr/bin/env python3
"""Run the instrumented V29 (dense products) over mini-split MLPs streamed from the HF parquet
shards and save per-MLP feature dumps: feats per layer (dict of (n,) arrays), prediction
(16, n), truth (16, n). Usage: feat_dump.py <start> <stop> [out_dir]"""
import glob, os, sys, time
os.environ.setdefault("V26_STRASSEN", "0")  # dense products: values identical, much faster locally
import numpy as np
import pyarrow.parquet as pq
import flopscope as flops
import flopscope.numpy as fnp
from whestbench.domain import MLP

sys.path.insert(0, "/home/user/arc-whitebox/work")
import estimator_v29_feat as EV

OUT = sys.argv[3] if len(sys.argv) > 3 else "/home/user/arc-whitebox/work/feats"
os.makedirs(OUT, exist_ok=True)
start, stop = int(sys.argv[1]), int(sys.argv[2])


class _Ctx:
    seed = 0
    width = 1024
    depth = 16
    flop_budget = 2 ** 41
    api_version = "x"
    scratch_dir = None
    submission_dir = None


def iter_rows():
    shards = sorted(glob.glob(os.path.expanduser(
        "~/.cache/huggingface/hub/datasets--aicrowd--arc-whestbench-public-2026/snapshots/*/data/mini-*.parquet")))
    i = 0
    for sh in shards:
        pf = pq.ParquetFile(sh)
        for batch in pf.iter_batches(batch_size=1):
            yield i, batch.to_pylist()[0]
            i += 1


est = EV.Estimator()
est.setup(_Ctx())
for i, row in iter_rows():
    if i < start:
        continue
    if i >= stop:
        break
    out = os.path.join(OUT, f"feat_{i:04d}.npz")
    if os.path.exists(out):
        continue
    w = np.asarray(row["weights"], dtype=np.float32).reshape(16, 1024, 1024)
    gt = np.asarray(row["all_layer_means"], dtype=np.float32).reshape(16, 1024)
    ws = [fnp.asarray(x) for x in w]
    mlp = MLP(width=1024, depth=16, weights=ws, seed=int(row["mlp_seed"]) % (2 ** 31))
    EV.FEAT.clear()
    t0 = time.time()
    with flops.BudgetContext(flop_budget=int(1e14), wall_time_limit_s=3600.0, quiet=True) as ctx:
        pred = est.predict(mlp, int(2 ** 41))
        C = float(ctx.flops_used)
    p = np.asarray(pred, dtype=np.float32)
    mse = float(np.mean((p[-1].astype(np.float64) - gt[-1]) ** 2))
    feats = {}
    for d in EV.FEAT:
        li = d["layer"]
        for k, v in d.items():
            if k == "layer":
                continue
            feats[f"L{li:02d}_{k}"] = np.asarray(v, dtype=np.float32)
    np.savez_compressed(out, pred=p, truth=gt, name=str(row["mlp_name"]), mse=mse, flops=C, **feats)
    print(f"[{i:03d}] {row['mlp_name']:22s} mse={mse:.4e} C/B={C / 2 ** 41:.4f} t={time.time() - t0:.0f}s", flush=True)
