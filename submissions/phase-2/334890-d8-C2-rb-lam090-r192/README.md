# Submission #334890 — d8-C2-rb-lam090-r192

| Field | Value |
|---|---|
| Submission ID | 334890 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334890> |
| Status | GRADED |
| Created (UTC) | 2026-10-08T22:01:23Z |
| Adjusted score (leaderboard) | 4.065911120200755e-09 |
| Raw final-layer MSE | 1.989828767534618e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track C nominee: robust V42 + warm-up 2 with LAM_SCALE 0.90 and R_OLD2 192; predicted ~4.02e-09, wall max ~105 s

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.066e-09, raw final-layer MSE 1.99e-08, all-layers MSE 8.82e-09, mean multiplier 0.20439464829978532, failed MLPs 0
- FLOPs per MLP: mean 4.4770e+11 (0.2036 x B), min 0.2003 x B, max 0.2136 x B
- Grader timing per MLP: kernel 92.5 s mean, predict wall 102.6 s mean / 108.2 s max, residual 0.285 s mean / 0.349 s max (cap 0.4 s)
- Smoke test: passed=True duration 45762.68584900004 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
