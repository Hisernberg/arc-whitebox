# Submissions

One folder per submission, named `<submission-id>-<short-label>` to keep the
listing stable when statuses change.

| Folder | Submission ID | Status | MSE | Created (UTC) | Description |
|--------|---------------|--------|-----|---------------|-------------|
| `334011-d4-N1-e12x2/`          | 334011 | ✅ GRADED  | **4.667e-09** | 2026-10-04 16:53 | nabid_nur: 2-member 12-epoch GRU ensemble (held-out 0.9187), V32 lone L2, leaf 8, first-call L5. Raw 1.972e-08. Best so far |
| `334012-d4-N2-e12x2-lam1/`     | 334012 | ✅ GRADED  | 4.687e-09    | 2026-10-04 16:53 | nabid_nur: as 334011 + lambda scale 1.00. Raw 1.981e-08 (+0.4%): the corrector is tuned to the default chain, so chain knobs hurt |
| `334013-d4-M1-e12x1/`          | 334013 | ✅ GRADED | **4.654e-09** | 2026-10-04 16:53 | multi_agent: single 12-epoch GRU member (held-out 0.9223), V32 lone L2, leaf 8, first-call L5. Raw 1.973e-08 (same as the pair on the public 50), cost 0.2359 x B. Best so far |
| `334014-d4-M2-e12x2-lam1-r192/` | 334014 | ✅ GRADED | 4.701e-09 | 2026-10-04 16:54 | multi_agent: 2-member 12-epoch ensemble + lambda 1.00 + nested rank 192. Raw 2.015e-08 (+2.2%) for cost −1.3%: worse |
| `334020-d4-N3-e12x3/`          | 334020 | ⚠️ GRADED  | 8.08e-02 | 2026-10-04 17:43 | nabid_nur: 3-member 12-epoch ensemble at leaf 8. **4 of 100 networks hit the time limits** (wall 108–120 s, residual 0.405 s) under today's grader load and fell back to zero. Lesson: each corrector member adds ~720 server round-trips; keep ≤2 members at leaf 8 |
| `334021-d4-M3-e12x2-r192/`     | 334021 | ✅ GRADED | 4.671e-09 | 2026-10-04 17:43 | multi_agent: 2-member 12-epoch ensemble + nested rank 192. Raw 2.002e-08 (+1.5%) for cost −1.3%: slightly worse than 334011, so rank 192 is out too |
| `333790-day3-N1-long3/`        | 333790 | ✅ GRADED  | **4.689e-09** | 2026-10-03 15:52 | nabid_nur: V32 leaf 8 + first-call L5 + 3-member 8-epoch CDF GRU ensemble (the 333605 recipe; grader is deterministic, same score). Best so far on this account |
| `333791-day3-N2-long2/`        | 333791 | ✅ GRADED  | **4.676e-09** | 2026-10-03 15:52 | nabid_nur: V32 leaf 8 + first-call L5 + 2-member 8-epoch CDF GRU ensemble. Same raw as 3 members (1.976e-08), one member less cost. Best so far |
| `333792-day3-M1-long2/`        | 333792 | ✅ GRADED | 4.676e-09 | 2026-10-03 15:53 | multi_agent: identical file to 333791 (2-member 8-epoch ensemble); identical score, confirming the grader is deterministic across accounts |
| `333793-day3-M2-long1/`        | 333793 | ✅ GRADED | 4.674e-09 | 2026-10-03 15:53 | multi_agent: single 8-epoch CDF GRU member (held-out 0.924). Raw 1.981e-08 (+0.3% vs 2 members), cost −0.3%: one or two members is the sweet spot |
| `333605-acct2-long3/` | 333605 | ✅ GRADED | 4.689e-09 | 2026-10-02 19:22 | multi_agent: V32 leaf 8 + first-call L5 + 3-member CDF GRU ensemble trained for 8 epochs (held-out 0.921). Raw 1.976e-08 |
| `333589-acct2-tanh3/`          | 333589 | ✅ GRADED | 4.734e-09 | 2026-10-02 17:03 | multi_agent: V32 leaf 8 + first-call L5 + 3-member tanh-gated GRU ensemble (held-out 0.935). Raw 2.000e-08 (tanh members worse than CDF's 1.983e-08), the cost knobs compensate |
| `333596-acct2-alldata3/`       | 333596 | ✅ GRADED | 4.729e-09 | 2026-10-02 18:02 | multi_agent: V32 leaf 8 + first-call L5 + 3-member CDF GRU ensemble trained on all 730 public MLPs (no holdout, 3 fixed epochs). Raw 1.992e-08: slightly worse than the early-stopped S1 members (1.983e-08) |
| `333578-sub14_S3-v32/`         | 333578 | ✅ GRADED  | **4.705e-09** | 2026-10-02 16:34 | **S3**: V32 with leaf 8 + first-call level 5 (both grader-verified) + the 3-member full-split GRU ensemble of S1 (held-out 0.925). Raw 1.983e-08, cost 0.2373 x B. Best so far |
| `333572-sub18_A2S2_leaf8-v32/` | 333572 | ✅ GRADED | 4.779e-09 | 2026-10-02 15:56 | multi_agent: S2 (5 members) with leaf 8. Worse than the 3-member 333566 (4.734e-09): extra members only add cost |
| `333571-sub13_S2-v32/`         | 333571 | ✅ GRADED  | 4.855e-09    | 2026-10-02 15:53 | **S2**: V32 (lone level 2, leaf 16) + 5-member GRU ensemble (3 x h64 + 2 x h96), 630 full-split MLPs, 100 mini held out at ratio 0.926. Same raw as S1 (1.984e-08) but +1% cost from the two extra members: ensembling is saturated at 3 |
| `333567-acct2-S1-first5/`      | 333567 | ✅ GRADED | 4.780e-09 | 2026-10-02 15:25 | multi_agent: S1 with the first predict of each worker at Strassen level 5 (V28_STRASSEN_FIRST=5): cost −0.5% vs S1, same raw; passed 100/100 |
| `333566-sub16_A2S1_leaf8-v32/` | 333566 | ✅ GRADED | 4.734e-09 | 2026-10-02 15:25 | multi_agent: S1 with smallest leaf 8 (cost 0.2388 x B); same raw as S1 (1.983e-08). Best score on that account |
| `333564-sub12_S1-v32/`         | 333564 | ✅ GRADED  | **4.804e-09** | 2026-10-02 15:22 | **S1**: V32 (lone level 2, leaf 16) + 3-member GRU ensemble (hidden 64) trained on 630 full-split MLPs, 100 mini held out at ratio 0.925. Raw 1.983e-08 (−7.0% vs V29). Best so far |
| `333557-acct2-v32-leaf8-gru-ens3/` | 333557 | ✅ GRADED | 4.855e-09 | 2026-10-02 14:40 | **multi_agent account**: 333531's recipe with smallest Strassen leaf 8 (cost 0.2388 x B, −1.2%), same raw 2.033e-08; residual stayed under the cap |
| `333531-v32-lone2-min16-gru-ens3/` | 333531 | ✅ GRADED | **4.913e-09** | 2026-10-02 11:48 | **V32**: V31 ensemble + Strassen pricing of the join's lone dense products (level cap 2, leaf 16). Same raw as 333530 (2.034e-08), cost 0.2416 x B (−5.5%). Best so far |
| `333530-v31-gru-ens3-mini/`    | 333530 | ✅ GRADED  | **5.199e-09** | 2026-10-02 11:44 | **V31 ensemble**: V29 + 3-member per-layer GRU corrector ensemble (CDF gates, hidden 48, early-stopped; trained on 80 mini MLPs, 20 held out at ratio 0.955). Raw 2.034e-08 (−4.6% vs V29), cost unchanged. Best so far |
| `333509-v31-gru-cdf-smoke5/`   | 333509 | ✅ GRADED  | 5.584e-09    | 2026-10-02 09:28 | V31 with a normal-CDF GRU (hidden 48) trained on only 20 mini MLPs (local held-out ratio 1.025): raw 2.193e-08, +2.8% worse than V29, matching the local held-out estimate |
| `333508-v31-gru-smoke4/`       | 333508 | ✅ GRADED  | **5.311e-09** | 2026-10-02 09:26 | **V31**: V29 + per-layer GRU corrector (tanh, hidden 48, trained on only 20 mini MLPs), model embedded, suite-shape gate + setup dry run. Raw 2.087e-08 (−2.2% vs V29), cost unchanged. First graded learned-corrector submission |
| `333489-v31-gru-smoke-failed/`  | 333489 | ❌ FAILED | — | 2026-10-02 08:44 | V31 pipeline test 1: V29 + GRU corrector (hidden 48, 20 mini MLPs) from gru_model.json. Smoke test failed: FLOPSCOPE_SERVER_ERROR |
| `333492-v31-gru-smoke2-failed/` | 333492 | ❌ FAILED | — | 2026-10-02 08:52 | V31 pipeline test 2 (defensive GRU step). Smoke test failed: FLOPSCOPE_SERVER_ERROR |
| `333497-v31-gru-smoke3-failed/` | 333497 | ❌ FAILED | — | 2026-10-02 09:02 | V31 pipeline test 3 (model embedded, contiguous readout). Smoke test failed: FLOPSCOPE_SERVER_ERROR |
| `333493-bisect-b1-hooks-only/` | 333493 | ✅ GRADED  | 5.420e-09    | 2026-10-02 08:56 | Bisection B1: V29 + per-layer feature-recording hooks only (GRU disabled). Raw identical to V29 |
| `333494-bisect-b2-load-only/`  | 333494 | ✅ GRADED  | 5.440e-09    | 2026-10-02 08:56 | Bisection B2: V29 + feature hooks + GRU model loaded in setup (step disabled). Grader-identical raw; the +0.4% is first-call Strassen-level scheduling, not the load |
| `333467-graded/`               | 333467 | ✅ GRADED  | 5.418e-09    | 2026-10-02 06:39:28 | V29 verbatim (504aldo, MIT) re-submitted from the `nabid_nur` account as the Phase 2 baseline; raw 2.133e-08, 0.2534 x B, grader kernel 62.5 s, residual 0.183 s mean |
| `333364-top-scored/`           | 333364 | ✅ GRADED  | **5.394e-09** | 2026-10-01 16:00:54 | V29 baseline (504aldo, MIT) + kappa4 lambda table scale 0.95→1.00 (mean raw -0.35% on 4 public mini-split MLPs) |
| `333330-graded/`               | 333330 | ✅ GRADED  | 5.406e-09    | 2026-10-01 11:11:03 | V29 + R_OLD2 192 cost trim |
| `333323-graded/`               | 333323 | ✅ GRADED  | 5.418e-09    | 2026-10-01 10:30:13 | K3 cumulant propagation V29 (504aldo MIT baseline) |
| `333177-graded/`               | 333177 | ✅ GRADED  | 9.950e-09    | 2026-09-30 17:22:57 | (no description provided) |
| `333363-failed-prohibited-file/` | 333363 | ❌ FAILED | — | 2026-10-01 15:56:44 | V29 baseline (504aldo, MIT) + kappa4 lambda table scale 0.95→1.00 (re-validated). Failure: "Prohibited file in submission" |
| `333166-failed-eval-error/`    | 333166 | ❌ FAILED | — | 2026-09-30 16:29:17 | (no description provided). Failure: "Evaluation error" |

Account note: the `nabid_nur` account appears on the public leaderboard under its team name **Hydrion-Labs** (rank 50 at 4.8e-09 on 2026-10-02 16:10 UTC); the `multi_agent` account (used from 14:40 UTC for the riskier cost variants, key supplied by the owner) is listed separately.
Account note: submissions up to #333364 were graded under the `koushik_rudra` participant;
#333467 onwards are graded under `nabid_nur` (the API key used from 2026-10-02). The grader is
deterministic, so an identical estimator gives an identical adjusted score on either account.

## Folder layout (per submission)

Each submission folder contains:

- `README.md` — human-readable context: what was submitted, what the score was,
  what the description said, what the grading report tells us.
- `submission-report.json` — the full grading evaluation JSON, exactly the file
  AICrowd's "Download report.json" button produces. Contains:
  - `schema_version`, `session_id`, `submission_id`, `state`, `phase`
  - `started_at`, `updated_at`, `completed_at`
  - `config_snapshot` — `n_mlps`, `depth`, `width`, `flop_budget`
  - `progress` — `total_mlps`, `mlps_completed`, `mlps_in_flight`, `mlps_failed`, `pct_complete`
  - `workers` — per-worker state
  - `smoke_test_result` — pass/fail, duration, worker_passes, errors
  - `results.per_mlp[]` — per-MLP telemetry: `mlp_index`, `mlp_name`, `state`,
    `telemetry.flops_used`, `telemetry.participant_predict_wall_s`,
    `telemetry.flopscope_server_kernel_wall_s`, `budget_exhausted`, `time_exhausted`,
    `error_code`, `error_message`, `traceback_index`
- `submission-metadata.json` — submission ID, status, score (primary + secondary),
  challenge ID, round ID, created_at, grading_message (from AICrowd Rails API),
  plus GraphQL-derived fields (participant, round, team, description).

The grading reports for the two FAILED submissions are much shorter — they
record the smoke-test failure that aborted the run before any MLPs were scored.
