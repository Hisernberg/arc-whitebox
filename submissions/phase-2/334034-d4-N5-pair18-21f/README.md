# Submission #334034 — d4-N5-pair18-21f

| Field | Value |
|---|---|
| Submission ID | 334034 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334034> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T19:32:02Z |
| Adjusted score (leaderboard) | 4.658161584849348e-09 |
| Raw final-layer MSE | 1.968839288934987e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + 2-member CDF GRU ensemble: 12-epoch s18 + fully trained final-weight-8 s21 (held-out 0.9180); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.658e-09, raw final-layer MSE 1.969e-08, all-layers MSE 8.597e-09, mean multiplier 0.23662795451336932, failed MLPs 0
- FLOPs per MLP: mean 5.1985e+11 (0.2364 x B), min 0.2362 x B, max 0.2407 x B
- Grader timing per MLP: kernel 83.8 s mean, predict wall 95.0 s mean / 111.1 s max, residual 0.323 s mean / 0.373 s max (cap 0.4 s)
- Smoke test: passed=True duration 47351.46302300018 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
