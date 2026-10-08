# Submission #334741 — d8-M1-v42lp4

| Field | Value |
|---|---|
| Submission ID | 334741 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334741> |
| Status | GRADED |
| Created (UTC) | 2026-10-08T00:22:14Z |
| Adjusted score (leaderboard) | 4.0362655228173015e-09 |
| Raw final-layer MSE | 1.9652343681286767e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

multi_agent: V42+LP4

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.036e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.20548891847858614, failed MLPs 0
- FLOPs per MLP: mean 4.4928e+11 (0.2043 x B), min 0.2007 x B, max 0.2147 x B
- Grader timing per MLP: kernel 99.8 s mean, predict wall 110.6 s mean / 118.4 s max, residual 0.303 s mean / 0.363 s max (cap 0.4 s)
- Smoke test: passed=True duration 46311.77542599972 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
