#!/usr/bin/env python3
"""Generate estimator_v30.py from estimator_v29.py: hub-column dropping.

Each K3 source keeps only NH of its n hub columns (the birth-layer neurons that generate
the source's third-cumulant content). Columns are ranked at birth by the Frobenius weight of
their rank-1 tensor terms (||X1_j|| ||Y1_j|| + ||X3_j|| ||Y3_j||), so neurons in the dead or
saturated ReLU regimes (which generate almost no non-Gaussianity) are the ones dropped. Every
transport, Hadamard product and hub contraction of the source then runs on n x NH legs.
Values are identical to V29 when NH = n (hub dropping off).
"""
import re, sys

src = open("/home/user/arc-whitebox/work/estimator_v29.py").read()
n_edits = 0


def rep(old, new, count=1):
    global src, n_edits
    c = src.count(old)
    assert c == count, (c, old[:120])
    src = src.replace(old, new)
    n_edits += 1


# ---- header / knobs ----
rep('STRASSEN_MIN = int(_os.environ.get("V26_STRASSEN_MIN", "32"))',
    'STRASSEN_MIN = int(_os.environ.get("V26_STRASSEN_MIN", "16"))  # V30: 16 so n x NH families (NH = 768: leaf 24) keep level 5')
rep('WARM = _os.environ.get("V26_WARM", "1") == "1"\n',
    'WARM = _os.environ.get("V26_WARM", "1") == "1"\n'
    '# V30: hub columns kept per K3 source (0 = all = exact V29 op stream); ranking mode imp | first\n'
    'HUB_NH = int(_os.environ.get("V30_HUB_NH", "768"))\n'
    'HUB_MODE = _os.environ.get("V30_HUB_MODE", "imp")\n'
    'HUB_MIN_N = int(_os.environ.get("V30_HUB_MIN_N", "512"))  # hub dropping only at widths >= this\n')

# ---- predict core: nh, keep list, covariance buffers ----
rep('''        riders = (n == 1024 and L == len(CORR_BETA))
''', '''        riders = (n == 1024 and L == len(CORR_BETA))
        # V30: hub-column count per source (n = off). Suite width only by default; the smoke
        # shapes run the exact V29 op stream.
        nh = HUB_NH if (0 < HUB_NH < n and n >= HUB_MIN_N) else n
        hub_on = nh < n
        self._nh = nh
        keep_list = []   # per source slot: index array of the kept hub columns (None = all)
''')
rep('''        abbuf = pool.get("abbuf", (t2max, n, n))
        T1 = NN("t1")   # layer-local (n,n) scratch
''', '''        abbuf = pool.get("abbuf", (t2max, n, n))
        T1 = NN("t1")   # layer-local (n,n) scratch
        # V30: the post-ReLU covariance no longer rides in the newborn's P slot (the slots are
        # n x NH); it gets its own (1, 1, n, n) family buffers.
        cb4 = pool.get("cb4", (1, 1, n, n))
        wc4 = pool.get("wc4", (1, 1, n, n))
        zeros_nh = fnp.zeros(nh, dtype=f32)
''')

# ---- transport family: A legs only ride; covariance transported separately ----
rep('''                extra = 2 if newborn is not None else 0
                if 2 * k + extra > 2 * ka:
                    smm.mm(W[None, None], legs4["AP0"][2 * ka:2 * k + extra],
                           legs4["AP1"][2 * ka:2 * k + extra], smm.level(n, n, n, s_lev))
''', '''                extra = 1 if newborn is not None else 0
                if 2 * k + extra > 2 * ka:
                    smm.mm(W[None, None], legs4["AP0"][2 * ka:2 * k + extra],
                           legs4["AP1"][2 * ka:2 * k + extra], smm.level(n, n, nh, s_lev))
''')
rep('''                if A_st is None:
                    # V29: layer 1 has no stack yet: the newborn + C family alone (slot 0
                    # written at birth on the AP0 side; output to AP1, then swap)
                    smm.mm(W[None, None], legs4["AP0"][0:2], legs4["AP1"][0:2],
                           smm.level(n, n, n, s_lev))
                    legs["AP0"], legs["AP1"] = legs["AP1"], legs["AP0"]
                    legs4["AP0"], legs4["AP1"] = legs4["AP1"], legs4["AP0"]
                # V29: C_pre from the transported covariance W C in the newborn's P slot
                WC = legs["AP0"][k, 1]
''', '''                if A_st is None:
                    # layer 1 has no stack yet: the newborn's A leg alone (slot 0 written at
                    # birth on the AP0 side; output to AP1, then swap)
                    smm.mm(W[None, None], legs4["AP0"][0:1], legs4["AP1"][0:1],
                           smm.level(n, n, nh, s_lev))
                    legs["AP0"], legs["AP1"] = legs["AP1"], legs["AP0"]
                    legs4["AP0"], legs4["AP1"] = legs4["AP1"], legs4["AP0"]
                # V30: C_pre from the transported covariance W C (its own family buffers)
                smm.mm(W[None, None], cb4, wc4, smm.level(n, n, n, s_lev))
                WC = wc4[0, 0]
''')
rep('''                fnp.copyto(legs["AP0"][k, 1], W)
                A_st = legs["AP0"][:k + 1, 0]
''', '''                if keep_list[k] is None:
                    fnp.copyto(legs["AP0"][k, 1], W)
                else:
                    fnp.copyto(legs["AP0"][k, 1], fnp.take(W, keep_list[k], axis=1))
                A_st = legs["AP0"][:k + 1, 0]
''')
rep('''                L_st = pool.get("l", (L - 1, n, r + 2))[:k + 1]
''', '''                L_st = pool.get("l", (L - 1, nh, r + 2))[:k + 1]
''')

# ---- join: Yq1 is hub-indexed ----
rep('''                    Yq1 = pool.get("yq1", (n, r_old))
''', '''                    Yq1 = pool.get("yq1", (nh, r_old))
''')
rep('''                    fap_new, fap4_new = pool.get_pair(("fap", fa_side), (L - 1, 2, r_old, n))
''', '''                    fap_new, fap4_new = pool.get_pair(("fap", fa_side), (L - 1, 2, r_old, nh))
''')
rep('''                        fap2_new, fap24_new = pool.get_pair(("fap2", f2_side), (L - 1, 2, r2, n))
''', '''                        fap2_new, fap24_new = pool.get_pair(("fap2", f2_side), (L - 1, 2, r2, nh))
''')
rep('''                    smm.mm(Qc[None, None], fap4[2 * fa_off:2 * (fa_off + m1)],
                           legs4["AP1"][2 * kb:2 * ka], smm.level(n, r_old, n, s_sb))
''', '''                    smm.mm(Qc[None, None], fap4[2 * fa_off:2 * (fa_off + m1)],
                           legs4["AP1"][2 * kb:2 * ka], smm.level(n, r_old, nh, s_sb))
''')
rep('''                    smm.mm(QU[None, None], fap24[:2 * kb], legs4["AP1"][:2 * kb],
                           smm.level(n, r2, n, s_sb))
''', '''                    smm.mm(QU[None, None], fap24[:2 * kb], legs4["AP1"][:2 * kb],
                           smm.level(n, r2, nh, s_sb))
''')

# ---- dslice buffers ----
rep('''                    bufs = {nm: pool.get(nm, (L - 1, n, n))
                            for nm in ("ap", "pp", "t", "mp", "xt", "yt", "u")}
                    bufs["lap"], bufs["lap4"] = pool.get_pair("lap", (L - 1, 2, n, n))   # V26: [LA | LP]
''', '''                    bufs = {nm: pool.get(nm, (L - 1, n, nh))
                            for nm in ("ap", "pp", "t", "mp", "xt", "yt", "u")}
                    bufs["lap"], bufs["lap4"] = pool.get_pair("lap", (L - 1, 2, n, nh))   # V26: [LA | LP]
''')

# ---- leg slot buffers ----
rep('''                pairs = {nm: pool.get_pair(nm, (L - 1, 2, n, n)) for nm in ("AP0", "AP1")}
''', '''                pairs = {nm: pool.get_pair(nm, (L - 1, 2, n, nh)) for nm in ("AP0", "AP1")}
''')

# ---- birth: a_b full (masked) + gathered into the slot; importance ranking ----
rep('''            k_b = 0 if A_st is None else A_st.shape[0]
            a_b = fnp.multiply(w1col, C_off, out=legs["AP0"][k_b, 0])
            if rfb > 0 and mode == 1:
''', '''            k_b = 0 if A_st is None else A_st.shape[0]
            # V30: the birth factor is formed in full (n x n) for the n^2 birth slices and the
            # importance ranking; only its kept columns enter the stack slot (below).
            a_b = fnp.multiply(w1col, C_off, out=NN("afull"))
            if rfb > 0 and mode == 1:
''')
# after the D21_new/D3_new block of the feedback path and the else path, before the regen feed:
rep('''            if regen and mode == 1 and not NO_FEED:
                # K4->K3 feed (F68): X3 = diag(w1^2 dG) + lam a_b d(w1), Y3 = y 1^T
''', '''            # ---- V30: hub-column selection of this newborn source ----
            if hub_on:
                cn_a = fnp.sqrt(fnp.sum(fnp.multiply(a_b, a_b, out=T1), axis=0))
                if rfb > 0 and mode == 1:
                    cn_x1 = fnp.sqrt(fnp.sum(fnp.multiply(X1_b, X1_b, out=T1), axis=0))
                    cn_y1 = fnp.sqrt(fnp.sum(fnp.multiply(Y1_b, Y1_b, out=T1), axis=0))
                else:
                    cn_x1 = cn_a * 3.0
                    cn_y1 = cn_a * fnp.abs(w2)
                imp = cn_x1 * cn_y1
                if regen and mode == 1 and not NO_FEED:
                    _dgw = (w1 * w1) * dG
                    _c1 = w1 * lam_prev
                    _ynorm = fnp.sqrt(fnp.sum(w2 * w2)) * (0.25 * METRIC_C)
                    imp = imp + fnp.sqrt(_dgw * _dgw + (_c1 * _c1) * (cn_a * cn_a)) * _ynorm
                if HUB_MODE == "first":
                    keep = fnp.arange(nh)
                else:
                    keep = fnp.sort(fnp.argsort(imp)[n - nh:])
                mask = fnp.zeros(n, dtype=f32)
                mask[keep] = 1.0
                maskr = (mask)[None, :]
                # zero the dropped columns in every birth-level n x n object that feeds the
                # n^2 birth slices (P = I at birth: column j of a leg is hub column j)
                fnp.multiply(a_b, maskr, out=a_b)
                if rfb > 0 and mode == 1:
                    fnp.multiply(X1_b, maskr, out=X1_b)
                    fnp.multiply(Y1_b, maskr, out=Y1_b)
                    xd = fnp.diag(X1_b)
                    yd = fnp.diag(Y1_b)
                    D21_new = fnp.multiply((xd)[:, None], Y1_b.T, out=NN("d21new"))
                    fnp.multiply(X1_b, Y1_b, out=T1)
                    fnp.add(D21_new, T1, out=D21_new)
                    fnp.multiply((yd)[:, None], X1_b.T, out=T1)
                    fnp.add(D21_new, T1, out=D21_new)
                    fnp.multiply(D21_new, 1.0 / 3.0, out=D21_new)
                    D3_new = xd * yd
                else:
                    D21_new = fnp.multiply(a_b, a_b, out=NN("d21new"))
                    fnp.multiply(D21_new, (w2)[None, :], out=D21_new)
                    D3_new = None
            else:
                keep = None
                mask = ones_n
            keep_list.append(keep)
            fnp.copyto(legs["AP0"][k_b, 0], a_b if keep is None else fnp.take(a_b, keep, axis=1))
            if regen and mode == 1 and not NO_FEED:
                # K4->K3 feed (F68): X3 = diag(w1^2 dG) + lam a_b d(w1), Y3 = y 1^T
''')
# regen feed birth slices with masks
rep('''                w1sq = w1 * w1
                y_b = w2 * (0.25 * METRIC_C)
                dgw = w1sq * dG
                u_b = y_b * dG
                c1_b = w1 * lam_prev
                # (V26 expression, same operation order, out= into the pooled buffers)
                fnp.multiply((dgw)[:, None], (y_b)[None, :], out=T1)
                fnp.multiply(T1, 1.0 / 3.0, out=T1)
                fnp.add(D21_new, T1, out=D21_new)
                fnp.multiply(a_b, (c1_b)[None, :], out=T1)
                fnp.multiply((y_b * (2.0 / 3.0))[:, None], T1, out=T1)
                fnp.add(D21_new, T1, out=D21_new)
                fnp.multiply((w1sq)[:, None], (u_b * (1.0 / 3.0))[None, :], out=T1)
                fnp.add(D21_new, T1, out=D21_new)
                D3_new = ((dgw * y_b + u_b * w1sq) if D3_new is None
                          else D3_new + dgw * y_b + u_b * w1sq)
''', '''                w1sq = w1 * w1
                y_b = w2 * (0.25 * METRIC_C)
                dgw = w1sq * dG
                u_b = y_b * dG
                c1_b = w1 * lam_prev
                # V30: hub-masked birth slices (hub index = the delta leg's index at birth):
                #   (1/3) 1[a in K] dgw_a y_c ;  (1/3) y_a a_b[a,c] c1_c (1[c in K] + 1[a in K])
                #   (a_b is already column-masked) ;  (1/3) 1[a in K] w1sq_a u_c
                dgw_m = dgw * mask
                w1sq_m = w1sq * mask
                fnp.multiply((dgw_m)[:, None], (y_b)[None, :], out=T1)
                fnp.multiply(T1, 1.0 / 3.0, out=T1)
                fnp.add(D21_new, T1, out=D21_new)
                fnp.multiply(a_b, (c1_b)[None, :], out=T1)
                fnp.multiply((y_b * (1.0 / 3.0))[:, None], T1, out=T1)
                fnp.multiply(T1, (1.0 + mask)[:, None], out=T1)
                fnp.add(D21_new, T1, out=D21_new)
                fnp.multiply((w1sq_m)[:, None], (u_b * (1.0 / 3.0))[None, :], out=T1)
                fnp.add(D21_new, T1, out=D21_new)
                D3_new = ((dgw_m * y_b + u_b * w1sq_m) if D3_new is None
                          else D3_new + dgw_m * y_b + u_b * w1sq_m)
''')
# ---- per-source statics restricted to the kept hub columns ----
rep('''            lb = pool.get("l", (L - 1, n, r + 2))
            fnp.copyto(lb[k_b, :, :r], Q)
            fnp.copyto(lb[k_b, :, r], w1sq)
            fnp.copyto(lb[k_b, :, r + 1], zeros_n)
            Lr_full = None
''', '''            lb = pool.get("l", (L - 1, nh, r + 2))
            if keep is None:
                fnp.copyto(lb[k_b, :, :r], Q)
                fnp.copyto(lb[k_b, :, r], w1sq)
            else:
                fnp.copyto(lb[k_b, :, :r], fnp.take(Q, keep, axis=0))
                fnp.copyto(lb[k_b, :, r], fnp.take(w1sq, keep))
            fnp.copyto(lb[k_b, :, r + 1], zeros_nh)
            Lr_full = None
''')
rep('''            newborn = (a_b, Rr_full, Lr_full, S3c, e_b, Ff_b)
            if rfb > 0:
                r1b = pool.get("r1t", (L - 1, n, rfb))
                r2b = pool.get("r2t", (L - 1, n, rfb))
                fnp.copyto(r1b[k_b], R1T_b)
                fnp.copyto(r2b[k_b], R2T_b)
                R1T_st = r1b[:k_b + 1]
                R2T_st = r2b[:k_b + 1]
            w2b_list.append(w2)
            # V21: hub-column Gram weights of this source's legs (X1 = 3A, Y1 ~ A d(w2),
            # M ~ P d(s) + 3 A d(e)): A-type 9 + w2^2 + 9 e^2, P-type 1 + s^2
            dA_list.append(9.0 + w2 * w2 + 9.0 * e_b * e_b)
            dP_list.append(1.0 + S3c * S3c)
            c1_list.append(c1_b)
            c2_list.append(dgw)
            y_list.append(y_b)
''', '''            def _hub(v):
                return v if keep is None else fnp.take(v, keep)
            newborn = (a_b, Rr_full, Lr_full, _hub(S3c), _hub(e_b), Ff_b)
            if rfb > 0:
                r1b = pool.get("r1t", (L - 1, nh, rfb))
                r2b = pool.get("r2t", (L - 1, nh, rfb))
                if keep is None:
                    fnp.copyto(r1b[k_b], R1T_b)
                    fnp.copyto(r2b[k_b], R2T_b)
                else:
                    fnp.copyto(r1b[k_b], fnp.take(R1T_b, keep, axis=0))
                    fnp.copyto(r2b[k_b], fnp.take(R2T_b, keep, axis=0))
                R1T_st = r1b[:k_b + 1]
                R2T_st = r2b[:k_b + 1]
            w2b_list.append(_hub(w2))
            # V21: hub-column Gram weights of this source's legs (X1 = 3A, Y1 ~ A d(w2),
            # M ~ P d(s) + 3 A d(e)): A-type 9 + w2^2 + 9 e^2, P-type 1 + s^2
            dA_list.append(_hub(9.0 + w2 * w2 + 9.0 * e_b * e_b))
            dP_list.append(_hub(1.0 + S3c * S3c))
            c1_list.append(_hub(c1_b))
            c2_list.append(_hub(dgw))
            y_list.append(y_b)
''')
# ---- covariance ride replaced by the cb4 buffer ----
rep('''            fnp.copyto(legs["AP0"][k_b, 1], C)
''', '''            fnp.copyto(cb4[0, 0], C)
''')
# ---- hub contraction levels ----
rep('''        self._smm.hub(bufs["lap4"][2 * k0:2 * k], apb4[2 * k0:2 * k], out[None],
                      self._smm.level(n, n, n, min(STRASSEN_HUB, self._s_hub)))
''', '''        self._smm.hub(bufs["lap4"][2 * k0:2 * k], apb4[2 * k0:2 * k], out[None],
                      self._smm.level(n, self._nh, n, min(STRASSEN_HUB, self._s_hub)))
''')
rep('''                smm.hub(bufs["lap4"][2 * kb:2 * ka], sb1, inner, smm.level(n, n, r1, s_sb))
''', '''                smm.hub(bufs["lap4"][2 * kb:2 * ka], sb1, inner, smm.level(n, self._nh, r1, s_sb))
''')
rep('''                smm.hub(bufs["lap4"][:2 * kb], sb2, inner2, smm.level(n, n, r2_, s_sb))
''', '''                smm.hub(bufs["lap4"][:2 * kb], sb2, inner2, smm.level(n, self._nh, r2_, s_sb))
''')
# docstring marker
rep('"""K3-simple factored cumulant propagation + MEMORYLESS KAPPA4 REGENERATION (V17)',
    '"""V30 (2026-10-02): HUB-COLUMN DROPPING. Each K3 source keeps NH of its n hub columns\n'
    '(ranked at birth by the Frobenius weight of the column\'s rank-1 tensor terms); dead and\n'
    'saturated ReLU neurons generate ~no third cumulant, so their columns are dropped and every\n'
    'transport / Hadamard / hub contraction of the source runs on n x NH legs. NH = n reproduces\n'
    'the V29 op stream. Below this line the V29 docstring follows unchanged.\n\n'
    'K3-simple factored cumulant propagation + MEMORYLESS KAPPA4 REGENERATION (V17)')

open("/home/user/arc-whitebox/work/estimator_v30.py", "w").write(src)
print("edits applied:", n_edits)
