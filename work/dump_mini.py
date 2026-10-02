"""Dump mini-split MLPs (weights + baked N=1e9 truth) to .npz, streaming the parquet shard."""
import glob, os, sys
import numpy as np
import pyarrow.parquet as pq

OUT = "/home/user/arc-whitebox/work/dumps"
shards = sorted(glob.glob(os.path.expanduser("~/.cache/huggingface/hub/datasets--aicrowd--arc-whestbench-public-2026/snapshots/*/data/mini-*.parquet")))
n_want = int(sys.argv[1]) if len(sys.argv) > 1 else 8
done = 0
for sh in shards:
    pf = pq.ParquetFile(sh)
    print(sh, pf.metadata.num_rows, pf.schema_arrow.names, flush=True)
    for batch in pf.iter_batches(batch_size=1):
        row = batch.to_pylist()[0]
        w = np.asarray(row["weights"], dtype=np.float32).reshape(16, 1024, 1024)
        gt = np.asarray(row["all_layer_means"], dtype=np.float32).reshape(16, 1024)
        fin = np.asarray(row["final_means"], dtype=np.float32)
        assert np.allclose(gt[-1], fin)
        name = row.get("mlp_name") or f"mlp{row.get('mlp_id', done)}"
        out = os.path.join(OUT, f"mlp_{done:04d}.npz")
        np.savez(out, weights=w, all_layer_means=gt, final_means=fin, name=str(name),
                 avg_variance=np.float64(row.get("avg_variance", np.nan)), mlp_seed=np.int64(row.get("mlp_seed", -1)))
        print(f"[OK] {out} {name} seed={row.get('mlp_seed')} avg_var={row.get('avg_variance')}", flush=True)
        done += 1
        if done >= n_want:
            sys.exit(0)
