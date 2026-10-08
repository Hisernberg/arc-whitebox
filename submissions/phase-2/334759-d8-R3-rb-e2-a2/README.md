# Submission #334759 — d8-R3-rb-e2-a2

| Field | Value |
|---|---|
| Submission ID | 334759 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334759> |
| Status | GRADED |
| Created (UTC) | 2026-10-08T02:36:29Z |
| Adjusted score (leaderboard) | 4.062670636230817e-09 |
| Raw final-layer MSE | 1.9651116396346425e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V42 robust (lone level 4) + warm-up on 2 calls/worker: nominee candidate; predicted ~4.06-4.065e-09, wall max ~105-110 s

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.063e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.20680613990880375, failed MLPs 0
- FLOPs per MLP: mean 4.5300e+11 (0.2060 x B), min 0.2027 x B, max 0.2161 x B
- Grader timing per MLP: kernel 89.1 s mean, predict wall 98.9 s mean / 105.9 s max, residual 0.276 s mean / 0.338 s max (cap 0.4 s)
- Smoke test: passed=True duration 45876.59895700017 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
