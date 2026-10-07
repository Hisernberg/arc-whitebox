# Submission #334629 — d7-V42-a1

| Field | Value |
|---|---|
| Submission ID | 334629 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334629> |
| Status | GRADED |
| Created (UTC) | 2026-10-07T12:05:52Z |
| Adjusted score (leaderboard) | 4.044913185965295e-09 |
| Raw final-layer MSE | 1.9654051932604942e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V42 LT cross-neuron corrector

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.045e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.2058999918211339, failed MLPs 0
- FLOPs per MLP: mean 4.5093e+11 (0.2051 x B), min 0.2013 x B, max 0.2147 x B
- Grader timing per MLP: kernel 96.5 s mean, predict wall 106.8 s mean / 118.5 s max, residual 0.293 s mean / 0.369 s max (cap 0.4 s)
- Smoke test: passed=True duration 46484.861454000114 ms, worker passes 8 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
