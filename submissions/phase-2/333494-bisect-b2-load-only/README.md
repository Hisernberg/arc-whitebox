# Submission #333494 — bisect-b2-load-only

| Field | Value |
|---|---|
| Submission ID | 333494 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333494> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T08:55:24Z |
| Adjusted score (leaderboard) | 5.440387809444694e-09 |
| Raw final-layer MSE | 2.132658536879717e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Bisection B2: V29 + feature hooks + gru_model.json loaded in setup() (json + fnp.asarray of nested lists), GRU step disabled. Tests the data-file loading path on the grader.

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 5.44e-09, raw final-layer MSE 2.133e-08, all-layers MSE 8.697e-09, mean multiplier 0.2552222253584296, failed MLPs 0
- FLOPs per MLP: mean 5.5844e+11 (0.2540 x B), min 0.2527 x B, max 0.2672 x B
- Grader timing per MLP: kernel 62.7 s mean, predict wall 69.1 s mean / 81.7 s max, residual 0.185 s mean / 0.201 s max (cap 0.4 s)
- Smoke test: passed=True duration 22211.36460300113 ms, worker passes 8 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
