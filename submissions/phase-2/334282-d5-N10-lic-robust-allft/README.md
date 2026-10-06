# Submission #334282 — d5-N10-lic-robust-allft

| Field | Value |
|---|---|
| Submission ID | 334282 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334282> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T19:03:06Z |
| Adjusted score (leaderboard) | 4.1614540919396394e-09 |
| Raw final-layer MSE | 2.0303024292900318e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

d5-N10-lic-robust-allft

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.161e-09, raw final-layer MSE 2.03e-08, all-layers MSE 8.782e-09, mean multiplier 0.20507334170662944, failed MLPs 0
- FLOPs per MLP: mean 4.4841e+11 (0.2039 x B), min 0.2003 x B, max 0.2149 x B
- Grader timing per MLP: kernel 90.0 s mean, predict wall 100.1 s mean / 108.2 s max, residual 0.289 s mean / 0.371 s max (cap 0.4 s)
- Smoke test: passed=True duration 45396.046898997156 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
