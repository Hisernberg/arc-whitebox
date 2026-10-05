# Submission #334168 — d5-K3-v34-ft33a-lone3

| Field | Value |
|---|---|
| Submission ID | 334168 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334168> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T07:12:23Z |
| Adjusted score (leaderboard) | 4.340109533588949e-09 |
| Raw final-layer MSE | 2.012890373492837e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V34 + GRU fine-tuned on V34 features (held-out 0.9247) + join lone products at Strassen level 3 (C/B -1.4%, +12% ops)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.34e-09, raw final-layer MSE 2.013e-08, all-layers MSE 8.701e-09, mean multiplier 0.2156715045359306, failed MLPs 0
- FLOPs per MLP: mean 4.7221e+11 (0.2147 x B), min 0.2114 x B, max 0.2239 x B
- Grader timing per MLP: kernel 83.5 s mean, predict wall 95.3 s mean / 106.4 s max, residual 0.346 s mean / 0.364 s max (cap 0.4 s)
- Smoke test: passed=True duration 46809.69057099992 ms, worker passes 8 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
