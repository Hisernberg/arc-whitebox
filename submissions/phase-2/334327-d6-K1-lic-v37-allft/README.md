# Submission #334327 — d6-K1-lic-v37-allft

| Field | Value |
|---|---|
| Submission ID | 334327 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334327> |
| Status | GRADED |
| Created (UTC) | 2026-10-06T00:23:04Z |
| Adjusted score (leaderboard) | 0.029950485621444426 |
| Raw final-layer MSE | 0.029950501112992783 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 + join level 3 + D21 feedback rank 2 + GRU fine-tuned on ~1000 MLPs; ships 504aldo's MIT notice

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 0.02995, raw final-layer MSE 0.02995, all-layers MSE 0.02568, mean multiplier 0.23585964561015316, failed MLPs 2
- FLOPs per MLP: mean 4.4580e+11 (0.2027 x B), min 0.1989 x B, max 0.2135 x B
- Grader timing per MLP: kernel 97.6 s mean, predict wall 108.2 s mean / 115.8 s max, residual 0.300 s mean / 0.384 s max (cap 0.4 s)
- Smoke test: passed=True duration 45920.57171599982 ms, worker passes 5 / failures 0
- MLPs completed: 98 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
