# Submission #334281 — d5-M10-lic-robust-allft

| Field | Value |
|---|---|
| Submission ID | 334281 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334281> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T19:03:02Z |
| Adjusted score (leaderboard) | 4.161474249860101e-09 |
| Raw final-layer MSE | 2.0303024292900318e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

d5-M10-lic-robust-allft

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.161e-09, raw final-layer MSE 2.03e-08, all-layers MSE 8.782e-09, mean multiplier 0.20507412783746987, failed MLPs 0
- FLOPs per MLP: mean 4.4840e+11 (0.2039 x B), min 0.2003 x B, max 0.2149 x B
- Grader timing per MLP: kernel 91.0 s mean, predict wall 101.3 s mean / 109.5 s max, residual 0.291 s mean / 0.374 s max (cap 0.4 s)
- Smoke test: passed=True duration 47937.117841000145 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
