# Submission #333493 — bisect-b1-hooks-only

| Field | Value |
|---|---|
| Submission ID | 333493 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333493> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T08:55:19Z |
| Adjusted score (leaderboard) | 5.420373430665984e-09 |
| Raw final-layer MSE | 2.1326515771136202e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Bisection B1: V29 + the per-layer feature-recording hooks of the instrumented estimator (GRU disabled, no data file). Tests whether the hook computations (row sums of C_off*C_off, D21 statistics, cumulant slices) pass the grader's flopscope client.

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 5.42e-09, raw final-layer MSE 2.133e-08, all-layers MSE 8.698e-09, mean multiplier 0.25426811575116515, failed MLPs 0
- FLOPs per MLP: mean 5.5739e+11 (0.2535 x B), min 0.2527 x B, max 0.2672 x B
- Grader timing per MLP: kernel 61.5 s mean, predict wall 67.8 s mean / 74.0 s max, residual 0.183 s mean / 0.190 s max (cap 0.4 s)
- Smoke test: passed=True duration 22005.237851000857 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
