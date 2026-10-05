# Submission #334188 — d5-K9-v36-ft33f-lone5

| Field | Value |
|---|---|
| Submission ID | 334188 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334188> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T10:04:46Z |
| Adjusted score (leaderboard) | 4.226604938034451e-09 |
| Raw final-layer MSE | 2.000859399942101e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V36 + GRU fine-tuned on 508 V34 dumps (held-out 0.9165) + join lone products at Strassen level 5

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.227e-09, raw final-layer MSE 2.001e-08, all-layers MSE 8.694e-09, mean multiplier 0.2112972280916074, failed MLPs 0
- FLOPs per MLP: mean 4.6305e+11 (0.2106 x B), min 0.2075 x B, max 0.2191 x B
- Grader timing per MLP: kernel 92.8 s mean, predict wall 102.3 s mean / 116.8 s max, residual 0.268 s mean / 0.376 s max (cap 0.4 s)
- Smoke test: passed=True duration 46056.70780900004 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
