# Submission #334012 — d4-N2-e12x2-lam1

| Field | Value |
|---|---|
| Submission ID | 334012 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334012> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T16:53:42Z |
| Adjusted score (leaderboard) | 4.687007138681653e-09 |
| Raw final-layer MSE | 1.9810381850504653e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

As d4-N1 plus kappa4 lambda table scale 0.95 -> 1.00 (grader-verified -0.45% on plain V29)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.687e-09, raw final-layer MSE 1.981e-08, all-layers MSE 8.558e-09, mean multiplier 0.23662795451336932, failed MLPs 0
- FLOPs per MLP: mean 5.1985e+11 (0.2364 x B), min 0.2362 x B, max 0.2407 x B
- Grader timing per MLP: kernel 82.5 s mean, predict wall 93.7 s mean / 101.3 s max, residual 0.317 s mean / 0.332 s max (cap 0.4 s)
- Smoke test: passed=True duration 46128.70800999986 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
