# Submission #334917 — d9-A2-rb-e2e

| Field | Value |
|---|---|
| Submission ID | 334917 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334917> |
| Status | GRADED |
| Created (UTC) | 2026-10-09T00:21:00Z |
| Adjusted score (leaderboard) | 4.055178772927455e-09 |
| Raw final-layer MSE | 1.9614483122154524e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track A nominee: robust V42 + warm-up 2 with the end-to-end corrector; predicted ~4.055e-09, wall max ~105 s

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.055e-09, raw final-layer MSE 1.961e-08, all-layers MSE 8.708e-09, mean multiplier 0.20680577313331014, failed MLPs 0
- FLOPs per MLP: mean 4.5300e+11 (0.2060 x B), min 0.2027 x B, max 0.2161 x B
- Grader timing per MLP: kernel 90.2 s mean, predict wall 100.1 s mean / 109.0 s max, residual 0.280 s mean / 0.348 s max (cap 0.4 s)
- Smoke test: passed=True duration 46048.89657000013 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
