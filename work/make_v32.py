#!/usr/bin/env python3
"""V32 = input estimator (V29/V31 family) + Strassen pricing of the join's lone dense products
(range finder, projections, rotations, basis transports, tier-2 formings) through the existing
`smm.mm` family code. Dense mode (V26_STRASSEN=0) is value-identical to the input.
Usage: make_v32.py <in.py> <out.py>"""
import ast, sys
src = open(sys.argv[1]).read()
def rep(old, new, count=1):
    global src
    assert src.count(old) == count, (src.count(old), old[:90])
    src = src.replace(old, new)

rep('''STRASSEN_FIRST = int(_os.environ.get("V28_STRASSEN_FIRST", "4"))''',
'''STRASSEN_FIRST = int(_os.environ.get("V28_STRASSEN_FIRST", "4"))
LONE_LEV = int(_os.environ.get("V32_LONE_LEV", "5"))   # V32: level cap of the lone join products (0 = V29 op stream)''')

# helper on the Estimator: one (m, kd) @ (kd, w) product, or a batched right operand (by, 1, kd, w), into out
rep('''    def _gru_step(self, li, fd, W, gst, n):''',
'''    def _lone(self, A, B, out, lev):
        """V32: Strassen-priced lone product A (m, kd) @ B (kd, w) -> out (m, w); B and out may be
        batched 4-D slabs (by, 1, kd, w) / (by, 1, m, w) (the rotation of the old factors)."""
        smm = self._smm
        if B.ndim == 2:
            smm.mm(A[None, None], B[None, None], out[None, None], smm.level(A.shape[0], A.shape[1], B.shape[1], lev))
        else:
            smm.mm(A[None, None], B, out, smm.level(A.shape[0], A.shape[1], B.shape[3], lev))

    def _gru_step(self, li, fd, W, gst, n):''')

# range finder (4 products per pass) and the core sandwich
rep('''                        fnp.matmul(Aj.T, Om, out=Yq1)
                        fnp.multiply(dAj, Yq1, out=Yq1)
                        fnp.matmul(Aj, Yq1, out=Yq)
                        fnp.matmul(Pj.T, Om, out=Yq1)
                        fnp.multiply(dPj, Yq1, out=Yq1)
                        fnp.matmul(Pj, Yq1, out=Yq2)''',
'''                        self._lone(Aj.T, Om, Yq1, LONE_LEV)
                        fnp.multiply(dAj, Yq1, out=Yq1)
                        self._lone(Aj, Yq1, Yq, LONE_LEV)
                        self._lone(Pj.T, Om, Yq1, LONE_LEV)
                        fnp.multiply(dPj, Yq1, out=Yq1)
                        self._lone(Pj, Yq1, Yq2, LONE_LEV)''')
rep('''                            fnp.matmul(Qp, Sfull @ (Qp.T @ Om), out=Yq2)''',
'''                            self._lone(Qp, Sfull @ (Qp.T @ Om), Yq2, LONE_LEV)''')
# projections of the joiner
rep('''                    FAj = fnp.matmul(Qn.T, Aj, out=fap_new[m1, 0])
                    FPj = fnp.matmul(Qn.T, Pj, out=fap_new[m1, 1])''',
'''                    FAj = fap_new[m1, 0]
                    self._lone(Qn.T, Aj, FAj, LONE_LEV)
                    FPj = fap_new[m1, 1]
                    self._lone(Qn.T, Pj, FPj, LONE_LEV)''')
# rotation of the tier-1 factors: batched through the old side's 4-D view
rep('''                            fnp.matmul(Tq[None, None], FAP, out=fap_new[:m1])''',
'''                            self._lone(Tq, fap4[2 * fa_off:2 * (fa_off + m1)], fap4_new[:2 * m1], LONE_LEV)''')
# tier-2 move: projections and rotation
rep('''                        fnp.matmul(Un.T, FA1, out=fap2_new[kb, 0])
                        fnp.matmul(Un.T, FP1, out=fap2_new[kb, 1])''',
'''                        self._lone(Un.T, FA1, fap2_new[kb, 0], LONE_LEV)
                        self._lone(Un.T, FP1, fap2_new[kb, 1], LONE_LEV)''')
rep('''                            fnp.matmul(T2[None, None], FAP2, out=fap2_new[:kb])''',
'''                            self._lone(T2, fap24[:2 * kb], fap24_new[:2 * kb], LONE_LEV)''')
# basis transports and the tier-2 lift
rep('''                    Qc = fnp.matmul(W, Qn, out=pool.get(("qc", qc_side), (n, r_old)))  # wick already inside Qn''',
'''                    Qc = pool.get(("qc", qc_side), (n, r_old))  # wick already inside Qn
                    self._lone(W, Qn, Qc, LONE_LEV)''')
rep('''                    Qc = fnp.matmul(WD, Qc, out=pool.get(("qc", qc_side), (n, r_old)))''',
'''                    Qc_new = pool.get(("qc", qc_side), (n, r_old))
                    self._lone(WD, Qc, Qc_new, LONE_LEV)
                    Qc = Qc_new''')
rep('''                    QU = fnp.matmul(Qc, U, out=pool.get("qu", (n, r2)))''',
'''                    QU = pool.get("qu", (n, r2))
                    self._lone(Qc, U, QU, LONE_LEV)''')
rep('''                lift = fnp.matmul(inner2[0], U2.T, out=self._pool.get("lift", (n, U2.shape[0])))''',
'''                lift = self._pool.get("lift", (n, U2.shape[0]))
                self._lone(inner2[0], U2.T, lift, LONE_LEV)''')
ast.parse(src)
open(sys.argv[2], "w").write(src)
print("wrote", sys.argv[2], len(src.splitlines()), "lines")
