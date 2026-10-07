# Submission #334557 — d7-K4-v41-lt-robust-ao7

| Field | Value |
|---|---|
| Submission ID | 334557 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334557> |
| Status | GRADED |
| Created (UTC) | 2026-10-07T01:36:32Z |
| Adjusted score (leaderboard) | 4.093141480906217e-09 |
| Raw final-layer MSE | 1.9953253165283512e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V41 LT on robust build, age gate 7

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.093e-09, raw final-layer MSE 1.995e-08, all-layers MSE 8.76e-09, mean multiplier 0.20523694700885245, failed MLPs 0
- FLOPs per MLP: mean 4.4877e+11 (0.2041 x B), min 0.2005 x B, max 0.2150 x B
- Grader timing per MLP: kernel 90.3 s mean, predict wall 100.4 s mean / 106.7 s max, residual 0.286 s mean / 0.361 s max (cap 0.4 s)
- Smoke test: passed=True duration 45873.57671799691 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
