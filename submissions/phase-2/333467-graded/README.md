# Submission #333467 — graded

| Field | Value |
|---|---|
| Submission ID | 333467 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333467> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T06:39:16Z |
| Adjusted score (leaderboard) | 5.418168137938331e-09 |
| Raw final-layer MSE | 2.1326515771136202e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V29 verbatim (504aldo, MIT): factorized K=3 cumulant propagation + memoryless kappa4 regeneration + age-gated shared basis + Strassen-Winograd families. Baseline resubmission under this account to anchor the grader (bit-identical to koushik_rudra's #333323).

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 5.418e-09, raw final-layer MSE 2.133e-08, all-layers MSE 8.698e-09, mean multiplier 0.25416470960872173, failed MLPs 0
- FLOPs per MLP: mean 5.5717e+11 (0.2534 x B), min 0.2526 x B, max 0.2671 x B
- Grader timing per MLP: kernel 62.5 s mean, predict wall 68.9 s mean / 75.4 s max, residual 0.183 s mean / 0.195 s max (cap 0.4 s)
- Smoke test: passed=True duration 21758.863191000273 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
