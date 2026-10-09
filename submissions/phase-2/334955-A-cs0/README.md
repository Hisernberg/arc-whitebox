# Submission #334955 — A-cs0

| Field | Value |
|---|---|
| Submission ID | 334955 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334955> |
| Status | GRADED |
| Created (UTC) | 2026-10-09T05:54:15Z |
| Adjusted score (leaderboard) | 4.44060964433171e-09 |
| Raw final-layer MSE | 2.1807612213819992e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track A grid: V44 + e2e corrector, scale 0.0

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.441e-09, raw final-layer MSE 2.181e-08, all-layers MSE 8.845e-09, mean multiplier 0.20369540384057472, failed MLPs 0
- FLOPs per MLP: mean 4.4579e+11 (0.2027 x B), min 0.1993 x B, max 0.2133 x B
- Grader timing per MLP: kernel 96.6 s mean, predict wall 107.6 s mean / 111.4 s max, residual 0.311 s mean / 0.363 s max (cap 0.4 s)
- Smoke test: passed=True duration 44719.00105200001 ms, worker passes 6 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
