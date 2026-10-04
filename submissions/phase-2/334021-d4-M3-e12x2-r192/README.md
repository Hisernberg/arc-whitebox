# Submission #334021 — d4-M3-e12x2-r192

| Field | Value |
|---|---|
| Submission ID | 334021 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334021> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T17:43:55Z |
| Adjusted score (leaderboard) | 4.6706770434082686e-09 |
| Raw final-layer MSE | 2.0023276761094168e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32 (lone L2, leaf 8, first-call L5, nested rank 192) + 2-member 12-epoch CDF GRU ensemble (held-out 0.9187); isolates the rank-192 cost trim

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.671e-09, raw final-layer MSE 2.002e-08, all-layers MSE 8.673e-09, mean multiplier 0.23329682844114358, failed MLPs 0
- FLOPs per MLP: mean 5.1253e+11 (0.2331 x B), min 0.2328 x B, max 0.2373 x B
- Grader timing per MLP: kernel 83.9 s mean, predict wall 95.1 s mean / 101.3 s max, residual 0.324 s mean / 0.334 s max (cap 0.4 s)
- Smoke test: passed=True duration 47622.22701900009 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
