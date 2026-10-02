# Submission #333571 — sub13_S2-v32

| Field | Value |
|---|---|
| Submission ID | 333571 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333571> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T15:53:39Z |
| Adjusted score (leaderboard) | 4.8545840843982785e-09 |
| Raw final-layer MSE | 1.9841617913129996e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32-S2: V29 (504aldo MIT) + Strassen-priced lone join products (level 2, leaf 16) + 5-member per-layer GRU corrector ensemble (CDF gates; 3 x hidden 64 + 2 x hidden 96) trained on 630 full-split MLPs with all 100 mini MLPs held out (held-out final-layer MSE ratio 0.9260 vs V29); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.855e-09, raw final-layer MSE 1.984e-08, all-layers MSE 8.605e-09, mean multiplier 0.24477478222788704, failed MLPs 0
- FLOPs per MLP: mean 5.3640e+11 (0.2439 x B), min 0.2431 x B, max 0.2587 x B
- Grader timing per MLP: kernel 77.8 s mean, predict wall 89.5 s mean / 105.2 s max, residual 0.333 s mean / 0.370 s max (cap 0.4 s)
- Smoke test: passed=True duration 30121.592153000165 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
