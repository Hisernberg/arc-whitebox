# Submission #334072 — d4-M8-soup21-a0.94

| Field | Value |
|---|---|
| Submission ID | 334072 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334072> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T22:26:06Z |
| Adjusted score (leaderboard) | 4.665153476259483e-09 |
| Raw final-layer MSE | 1.976646895940348e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + single weight-averaged final-weight-8 member soup21, correction scaled 0.94 (held-out 0.9203)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.665e-09, raw final-layer MSE 1.977e-08, all-layers MSE 8.602e-09, mean multiplier 0.23603919637431317, failed MLPs 0
- FLOPs per MLP: mean 5.1846e+11 (0.2358 x B), min 0.2355 x B, max 0.2400 x B
- Grader timing per MLP: kernel 82.2 s mean, predict wall 93.0 s mean / 98.0 s max, residual 0.312 s mean / 0.327 s max (cap 0.4 s)
- Smoke test: passed=True duration 45640.766791999995 ms, worker passes 7 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
