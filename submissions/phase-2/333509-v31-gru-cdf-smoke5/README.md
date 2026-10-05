# Submission #333509 — v31-gru-cdf-smoke5

| Field | Value |
|---|---|
| Submission ID | 333509 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333509> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T09:28:23Z |
| Adjusted score (leaderboard) | 5.5842127726251894e-09 |
| Raw final-layer MSE | 2.192800408806761e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V31 pipeline test 5: GRU corrector with normal-CDF gates and 2*CDF-1 candidate (no tanh/exp: only ops V29 already runs on the grader), suite-shape gate, setup dry run, model embedded (hidden 48, trained on 20 mini MLPs with --act cdf).

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 5.584e-09, raw final-layer MSE 2.193e-08, all-layers MSE 8.735e-09, mean multiplier 0.2547297448773861, failed MLPs 0
- FLOPs per MLP: mean 5.5841e+11 (0.2539 x B), min 0.2531 x B, max 0.2676 x B
- Grader timing per MLP: kernel 62.6 s mean, predict wall 69.3 s mean / 74.6 s max, residual 0.191 s mean / 0.202 s max (cap 0.4 s)
- Smoke test: passed=True duration 22090.907485000116 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
