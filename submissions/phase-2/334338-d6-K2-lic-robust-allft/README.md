# Submission #334338 — d6-K2-lic-robust-allft

| Field | Value |
|---|---|
| Submission ID | 334338 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334338> |
| Status | GRADED |
| Created (UTC) | 2026-10-06T01:15:58Z |
| Adjusted score (leaderboard) | 4.1614540919396394e-09 |
| Raw final-layer MSE | 2.0303024292900318e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Robust licensed build: lone products at Strassen level 4 + join level 3 + D21 feedback rank 2 + GRU fine-tuned on ~1000 MLPs

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.161e-09, raw final-layer MSE 2.03e-08, all-layers MSE 8.782e-09, mean multiplier 0.20507334170662944, failed MLPs 0
- FLOPs per MLP: mean 4.4841e+11 (0.2039 x B), min 0.2003 x B, max 0.2149 x B
- Grader timing per MLP: kernel 90.6 s mean, predict wall 100.8 s mean / 108.8 s max, residual 0.291 s mean / 0.363 s max (cap 0.4 s)
- Smoke test: passed=True duration 46547.59470799945 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
