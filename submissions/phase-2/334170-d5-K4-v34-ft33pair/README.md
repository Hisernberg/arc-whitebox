# Submission #334170 — d5-K4-v34-ft33pair

| Field | Value |
|---|---|
| Submission ID | 334170 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334170> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T07:36:35Z |
| Adjusted score (leaderboard) | 4.391804992388969e-09 |
| Raw final-layer MSE | 1.9995852227339128e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V34 + 2-member GRU fine-tuned on V34 features (s18 + final-weight-8 s21, held-out 0.9206)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.392e-09, raw final-layer MSE 2e-08, all-layers MSE 8.692e-09, mean multiplier 0.21967113648261147, failed MLPs 0
- FLOPs per MLP: mean 4.8086e+11 (0.2187 x B), min 0.2153 x B, max 0.2267 x B
- Grader timing per MLP: kernel 82.4 s mean, predict wall 93.3 s mean / 106.1 s max, residual 0.318 s mean / 0.339 s max (cap 0.4 s)
- Smoke test: passed=True duration 46188.21388400005 ms, worker passes 8 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
