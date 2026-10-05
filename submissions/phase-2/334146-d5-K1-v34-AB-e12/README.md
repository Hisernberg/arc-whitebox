# Submission #334146 — d5-K1-v34-AB-e12

| Field | Value |
|---|---|
| Submission ID | 334146 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334146> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T05:33:45Z |
| Adjusted score (leaderboard) | 4.533789496996293e-09 |
| Raw final-layer MSE | 2.0762865347023762e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V34: dead-ReLU pruning (transport + hub/old tier), shared Strassen scratch, dense join products, D21 feedback rank 8, leaf 8 + single GRU corrector (telemetry run)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.534e-09, raw final-layer MSE 2.076e-08, all-layers MSE 8.74e-09, mean multiplier 0.21841712293025922, failed MLPs 0
- FLOPs per MLP: mean 4.7874e+11 (0.2177 x B), min 0.2146 x B, max 0.2260 x B
- Grader timing per MLP: kernel 81.8 s mean, predict wall 92.4 s mean / 99.8 s max, residual 0.309 s mean / 0.327 s max (cap 0.4 s)
- Smoke test: passed=True duration 45640.32616700024 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
