# Submission #334221 — d5-N5-v37lp3-rfb2-ft33f

| Field | Value |
|---|---|
| Submission ID | 334221 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334221> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T13:56:46Z |
| Adjusted score (leaderboard) | 4.145184488570746e-09 |
| Raw final-layer MSE | 2.0363801915834756e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 + join products at Strassen level 3 after the first 5 MLPs + D21 feedback rank 2 + GRU ft33f

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.145e-09, raw final-layer MSE 2.036e-08, all-layers MSE 8.79e-09, mean multiplier 0.20367103722095636, failed MLPs 0
- FLOPs per MLP: mean 4.4531e+11 (0.2025 x B), min 0.1989 x B, max 0.2135 x B
- Grader timing per MLP: kernel 95.3 s mean, predict wall 105.8 s mean / 113.4 s max, residual 0.301 s mean / 0.375 s max (cap 0.4 s)
- Smoke test: passed=True duration 46165.88386700005 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
