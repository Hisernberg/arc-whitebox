# Submission #334889 — d8-C1-l5-lam090-r192

| Field | Value |
|---|---|
| Submission ID | 334889 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334889> |
| Status | GRADED |
| Created (UTC) | 2026-10-08T22:01:18Z |
| Adjusted score (leaderboard) | 4.023068567185123e-09 |
| Raw final-layer MSE | 1.988293888643966e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track C: V42+LP4+warm-up 2 with LAM_SCALE 0.90 and R_OLD2 192 (local -1.0%); predicted ~3.98-3.99e-09

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.023e-09, raw final-layer MSE 1.988e-08, all-layers MSE 8.817e-09, mean multiplier 0.20240440151421354, failed MLPs 0
- FLOPs per MLP: mean 4.4324e+11 (0.2016 x B), min 0.1982 x B, max 0.2122 x B
- Grader timing per MLP: kernel 97.2 s mean, predict wall 107.8 s mean / 118.2 s max, residual 0.302 s mean / 0.351 s max (cap 0.4 s)
- Smoke test: passed=True duration 44351.783119000174 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
