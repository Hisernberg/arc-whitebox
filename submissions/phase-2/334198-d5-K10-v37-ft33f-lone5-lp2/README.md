# Submission #334198 — d5-K10-v37-ft33f-lone5-lp2

| Field | Value |
|---|---|
| Submission ID | 334198 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334198> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T11:25:21Z |
| Adjusted score (leaderboard) | 4.19206923395615e-09 |
| Raw final-layer MSE | 1.9986691341955522e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37: V36 + GRU ft33f (held-out 0.907 on 143 unseen MLPs) + lone level 5; after the first 5 predicts the join products also go through Strassen level 2 (C/B -1%)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.192e-09, raw final-layer MSE 1.999e-08, all-layers MSE 8.689e-09, mean multiplier 0.20983762119871244, failed MLPs 0
- FLOPs per MLP: mean 4.5989e+11 (0.2091 x B), min 0.2053 x B, max 0.2191 x B
- Grader timing per MLP: kernel 95.1 s mean, predict wall 105.4 s mean / 113.1 s max, residual 0.292 s mean / 0.370 s max (cap 0.4 s)
- Smoke test: passed=True duration 45341.51537099996 ms, worker passes 7 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
