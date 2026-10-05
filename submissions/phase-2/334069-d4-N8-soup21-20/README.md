# Submission #334069 — d4-N8-soup21-20

| Field | Value |
|---|---|
| Submission ID | 334069 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334069> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T22:25:43Z |
| Adjusted score (leaderboard) | 4.664074227339462e-09 |
| Raw final-layer MSE | 1.9713246182107013e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + pair of weight-averaged final-weight-8 GRU members soup21 + soup20 (held-out 0.9179)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.664e-09, raw final-layer MSE 1.971e-08, all-layers MSE 8.598e-09, mean multiplier 0.23662795451336932, failed MLPs 0
- FLOPs per MLP: mean 5.1985e+11 (0.2364 x B), min 0.2362 x B, max 0.2407 x B
- Grader timing per MLP: kernel 83.4 s mean, predict wall 94.5 s mean / 99.9 s max, residual 0.318 s mean / 0.326 s max (cap 0.4 s)
- Smoke test: passed=True duration 46968.33568900183 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
