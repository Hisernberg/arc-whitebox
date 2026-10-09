# Submission #334959 — C-rold2-256

| Field | Value |
|---|---|
| Submission ID | 334959 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334959> |
| Status | GRADED |
| Created (UTC) | 2026-10-09T05:54:30Z |
| Adjusted score (leaderboard) | 0.047829270586543335 |
| Raw final-layer MSE | 0.04782928525813265 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track C grid: V44, R_OLD2 256

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 0.04783, raw final-layer MSE 0.04783, all-layers MSE 0.04238, mean multiplier 0.2534121060916823, failed MLPs 3
- FLOPs per MLP: mean 4.5075e+11 (0.2050 x B), min 0.2014 x B, max 0.2160 x B
- Grader timing per MLP: kernel 102.0 s mean, predict wall 112.6 s mean / 119.6 s max, residual 0.293 s mean / 0.358 s max (cap 0.4 s)
- Smoke test: passed=True duration 46765.39280299994 ms, worker passes 6 / failures 0
- MLPs completed: 93 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
