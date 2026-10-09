# Submission #334957 — A-cs15

| Field | Value |
|---|---|
| Submission ID | 334957 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334957> |
| Status | GRADED |
| Created (UTC) | 2026-10-09T05:54:23Z |
| Adjusted score (leaderboard) | 4.114820508108998e-09 |
| Raw final-layer MSE | 2.0232541864118048e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track A grid: V44 + e2e corrector, scale 1.5

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.115e-09, raw final-layer MSE 2.023e-08, all-layers MSE 8.747e-09, mean multiplier 0.20343710095832648, failed MLPs 0
- FLOPs per MLP: mean 4.4550e+11 (0.2026 x B), min 0.1993 x B, max 0.2133 x B
- Grader timing per MLP: kernel 95.9 s mean, predict wall 106.8 s mean / 114.4 s max, residual 0.309 s mean / 0.373 s max (cap 0.4 s)
- Smoke test: passed=True duration 46266.046768 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
