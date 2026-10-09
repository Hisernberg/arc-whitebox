#!/usr/bin/env python3
"""V44 (Track B): replace the 4-operand einsum PK2 = einsum("tij,ti,tj,tg->gij", AB, WL2, WR2, IND2) by two in-place
broadcast multiplies on the AB buffer and contiguous group sums (IND2 is a 0/1 indicator whose terms are grouped by g
in order). Same values up to summation order; fewer FLOPs and ~5x less wall time on that op.
Usage: make_v44.py <src.py> <dst.py>"""
import sys
src, dst = sys.argv[1:3]
s = open(src).read()
a = '                PK2 = fnp.einsum("tij,ti,tj,tg->gij", ABstack, WL2, WR2, fpm["IND2"])\n'
assert s.count(a) == 1, "PK2 einsum not found"
b = '''                # V44: AB * WL2 (rows) * WR2 (cols) in place, then contiguous group sums (IND2 is a 0/1 indicator)
                fnp.multiply(ABstack, WL2[:, :, None], out=ABstack)
                fnp.multiply(ABstack, WR2[:, None, :], out=ABstack)
                gid = [row.index(1.0) for row in prog["IND2"]]
                n2_ = ABstack.shape[1]
                parts = []
                for g_ in range(len(prog["IND2"][0])):
                    ts_ = [t_ for t_ in range(len(gid)) if gid[t_] == g_]
                    if not ts_:
                        parts.append(fnp.zeros((n2_, n2_), dtype=f32))
                    elif len(ts_) == 1:
                        parts.append(ABstack[ts_[0]])
                    else:
                        assert ts_ == list(range(ts_[0], ts_[-1] + 1)), "V44: IND2 groups not contiguous"
                        parts.append(fnp.sum(ABstack[ts_[0]:ts_[-1] + 1], axis=0))
                PK2 = fnp.stack(parts, axis=0)
'''
s = s.replace(a, b)
open(dst, "w").write(s); print("V44 written", dst)
