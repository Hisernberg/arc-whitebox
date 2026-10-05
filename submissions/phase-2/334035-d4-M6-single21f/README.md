# Submission #334035 — d4-M6-single21f

| Field | Value |
|---|---|
| Submission ID | 334035 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334035> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T19:32:10Z |
| Adjusted score (leaderboard) | 4.674417687206581e-09 |
| Raw final-layer MSE | 1.9813934564183454e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + single fully trained final-weight-8 CDF GRU member s21 (held-out 0.9212, best single); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.674e-09, raw final-layer MSE 1.981e-08, all-layers MSE 8.605e-09, mean multiplier 0.23594839683601093, failed MLPs 0
- FLOPs per MLP: mean 5.1836e+11 (0.2357 x B), min 0.2355 x B, max 0.2400 x B
- Grader timing per MLP: kernel 82.5 s mean, predict wall 93.4 s mean / 99.7 s max, residual 0.311 s mean / 0.319 s max (cap 0.4 s)
- Smoke test: passed=True duration 45526.73271599997 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
