# Submission #334020 — d4-N3-e12x3

| Field | Value |
|---|---|
| Submission ID | 334020 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334020> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T17:43:47Z |
| Adjusted score (leaderboard) | 0.08077603528925095 |
| Raw final-layer MSE | 0.08077604900345534 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + 3-member 12-epoch-schedule CDF GRU ensemble (held-out ratio 0.9180 on 100 mini MLPs vs 0.9213 for the 333790 ensemble); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 0.08078, raw final-layer MSE 0.08078, all-layers MSE 0.06486, mean multiplier 0.29854083010739485, failed MLPs 4
- FLOPs per MLP: mean 5.2002e+11 (0.2365 x B), min 0.1998 x B, max 0.2414 x B
- Grader timing per MLP: kernel 84.9 s mean, predict wall 96.0 s mean / 119.6 s max, residual 0.315 s mean / 0.405 s max (cap 0.4 s)
- Smoke test: passed=True duration 46413.06793400008 ms, worker passes 5 / failures 0
- MLPs completed: 96 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
