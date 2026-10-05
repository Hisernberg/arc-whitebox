#!/usr/bin/env python3
"""V36 = V35 + cached quadrant views: the Strassen recursion slices its operands / outputs into
quadrants (X[..., :h, :q] ...) on every call; for pool-owned buffers (every operand below the top
level) those views are now made once and reused, as are out[None] and Mb4[0]. Same ops in the same
order (bit-identical predictions); fewer view creations -> less residual time.
Usage: make_v36.py <v35_in.py> <out.py>"""
import sys
src = open(sys.argv[1]).read()
def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, (c, old[:90])
    src = src.replace(old, new)

rep("        self.fast2 = {}   # V35: (key, shape5) -> (b5, b4, slot views)\n",
    "        self.fast2 = {}   # V35: (key, shape5) -> (b5, b4, slot views)\n        self.owned = {}   # V36: id -> pool-owned view (kept alive while cached)\n        self.qc = {}      # V36: cached quadrant / [None] / [0] views of owned views\n")
rep("            self.fast.clear(); self.fast2.clear()\n",
    "            self.fast.clear(); self.fast2.clear(); self.owned.clear(); self.qc.clear()\n")
rep('''            v = self._flatview(key, tuple(shape))
            self.fast[fk] = v
''', '''            v = self._flatview(key, tuple(shape))
            self.fast[fk] = v
            self.owned[id(v)] = v
''')
rep('''            e = (b5, b4, tuple(b5[:, i] for i in range(7)))
            self.fast2[fk] = e
''', '''            e = (b5, b4, tuple(b5[:, i] for i in range(7)))
            self.fast2[fk] = e
            self.owned[id(b5)] = b5; self.owned[id(b4)] = b4
''')
# helpers, inserted before _combos
rep('''    def _combos(self, X, Q, kind, key):''', '''    def _quads(self, X):
        """V36: (X11, X12, X21, X22) halves of the last two axes; cached for pool-owned views."""
        i = id(X)
        own = i in self.owned
        if own:
            e = self.qc.get(i)
            if e is not None:
                return e
        h, q = X.shape[-2] // 2, X.shape[-1] // 2
        e = (X[..., :h, :q], X[..., :h, q:], X[..., h:, :q], X[..., h:, q:])
        if own:
            self.qc[i] = e
        return e

    def _sub(self, X, tag):
        """V36: X[None] (tag 'n') or X[0] (tag '0'), cached and owned when X is pool-owned."""
        i = id(X)
        if i not in self.owned:
            return X[None] if tag == "n" else X[0]
        k = (tag, i)
        e = self.qc.get(k)
        if e is None:
            e = X[None] if tag == "n" else X[0]
            self.qc[k] = e
            self.owned[id(e)] = e
        return e

    def _combos(self, X, Q, kind, key):''')
rep('''    @staticmethod
    def _assemble(M, out):''', '''    def _assemble(self, M, out):''')
rep('''        C11, C12 = out[..., :h, :w], out[..., :h, w:]
        C21, C22 = out[..., h:, :w], out[..., h:, w:]
''', '''        C11, C12, C21, C22 = self._quads(out)
''')
rep("        XQ = (X[..., :h, :q], X[..., :h, q:], X[..., h:, :q], X[..., h:, q:])\n", "        XQ = self._quads(X)\n", 2)
rep("        YQ = (Y[..., :q, :v], Y[..., :q, v:], Y[..., q:, :v], Y[..., q:, v:])\n", "        YQ = self._quads(Y)\n")
rep("        YQ = (Y[..., :v, :q], Y[..., v:, :q], Y[..., :v, q:], Y[..., v:, q:])\n", "        _y = self._quads(Y)\n        YQ = (_y[0], _y[2], _y[1], _y[3])\n")
rep("(out[..., :h, :v], out[..., :h, v:], out[..., h:, :v], out[..., h:, v:])", "self._quads(out)", 2)
rep("        self.hub(Xc, Yc, Mb4[0], lev - 1)\n", "        self.hub(Xc, Yc, self._sub(Mb4, \"0\"), lev - 1)\n")
rep("        self._assemble(Ms, out[None])\n", "        self._assemble(Ms, self._sub(out, \"n\"))\n")
open(sys.argv[2], "w").write(src)
print("ok")
