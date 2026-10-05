# Submission #334187 — d5-K8-v36-ft33e-lone4

| Field | Value |
|---|---|
| Submission ID | 334187 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334187> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T09:49:20Z |
| Adjusted score (leaderboard) | 4.284847790847807e-09 |
| Raw final-layer MSE | 2.0150334911761546e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V36 + GRU fine-tuned on 456 V34 dumps from e12 s17 (held-out 0.920) + join lone products at Strassen level 4

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.285e-09, raw final-layer MSE 2.015e-08, all-layers MSE 8.703e-09, mean multiplier 0.21269953257728047, failed MLPs 0
- FLOPs per MLP: mean 4.6614e+11 (0.2120 x B), min 0.2089 x B, max 0.2205 x B
- Grader timing per MLP: kernel 85.8 s mean, predict wall 94.7 s mean / 113.8 s max, residual 0.254 s mean / 0.344 s max (cap 0.4 s)
- Smoke test: passed=True duration 45624.824924999986 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
