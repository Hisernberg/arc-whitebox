# Submission #333596 — acct2-alldata3

| Field | Value |
|---|---|
| Submission ID | 333596 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333596> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T18:02:36Z |
| Adjusted score (leaderboard) | 4.728793883060383e-09 |
| Raw final-layer MSE | 1.992145580942406e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Acct2 V32 all-data-3: lone level 2, leaf 8, first-call level 5 + 3-member CDF-gated GRU corrector ensemble (hidden 64) trained on all 730 public MLPs (full + mini, no holdout, 3 fixed epochs); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.729e-09, raw final-layer MSE 1.992e-08, all-layers MSE 8.611e-09, mean multiplier 0.23739831172902995, failed MLPs 0
- FLOPs per MLP: mean 5.2145e+11 (0.2371 x B), min 0.2369 x B, max 0.2414 x B
- Grader timing per MLP: kernel 85.3 s mean, predict wall 96.8 s mean / 106.8 s max, residual 0.331 s mean / 0.347 s max (cap 0.4 s)
- Smoke test: passed=True duration 48030.330378000144 ms, worker passes 6 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
