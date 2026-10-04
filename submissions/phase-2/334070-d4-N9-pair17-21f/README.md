# Submission #334070 — d4-N9-pair17-21f

| Field | Value |
|---|---|
| Submission ID | 334070 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334070> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T22:25:51Z |
| Adjusted score (leaderboard) | 4.677469973267987e-09 |
| Raw final-layer MSE | 1.9770037269495334e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + pair 12-epoch s17 + final-weight-8 s21 (held-out 0.9183)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.677e-09, raw final-layer MSE 1.977e-08, all-layers MSE 8.602e-09, mean multiplier 0.23662795451336932, failed MLPs 0
- FLOPs per MLP: mean 5.1985e+11 (0.2364 x B), min 0.2362 x B, max 0.2407 x B
- Grader timing per MLP: kernel 84.4 s mean, predict wall 95.7 s mean / 104.7 s max, residual 0.323 s mean / 0.346 s max (cap 0.4 s)
- Smoke test: passed=True duration 47262.42071899833 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
