# Submission #333489 — v31-gru-smoke-failed

| Field | Value |
|---|---|
| Submission ID | 333489 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333489> |
| Status | FAILED |
| Created (UTC) | 2026-10-02T08:44:21Z |
| Adjusted score (leaderboard) | None |
| Raw final-layer MSE | None |
| Participant | nabid_nur |
| Grading message | <p>Error : Smoke test failed</p> |

## What was submitted

V31 pipeline test: V29 (504aldo, MIT) + per-layer GRU corrector (hidden 48, 16,850 params, trained on 20 mini-split MLPs for 40 epochs; held-out final-layer MSE -3%) loaded from gru_model.json in the submission folder. Purpose: validate data-file loading, cost and residual time of the GRU step on the grader.

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
