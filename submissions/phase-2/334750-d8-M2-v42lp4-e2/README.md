# Submission #334750 — d8-M2-v42lp4-e2

| Field | Value |
|---|---|
| Submission ID | 334750 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334750> |
| Status | GRADED |
| Created (UTC) | 2026-10-08T01:44:19Z |
| Adjusted score (leaderboard) | 4.023065121284734e-09 |
| Raw final-layer MSE | 1.9649280602607177e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V42 + LP4 + warm-up on 2 calls (graded 4.023e-09 on koushik_rudra); predicted ~4.02-4.03e-09

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.023e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.20481567204398743, failed MLPs 0
- FLOPs per MLP: mean 4.4854e+11 (0.2040 x B), min 0.2006 x B, max 0.2147 x B
- Grader timing per MLP: kernel 100.4 s mean, predict wall 111.3 s mean / 119.3 s max, residual 0.307 s mean / 0.363 s max (cap 0.4 s)
- Smoke test: passed=True duration 44331.71154299998 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
