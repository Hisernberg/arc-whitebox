#!/usr/bin/env python3
"""cProfile one steady-state predict (after a warm-up predict); print the estimator's own functions
by self time (proxy for grader residual time). Usage: py_prof.py <estimator.py>"""
import sys, os, cProfile, pstats, importlib.util, io
import numpy as np, flopscope as flops, flopscope.numpy as fnp
from whestbench.domain import MLP
spec = importlib.util.spec_from_file_location("est", sys.argv[1]); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
class C: seed = 0; width = 1024; depth = 16; flop_budget = 2 ** 41; api_version = "x"; scratch_dir = None; submission_dir = None
T = np.load("/home/user/arc-whitebox/work/truth_all.npz")
_i = [k for k in range(len(T["names"])) if str(T["names"][k]) == "logan-fitzgerald"][0]
from numpy.random import SeedSequence, default_rng
_rng = default_rng(SeedSequence(int(T["seeds"][_i])).spawn(3)[0])
w = np.stack([(_rng.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float16).astype(np.float32) for _ in range(16)]); del T
mlp = MLP(width=1024, depth=16, weights=[fnp.asarray(x) for x in w], seed=1)
est = M.Estimator(); est.setup(C())
with flops.BudgetContext(flop_budget=10 ** 14, quiet=True):
    est.predict(mlp, 2 ** 41)
pr = cProfile.Profile()
with flops.BudgetContext(flop_budget=10 ** 14, quiet=True):
    pr.enable(); _out = est.predict(mlp, 2 ** 41); pr.disable()
if os.environ.get('PRED_OUT'): np.save(os.environ['PRED_OUT'], np.asarray(_out))
s = io.StringIO(); ps = pstats.Stats(pr, stream=s)
st = ps.stats
own = [(v[2], v[3], v[1], k) for k, v in st.items() if k[0] == sys.argv[1]]
tot_own = sum(x[0] for x in own)
print("estimator self time %.3f s over %d functions" % (tot_own, len(own)))
for tt, ct, nc, k in sorted(own, reverse=True)[:25]:
    print("%7.3f s self %7.3f s cum %7d calls  %s:%d %s" % (tt, ct, nc, os.path.basename(k[0]), k[1], k[2]))
