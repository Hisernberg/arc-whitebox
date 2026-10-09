#!/usr/bin/env python3
"""Evaluate an estimator on MLPs regenerated from their seeds (no dataset download): final-layer MSE against the
1e9-sample truth in truth_all.npz, and C/B from the flopscope counter. One warm-up predict first (steady state).
Usage: eval_seeds.py <estimator.py> <split full|mini> <n> [offset]   (env knobs apply)"""
import sys, time, importlib.util
import numpy as np, flopscope as flops, flopscope.numpy as fnp
from numpy.random import SeedSequence, default_rng
from whestbench.domain import MLP
spec = importlib.util.spec_from_file_location("est", sys.argv[1]); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
split, n = sys.argv[2], int(sys.argv[3]); off = int(sys.argv[4]) if len(sys.argv) > 4 else 0
T = np.load("/home/user/arc-whitebox/work/truth_all.npz")
idx = [i for i in range(len(T["split"])) if str(T["split"][i]) == split][off:off + n]
class C: seed = 0; width = 1024; depth = 16; flop_budget = 2 ** 41; api_version = "x"; scratch_dir = None; submission_dir = None
def mlp_of(seed):
    r = default_rng(SeedSequence(int(seed)).spawn(3)[0])
    w = [(r.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float32) for _ in range(16)]
    return MLP(width=1024, depth=16, weights=[fnp.asarray(x) for x in w], seed=1)
est = M.Estimator(); est.setup(C())
with flops.BudgetContext(flop_budget=10 ** 14, quiet=True):
    est.predict(mlp_of(T["seeds"][idx[0]]), 2 ** 41)
mses, cbs = [], []
for i in idx:
    m = mlp_of(T["seeds"][i]); t0 = time.time()
    with flops.BudgetContext(flop_budget=10 ** 14, quiet=True) as ctx:
        out = est.predict(m, 2 ** 41)
    pred = np.asarray(out)[-1] if np.asarray(out).ndim == 2 else np.asarray(out)
    mse = float(np.mean((pred - T["final"][i]) ** 2)); cb = ctx.flops_used / 2 ** 41
    mses.append(mse); cbs.append(cb)
    print("%s mse %.4e C/B %.4f wall %.0f s" % (str(T["names"][i]), mse, cb, time.time() - t0), flush=True)
mse, cb = float(np.mean(mses)), float(np.mean(cbs))
print("MEAN raw %.4e C/B %.4f score %.4e n %d" % (mse, cb, mse * max(0.1, cb), len(idx)))
