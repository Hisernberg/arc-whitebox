# Submission #334260 — d5-N8-lic-v37lp3-rfb2

| Field | Value |
|---|---|
| Submission ID | 334260 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334260> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T16:56:37Z |
| Adjusted score (leaderboard) | 4.149363195172971e-09 |
| Raw final-layer MSE | 2.0352766263442846e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 + join level 3 + D21 feedback rank 2 + GRU ft33f (the 334221 build); ships 504aldo's MIT notice (attribution)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.149e-09, raw final-layer MSE 2.035e-08, all-layers MSE 8.789e-09, mean multiplier 0.20389499650496873, failed MLPs 0
- FLOPs per MLP: mean 4.4556e+11 (0.2026 x B), min 0.1989 x B, max 0.2135 x B
- Grader timing per MLP: kernel 95.6 s mean, predict wall 106.3 s mean / 115.7 s max, residual 0.304 s mean / 0.384 s max (cap 0.4 s)
- Smoke test: passed=True duration 46246.489239001676 ms, worker passes 6 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
