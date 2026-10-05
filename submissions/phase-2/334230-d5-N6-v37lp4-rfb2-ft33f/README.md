# Submission #334230 — d5-N6-v37lp4-rfb2-ft33f

| Field | Value |
|---|---|
| Submission ID | 334230 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334230> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T14:55:50Z |
| Adjusted score (leaderboard) | 0.01508895803610041 |
| Raw final-layer MSE | 0.015088973919791505 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V37 + join products at Strassen level 4 after the first 5 MLPs + D21 feedback rank 2 + GRU ft33f; ships 504aldo's MIT notice (attribution)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 0.01509, raw final-layer MSE 0.01509, all-layers MSE 0.01324, mean multiplier 0.21980796966378877, failed MLPs 1
- FLOPs per MLP: mean 4.4619e+11 (0.2029 x B), min 0.1983 x B, max 0.2135 x B
- Grader timing per MLP: kernel 95.1 s mean, predict wall 105.8 s mean / 119.5 s max, residual 0.304 s mean / 0.395 s max (cap 0.4 s)
- Smoke test: passed=True duration 50640.159315000004 ms, worker passes 10 / failures 0
- MLPs completed: 99 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
