# Submission #333589 — acct2-tanh3

| Field | Value |
|---|---|
| Submission ID | 333589 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333589> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T17:03:51Z |
| Adjusted score (leaderboard) | 4.734191368920068e-09 |
| Raw final-layer MSE | 1.9999398794823263e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Acct2 V32 tanh-3: lone level 2, leaf 8, first-call level 5 + 3-member tanh-gated GRU corrector ensemble (hidden 64) trained on 630 full-split MLPs, 100 mini held out (ratio 0.9349); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.734e-09, raw final-layer MSE 2e-08, all-layers MSE 8.616e-09, mean multiplier 0.23674675169268083, failed MLPs 0
- FLOPs per MLP: mean 5.2011e+11 (0.2365 x B), min 0.2363 x B, max 0.2408 x B
- Grader timing per MLP: kernel 84.6 s mean, predict wall 96.2 s mean / 101.1 s max, residual 0.333 s mean / 0.344 s max (cap 0.4 s)
- Smoke test: passed=True duration 46828.13878199977 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
