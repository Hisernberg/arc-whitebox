# Submission #334345 — d6-N2-rb-lp2

| Field | Value |
|---|---|
| Submission ID | 334345 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334345> |
| Status | GRADED |
| Created (UTC) | 2026-10-06T02:04:51Z |
| Adjusted score (leaderboard) | 4.169529494951764e-09 |
| Raw final-layer MSE | 2.028790156316518e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Robust licensed build with join products at Strassen level 2 (less wall time)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.17e-09, raw final-layer MSE 2.029e-08, all-layers MSE 8.782e-09, mean multiplier 0.20560832509185276, failed MLPs 0
- FLOPs per MLP: mean 4.4984e+11 (0.2046 x B), min 0.2011 x B, max 0.2149 x B
- Grader timing per MLP: kernel 88.4 s mean, predict wall 98.2 s mean / 105.0 s max, residual 0.277 s mean / 0.355 s max (cap 0.4 s)
- Smoke test: passed=True duration 45401.783979001266 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
