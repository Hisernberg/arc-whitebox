# Submission #334031 — d4-M4-single21

| Field | Value |
|---|---|
| Submission ID | 334031 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334031> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T19:03:32Z |
| Adjusted score (leaderboard) | 4.668418826992383e-09 |
| Raw final-layer MSE | 1.9788525982278314e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + single CDF GRU member trained with final-layer loss weight 8 (held-out 0.9218, best single so far); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.668e-09, raw final-layer MSE 1.979e-08, all-layers MSE 8.603e-09, mean multiplier 0.23594839683601093, failed MLPs 0
- FLOPs per MLP: mean 5.1836e+11 (0.2357 x B), min 0.2355 x B, max 0.2400 x B
- Grader timing per MLP: kernel 83.4 s mean, predict wall 94.5 s mean / 106.9 s max, residual 0.315 s mean / 0.370 s max (cap 0.4 s)
- Smoke test: passed=True duration 46906.17014700001 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
