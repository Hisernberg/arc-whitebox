# Submission #334631 — d7-V42-a2

| Field | Value |
|---|---|
| Submission ID | 334631 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334631> |
| Status | GRADED |
| Created (UTC) | 2026-10-07T12:06:01Z |
| Adjusted score (leaderboard) | 4.051852605910652e-09 |
| Raw final-layer MSE | 1.9656288827718528e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V42 LT cross-neuron corrector

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.052e-09, raw final-layer MSE 1.966e-08, all-layers MSE 8.711e-09, mean multiplier 0.20625479334561533, failed MLPs 0
- FLOPs per MLP: mean 4.5117e+11 (0.2052 x B), min 0.2013 x B, max 0.2147 x B
- Grader timing per MLP: kernel 96.2 s mean, predict wall 106.5 s mean / 114.1 s max, residual 0.291 s mean / 0.361 s max (cap 0.4 s)
- Smoke test: passed=True duration 45855.03090800012 ms, worker passes 7 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
