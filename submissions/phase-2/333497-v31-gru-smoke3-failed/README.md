# Submission #333497 — v31-gru-smoke3-failed

| Field | Value |
|---|---|
| Submission ID | 333497 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333497> |
| Status | FAILED |
| Created (UTC) | 2026-10-02T09:02:36Z |
| Adjusted score (leaderboard) | None |
| Raw final-layer MSE | None |
| Participant | nabid_nur |
| Grading message | <p>Error : Smoke test failed</p> |

## What was submitted

V31 pipeline test 3: V29 (504aldo, MIT) + per-layer GRU corrector (hidden 48, 20 mini-split MLPs) with the model embedded as a JSON literal in estimator.py (single-file submission) and contiguous readout vectors (u, q from two matvecs).

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
