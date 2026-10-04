# Submission #334073 — d4-M9-soup21-s18

| Field | Value |
|---|---|
| Submission ID | 334073 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334073> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T22:26:14Z |
| Adjusted score (leaderboard) | 4.6580040543971175e-09 |
| Raw final-layer MSE | 1.968046984046623e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + pair soup21 + 12-epoch s18 (held-out 0.9182)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.658e-09, raw final-layer MSE 1.968e-08, all-layers MSE 8.596e-09, mean multiplier 0.23671875405167156, failed MLPs 0
- FLOPs per MLP: mean 5.1995e+11 (0.2364 x B), min 0.2362 x B, max 0.2407 x B
- Grader timing per MLP: kernel 82.3 s mean, predict wall 93.4 s mean / 99.3 s max, residual 0.315 s mean / 0.322 s max (cap 0.4 s)
- Smoke test: passed=True duration 46419.07066099975 ms, worker passes 6 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
