# Submission #334161 — d5-K2-v34-ft33ep3

| Field | Value |
|---|---|
| Submission ID | 334161 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334161> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T06:34:00Z |
| Adjusted score (leaderboard) | 4.3807627987703416e-09 |
| Raw final-layer MSE | 2.0061370058499506e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V34 (pruning, shared Strassen scratch, dense joins, FB rank 8, leaf 8) + GRU fine-tuned on V34 features (held-out 0.925)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.381e-09, raw final-layer MSE 2.006e-08, all-layers MSE 8.696e-09, mean multiplier 0.21841704818369181, failed MLPs 0
- FLOPs per MLP: mean 4.7874e+11 (0.2177 x B), min 0.2146 x B, max 0.2260 x B
- Grader timing per MLP: kernel 79.7 s mean, predict wall 90.1 s mean / 99.3 s max, residual 0.303 s mean / 0.328 s max (cap 0.4 s)
- Smoke test: passed=True duration 46369.078236999485 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
