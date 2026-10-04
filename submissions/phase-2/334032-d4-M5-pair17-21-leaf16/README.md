# Submission #334032 — d4-M5-pair17-21-leaf16

| Field | Value |
|---|---|
| Submission ID | 334032 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334032> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T19:04:39Z |
| Adjusted score (leaderboard) | 4.744093585497563e-09 |
| Raw final-layer MSE | 1.9739087164794e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Safe variant for the private rerun: V32 (lone L2, leaf 16, first-call L5) + the best held-out pair (12-epoch s17 + final-weight-8 s21, held-out 0.9180); leaf 16 keeps grader wall time ~10 s further from the 120 s cap; model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.744e-09, raw final-layer MSE 1.974e-08, all-layers MSE 8.599e-09, mean multiplier 0.2403745732396601, failed MLPs 0
- FLOPs per MLP: mean 5.2811e+11 (0.2402 x B), min 0.2399 x B, max 0.2443 x B
- Grader timing per MLP: kernel 74.3 s mean, predict wall 85.0 s mean / 92.2 s max, residual 0.305 s mean / 0.314 s max (cap 0.4 s)
- Smoke test: passed=True duration 29394.6450859994 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
