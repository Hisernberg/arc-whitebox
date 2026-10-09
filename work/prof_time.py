#!/usr/bin/env python3
"""Run an estimator on one mini MLP (second predict = steady state) and aggregate the flopscope op log
by (op name, operand shapes). Usage: profile_ops.py <estimator.py>  (env knobs apply)"""
import sys, os, glob, collections, importlib.util
import numpy as np, pyarrow.parquet as pq, flopscope as flops, flopscope.numpy as fnp
from whestbench.domain import MLP
spec = importlib.util.spec_from_file_location("est", sys.argv[1]); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
class C: seed = 0; width = 1024; depth = 16; flop_budget = 2 ** 41; api_version = "x"; scratch_dir = None; submission_dir = None
T = np.load("/home/user/arc-whitebox/work/truth_all.npz")
_i = [k for k in range(len(T["names"])) if str(T["names"][k]) == os.environ.get("PROF_MLP", "logan-fitzgerald")][0]
from numpy.random import SeedSequence, default_rng
_rng = default_rng(SeedSequence(int(T["seeds"][_i])).spawn(3)[0])
w = np.stack([(_rng.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16).astype(np.float32) for _ in range(16)]); del T
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
byn = collections.Counter()
for (nm, sh_), (fl, c) in agg.items(): byn[nm] += c
print('by op name:', ', '.join('%s %d' % kv for kv in byn.most_common(25)))

tagg = collections.defaultdict(lambda: [0.0, 0.0, 0])
for r in log:
    d = todict(r)
    name = d.get("op_name") or "?"
    shp = d.get("shapes") or ""
    key = (name, str(shp)[:60])
    tagg[key][0] += float(d.get("flopscope_backend_duration_s") or 0); tagg[key][1] += float(d.get("flopscope_overhead_duration_s") or 0); tagg[key][2] += 1
tb = sum(v[0] for v in tagg.values()); to = sum(v[1] for v in tagg.values())
print("WALL backend %.1f s  overhead %.1f s" % (tb, to))
for k, v in sorted(tagg.items(), key=lambda kv: -(kv[1][0] + kv[1][1]))[:30]:
    print("  %6.2f s backend %5.2f s ovh %5d x %-12s %s" % (v[0], v[1], v[2], k[0], k[1]))
byt = collections.defaultdict(lambda: [0.0, 0.0, 0])
for (nm, sh_), v in tagg.items():
    byt[nm][0] += v[0]; byt[nm][1] += v[1]; byt[nm][2] += v[2]
print("WALL by op name:", ", ".join("%s %.1f+%.1f s (%d)" % (k, v[0], v[1], v[2]) for k, v in sorted(byt.items(), key=lambda kv: -(kv[1][0] + kv[1][1]))[:15]))
import resource
print("peak RSS %.2f GB" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1048576))
