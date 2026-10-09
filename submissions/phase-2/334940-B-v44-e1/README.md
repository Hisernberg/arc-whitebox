# Submission #334940 — B-v44-e1

| Field | Value |
|---|---|
| Submission ID | 334940 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334940> |
| Status | GRADED |
| Created (UTC) | 2026-10-09T03:42:30Z |
| Adjusted score (leaderboard) | 3.995967704773497e-09 |
| Raw final-layer MSE | 1.9649280602607177e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track B: V44 with warm-up on 1 call/worker. pred ~3.985e-09 or fail

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 3.996e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.20343619803090404, failed MLPs 0
- FLOPs per MLP: mean 4.4550e+11 (0.2026 x B), min 0.1993 x B, max 0.2133 x B
- Grader timing per MLP: kernel 94.5 s mean, predict wall 105.4 s mean / 113.8 s max, residual 0.309 s mean / 0.376 s max (cap 0.4 s)
- Smoke test: passed=True duration 45067.341253999984 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
