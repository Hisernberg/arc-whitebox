# Submission #334344 — d6-M2-rb-pair

| Field | Value |
|---|---|
| Submission ID | 334344 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334344> |
| Status | GRADED |
| Created (UTC) | 2026-10-06T02:04:47Z |
| Adjusted score (leaderboard) | 4.160035964729637e-09 |
| Raw final-layer MSE | 2.0228938204525094e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Robust licensed build + 2-member GRU (all-data fine-tune + from-scratch, held-out 0.9105)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.16e-09, raw final-layer MSE 2.023e-08, all-layers MSE 8.778e-09, mean multiplier 0.20575008416770288, failed MLPs 0
- FLOPs per MLP: mean 4.4990e+11 (0.2046 x B), min 0.2010 x B, max 0.2155 x B
- Grader timing per MLP: kernel 91.5 s mean, predict wall 102.0 s mean / 111.6 s max, residual 0.300 s mean / 0.377 s max (cap 0.4 s)
- Smoke test: passed=True duration 47039.63074300191 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
