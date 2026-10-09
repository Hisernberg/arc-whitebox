# Daily submission plan (30 per UTC day)

Three accounts × 10 submissions per UTC day: `nabid_nur` (Hydrion-Labs), `multi_agent`, `koushik_rudra`.
Grading takes 30–60 min per submission and several can grade at once, so a day runs as rounds of
2–3 parallel submissions, one change per submission, with each round chosen from the last one's results.

## Shape of a day
| Phase | Slots | What goes in |
|---|---|---|
| 1. Carry-over (just after 00:00 UTC) | up to 3 | The best known build, sent to each account whose own best is worse |
| 2. Exploration | ~18 | One change per submission, different change per account, measured locally first (cost profile + raw accuracy) |
| 3. Consolidation | ~6 | Combine the changes that won; send the combined build to all three accounts |
| 4. Close (before 23:59 UTC) | 1–3 | A robust build (more wall/residual margin) to keep as the prize-nomination candidate |

## Guardrails (every build, before it is submitted)
- `whest validate` passes; builds made only through `work/build_v34.sh` + `make_v35/36/37.py` + `make_variant.py`.
- Wall time per MLP: graded max must stay under ~116 s (limit 120 s).
- Residual time: under ~0.38 s on the first 5 MLPs and ~0.33 s afterwards (limit 0.4 s).
- Memory: estimator peak (via `work/mem_probe.py`) under ~7 GB (limit 8 GB).
- Changes to helper code must reproduce the previous predictions bit-for-bit before they are submitted.

## Where the next gains come from
Best today is 4.145e-09; #1 on the leaderboard is ~1.5e-09, at C/B 0.10–0.15 with raw MSE 1.1–1.5e-08.
Tuning the current chain gives ~0.5–1% per day; reaching the top needs a structural step:
1. A cheaper chain (C/B ≈ 0.15) whose extra error the learned corrector absorbs, retrained on that chain.
2. A stronger corrector (more training MLPs, training through the corrected chain instead of on uncorrected features).
3. Memory-lean buffers so the main transport can use one more Strassen level (currently blocked by the 8 GB cap).

## Account tracks (from 2026-10-09): three accounts, three independent research lines
Each account runs its own line of builds; **no build is ever submitted to two accounts**. A gain found on one track is
re-implemented in that track's own lineage only if it fits that track's approach, never copied across as-is.

| Account | Track | Approach | Starting point | Next experiments (one hypothesis per slot) |
|---|---|---|---|---|
| `nabid_nur` | **A. Learned corrector** | Better learning on top of the chain: what the error is predicted from and how the correction is carried through the network | V42 (LT + cross-neuron inputs), 4.023e-09 | x3 inputs; end-to-end training through the transport (loss on the final layer); per-layer loss weighting; two-layer-back inputs; corrector width/depth vs. its own FLOPs; ensembles only if they pay for their FLOPs |
| `multi_agent` | **B. Cost and wall-time engineering** | Same maths, fewer FLOPs and less wall time: Strassen depth per product family, warm-up schedule, block layouts, op-count/overhead cuts that buy wall headroom for deeper Strassen | V42 + LP4 + warm-up 2 | hub-only / C_pre-only Strassen level 6; cutting Python/op overhead (12 s of the 120 s) to make level 6 fit; LP5; memory/op-log robustness |
| `koushik_rudra` | **C. Chain closure and structure** | Change what the chain computes: ranks, ages, feedback, pruning, closure terms; trade accuracy against cost at the source | robust V42 + warm-up 2 lineage | R_OLD2 / AGE_OLD2 / QPASS re-tunes under the LT corrector; pruning threshold and set sizes; LAM_SCALE; closure-term ablations with the corrector retrained on each |

Daily rhythm per track: round 1 (3–4 slots) from the previous evening's offline results; research block; round 2
(3–4 slots); close with that track's own robust nominee (1–2 slots). Grades are compared against the logged prediction.

## Competition plan (from 2026-10-07, 11 days left)
**Where we are**: all three accounts 4.063e-09 (rank ~48). #1 J2W 1.5e-09 (raw 1.47e-08 at C/B 0.105);
top 10 ≤ 2.1e-09. Our raw 1.98e-08 at C/B 0.204. Rank 1 needs both ~25% lower error and ~half the cost: no
known path yet, so every day must buy either a measured gain or a measured fact.

**Rules for every one of the 30 daily slots**
1. One hypothesis per submission, with a written local prediction (score, C/B, wall max) logged before submitting;
   graded vs predicted goes in the research log. Never a blind copy.
2. Exploration slots go to builds whose local/offline measurement is at least neutral; the grader is deterministic,
   so a graded repeat only buys wall-time information.
3. Every account ends the day holding the day's best build and a robust nominee (wall max < 112 s, 0 failures).

**Daily schedule (UTC)**
| Time | Work |
|---|---|
| 00:20 | Archive late grades; leaderboard + forum scan (new write-ups, rank deltas, score/C-B of movers); carry the best build to any account below it |
| 00:30–06:00 | Round 1: 3 variants per account (9 slots), each a different measured change |
| 06:00–14:00 | Research block: train/measure the next lever offline (corrector, closure, cost); round 2 (9 slots) |
| 14:00–22:00 | Round 3 (9 slots): combine the winners of rounds 1–2 |
| 22:00–23:59 | Close: best build + robust nominee on every account (3 slots) |

**Research tracks, by expected gain**
| Track | Lever | Status / next step |
|---|---|---|
| A. Corrector | V41 LT (per-layer local error, carried through W) gave −1.7% | add cross-neuron inputs (W-weighted aggregates of the previous layer's features and predicted errors); train end-to-end through the transport; retrain on dumps from the exact production config |
| B. Closure | 66% of error in Φ>0.9 neurons; local error 3–4.5e-09/layer | find which closure term the local error tracks (per-feature attribution of the LT model), then replace that term |
| C. Cost | C/B 0.204; L5 build hits 116–119.7 s wall | cut ops (wall) to make L5/LP4 safe; measure cheaper chain + LT retrained on it |
| D. Robustness | final hidden eval: one long-lived worker, op-log memory grows per MLP (forum 18238) | measure RSS growth over 20+ MLPs in one process; nominate builds with margin |
| E. Intelligence | leaderboard + forum daily | log movers' raw/C-B to infer their method class |

## Research log
### 2026-10-05
- **Error anatomy** (53 held-out MLPs, chain without corrector): final-layer error grows linearly with depth
  (0.7e-9 at layer 0 → 23e-9 at layer 15). 66% of it sits in nearly-always-active neurons (Φ > 0.9),
  where ReLU is ~linear, so it is mean error inherited through W. No global or per-MLP bias (<0.5%).
- **Corrector**: held-out ratio improves slowly with data (71 → 142 → 418 → ~950 MLPs: 0.928 → 0.925 →
  0.917 → 0.913). A residual connection (u = Φ·(W·u_prev) + local term) was *worse* in a controlled pilot
  (0.949 vs 0.944). Training from scratch on ~950 MLPs reached 0.917; fine-tuning the old model on them, 0.913.
- **Cheaper chain + corrector does not work**: the corrector removes a fixed ~9% of whatever error the chain
  leaves (AGE_OLD=3: ratio 0.924 on +15% raw; R_OLD2=192: 0.914 on +1.6% raw). The leaders' gap is not
  "cheap chain + our corrector"; it needs either a better closure or a corrector with richer cross-neuron inputs.
- **Cost levers that worked on the grader**: join products at Strassen level 2/3 after the first 5 MLPs,
  D21 feedback rank 8 → 2 (C/B −2.7%, raw +1.9%, corrector unaffected). Level 4 overran the 120 s wall limit.
- **Levers measured and rejected**: deeper Strassen on small blocks (V38), finer pruning sizes, pruning
  threshold 0.002/0.003, QPASS2=1, R_OLD=352, AGE_OLD2 6/8, R_FB=1.
### 2026-10-06
- **Wall time is now the binding risk.** The 4.133e-09 build (lone products at Strassen level 5) overran the
  120 s limit on 2 networks on koushik_rudra (334327, score 0.030) while the identical build passed on the other
  accounts. With level-4 join products (334230) that makes two wall failures. Default exploration base is now
  the robust lone-level-4 build (4.161e-09, wall max 108–110 s).
- Corrector: hidden-state transport through W (`--hprop`) was worse (0.940 vs 0.930 at 2 epochs); a wider
  hidden-96 model plateaued at 0.925 (overfits); the best pair (all-data fine-tune + from-scratch) gains only
  0.3% (0.9105) — below the ~0.6% needed to pay for a second member. The corrector is saturated at ~0.913.
- Chain from the other side: AGE_OLD=5 (−3.1% raw, +3.9% cost, 8.2 GB peak) and R_OLD=416 (−2.0% raw, +3.0%
  cost) are net worse. D21 feedback rank 3 graded 4.143e-09 (rank 2 stays); nested-tier age gate 8 graded
  4.133e-09 (neutral).
- **Rank 18–22 target (asked 10-06)**: needs ~2.7–2.8e-09, i.e. −33% vs 4.13e-09 (MSE 1.37e-08 at our C/B 0.204, or
  C/B 0.139 at our MSE). Every lever in this chain family moves raw and cost along a near-neutral frontier
  (AGE_OLD=5: −3.1% raw / +3.9% cost; R_OLD=416: −2.0% / +3.0%), 504aldo's ablation table and the forum
  (topics 18218, 18219) list no unexplored large lever, and wall time (max 118.5 s on 334393) blocks deeper
  Strassen. kaileh57 (rank 19) runs at our cost (C/B 0.19) with 30% lower MSE (1.41e-08): the gap is a better
  closure, not tuning. No submission was made for this target; copies of existing builds would not move the rank.
- **Layer-transport error decomposition** (`work/lt/decomp.py`, 20 MLPs): the pre-activation mean is exactly linear in the
  previous layer's mean, so each layer's error = Phi ⊙ (previous error @ W) + a new local error. The new local error is
  3–4.5e-09 per layer; at the final layer 80% of the error is carried forward and 20% is new.
- **Per-layer local-error corrector** (`work/lt/train_lt.py`): an MLP predicting each layer's local error from that layer's
  per-neuron statistics, with the corrections carried forward through W. Trained on 972 MLPs, held-out 53: **ratio 0.900**
  vs 0.913 for the production GRU (which already transports corrections through W). Local predictability is weak at depth
  (unexplained 0.90–0.94 from layer 7 on): the closure error is not a function of per-neuron statistics. ~1.5% better than
  the current corrector, below the 10% bar for a submission.
### 2026-10-07
- **V41 (LT corrector replaces the GRU)**: offline on the 53 held-out MLPs LT 0.900 vs GRU 0.922 (same dumps); leave-one-out
  blend of both 0.897 (not worth two models). Local whest A/B on 2 mini MLPs: MSE ratio 0.974 / 0.997, cost +0.08%.
  Submitted on koushik_rudra: 334554 (L5 build) and 334555 (robust L4 build), plus accidental repeats 334556 / 334557.
- LT seed ensemble (3 seeds): 0.8996 vs 0.900 single — no gain; seeds converge to the same function.
- **V42 (LT + cross-neuron inputs)**: previous layer's var, phi, Phi, K3v, K4v, pred, g_post, e_b carried through W and W²
  as 16 extra inputs. Held-out 0.892 (vs 0.900); local A/B vs V41: 1.944e-08 vs 1.990e-08 and 1.983e-08 vs 2.009e-08,
  cost +0.13%. Submitted on all three accounts (334627–334632); predicted L5 ~4.02–4.03e-09, robust ~4.06e-09.
- LT hidden 256 / 8 epochs with x2: held-out 0.889 (−0.3%) for ~4x the corrector FLOPs (~+1% C/B): net zero, not built.
- LT x3 (+18 remaining previous-layer features through W): held-out 0.8906 vs 0.8919 for x2 (−0.15%) — saturating;
  not built. Corrector track is near its ceiling (~0.89 of raw); next gains must come from the chain or the cost.
- **V42 graded** 4.0449e-09 (L5) / 4.0734e-09 (robust) vs predicted 4.02–4.03 / 4.06: raw fell 0.6% (1.9654e-08 vs
  1.9769e-08) — the offline held-out gain (0.9%) only partly transfers — and C/B rose 0.3% (16 matvecs + W*W per layer).
  Lesson: discount offline corrector gains by ~half; charge the corrector's own FLOPs.
### 2026-10-08
- **Late grades**: V42+LP4 passed twice (4.036e-09 nabid_nur, 4.051e-09 koushik_rudra; wall max 116.5 / 112.3 s).
- **Grader spread on identical builds (~0.4%) explained**: the V37 warm-up schedule runs each worker's first 5 calls
  at the expensive early levels (C/B ~0.212 vs ~0.2035 late). The number of such MLPs varies 9–15 per run (worker
  count/restarts), so C/B and the score move with it. Lever: fewer early calls (V37_NEARLY 5 → 2/3), ~−0.5% C/B,
  at some wall risk on cold first calls. Round 1: 334741 (multi_agent, LP4 carry, pred ~4.04), 334742 (koushik_rudra,
  NEARLY=2, pred ~4.02–4.03), 334743 (nabid_nur, NEARLY=3, pred ~4.025–4.03).
- **Chain knob frontier** (`work/cost_sweep.sh`, 2 mini MLPs, V42+LP4, warm-up off): base raw 1.960e-08 / C/B 0.2080 /
  4.076e-09. Every cost cut loses: R_OLD 256 (C/B −11%, raw +34%) 4.84e-09; AGE_OLD 3 (−4%, +19%) 4.67e-09; NO_FEED
  (0%, +6%) 4.32e-09; NO_WK431 (0%, +24%) 5.03e-09; NO_SRC_LAST and NO_REGEN ~10x worse. NO_FB crashed; R_OLD2 160
  unfinished. The chain sits at its knob optimum: lode_dockx's raw 2.1e-08 at C/B 0.10 must be a different method,
  not a tuned version of ours.
- **Round 1 graded (all within prediction)**: multi_agent LP4 4.036e-09 (pred ~4.04); koushik_rudra warm-up 2
  4.023e-09 (pred 4.02–4.03, 7 early MLPs); nabid_nur warm-up 3 4.030e-09 (pred 4.025–4.03). The "failed" MLPs in
  334742/334743 are grader-side cuts (TIME_EXHAUSTED at ~109 s participant wall with ~1 s overhead and 0 residual);
  the score was computed regardless. Round 2: koushik_rudra warm-up 1 (334749, pred ~4.015–4.02), multi_agent and
  nabid_nur warm-up 2 (334750, 334751, pred 4.02–4.03).
- **Round 2 graded**: multi_agent warm-up 2 4.0231e-09 (pred 4.02–4.03; second identical 4.0231 grade). koushik_rudra
  warm-up 1 **failed** (MLPs 30/31 TIME_EXHAUSTED at 109.6 s, ~1 s overhead, likely a restarted worker's unprotected
  second call): warm-up 2 is the floor. Round 3: robust nominee + warm-up 2 (334758 koushik_rudra, 334759 multi_agent;
  pred 4.06–4.065, wall max ~105–110 s).
- **Round 3 graded**: nabid_nur warm-up 2 4.0231e-09 (third identical grade); robust + warm-up 2 4.0627e-09 on
  koushik_rudra and multi_agent (pred 4.06–4.065; wall max 105–106 s, 0 failures) — the new nominee build; sent to
  nabid_nur too (334765).
- **Production-config features**: the deployed V42 corrector scores 0.892 on dumps from the exact production chain
  (same as on the older dumps), so feature mismatch does not explain why the grader shows only half the offline gain;
  retraining on production dumps is not worth it. Dumps stopped at 101 full + 53 mini.
- **Symmetric billing (flopscope)**: einsum('ij,kj->ik', A, A) is billed half of A@B (1.07e9 vs 2.15e9 at n=1024) and
  returns a SymmetricTensor; W·S·Wᵀ with a symmetric-tagged S is billed 3.22e9 vs 4.29e9 dense. Strassen L5 (~0.51x)
  already beats both, but computing only the upper-triangle blocks of symmetric-output products would cut those
  products ~in half under any pricing. Mapping which large products have symmetric outputs (research agent running).
- LT x2 + GRU blend: leave-one-out 0.8905 vs 0.8919 LT alone (−0.15%) — not worth the GRU's FLOPs.
- **Symmetric-output products** (code audit, `work/runs/symreport_day8.md`): the dominant Strassen leaves are the
  transport family W·A_j / W·P_j / W·C and the D21 hub — none symmetric. The only large symmetric product, C_pre =
  W C Wᵀ, already computes 3 of 4 blocks; a 4×4 split (10/16 blocks) would save ~1% of total FLOPs, Sj/S_s Grams
  ~0.7%, small r×r ~0.3%. Ceiling ~2–2.5%; C_pre 4×4 split (~1%) is the only item worth building.
- **V43 (C_pre 4×4 symmetric split) rejected**: local C/B 0.21047→0.21026 and 0.20548→0.20504 (−0.1/−0.2%); raw moved
  ±0.7% from rounding order (1.931→1.946e-08, 1.989→1.980e-08) — net zero. The symmetric-product track is closed.
- **End of day-8 research**: corrector (~0.89 ceiling), chain knobs (at optimum), warm-up schedule (2 is the floor),
  symmetric products (<0.3%) are all exhausted. Remaining slots are held rather than spent on unmeasured builds. The
  next real step needs a different chain (leaders reach raw 1.2–1.5e-08 at C/B 0.10–0.14).
- **Deeper Strassen (V26_STRASSEN 5→6)** on V42+LP4+warm-up 2, local: C/B 0.2080 → 0.2032 (−2.3%), raw unchanged
  (score 4.076 → 3.992e-09), but local wall +40–50% (201→277 s, 133→198 s): the L5 build already sits at 112–118 s
  of the 120 s grader limit, so the full change cannot ship. Testing hub-only level 6 on the robust build (wall ~105 s,
  ~12–15 s headroom). L7 run did not finish.
- Hub-only Strassen level 6 (V26_STRASSEN_HUB=6) on the robust build: bit-identical to base (the hub level is capped by
  `min(STRASSEN_HUB, self._s_hub)`), so it is a no-op. Track B needs per-family level control in code, not a knob.
### Track C sweep (robust V42 + warm-up 2, 2 mini MLPs, warm-up off; base raw 1.9661e-08 / C/B 0.2099 / 4.1273e-09)
| Knob | raw | C/B | score | vs base |
|---|---|---|---|---|
| V17_LAM_SCALE 0.90 | 1.9544e-08 | 0.2099 | 4.1027e-09 | **−0.6%** |
| V24_R_OLD2 192 | 1.9838e-08 | 0.2075 | 4.1162e-09 | −0.3% |
| V24_R_OLD2 256 | 1.9707e-08 | 0.2124 | 4.1842e-09 | +1.4% |
| V24_AGE_OLD2 6 / 10 | 2.0531 / 1.9719e-08 | 0.2066 / 0.2135 | 4.2387 / 4.2090e-09 | +2.7% / +2.0% |
| V33_R_FB 3 | 1.9734e-08 | 0.2109 | 4.1611e-09 | +0.8% |
| V33_PRUNE_THR 0.001 / 0.002 | 1.9756e-08 / = base | 0.2112 / = base | 4.1734e-09 / = base | +1.1% / 0 |
| V17_LAM_SCALE 1.0 | 2.0021e-08 | 0.2099 | 4.2025e-09 | +1.8% |
Follow-ups running: LAM 0.85, 0.80, LAM 0.90 + R_OLD2 192.
Follow-ups: LAM 0.85 4.1570e-09, LAM 0.80 4.2383e-09 (0.90 is the optimum); **LAM 0.90 + R_OLD2 192: 4.0865e-09
(−1.0% vs base)**. Submitted on koushik_rudra (Track C): 334889 (L5 + LP4 + warm-up 2, pred ~3.98–3.99e-09),
334890 (robust nominee, pred ~4.02e-09).
- **Track A**: per-layer loss weighting (later layers ×4) 0.8917 vs 0.8919 — no gain. Started end-to-end fine-tune
  (`work/lt/train_e2e.py`): loss on the final-layer error after the transport, init from lt_x2, 2 epochs.
- **Track A end-to-end fine-tune**: held-out 0.8919 → 0.8918 (epoch 1) → **0.8896** (epoch 2), still improving; 4 more
  epochs running from the epoch-2 checkpoint.
- **Track C graded**: 334889 (L5 + LAM 0.90 + R_OLD2 192) 4.0231e-09 = previous best; 334890 (robust) 4.0659e-09 vs
  4.0627. The local −1.0% (2 MLPs) did not transfer: on the grader's 100 MLPs raw rose (1.965 → 1.988e-08) as C/B
  fell. **Lesson: 2-MLP local sweeps have ~1% noise; Track C knob decisions now need ≥8 MLPs (dense-mode raw on the
  feature dumps) before a slot is spent.**
- Track A end-to-end: 0.8896 → 0.8915 → 0.8893 → 0.8881 (epochs 3–5 of 6).
- Track A e2e epoch 6 jumped to 0.8986 (lr 3e-4 too high; the per-epoch save overwrote the 0.8881 checkpoint).
  Fixed: save-best only. Rerun from the 0.8896 checkpoint at lr 1e-4, 4 epochs.
- **Track A e2e (lr 1e-4, save-best)**: 0.8896 → 0.8897 → 0.8869 → **0.8866** → 0.8906; best kept. Built as
  `sub128_A_e2e` (sub121 lineage, only the model literal changed) and submitted on nabid_nur: 334900, pred ~4.01e-09.
- **Track A graded**: 334900 nabid_nur 4.0155e-09 (pred ~4.01) — new best; raw 1.9612e-08 vs 1.9649e-08 (−0.2%, about
  half the offline −0.6%, as for V42). The three accounts now differ: A 4.0155, B 4.0231, C 4.0231.
### 2026-10-09 (first three-track day)
- Leaderboard/forum: no change at the top (J2W 1.5e-09; top 10 ≤ 2.1e-09); no new forum posts. Ours ~4.0e-09 (#50–56).
- **Track A round 1**: 334917 nabid_nur robust nominee with the end-to-end corrector (pred ~4.055e-09).
- **Track B round 1 (local first)**: C_pre family at Strassen level 6 (V29_CPRE_LEV) and join products at level 5
  (V37_LP_LATE) on multi_agent's lineage; FLOP-only changes, so 2 MLPs suffice for C/B and wall.
- **Track C**: 8-MLP local measurements queued after Track B.
- **Track B local**: C_pre level 6 (V29_CPRE_LEV=6) bit-identical to base (capped like the hub); join level 5
  (V37_LP_LATE=5) C/B −0.14% (0.21047→0.21018, 0.20548→0.20519), raw within noise, wall ±2%. Knob space exhausted;
  Track B moves to code: wall-time profile by op family (`work/prof_time.py`) at Strassen L5 vs L6, to find the time
  that does not buy FLOPs and make L6 fit the 120 s limit.
- **Track A graded**: 334917 nabid_nur robust + e2e 4.0552e-09 (pred ~4.055; robust floor improved from 4.0627).
- **Track B profile** (L5, local, steady state): backend 125 s + overhead 11.5 s; Strassen add/sub ~67 s, the single
  `"tij,ti,tj,tg->gij"` PK2 einsum (52×1024×1024, 14 calls) 20.4 s (~16%), matmul 16.8 s.
- **V44** (`work/make_v44.py`): PK2 einsum → two in-place broadcasts + sums over the contiguous IND2 groups.
  Local (2 MLPs): raw bit-identical (1.9601e-08), C/B 0.2080 → 0.2066 (−0.67%), wall 135 → 116 s (−14%).
  Submitted on multi_agent: 334922 `sub130_B_v44`, pred ~3.996e-09. The freed ~18 s of wall is the budget for the
  next Track B step (deeper Strassen where it now fits).
- **Track C (queued, 8 MLPs, paired)**: the 334889 grade raised raw, so which knob did it? Robust base vs
  LAM 0.90 alone vs R_OLD2 192 alone on 8 mini MLPs (`NM=8 work/cost_sweep.sh`). A knob ships on koushik_rudra only if
  it wins on the 8-MLP mean.
- **Track B graded**: 334922 multi_agent V44 **3.9959e-09** (pred ~3.996) — new overall best; raw 1.9649e-08 unchanged,
  C/B down as measured.
- **Track B L6 per family (local)**: `V28_STRASSEN_SB=6` and `V32_LONE_LEV=6` on V44 are bit-identical (capped by block
  divisibility). Built `sub131_B_fam` (V44 + `V44_LEG_LEV` cap) to run leg transport, hub and C_pre at L6 one at a
  time (queued).
- **Track C 8-MLP paired result** (robust base 4.2738e-09): LAM 0.90 alone raw −0.57% (6/8 MLPs better), C/B same →
  4.2492 (−0.58%); R_OLD2 192 alone raw +0.75% (+2.7% worst), C/B −1.2% → 4.2553 (−0.43%), uneven. The 334889 raw rise
  came from R_OLD2 192. Submitted LAM 0.90 alone on sub121: 334929 koushik_rudra, pred ~4.00e-09.
- **Track C graded**: 334929 koushik_rudra LAM 0.90 alone **4.0435e-09** vs 4.0231 for the same build at LAM 0.95
  (334742): raw 1.9749 vs 1.9649e-08 (+0.5%). The grader scores **the same 100 MLPs in every submission** (names
  identical across 334742 / 334922 / 334929; only 1 of them in our 1100 local MLPs), so this is an exact paired
  comparison: LAM 0.90 is worse on the grader set although it won on 8 local mini MLPs (−0.6%, 6/8, SE ~0.17%).
  **Lesson: the mini split does not predict chain-knob effects on the grader set.** Track C now tests chain changes
  on ≥24 MLPs from the `full` split before any slot, and prefers structural changes over scale knobs (LAM 0.95 and
  R_OLD2 are at their grader optima).
- Ops: the queued Track B family runs waited on `pgrep -f trackC8.sh`, which matched its own command line, so they never
  started (2 h lost). Restarted directly at 03:20.
- **Track B L6 per family** (`sub131_B_fam`, 2 MLPs vs V44 4.0486e-09 / C/B 0.2066 / wall 166,116 s):
  legs L6 4.0129 (C/B −1.2%, raw +0.3%, wall +25 s); hub L6 4.0234 (−0.6%, +24 s); C_pre L6 4.0586 (no C/B change).
- **Grader wall telemetry**: V44 saved only ~3% on the grader (median 108.9 → 105.6 s, max 118.7 → 111.4 s), not the
  local 14%. The real limit is the **120 s round trip** (predict + ~10 s worker setup on some calls): 334742 and
  334749 each had 2 MLPs cut at 120.2 s round trip with predict ~109 s. 334922 is the first build with no cuts (max round trip 111.7 s), so
  the legs-L6 +25 s cannot ship. Op count per predict 34.4k (add 14.9k, subtract 7.0k, copyto 4.2k), ~0.32 ms grader
  overhead each.
- **Track B round 2**: 334940 multi_agent V44 + warm-up 1 (`sub133_B_e1`); uses the V44 headroom to cut the op-lean
  calls; pred ~3.985e-09 or a fail.
- **Track A**: e2e continuation from the best checkpoint at lr 3e-5 (train ≈ held-out ≈ 0.888 on ~1000 MLPs: the
  corrector is feature-limited, not data-limited; new error features are the next Track A step).
- **Track A**: e2e continuation at lr 3e-5: 0.8866 → 0.8880 → 0.8869 (no gain; converged). A var-correction head adds
  no new signal (the per-layer mean target g_l already absorbs pre-activation variance errors through the ReLU mean).
  Dataset `n_samples` = 1e9, so the grader truth's MC floor (~7.5e-11) is negligible: the gap to the leaders is all
  method. **Strategic note**: lode_dockx reaches raw 2.1e-08 (≈ ours) at C/B 0.10 (half ours); halving our cost at
  equal raw would put us at ~2.0e-09 (top 10). Track A pivots to cost-at-equal-raw work on the chain (rank/tier
  structure re-derived for C/B 0.10) after today's slots, measured on ≥24 `full` MLPs.
- **Per-family FLOP attribution** (`work/profile_ns.py`, V44, steady-state predict, C/B 0.2057, 34.4k ops):
  leg transport (mm L1226/L1233) 26.8%; hub L2045 12.3%, hub L1777 (slot sum) 11.4%, hubs L2052/L2057/L2077 9.0%;
  inline 10.9% (6.3k ops, 15.5 s); shared-basis mm L1208/L1214 11.3%; lone products ~14% in total (≈1% each, ~1.1k ops each);
  C_pre 3.0%; lp 3.3%; corrector 0.5%. No family dominates: halving cost needs fewer/lower-rank slots across
  legs + hubs together (≈65% of C/B scales with slot count × rank), not a single-kernel fix.
