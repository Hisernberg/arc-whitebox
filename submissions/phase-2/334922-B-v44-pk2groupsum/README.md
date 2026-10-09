# Submission #334922 — B-v44-pk2groupsum

| Field | Value |
|---|---|
| Submission ID | 334922 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334922> |
| Status | GRADED |
| Created (UTC) | 2026-10-09T00:59:07Z |
| Adjusted score (leaderboard) | 3.995942402774597e-09 |
| Raw final-layer MSE | 1.9649280602607177e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track B: V44 PK2 einsum -> in-place mul + contiguous group sums (sub121 lineage). local raw same, C/B -0.67%, wall -14%. pred ~3.996e-09

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 3.996e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.20343583125541045, failed MLPs 0
- FLOPs per MLP: mean 4.4550e+11 (0.2026 x B), min 0.1993 x B, max 0.2133 x B
- Grader timing per MLP: kernel 93.8 s mean, predict wall 104.5 s mean / 111.4 s max, residual 0.303 s mean / 0.367 s max (cap 0.4 s)
- Smoke test: passed=True duration 45297.58351300006 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
