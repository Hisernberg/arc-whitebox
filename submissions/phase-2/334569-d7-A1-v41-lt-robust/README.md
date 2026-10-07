# Submission #334569 — d7-A1-v41-lt-robust

| Field | Value |
|---|---|
| Submission ID | 334569 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334569> |
| Status | GRADED |
| Created (UTC) | 2026-10-07T02:54:23Z |
| Adjusted score (leaderboard) | 4.09207861042283e-09 |
| Raw final-layer MSE | 1.976891837784933e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

nabid_nur: V41 LT on the robust build

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.092e-09, raw final-layer MSE 1.977e-08, all-layers MSE 8.717e-09, mean multiplier 0.20709221231700212, failed MLPs 0
- FLOPs per MLP: mean 4.5302e+11 (0.2060 x B), min 0.2024 x B, max 0.2158 x B
- Grader timing per MLP: kernel 90.8 s mean, predict wall 100.6 s mean / 108.0 s max, residual 0.276 s mean / 0.341 s max (cap 0.4 s)
- Smoke test: passed=True duration 45012.901258000056 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
