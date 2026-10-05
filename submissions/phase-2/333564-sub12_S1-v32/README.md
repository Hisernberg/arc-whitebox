# Submission #333564 — sub12_S1-v32

| Field | Value |
|---|---|
| Submission ID | 333564 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333564> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T15:22:44Z |
| Adjusted score (leaderboard) | 4.803538873947467e-09 |
| Raw final-layer MSE | 1.9832443811651502e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32-S1: V29 (504aldo MIT) + Strassen-priced lone join products (level 2, leaf 16) + 3-member per-layer GRU corrector ensemble (CDF gates, hidden 64, 5 epochs) trained on 630 full-split MLPs with all 100 mini MLPs held out (held-out final-layer MSE ratio 0.9252 vs V29); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.804e-09, raw final-layer MSE 1.983e-08, all-layers MSE 8.605e-09, mean multiplier 0.24231512671203745, failed MLPs 0
- FLOPs per MLP: mean 5.3136e+11 (0.2416 x B), min 0.2406 x B, max 0.2562 x B
- Grader timing per MLP: kernel 75.3 s mean, predict wall 86.4 s mean / 98.0 s max, residual 0.317 s mean / 0.345 s max (cap 0.4 s)
- Smoke test: passed=True duration 28631.365322999955 ms, worker passes 6 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
