# Submission #334215 — d5-N4-v37-rfb2-ft33f

| Field | Value |
|---|---|
| Submission ID | 334215 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334215> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T13:08:40Z |
| Adjusted score (leaderboard) | 4.156257652586278e-09 |
| Raw final-layer MSE | 2.036341065547731e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 + D21 feedback rank 2 (C/B -2.7%) + GRU ft33f

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.156e-09, raw final-layer MSE 2.036e-08, all-layers MSE 8.789e-09, mean multiplier 0.2042040509458093, failed MLPs 0
- FLOPs per MLP: mean 4.4675e+11 (0.2032 x B), min 0.1997 x B, max 0.2135 x B
- Grader timing per MLP: kernel 94.3 s mean, predict wall 104.6 s mean / 112.9 s max, residual 0.291 s mean / 0.370 s max (cap 0.4 s)
- Smoke test: passed=True duration 46238.07250700065 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
