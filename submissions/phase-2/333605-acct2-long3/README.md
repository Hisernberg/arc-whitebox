# Submission #333605 — acct2-long3

| Field | Value |
|---|---|
| Submission ID | 333605 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333605> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T19:22:19Z |
| Adjusted score (leaderboard) | 4.6890244120345144e-09 |
| Raw final-layer MSE | 1.976181152940626e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Acct2 V32 long-3: lone level 2, leaf 8, first-call level 5 + 3-member CDF-gated GRU corrector ensemble (hidden 64) trained for 8 epochs on 630 full-split MLPs, 100 mini held out (ratio 0.9213); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.689e-09, raw final-layer MSE 1.976e-08, all-layers MSE 8.601e-09, mean multiplier 0.2373075121907277, failed MLPs 0
- FLOPs per MLP: mean 5.2135e+11 (0.2371 x B), min 0.2369 x B, max 0.2414 x B
- Grader timing per MLP: kernel 82.4 s mean, predict wall 93.6 s mean / 101.6 s max, residual 0.323 s mean / 0.342 s max (cap 0.4 s)
- Smoke test: passed=True duration 46941.763163999894 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
