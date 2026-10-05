# Submission #333792 — day3-M1-long2

| Field | Value |
|---|---|
| Submission ID | 333792 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333792> |
| Status | GRADED |
| Created (UTC) | 2026-10-03T15:53:06Z |
| Adjusted score (leaderboard) | 4.67552789035962e-09 |
| Raw final-layer MSE | 1.976154294425214e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone level 2, leaf 8, first-call level 5) + 2-member CDF GRU corrector ensemble (the two best 8-epoch members); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.676e-09, raw final-layer MSE 1.976e-08, all-layers MSE 8.601e-09, mean multiplier 0.23662795451336932, failed MLPs 0
- FLOPs per MLP: mean 5.1985e+11 (0.2364 x B), min 0.2362 x B, max 0.2407 x B
- Grader timing per MLP: kernel 82.8 s mean, predict wall 94.0 s mean / 102.4 s max, residual 0.321 s mean / 0.338 s max (cap 0.4 s)
- Smoke test: passed=True duration 46315.29095499991 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
