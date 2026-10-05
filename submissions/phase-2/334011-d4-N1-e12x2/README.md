# Submission #334011 — d4-N1-e12x2

| Field | Value |
|---|---|
| Submission ID | 334011 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334011> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T16:53:32Z |
| Adjusted score (leaderboard) | 4.666501259287209e-09 |
| Raw final-layer MSE | 1.9723755322331727e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + 2-member CDF GRU corrector (hidden 64, 12-epoch schedule, best held-out 0.9223/0.9224 at epoch 8; 630 full-split MLPs, mini held out); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.667e-09, raw final-layer MSE 1.972e-08, all-layers MSE 8.599e-09, mean multiplier 0.23662795451336932, failed MLPs 0
- FLOPs per MLP: mean 5.1985e+11 (0.2364 x B), min 0.2362 x B, max 0.2407 x B
- Grader timing per MLP: kernel 85.9 s mean, predict wall 97.4 s mean / 103.6 s max, residual 0.327 s mean / 0.345 s max (cap 0.4 s)
- Smoke test: passed=True duration 49520.75405600001 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
