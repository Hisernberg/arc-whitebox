# Submission #334220 — d5-M5-v37lp3-rfb4-ft33f

| Field | Value |
|---|---|
| Submission ID | 334220 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334220> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T13:55:28Z |
| Adjusted score (leaderboard) | 4.157495341256119e-09 |
| Raw final-layer MSE | 2.023661284766831e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 + join products at Strassen level 3 after the first 5 MLPs + D21 feedback rank 4 + GRU ft33f

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.157e-09, raw final-layer MSE 2.024e-08, all-layers MSE 8.756e-09, mean multiplier 0.20554816554289573, failed MLPs 0
- FLOPs per MLP: mean 4.4944e+11 (0.2044 x B), min 0.2008 x B, max 0.2154 x B
- Grader timing per MLP: kernel 97.0 s mean, predict wall 107.8 s mean / 114.3 s max, residual 0.306 s mean / 0.378 s max (cap 0.4 s)
- Smoke test: passed=True duration 45189.52146200172 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
