# Submission #333572 — sub18_A2S2_leaf8-v32

| Field | Value |
|---|---|
| Submission ID | 333572 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333572> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T15:56:48Z |
| Adjusted score (leaderboard) | 4.77916328139352e-09 |
| Raw final-layer MSE | 1.9837512112985677e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Acct2 V32-S2 leaf-8: lone level 2, leaf 8 + 5-member GRU corrector ensemble (3 x h64 + 2 x h96, full split, 100 mini held out, ratio 0.9260); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.779e-09, raw final-layer MSE 1.984e-08, all-layers MSE 8.607e-09, mean multiplier 0.24102327601385695, failed MLPs 0
- FLOPs per MLP: mean 5.2814e+11 (0.2402 x B), min 0.2393 x B, max 0.2554 x B
- Grader timing per MLP: kernel 87.5 s mean, predict wall 99.8 s mean / 118.5 s max, residual 0.349 s mean / 0.388 s max (cap 0.4 s)
- Smoke test: passed=True duration 30160.138391000146 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
