# Submission #334030 — d4-N4-pair17-21

| Field | Value |
|---|---|
| Submission ID | 334030 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334030> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T19:03:22Z |
| Adjusted score (leaderboard) | 4.670282199297089e-09 |
| Raw final-layer MSE | 1.9739661141215948e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + 2-member CDF GRU ensemble: 12-epoch member s17 + final-layer-weight-8 member s21 (held-out ratio 0.9180 on 100 mini MLPs, best pair so far); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.67e-09, raw final-layer MSE 1.974e-08, all-layers MSE 8.6e-09, mean multiplier 0.23662795451336932, failed MLPs 0
- FLOPs per MLP: mean 5.1985e+11 (0.2364 x B), min 0.2362 x B, max 0.2407 x B
- Grader timing per MLP: kernel 87.6 s mean, predict wall 99.4 s mean / 109.6 s max, residual 0.334 s mean / 0.361 s max (cap 0.4 s)
- Smoke test: passed=True duration 48106.44992400012 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
