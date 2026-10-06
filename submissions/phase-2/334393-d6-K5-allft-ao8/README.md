# Submission #334393 — d6-K5-allft-ao8

| Field | Value |
|---|---|
| Submission ID | 334393 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334393> |
| Status | GRADED |
| Created (UTC) | 2026-10-06T08:47:03Z |
| Adjusted score (leaderboard) | 4.132530454164948e-09 |
| Raw final-layer MSE | 2.012281004937222e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 lone L5 + join L3 + D21 rank 2 + AGE_OLD2=8 + GRU all-data ft; ships 504aldo's MIT notice

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.133e-09, raw final-layer MSE 2.012e-08, all-layers MSE 8.739e-09, mean multiplier 0.205466837717031, failed MLPs 0
- FLOPs per MLP: mean 4.4943e+11 (0.2044 x B), min 0.2008 x B, max 0.2143 x B
- Grader timing per MLP: kernel 96.9 s mean, predict wall 107.3 s mean / 118.5 s max, residual 0.294 s mean / 0.355 s max (cap 0.4 s)
- Smoke test: passed=True duration 45742.68681899957 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
