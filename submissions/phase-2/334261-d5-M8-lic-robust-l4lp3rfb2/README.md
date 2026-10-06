# Submission #334261 — d5-M8-lic-robust-l4lp3rfb2

| Field | Value |
|---|---|
| Submission ID | 334261 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334261> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T16:56:42Z |
| Adjusted score (leaderboard) | 4.1737451453709985e-09 |
| Raw final-layer MSE | 2.0363222148489514e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Robust nomination build: lone join products at Strassen level 4 + join level 3 + D21 feedback rank 2 + GRU ft33f; ships 504aldo's MIT notice

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.174e-09, raw final-layer MSE 2.036e-08, all-layers MSE 8.786e-09, mean multiplier 0.20507334170662944, failed MLPs 0
- FLOPs per MLP: mean 4.4841e+11 (0.2039 x B), min 0.2003 x B, max 0.2149 x B
- Grader timing per MLP: kernel 89.8 s mean, predict wall 100.0 s mean / 106.9 s max, residual 0.288 s mean / 0.361 s max (cap 0.4 s)
- Smoke test: passed=True duration 44908.75357699997 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
