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
