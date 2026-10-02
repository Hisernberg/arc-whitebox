# Submission #333578 — sub14_S3-v32

| Field | Value |
|---|---|
| Submission ID | 333578 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333578> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T16:34:13Z |
| Adjusted score (leaderboard) | 4.704996849926751e-09 |
| Raw final-layer MSE | 1.9829122308578918e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

S3: V32 with leaf 8 and first-call Strassen level 5 (both grader-verified on the second account) + the 3-member full-split GRU ensemble of S1 (held-out ratio 0.925). The 7-member ensemble evaluated at 0.9267, no better, so the lighter 3-member one was kept.

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.705e-09, raw final-layer MSE 1.983e-08, all-layers MSE 8.606e-09, mean multiplier 0.2373075121907277, failed MLPs 0
- FLOPs per MLP: mean 5.2135e+11 (0.2371 x B), min 0.2369 x B, max 0.2414 x B
- Grader timing per MLP: kernel 85.7 s mean, predict wall 97.4 s mean / 106.3 s max, residual 0.335 s mean / 0.349 s max (cap 0.4 s)
- Smoke test: passed=True duration 48160.923043000366 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
