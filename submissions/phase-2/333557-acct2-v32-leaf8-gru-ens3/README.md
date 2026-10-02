# Submission #333557 — acct2-v32-leaf8-gru-ens3

| Field | Value |
|---|---|
| Submission ID | 333557 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333557> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T14:40:12Z |
| Adjusted score (leaderboard) | 4.8548392871855276e-09 |
| Raw final-layer MSE | 2.0334141410671693e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Second account: V32 with leaf 8 (local steady cost 0.2358 x B vs 0.2400 at leaf 16; residual risk) + the 3-member GRU corrector ensemble of 333531.

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.855e-09, raw final-layer MSE 2.033e-08, all-layers MSE 8.637e-09, mean multiplier 0.2389359403533854, failed MLPs 0
- FLOPs per MLP: mean 5.2279e+11 (0.2377 x B), min 0.2362 x B, max 0.2523 x B
- Grader timing per MLP: kernel 84.9 s mean, predict wall 96.6 s mean / 108.4 s max, residual 0.333 s mean / 0.359 s max (cap 0.4 s)
- Smoke test: passed=True duration 29410.116840999763 ms, worker passes 10 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
