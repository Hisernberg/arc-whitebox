# Submission #334554 — d7-K1-v41-lt

| Field | Value |
|---|---|
| Submission ID | 334554 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334554> |
| Status | GRADED |
| Created (UTC) | 2026-10-07T01:29:05Z |
| Adjusted score (leaderboard) | 0.020395831281640592 |
| Raw final-layer MSE | 0.020395846712451374 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V41 LT corrector on L5 + age gate 8

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 0.0204, raw final-layer MSE 0.0204, all-layers MSE 0.01584, mean multiplier 0.22134680012224636, failed MLPs 1
- FLOPs per MLP: mean 4.4979e+11 (0.2045 x B), min 0.2010 x B, max 0.2144 x B
- Grader timing per MLP: kernel 98.4 s mean, predict wall 108.7 s mean / 119.7 s max, residual 0.293 s mean / 0.374 s max (cap 0.4 s)
- Smoke test: passed=True duration 46392.189779006 ms, worker passes 5 / failures 0
- MLPs completed: 99 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
