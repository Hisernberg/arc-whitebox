# Submission #334961 — B-lp5

| Field | Value |
|---|---|
| Submission ID | 334961 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334961> |
| Status | GRADED |
| Created (UTC) | 2026-10-09T05:54:38Z |
| Adjusted score (leaderboard) | 0.01577816162472673 |
| Raw final-layer MSE | 0.01577817696149083 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track B grid: V44 + LP_LATE 5

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 0.01578, raw final-layer MSE 0.01578, all-layers MSE 0.0124, mean multiplier 0.2193502773819182, failed MLPs 1
- FLOPs per MLP: mean 4.4546e+11 (0.2026 x B), min 0.1960 x B, max 0.2133 x B
- Grader timing per MLP: kernel 98.9 s mean, predict wall 109.9 s mean / 117.5 s max, residual 0.310 s mean / 0.365 s max (cap 0.4 s)
- Smoke test: passed=True duration 45555.639810000226 ms, worker passes 5 / failures 0
- MLPs completed: 97 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
