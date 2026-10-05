# Submission #333492 — v31-gru-smoke2-failed

| Field | Value |
|---|---|
| Submission ID | 333492 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333492> |
| Status | FAILED |
| Created (UTC) | 2026-10-02T08:51:55Z |
| Adjusted score (leaderboard) | None |
| Raw final-layer MSE | None |
| Participant | nabid_nur |
| Grading message | <p>Error : Smoke test failed</p> |

## What was submitted

V31 pipeline test 2: V29 (504aldo, MIT) + per-layer GRU corrector (hidden 48, trained on 20 mini-split MLPs) from gru_model.json; GRU step rewritten after 333489's smoke-test failure (fresh zero operands per column, sigmoid via tanh, host-side transposes, no array .copy()).

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
