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
