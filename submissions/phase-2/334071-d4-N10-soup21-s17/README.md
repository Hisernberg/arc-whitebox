# Submission #334071 — d4-N10-soup21-s17

| Field | Value |
|---|---|
| Submission ID | 334071 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334071> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T22:25:58Z |
| Adjusted score (leaderboard) | 4.672458723144228e-09 |
| Raw final-layer MSE | 1.9748857660317753e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + pair soup21 + 12-epoch s17 (held-out 0.9180)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.672e-09, raw final-layer MSE 1.975e-08, all-layers MSE 8.601e-09, mean multiplier 0.23662795451336932, failed MLPs 0
- FLOPs per MLP: mean 5.1985e+11 (0.2364 x B), min 0.2362 x B, max 0.2407 x B
- Grader timing per MLP: kernel 83.7 s mean, predict wall 94.9 s mean / 113.7 s max, residual 0.321 s mean / 0.350 s max (cap 0.4 s)
- Smoke test: passed=True duration 46427.395490998606 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
