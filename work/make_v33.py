#!/usr/bin/env python3
"""V33 = V32 + dead-ReLU pruning of the two biggest product families.
(A) young-leg transport family: inner dimension restricted to previous-layer neurons that fire
    (Phi_prev > THR); their rows of the legs / newborn / covariance are Phi-scaled, so the
    dropped terms are O(THR).
(B) hub contraction (young + old tier): output rows/cols restricted to current-layer neurons
    that fire; the live block is expanded back to n x n (dead rows/cols = 0) by an
    inverse-index gather. Live counts are rounded up to a multiple of Q (Strassen divisibility).
Knobs: V33_PRUNE_THR (0 disables -> V32 op stream), V33_PRUNE_Q, V33_PRUNE_MIN.
Usage: make_v33.py <v32_in.py> <out.py>"""
import ast, sys
src = open(sys.argv[1]).read()
def rep(old, new, count=1):
    global src
    assert src.count(old) == count, (src.count(old), old[:100])
    src = src.replace(old, new)

rep('''LONE_LEV = int(_os.environ.get("V32_LONE_LEV", "5"))''',
'''LONE_LEV = int(_os.environ.get("V32_LONE_LEV", "5"))
PRUNE_THR = float(_os.environ.get("V33_PRUNE_THR", "0.00135"))   # V33: Phi threshold of a firing neuron (0 = off)
PRUNE_Q = int(_os.environ.get("V33_PRUNE_Q", "64"))              # V33: live-count rounding (Strassen divisibility)
PRUNE_MIN = int(_os.environ.get("V33_PRUNE_MIN", "512"))
PRUNE_PARTS = _os.environ.get("V33_PARTS", "AB")
PRUNE_MSET = sorted(int(x) for x in _os.environ.get("V33_MSET", "896,960").split(","))   # V33: allowed live sizes (bounded buffer variety)                 # V33: A = transport inner dim, B = hub output block''')

# helpers
rep('''    def _lone(self, A, B, out, lev):''',
'''    def _live(self, w1v, n):
        """V33: indices (sorted) of the m most-firing neurons, m = live count rounded up to PRUNE_Q;
        None when nothing would be pruned."""
        if PRUNE_THR <= 0 or w1v is None or n != 1024:
            return None
        cnt = int(fnp.sum(w1v > PRUNE_THR))
        fits = [v for v in PRUNE_MSET if v >= cnt and v < n]
        if not fits:
            return None
        m = fits[0]
        idx = fnp.sort(fnp.argsort(w1v)[n - m:])
        return idx, m

    def _expand(self, block, idx, m, n, out):
        """V33: scatter a (m, m) live block into out (n, n) with zeros elsewhere (inverse-index gather)."""
        f32 = fnp.float32
        ar = fnp.arange(n)
        pos = fnp.searchsorted(idx, ar)
        hit = fnp.take(idx, fnp.minimum(pos, m - 1)) == ar
        inv = fnp.where(hit, pos, m)
        padded = fnp.concatenate([fnp.concatenate([block, fnp.zeros((m, 1), dtype=f32)], axis=1),
                                  fnp.zeros((1, m + 1), dtype=f32)], axis=0)
        fnp.copyto(out, fnp.take(fnp.take(padded, inv, axis=0), inv, axis=1))
        return out

    def _lone(self, A, B, out, lev):''')

# (A) transport family
rep('''                if 2 * k + extra > 2 * ka:
                    smm.mm(W[None, None], legs4["AP0"][2 * ka:2 * k + extra],
                           legs4["AP1"][2 * ka:2 * k + extra], smm.level(n, n, n, s_lev))''',
'''                if 2 * k + extra > 2 * ka:
                    lvp = self._live(w1_prev, n) if "A" in PRUNE_PARTS else None
                    if lvp is None:
                        smm.mm(W[None, None], legs4["AP0"][2 * ka:2 * k + extra],
                               legs4["AP1"][2 * ka:2 * k + extra], smm.level(n, n, n, s_lev))
                    else:
                        # V33: previous-layer dead neurons dropped from the contraction
                        ip, mp = lvp
                        Wp = fnp.take(W, ip, axis=1)
                        Rp = fnp.take(legs4["AP0"][2 * ka:2 * k + extra], ip, axis=2)
                        smm.mm(Wp[None, None], Rp, legs4["AP1"][2 * ka:2 * k + extra],
                               smm.level(n, mp, n, s_lev))''')

# current-layer live set, passed to dslices
rep('''                D3, D21 = self._dslices(A_st, P_st, Z_st, L_st, w2b_list, s_list, e_list,
                                        c1_list, c2_list, y_list, n, bufs,''',
'''                lvc = None
                if not trim and PRUNE_THR > 0 and n == 1024 and "B" in PRUNE_PARTS:
                    lvc = self._live(flops.stats.norm.cdf(mu / fnp.sqrt(var)).astype(f32), n)
                D3, D21 = self._dslices(A_st, P_st, Z_st, L_st, w2b_list, s_list, e_list,
                                        c1_list, c2_list, y_list, n, bufs,''')
rep('''                                        sb2=(fap24[:2 * kb] if kb > 0 else None), s_sb=s_sb)''',
    '''                                        sb2=(fap24[:2 * kb] if kb > 0 else None), s_sb=s_sb, live=lvc)''')
rep('''                 sb1=None, sb2=None, s_sb=0):''', '''                 sb1=None, sb2=None, s_sb=0, live=None):''')

# (B) contraction: replace the old-tier + young hub block when live is given
old_b = '''        if ka > 0:
            # V21: old sources through the shared basis: [sum LA FAo^T + LP FPo^T] Qc^T'''
new_b = '''        if live is not None:
            # V33: live x live block of (young hub + old tier through the basis), expanded to n x n
            il, ml = live
            smm = self._smm
            blk = None
            if ka < k:
                Xp = fnp.take(bufs["lap4"][2 * ka:2 * k], il, axis=2)
                Yp = fnp.take(apb4[2 * ka:2 * k], il, axis=2)
                hb = self._pool.get(("hubp", ml), (1, ml, ml))
                smm.hub(Xp, Yp, hb, smm.level(ml, n, ml, min(STRASSEN_HUB, self._s_hub)))
                blk = hb[0]
            if ka > 0:
                innerp = None
                if ka > kb:
                    r1 = sb1.shape[2]
                    ib = self._pool.get(("innerp", ml), (1, ml, r1))
                    smm.hub(fnp.take(bufs["lap4"][2 * kb:2 * ka], il, axis=2), sb1, ib, smm.level(ml, n, r1, s_sb))
                    innerp = ib[0]
                if kb > 0:
                    r2_ = sb2.shape[2]
                    ib2 = self._pool.get(("inner2p", ml), (1, ml, r2_))
                    smm.hub(fnp.take(bufs["lap4"][:2 * kb], il, axis=2), sb2, ib2, smm.level(ml, n, r2_, s_sb))
                    liftp = ib2[0] @ U2.T
                    innerp = liftp if innerp is None else innerp + liftp
                oldb = innerp @ fnp.take(Qc, il, axis=0).T
                blk = oldb if blk is None else blk + oldb
            D21 = self._expand(blk, il, ml, n, bufs["d21"])
            fnp.matmul(R.T, Yk, out=bufs["t1"])
            fnp.multiply(bufs["t1"], 1.0 / 3.0, out=bufs["t1"])
            fnp.add(D21, bufs["t1"], out=D21)
        elif ka > 0:
            # V21: old sources through the shared basis: [sum LA FAo^T + LP FPo^T] Qc^T'''
rep(old_b, new_b)

# ---- V33b: remaining dense products routed through the Strassen helper (value-identical up to rounding) ----
rep("""    R_FB = 16    #""", """    R_FB = int(_os.environ.get("V33_R_FB", "16"))    #""")
rep("""    def _lone(self, A, B, out, lev):""", """    def _lp(self, A, B, key):
        \"\"\"V33: Strassen-priced A @ B into a pooled (A.shape[0], B.shape[1]) buffer.\"\"\"
        out = self._pool.get(key, (A.shape[0], B.shape[1]))
        self._lone(A, B, out, LONE_LEV)
        return out

    def _lone(self, A, B, out, lev):""")
rep("""                            self._lone(Qp, Sfull @ (Qp.T @ Om), Yq2, LONE_LEV)""",
    """                            self._lone(Qp, Sfull @ self._lp(Qp.T, Om, "qpom"), Yq2, LONE_LEV)""")
rep("""                        Tq = Qn.T @ Qp                      # (r, r) rotation of the old factors""",
    """                        Tq = fnp.copy(self._lp(Qn.T, Qp, "tq"))   # (r, r) rotation of the old factors""")
rep("""                    Sj = (FAj @ (dAj * FAj.T)) + (FPj @ (dPj * FPj.T))""",
    """                    Sj = self._lp(FAj, dAj * FAj.T, "sja") + self._lp(FPj, dPj * FPj.T, "sjp")""")
rep("""                        S_s = (FA1 @ (dAb * FA1.T)) + (FP1 @ (dPb * FP1.T))   # (r1, r1)""",
    """                        S_s = self._lp(FA1, dAb * FA1.T, "ssa") + self._lp(FP1, dPb * FP1.T, "ssp")   # (r1, r1)""")
rep("""                fnp.add(D21, fnp.matmul(inner, Qc.T, out=bufs["t1"]), out=D21)""",
    """                self._lone(inner, Qc.T, bufs["t1"], LONE_LEV)
                fnp.add(D21, bufs["t1"], out=D21)""")
rep("""                D21 = fnp.matmul(inner, Qc.T, out=bufs["d21"])""",
    """                D21 = bufs["d21"]
                self._lone(inner, Qc.T, D21, LONE_LEV)""")
rep("""                oldb = innerp @ fnp.take(Qc, il, axis=0).T""",
    """                oldb = self._lp(innerp, fnp.take(Qc, il, axis=0).T, ("oldb", ml))""")

ast.parse(src)
open(sys.argv[2], "w").write(src)
print("wrote", sys.argv[2], len(src.splitlines()), "lines")
