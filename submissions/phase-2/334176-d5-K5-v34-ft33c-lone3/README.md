# Submission #334176 — d5-K5-v34-ft33c-lone3

| Field | Value |
|---|---|
| Submission ID | 334176 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334176> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T08:13:44Z |
| Adjusted score (leaderboard) | 4.304334085042368e-09 |
| Raw final-layer MSE | 2.0001488074683492e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V34 + GRU fine-tuned on 418 V34 dumps (held-out 0.9218) + join lone products at Strassen level 3

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.304e-09, raw final-layer MSE 2e-08, all-layers MSE 8.693e-09, mean multiplier 0.21525184362923028, failed MLPs 0
- FLOPs per MLP: mean 4.7244e+11 (0.2148 x B), min 0.2114 x B, max 0.2239 x B
- Grader timing per MLP: kernel 84.0 s mean, predict wall 95.8 s mean / 103.4 s max, residual 0.349 s mean / 0.368 s max (cap 0.4 s)
- Smoke test: passed=True duration 47209.93299800011 ms, worker passes 9 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
