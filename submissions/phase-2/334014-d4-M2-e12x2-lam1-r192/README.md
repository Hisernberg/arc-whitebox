# Submission #334014 — d4-M2-e12x2-lam1-r192

| Field | Value |
|---|---|
| Submission ID | 334014 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334014> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T16:54:01Z |
| Adjusted score (leaderboard) | 4.700854808540081e-09 |
| Raw final-layer MSE | 2.015251805431717e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

As d4-N1 plus lambda scale 1.00 and nested-tier rank 224 -> 192 (both grader-verified on plain V29)

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.701e-09, raw final-layer MSE 2.015e-08, all-layers MSE 8.642e-09, mean multiplier 0.23329682844114358, failed MLPs 0
- FLOPs per MLP: mean 5.1253e+11 (0.2331 x B), min 0.2328 x B, max 0.2373 x B
- Grader timing per MLP: kernel 82.5 s mean, predict wall 93.6 s mean / 107.0 s max, residual 0.316 s mean / 0.343 s max (cap 0.4 s)
- Smoke test: passed=True duration 45352.39967100006 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
