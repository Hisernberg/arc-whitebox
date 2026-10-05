# Submission #334213 — d5-M4-v37-rfb4-ft33f

| Field | Value |
|---|---|
| Submission ID | 334213 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334213> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T13:02:17Z |
| Adjusted score (leaderboard) | 4.16585082920776e-09 |
| Raw final-layer MSE | 2.0223369858740624e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 + D21 feedback rank 4 (C/B -1.8%; GRU ft33f unchanged: held-out 0.9166 on rank-4 features)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.166e-09, raw final-layer MSE 2.022e-08, all-layers MSE 8.756e-09, mean multiplier 0.20608202961531788, failed MLPs 0
- FLOPs per MLP: mean 4.5087e+11 (0.2050 x B), min 0.2016 x B, max 0.2154 x B
- Grader timing per MLP: kernel 96.0 s mean, predict wall 106.5 s mean / 112.5 s max, residual 0.299 s mean / 0.377 s max (cap 0.4 s)
- Smoke test: passed=True duration 45125.62030900153 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
