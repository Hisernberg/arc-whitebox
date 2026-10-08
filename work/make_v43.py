#!/usr/bin/env python3
"""V43: symmetric product C_pre = (W C) W^T on a g x g block partition (g = V43_SYM_SPLIT, default 4):
only the g(g+1)/2 upper blocks are computed (one Strassen family) and mirrored; g = 2 is V29's 3-of-4.
Usage: make_v43.py <src.py> <dst.py>"""
import sys
src, dst = sys.argv[1:3]
s = open(src).read()
a = '''        h = n // 2
        if n % 2 or n < 4:
            return fnp.matmul(X, Y, out=out)
        pool = self._pool
        X3 = pool.get("sym_x", (3, 1, h, n))
        Y3 = pool.get("sym_y", (3, 1, n, h))
        O3 = pool.get("sym_o", (3, 1, h, h))
        fnp.copyto(X3[0, 0], X[:h]); fnp.copyto(X3[1, 0], X[:h]); fnp.copyto(X3[2, 0], X[h:])
        fnp.copyto(Y3[0, 0], Y[:, :h]); fnp.copyto(Y3[1, 0], Y[:, h:]); fnp.copyto(Y3[2, 0], Y[:, h:])
        self._smm.mm(X3, Y3, O3, self._smm.level(h, n, h, lev))
        fnp.copyto(out[:h, :h], O3[0, 0]); fnp.copyto(out[:h, h:], O3[1, 0])
        fnp.copyto(out[h:, h:], O3[2, 0]); fnp.copyto(out[h:, :h], O3[1, 0].T)
        return out
'''
b = '''        g = SYM_SPLIT if (n % SYM_SPLIT == 0 and n >= 4 * SYM_SPLIT) else 2   # V43: g x g partition
        h = n // g
        if n % 2 or n < 4:
            return fnp.matmul(X, Y, out=out)
        pool = self._pool
        pairs = [(i, j) for i in range(g) for j in range(i, g)]
        P = len(pairs)
        Xb = pool.get("sym_x%d_%d" % (g, h), (P, 1, h, n))
        Yb = pool.get("sym_y%d_%d" % (g, h), (P, 1, n, h))
        Ob = pool.get("sym_o%d_%d" % (g, h), (P, 1, h, h))
        for k, (i, j) in enumerate(pairs):
            fnp.copyto(Xb[k, 0], X[i * h:(i + 1) * h]); fnp.copyto(Yb[k, 0], Y[:, j * h:(j + 1) * h])
        self._smm.mm(Xb, Yb, Ob, self._smm.level(h, n, h, lev))
        for k, (i, j) in enumerate(pairs):
            fnp.copyto(out[i * h:(i + 1) * h, j * h:(j + 1) * h], Ob[k, 0])
            if i != j:
                fnp.copyto(out[j * h:(j + 1) * h, i * h:(i + 1) * h], Ob[k, 0].T)
        return out
'''
assert s.count(a) == 1, "sym_product body not found"
s = s.replace(a, b)
a2 = 'def _lt_from_dict(d):\n'
assert s.count(a2) == 1
s = s.replace(a2, 'SYM_SPLIT = int(_os.environ.get("V43_SYM_SPLIT", "4"))   # V43: block partition of the symmetric C_pre product\n\n\n' + a2)
open(dst, "w").write(s); print("V43 written", dst)
