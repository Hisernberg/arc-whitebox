# Submission #334074 — d4-M10-s17-a0.88

| Field | Value |
|---|---|
| Submission ID | 334074 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334074> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T22:26:21Z |
| Adjusted score (leaderboard) | 4.6776383947703825e-09 |
| Raw final-layer MSE | 1.982779011200364e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + single 12-epoch s17, correction scaled 0.88 (held-out 0.9209)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.678e-09, raw final-layer MSE 1.983e-08, all-layers MSE 8.605e-09, mean multiplier 0.23594839683601093, failed MLPs 0
- FLOPs per MLP: mean 5.1836e+11 (0.2357 x B), min 0.2355 x B, max 0.2400 x B
- Grader timing per MLP: kernel 83.9 s mean, predict wall 94.9 s mean / 119.0 s max, residual 0.315 s mean / 0.342 s max (cap 0.4 s)
- Smoke test: passed=True duration 47382.625572001416 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
