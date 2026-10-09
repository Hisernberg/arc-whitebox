# Submission #334956 — A-cs05

| Field | Value |
|---|---|
| Submission ID | 334956 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334956> |
| Status | GRADED |
| Created (UTC) | 2026-10-09T05:54:19Z |
| Adjusted score (leaderboard) | 4.095274385108171e-09 |
| Raw final-layer MSE | 2.0137575695855504e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track A grid: V44 + e2e corrector, scale 0.5

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.095e-09, raw final-layer MSE 2.014e-08, all-layers MSE 8.741e-09, mean multiplier 0.20343652978881438, failed MLPs 0
- FLOPs per MLP: mean 4.4550e+11 (0.2026 x B), min 0.1993 x B, max 0.2133 x B
- Grader timing per MLP: kernel 94.3 s mean, predict wall 105.1 s mean / 110.1 s max, residual 0.304 s mean / 0.361 s max (cap 0.4 s)
- Smoke test: passed=True duration 45229.35722199998 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
