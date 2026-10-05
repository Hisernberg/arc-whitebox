#!/usr/bin/env python3
"""V35 = V34 + residual trims in the Strassen helper: one-dict fast path for pooled buffer views
(exact shapes, so the [:b] re-slices go away), and cached per-product slot views (buf[:, i]) for the
combos / assemble steps (7-8 fewer view creations per call). Same ops in the same order: predictions
are bit-identical. Usage: make_v35.py <v34_in.py> <out.py>"""
import sys
src = open(sys.argv[1]).read()
def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, (c, old[:80])
    src = src.replace(old, new)

rep("        self.pool = {}\n        self.flat = {}\n",
    "        self.pool = {}\n        self.flat = {}\n        self.fast = {}    # V35: (key, shape) -> view\n        self.fast2 = {}   # V35: (key, shape5) -> (b5, b4, slot views)\n")
# growth invalidates the fast caches (old blocks are released)
rep("            f = (fb, size)\n            self.flat[role] = f\n",
    "            f = (fb, size)\n            self.flat[role] = f\n            self.fast.clear(); self.fast2.clear()\n")
# _buf / _buf2 fast paths
rep('''    def _buf(self, key, shape):
        return self._flatview(key, tuple(shape))
''', '''    def _buf(self, key, shape):
        fk = (key, shape)
        v = self.fast.get(fk)
        if v is None:
            v = self._flatview(key, tuple(shape))
            self.fast[fk] = v
        return v
''')
rep('''    def _buf2(self, key, shape5):
        shape5 = tuple(int(s) for s in shape5)
''', '''    def _buf2(self, key, shape5):
        e = self._buf2s(key, shape5)
        return e[0], e[1]

    def _buf2s(self, key, shape5):
        """V35: (b5, b4, (b5[:, 0], ..., b5[:, 6])) for a pooled 7-slot buffer, cached."""
        fk = (key, shape5)
        e = self.fast2.get(fk)
        if e is None:
            b5, b4 = self._buf2_make(key, shape5)
            e = (b5, b4, tuple(b5[:, i] for i in range(7)))
            self.fast2[fk] = e
        return e

    def _buf2_make(self, key, shape5):
        shape5 = tuple(int(s) for s in shape5)
''')
# combos: slot views
old_c = src[src.index("        buf, buf4 = self._buf2(key, (b, 7, P, h, q))\n"):src.index("        return buf4\n")]
new_c = old_c.replace("buf, buf4 = self._buf2(key, (b, 7, P, h, q))", "buf, buf4, S = self._buf2s(key, (b, 7, P, h, q))")
for i in range(7):
    new_c = new_c.replace("buf[:, %d]" % i, "S[%d]" % i)
assert "buf[:" not in new_c
rep(old_c, new_c)
# assemble takes the slot views
rep('''    @staticmethod
    def _assemble(M, out):
        """M (b, 7, P, h, w) products -> out (b, P, m, w) quadrants (8 ops)."""
        h, w = M.shape[3], M.shape[4]
''', '''    @staticmethod
    def _assemble(M, out):
        """M = slot views (M_0..M_6) of the (b, 7, P, h, w) products -> out (b, P, m, w) quadrants (8 ops)."""
        h, w = M[0].shape[2], M[0].shape[3]
''')
old_a = src[src.index('        C11, C12 = out[..., :h, :w], out[..., :h, w:]\n'):src.index("    def mm(self, X, Y, out, lev):")]
new_a = old_a
for i in range(7):
    new_a = new_a.replace("M[:, %d]" % i, "M[%d]" % i)
rep(old_a, new_a)
rep("        Mb, Mb4 = self._buf2(mkey, (by, 7, P, h, v))\n", "        Mb, Mb4, Ms = self._buf2s(mkey, (by, 7, P, h, v))\n")
rep("        self._assemble(Mb, out)\n", "        self._assemble(Ms, out)\n")
rep('        Mb, Mb4 = self._buf2(("HM", P, h, v), (1, 7, P, h, v))\n', '        Mb, Mb4, Ms = self._buf2s(("HM", P, h, v), (1, 7, P, h, v))\n')
rep("        self._assemble(Mb, out[None])\n", "        self._assemble(Ms, out[None])\n")
# exact-shape views: drop the redundant re-slices
for a, b in [("(bx, P, h, q))[:bx]", "(bx, P, h, q))"), ("(by, P, q, v))[:by]", "(by, P, q, v))"), ("(by, P, h, v))[:by]", "(by, P, h, v))"),
             ("(k, P, m, w))[:k]", "(k, P, m, w))"), ("(k, P, h, q))[:k]", "(k, P, h, q))"), ("(k, P, v, q))[:k]", "(k, P, v, q))"), ("(k, P, h, v))[:k]", "(k, P, h, v))")]:
    rep(a, b)
open(sys.argv[2], "w").write(src)
print("ok")
