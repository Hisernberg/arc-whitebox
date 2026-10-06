# Submission #334265 — d5-N9-lic-v37-allft

| Field | Value |
|---|---|
| Submission ID | 334265 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334265> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T17:22:59Z |
| Adjusted score (leaderboard) | 4.132984594961251e-09 |
| Raw final-layer MSE | 2.030371831551747e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 + join level 3 + D21 feedback rank 2 + GRU fine-tuned on ~1000 MLPs (held-out 0.913); ships 504aldo's MIT notice

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.133e-09, raw final-layer MSE 2.03e-08, all-layers MSE 8.786e-09, mean multiplier 0.20367030366996913, failed MLPs 0
- FLOPs per MLP: mean 4.4531e+11 (0.2025 x B), min 0.1989 x B, max 0.2135 x B
- Grader timing per MLP: kernel 96.4 s mean, predict wall 107.1 s mean / 116.2 s max, residual 0.307 s mean / 0.389 s max (cap 0.4 s)
- Smoke test: passed=True duration 46523.32698600003 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
