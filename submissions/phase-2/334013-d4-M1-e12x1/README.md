# Submission #334013 — d4-M1-e12x1

| Field | Value |
|---|---|
| Submission ID | 334013 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334013> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T16:53:52Z |
| Adjusted score (leaderboard) | 4.654397819707255e-09 |
| Raw final-layer MSE | 1.9729222877629126e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5) + single 12-epoch-schedule CDF GRU member (held-out 0.9223); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.654e-09, raw final-layer MSE 1.973e-08, all-layers MSE 8.599e-09, mean multiplier 0.23594839683601093, failed MLPs 0
- FLOPs per MLP: mean 5.1836e+11 (0.2357 x B), min 0.2355 x B, max 0.2400 x B
- Grader timing per MLP: kernel 84.2 s mean, predict wall 95.2 s mean / 102.8 s max, residual 0.315 s mean / 0.327 s max (cap 0.4 s)
- Smoke test: passed=True duration 47554.09367999982 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
