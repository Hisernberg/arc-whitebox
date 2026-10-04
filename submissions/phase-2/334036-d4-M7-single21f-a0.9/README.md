# Submission #334036 — d4-M7-single21f-a0.9

| Field | Value |
|---|---|
| Submission ID | 334036 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334036> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T19:42:54Z |
| Adjusted score (leaderboard) | 4.665452575319932e-09 |
| Raw final-layer MSE | 1.977593576896197e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + single final-weight-8 CDF GRU member s21 with its correction scaled by 0.9 (it over-corrects; held-out 0.9212 -> 0.9200); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.665e-09, raw final-layer MSE 1.978e-08, all-layers MSE 8.602e-09, mean multiplier 0.23594839683601093, failed MLPs 0
- FLOPs per MLP: mean 5.1836e+11 (0.2357 x B), min 0.2355 x B, max 0.2400 x B
- Grader timing per MLP: kernel 84.1 s mean, predict wall 95.2 s mean / 108.5 s max, residual 0.316 s mean / 0.345 s max (cap 0.4 s)
- Smoke test: passed=True duration 47226.67895599989 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
