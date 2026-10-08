# Submission #334743 — d8-N1-v42lp4-e3

| Field | Value |
|---|---|
| Submission ID | 334743 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334743> |
| Status | GRADED |
| Created (UTC) | 2026-10-08T00:22:24Z |
| Adjusted score (leaderboard) | 4.029883677900908e-09 |
| Raw final-layer MSE | 1.9650111120483872e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

nabid_nur: V42+LP4, warm-up 3 calls

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.03e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.20515167604658927, failed MLPs 0
- FLOPs per MLP: mean 4.4948e+11 (0.2044 x B), min 0.2007 x B, max 0.2147 x B
- Grader timing per MLP: kernel 100.1 s mean, predict wall 110.7 s mean / 117.2 s max, residual 0.297 s mean / 0.365 s max (cap 0.4 s)
- Smoke test: passed=True duration 45163.16138400043 ms, worker passes 5 / failures 0
- MLPs completed: 97 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
