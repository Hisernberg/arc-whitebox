#!/usr/bin/env python3
"""Run one mini MLP (two predicts) and list the persistent buffers held by the estimator
(_Pool, Strassen pool/flat) by size, plus peak RSS. Usage: mem_probe.py <estimator.py>"""
import sys, os, glob, collections, importlib.util, resource
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
def st(k):
    for line in open("/proc/self/status"):
        if line.startswith(k): return int(line.split()[1]) / 1048576
import gc; gc.collect()
try:
    pa = __import__("pyarrow"); pa.default_memory_pool().release_unused()
except Exception: pass
print("after load: VmRSS %.2f GB VmHWM %.2f GB" % (st("VmRSS"), st("VmHWM")), flush=True)
open("/proc/self/clear_refs", "w").write("5")   # reset the peak (VmHWM) to the current RSS
def rss(): return st("VmHWM")
est = M.Estimator(); est.setup(C())
for k in range(2):
    with flops.BudgetContext(flop_budget=10 ** 14, quiet=True):
        est.predict(mlp, 2 ** 41)
    print("after predict %d peak %.2f GB" % (k, rss()), flush=True)
seen = {}
def nb(a):
    try:
        base = a
        while getattr(base, "base", None) is not None: base = base.base
        return id(base), int(np.asarray(base).nbytes) if hasattr(base, "nbytes") else 0
    except Exception: return None, 0
def walk(obj, path, depth=0):
    if depth > 4: return
    if hasattr(obj, "shape") and hasattr(obj, "dtype"):
        i, b = nb(obj)
        if i is not None and i not in seen: seen[i] = (b, path)
        return
    if isinstance(obj, dict):
        for k, v in obj.items(): walk(v, path + "/" + str(k)[:40], depth + 1)
    elif isinstance(obj, (list, tuple)):
        for k, v in enumerate(obj): walk(v, path + "[%d]" % k, depth + 1)
    elif hasattr(obj, "__dict__") and depth < 3 and type(obj).__module__ == "est":
        for k, v in vars(obj).items(): walk(v, path + "." + k, depth + 1)
import traceback
try:
    walk(est, "est")
except Exception:
    traceback.print_exc(file=sys.stdout)
tot = sum(b for b, _ in seen.values())
print("held buffers %.2f GB in %d arrays" % (tot / 2 ** 30, len(seen)))
grp = collections.defaultdict(int)
for b, p in seen.values():
    grp[p.split("/")[0] if "/" in p else p] += b
for p, b in sorted(grp.items(), key=lambda x: -x[1])[:12]: print("  %.3f GB  %s" % (b / 2 ** 30, p))
for b, p in sorted(seen.values(), key=lambda x: -x[0])[:25]: print("  %.1f MB  %s" % (b / 2 ** 20, p))
