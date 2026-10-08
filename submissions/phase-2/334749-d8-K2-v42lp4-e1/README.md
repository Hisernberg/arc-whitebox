# Submission #334749 — d8-K2-v42lp4-e1

| Field | Value |
|---|---|
| Submission ID | 334749 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334749> |
| Status | GRADED |
| Created (UTC) | 2026-10-08T01:44:14Z |
| Adjusted score (leaderboard) | 0.031977732470156436 |
| Raw final-layer MSE | 0.031977747431602595 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V42 + LP4 + warm-up schedule on the first call per worker only; predicted ~4.015-4.02e-09 (wall risk on cold first calls)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 0.03198, raw final-layer MSE 0.03198, all-layers MSE 0.02684, mean multiplier 0.23715247391889535, failed MLPs 2
- FLOPs per MLP: mean 4.4907e+11 (0.2042 x B), min 0.2007 x B, max 0.2147 x B
- Grader timing per MLP: kernel 100.6 s mean, predict wall 111.4 s mean / 117.6 s max, residual 0.306 s mean / 0.364 s max (cap 0.4 s)
- Smoke test: passed=True duration 45782.01119300047 ms, worker passes 5 / failures 0
- MLPs completed: 98 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
