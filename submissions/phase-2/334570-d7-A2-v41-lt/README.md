# Submission #334570 — d7-A2-v41-lt

| Field | Value |
|---|---|
| Submission ID | 334570 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334570> |
| Status | GRADED |
| Created (UTC) | 2026-10-07T02:54:27Z |
| Adjusted score (leaderboard) | 4.063218059696819e-09 |
| Raw final-layer MSE | 1.9769000090263943e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

multi_agent: V41 LT on L5 + age gate 8

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.063e-09, raw final-layer MSE 1.977e-08, all-layers MSE 8.717e-09, mean multiplier 0.20563117657024121, failed MLPs 0
- FLOPs per MLP: mean 4.4979e+11 (0.2045 x B), min 0.2010 x B, max 0.2144 x B
- Grader timing per MLP: kernel 97.7 s mean, predict wall 108.1 s mean / 118.6 s max, residual 0.294 s mean / 0.366 s max (cap 0.4 s)
- Smoke test: passed=True duration 46674.11386400636 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
