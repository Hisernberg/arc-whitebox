#!/usr/bin/env python3
"""V34 = V33 + shared Strassen scratch: every (kind, P) role keeps ONE flat buffer sized to the
largest request seen, and each requested shape is a cached reshape view of its prefix. The pruned
inner sizes (896/960) then reuse the full-size (1024) buffers instead of adding their own set
(V33 peak RSS 9.6-11.2 GB vs V32 8.1 GB). Usage: make_v34.py <v33_in.py> <out.py>"""
import sys
src = open(sys.argv[1]).read()
old_buf = src[src.index("    def _buf(self, key, shape):"):src.index("    def level(self, m, kd, w, lev):")]
new_buf = '''    def _flatview(self, key, shape):
        """V34: a cached view of the shared flat buffer of role (kind, P). Growing a role
        drops its cached views (callers still holding one keep the old block alive)."""
        ent = self.pool.get(key)
        if ent is not None and ent[0] is self.flat.get((key[0], key[1]), (None,))[0]:
            v = ent[1].get(shape)
            if v is not None:
                return v
        role = (key[0], key[1])
        size = 1
        for s in shape:
            size *= int(s)
        f = self.flat.get(role)
        if f is None or f[1] < size:
            fb = fnp.empty((size,), dtype=self.dtype)
            fnp.copyto(fb, 0.0)   # metered page touch (first-MLP residual, F80)
            f = (fb, size)
            self.flat[role] = f
        ent = self.pool.get(key)
        if ent is None or ent[0] is not f[0]:
            ent = (f[0], {})
            self.pool[key] = ent
        v = fnp.reshape(f[0][:size], tuple(int(s) for s in shape))
        ent[1][shape] = v
        return v

    def _buf(self, key, shape):
        return self._flatview(key, tuple(shape))

    def _buf2(self, key, shape5):
        shape5 = tuple(int(s) for s in shape5)
        b5 = self._flatview(key, shape5)
        k4 = ("~4",) + shape5
        ent = self.pool[key]
        b4 = ent[1].get(k4)
        if b4 is None:
            b4 = fnp.reshape(b5, (shape5[0], shape5[1] * shape5[2], shape5[3], shape5[4]))
            ent[1][k4] = b4
        return b5, b4

'''
assert src.count(old_buf) == 1
src = src.replace(old_buf, new_buf)
old_init = "        self.pool = {}\n"
assert src.count(old_init) == 1, src.count(old_init)
src = src.replace(old_init, "        self.pool = {}\n        self.flat = {}\n")
old_lp = '        self._lone(A, B, out, LONE_LEV)\n        return out\n'
assert src.count(old_lp) == 1
src = src.replace(old_lp, '        if LP_LEV <= 0:\n            fnp.matmul(A, B, out=out)   # V34: dense (1 op instead of ~45 at level 2)\n        else:\n            self._lone(A, B, out, LP_LEV)\n        return out\n')
old_k = 'LONE_LEV = int(_os.environ.get("V32_LONE_LEV", "2"))\n'
assert src.count(old_k) == 1
src = src.replace(old_k, old_k + 'LP_LEV = int(_os.environ.get("V34_LP_LEV", "0"))   # V34: level of the V33b rerouted join products (0 = dense)\n')
open(sys.argv[2], "w").write(src)
print("ok")
