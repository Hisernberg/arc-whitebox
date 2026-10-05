# Submission #334239 — d5-M7-lic-v37lp3-rfb2

| Field | Value |
|---|---|
| Submission ID | 334239 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334239> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T15:41:36Z |
| Adjusted score (leaderboard) | 4.145182060754311e-09 |
| Raw final-layer MSE | 2.0363801915834756e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 + join level 3 + D21 feedback rank 2 + GRU ft33f (the 334221 build); ships 504aldo's MIT notice (attribution)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.145e-09, raw final-layer MSE 2.036e-08, all-layers MSE 8.79e-09, mean multiplier 0.2036709482491642, failed MLPs 0
- FLOPs per MLP: mean 4.4532e+11 (0.2025 x B), min 0.1989 x B, max 0.2135 x B
- Grader timing per MLP: kernel 98.4 s mean, predict wall 109.3 s mean / 117.6 s max, residual 0.308 s mean / 0.386 s max (cap 0.4 s)
- Smoke test: passed=True duration 46057.115110997984 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
