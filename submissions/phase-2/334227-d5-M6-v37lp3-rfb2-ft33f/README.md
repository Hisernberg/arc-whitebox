# Submission #334227 — d5-M6-v37lp3-rfb2-ft33f

| Field | Value |
|---|---|
| Submission ID | 334227 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334227> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T14:36:09Z |
| Adjusted score (leaderboard) | 4.145165043180927e-09 |
| Raw final-layer MSE | 2.0363801915834756e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 + join products at Strassen level 3 after the first 5 MLPs + D21 feedback rank 2 + GRU ft33f (same build as nabid_nur 334221)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.145e-09, raw final-layer MSE 2.036e-08, all-layers MSE 8.79e-09, mean multiplier 0.20367018687338714, failed MLPs 0
- FLOPs per MLP: mean 4.4531e+11 (0.2025 x B), min 0.1989 x B, max 0.2135 x B
- Grader timing per MLP: kernel 96.3 s mean, predict wall 106.9 s mean / 117.7 s max, residual 0.302 s mean / 0.377 s max (cap 0.4 s)
- Smoke test: passed=True duration 46016.900026006624 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
