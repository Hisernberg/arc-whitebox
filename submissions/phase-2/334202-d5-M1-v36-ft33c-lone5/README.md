# Submission #334202 — d5-M1-v36-ft33c-lone5

| Field | Value |
|---|---|
| Submission ID | 334202 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334202> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T11:57:40Z |
| Adjusted score (leaderboard) | 4.2216534466011745e-09 |
| Raw final-layer MSE | 1.9984850787579945e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V36: dead-ReLU pruning, shared Strassen scratch, lean Strassen helper, lone join products at Strassen level 5 + GRU corrector fine-tuned on V34 features

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.222e-09, raw final-layer MSE 1.998e-08, all-layers MSE 8.692e-09, mean multiplier 0.21129713911981526, failed MLPs 0
- FLOPs per MLP: mean 4.6305e+11 (0.2106 x B), min 0.2075 x B, max 0.2191 x B
- Grader timing per MLP: kernel 95.5 s mean, predict wall 105.3 s mean / 113.5 s max, residual 0.276 s mean / 0.375 s max (cap 0.4 s)
- Smoke test: passed=True duration 46547.82080700005 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
