# Submission #334751 — d8-N2-v42lp4-e2

| Field | Value |
|---|---|
| Submission ID | 334751 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334751> |
| Status | GRADED |
| Created (UTC) | 2026-10-08T01:44:23Z |
| Adjusted score (leaderboard) | 4.023058072913459e-09 |
| Raw final-layer MSE | 1.9649280602607177e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V42 + LP4 + warm-up on 2 calls; predicted ~4.02-4.03e-09

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.023e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.20481530526849384, failed MLPs 0
- FLOPs per MLP: mean 4.4854e+11 (0.2040 x B), min 0.2007 x B, max 0.2147 x B
- Grader timing per MLP: kernel 96.4 s mean, predict wall 107.0 s mean / 112.5 s max, residual 0.301 s mean / 0.356 s max (cap 0.4 s)
- Smoke test: passed=True duration 44189.02852800056 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
