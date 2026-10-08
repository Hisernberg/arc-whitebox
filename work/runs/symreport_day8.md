# Symmetric-output products in sub124_rb_e2/estimator.py

Units: D = one dense 1024^3 product = 2*n^3 = 2.15e9 FLOPs. Total per predict ~4.5e11 = ~210 D.
Strassen L5 = 0.513 D per n^3 product, before additions. L3 = 0.67x.

## Where the cost goes: none of these outputs is symmetric
- **Transport family** (L1226/1233, also L1248): `smm.mm(W, legs4[AP0][2ka:2k+extra])`. The by=8 slots give the profiled ((1,2401,32,32),(8,2401,32,32)) leaves. Outputs are W·A_j, W·P_j, W·a_b and W·C. None is symmetric: A and P are transported legs, and W·C is not symmetric even though C is. About 110 slot-products per predict, ≈56 D plus additions.
- **Hub D21** (`_hub2` L1757 and `smm.hub` L2030/2062): D21 = Σ LA_k A_kᵀ + LP_k P_kᵀ. LA ≠ A, and D21 is the (2,1) slice, used together with D21ᵀ. **Not symmetric.**
- **Shared-basis products** `Qc·FAP` (L1208/1214) and `inner·Qcᵀ` (L2075/2079): rank-384 outputs that are not symmetric.

## Symmetric candidates, ranked by saving from computing only the upper half
1. **C_pre = (W C) W^T**, L1258 → `_sym_product` (L1738). C is symmetric, so the result is exactly symmetric. It already computes only the 11/12/22 blocks: one Strassen family X3 (3,1,512,1024) @ Y3 (3,1,1024,512) at L5, 0.75 of the dense count. It runs at layers 1–14 (the last layer is trimmed to diag only): 14 × 0.385 D ≈ 5.4 D, or ~2.6% of matmul FLOPs (~3.5% with Strassen additions). The remaining opportunity is to recurse the symmetric split: the diagonal blocks 11/22 are themselves symmetric. With a 4x4 partition you need 10/16 = 0.625, with 8x8 36/64 = 0.5625. That saves about 0.15–0.19 D per layer, ≈2.5 D ≈ **1.0–1.2%**. The cost is shallower Strassen on the smaller blocks. WC itself is one non-symmetric family slot.
2. **Sj = FAj (dA·FAjᵀ) + FPj (dP·FPjᵀ)**, L1155 (`_lp` "sja"/"sjp"). Weighted Grams (384×1024)(1024×384) give an **exactly symmetric** r×r output. They use Strassen L3 (LP_LATE), or dense in the first 2 calls. 2 products per joiner layer, at layers 5–14 (10 layers): 20 × 0.094 D ≈ 1.9 D ≈ **0.9%**. Half-blocks save ≈0.45%. Merging the pair as [FAj|FPj]·diag·[FAj|FPj]ᵀ changes nothing in FLOPs.
3. **S_s = FA1 (dAb·FA1ᵀ) + FP1 (dPb·FP1ᵀ)**, L1170 ("ssa"/"ssp"). Same r×n×r symmetric Grams. They run at the nest layers 9–14 (6 layers): 12 × 0.094 ≈ 1.1 D ≈ **0.5%**. Half saves ≈0.27%.
4. **Small r×r congruences (plain `@`, dense, exactly symmetric):**
   - `Sg = Tq @ (Sg @ Tq.T)` at L1145: 2×384³ = 0.105 D per joiner layer, ≈1.0 D ≈ 0.5%.
   - `U @ (S2 @ U.T)` at L1127/1171: 384·224·(224+384), ≈0.05 D each.
   - `S2 = Un.T @ (G2 @ Un)` at L1187: ≈0.05 D.
   - Together these are ≈1.5 D ≈ 0.7%. Only the outer product of each pair is symmetric, so computing half its blocks saves ≈0.2–0.3%.
5. **Layer-0 Gram** `einsum("ia,ib->ab", w32, w32)` at L1079 (A·Aᵀ form). It is already billed at half by flopscope as an aliased symmetric einsum. That is ≈0.5 D, ~0.25%, so **nothing left**.
6. **Elementwise only** (no matmul): PK2 einsum L1441 → pk11/pk22 symmetrised at L1446–1449; C = (K11 + K11ᵀ)/2 at L1679. These are O(t·n²), well under 0.5% in total.

## Products where both operands are the same matrix
The only one is L1079: w32ᵀw32, which is already discounted. The dense legs never appear as A·Aᵀ. The (W*W)@vec calls are matrix-vector products.

## Bottom line
The dominant (·,2401,32,32) cost comes from the transport family and the hub, and **neither has a symmetric output**. The only large symmetric product is C_pre, which already takes the 3/4-block shortcut. Recursing it, plus half-block Sj/S_s Grams and the small cores, gives a combined ceiling of about **2–2.5% of total FLOPs**.
