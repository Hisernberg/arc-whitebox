# Submission #334765 — d8-R3-rb-e2-a1

| Field | Value |
|---|---|
| Submission ID | 334765 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334765> |
| Status | GRADED |
| Created (UTC) | 2026-10-08T03:27:35Z |
| Adjusted score (leaderboard) | 4.062612229560225e-09 |
| Raw final-layer MSE | 1.9651116396346425e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

nabid_nur: robust V42 + warm-up 2 nominee

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.063e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.2068034414891008, failed MLPs 0
- FLOPs per MLP: mean 4.5325e+11 (0.2061 x B), min 0.2028 x B, max 0.2161 x B
- Grader timing per MLP: kernel 91.8 s mean, predict wall 101.7 s mean / 117.3 s max, residual 0.279 s mean / 0.357 s max (cap 0.4 s)
- Smoke test: passed=True duration 45837.11758900063 ms, worker passes 5 / failures 0
- MLPs completed: 99 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
