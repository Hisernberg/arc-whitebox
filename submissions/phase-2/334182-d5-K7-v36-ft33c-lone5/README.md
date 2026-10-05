# Submission #334182 — d5-K7-v36-ft33c-lone5

| Field | Value |
|---|---|
| Submission ID | 334182 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334182> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T09:24:13Z |
| Adjusted score (leaderboard) | 4.225170401455002e-09 |
| Raw final-layer MSE | 1.9984850787579945e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V36 + ft33c GRU + lone level 5

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.225e-09, raw final-layer MSE 1.998e-08, all-layers MSE 8.692e-09, mean multiplier 0.2114657890747185, failed MLPs 0
- FLOPs per MLP: mean 4.6412e+11 (0.2111 x B), min 0.2075 x B, max 0.2191 x B
- Grader timing per MLP: kernel 94.9 s mean, predict wall 104.6 s mean / 116.8 s max, residual 0.275 s mean / 0.382 s max (cap 0.4 s)
- Smoke test: passed=True duration 44885.96128500012 ms, worker passes 10 / failures 0
- MLPs completed: 99 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
