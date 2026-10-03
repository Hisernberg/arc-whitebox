# Submission #333793 — day3-M2-long1

| Field | Value |
|---|---|
| Submission ID | 333793 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333793> |
| Status | GRADED |
| Created (UTC) | 2026-10-03T15:53:17Z |
| Adjusted score (leaderboard) | 4.674446731053739e-09 |
| Raw final-layer MSE | 1.9813764673415336e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone level 2, leaf 8, first-call level 5) + a single CDF GRU corrector (hidden 64, 8 epochs, held-out 0.924); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.674e-09, raw final-layer MSE 1.981e-08, all-layers MSE 8.605e-09, mean multiplier 0.23594839683601093, failed MLPs 0
- FLOPs per MLP: mean 5.1836e+11 (0.2357 x B), min 0.2355 x B, max 0.2400 x B
- Grader timing per MLP: kernel 82.5 s mean, predict wall 93.4 s mean / 101.4 s max, residual 0.311 s mean / 0.322 s max (cap 0.4 s)
- Smoke test: passed=True duration 45899.232639000045 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
