#!/usr/bin/env python3
"""Run an estimator on one mini MLP (second predict = steady state) and aggregate the flopscope op log
by (op name, operand shapes). Usage: profile_ops.py <estimator.py>  (env knobs apply)"""
import sys, os, glob, collections, importlib.util
import numpy as np, pyarrow.parquet as pq, flopscope as flops, flopscope.numpy as fnp
from whestbench.domain import MLP
spec = importlib.util.spec_from_file_location("est", sys.argv[1]); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
class C: seed = 0; width = 1024; depth = 16; flop_budget = 2 ** 41; api_version = "x"; scratch_dir = None; submission_dir = None
sh = sorted(glob.glob(os.path.expanduser("~/.cache/huggingface/hub/datasets--aicrowd--arc-whestbench-public-2026/snapshots/*/data/mini-*.parquet")))[0]
row = next(pq.ParquetFile(sh).iter_batches(batch_size=1, columns=["weights", "mlp_seed"])).to_pylist()[0]
w = np.asarray(row["weights"], dtype=np.float32).reshape(16, 1024, 1024)
mlp = MLP(width=1024, depth=16, weights=[fnp.asarray(x) for x in w], seed=1)
est = M.Estimator(); est.setup(C())
with flops.BudgetContext(flop_budget=10 ** 14, quiet=True):
    est.predict(mlp, 2 ** 41)   # first call (first-call Strassen level)
with flops.BudgetContext(flop_budget=10 ** 14, quiet=True) as ctx:
    est.predict(mlp, 2 ** 41)
    log = list(ctx._op_log)
tot = ctx.flops_used; U = 2 ** 31
agg = collections.defaultdict(lambda: [0, 0])
ex = log[0]
fields = [a for a in dir(ex) if not a.startswith("_")]
print("OpRecord fields:", fields)
def todict(r):
    return {a: getattr(r, a) for a in fields if not callable(getattr(r, a))}
for r in log:
    d = todict(r)
    name = d.get("op_name") or d.get("name") or d.get("op") or "?"
    shp = d.get("input_shapes") or d.get("shapes") or d.get("operand_shapes") or ""
    fl = d.get("flops") or d.get("flop_cost") or d.get("cost") or 0
    agg[(name, str(shp)[:70])][0] += fl; agg[(name, str(shp)[:70])][1] += 1
print("total C/B %.5f  units %.1f  ops %d" % (tot / 2 ** 41, tot / U, len(log)))
for (nm, sh_), (fl, c) in sorted(agg.items(), key=lambda kv: -kv[1][0])[:28]:
    print("%7.2f u %5.1f%% %5d x  %-14s %s" % (fl / U, 100 * fl / tot, c, nm, sh_))
import resource
print("peak RSS %.2f GB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576))
