# Submission #334632 — d7-V42rb-a2

| Field | Value |
|---|---|
| Submission ID | 334632 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334632> |
| Status | GRADED |
| Created (UTC) | 2026-10-07T12:06:07Z |
| Adjusted score (leaderboard) | 4.0803604980220465e-09 |
| Raw final-layer MSE | 1.965242567791847e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

multi_agent: V42 on the robust build

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.08e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.2077117684467157, failed MLPs 0
- FLOPs per MLP: mean 4.5400e+11 (0.2065 x B), min 0.2027 x B, max 0.2175 x B
- Grader timing per MLP: kernel 90.0 s mean, predict wall 99.7 s mean / 107.1 s max, residual 0.277 s mean / 0.346 s max (cap 0.4 s)
- Smoke test: passed=True duration 46370.68787899989 ms, worker passes 6 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
