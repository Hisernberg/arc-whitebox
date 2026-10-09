#!/usr/bin/env python3
"""Per-family FLOP attribution: every top-level call from Estimator._predict_core into a heavy helper
(_Strassen.mm/hub, _sym_product, _lone, _lp, _gru_step, _expand) runs in a flopscope namespace named
'<helper>_L<caller line>'; everything else is 'inline'. Usage: profile_ns.py <estimator.py>  (env knobs apply)"""
import sys, os, inspect, functools, collections, importlib.util
import numpy as np, flopscope as flops, flopscope.numpy as fnp
from whestbench.domain import MLP
spec = importlib.util.spec_from_file_location("est", sys.argv[1]); M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
depth = [0]
def wrap(cls, name):
    f = getattr(cls, name)
    @functools.wraps(f)
    def g(*a, **k):
        if depth[0] or flops.namespace is None:
            return f(*a, **k)
        fr = inspect.currentframe().f_back
        depth[0] += 1
        try:
            with flops.namespace("%s_L%d" % (name.strip("_"), fr.f_lineno)):
                return f(*a, **k)
        finally:
            depth[0] -= 1
    setattr(cls, name, g)
for n in ("mm", "hub"): wrap(M._Strassen, n)
for n in ("_sym_product", "_lone", "_lp", "_gru_step", "_expand"):
    if hasattr(M.Estimator, n): wrap(M.Estimator, n)
class C: seed = 0; width = 1024; depth = 16; flop_budget = 2 ** 41; api_version = "x"; scratch_dir = None; submission_dir = None
from numpy.random import SeedSequence, default_rng
_rng = default_rng(SeedSequence(int(os.environ.get("PROF_SEED", "12345"))).spawn(3)[0])
w = np.stack([(_rng.standard_normal((1024, 1024)) * np.sqrt(2.0 / 1024)).astype(np.float32) for _ in range(16)])
mlp = MLP(width=1024, depth=16, weights=[fnp.asarray(x) for x in w], seed=1)
est = M.Estimator(); est.setup(C())
with flops.BudgetContext(flop_budget=10 ** 14, quiet=True):
    est.predict(mlp, 2 ** 41)
with flops.BudgetContext(flop_budget=10 ** 14, quiet=True) as ctx:
    est.predict(mlp, 2 ** 41)
    log = list(ctx._op_log)
tot = ctx.flops_used
agg = collections.defaultdict(lambda: [0, 0, 0.0])
for r in log:
    k = r.namespace or "inline"
    agg[k][0] += r.flop_cost; agg[k][1] += 1; agg[k][2] += (r.flopscope_backend_duration_s or 0) + (r.flopscope_overhead_duration_s or 0)
print("total C/B %.5f ops %d" % (tot / 2 ** 41, len(log)))
for k, (fl, c, t) in sorted(agg.items(), key=lambda kv: -kv[1][0]):
    print("%6.2f%% C/B %.5f  %6d ops  %6.1f s  %s" % (100 * fl / tot, fl / 2 ** 41, c, t, k))
