# Submission #334630 — d7-V42rb-a1

| Field | Value |
|---|---|
| Submission ID | 334630 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334630> |
| Status | GRADED |
| Created (UTC) | 2026-10-07T12:05:57Z |
| Adjusted score (leaderboard) | 4.0734120487940204e-09 |
| Raw final-layer MSE | 1.965303834339238e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V42 LT cross-neuron corrector

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.073e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.20736139434338838, failed MLPs 0
- FLOPs per MLP: mean 4.5394e+11 (0.2064 x B), min 0.2027 x B, max 0.2161 x B
- Grader timing per MLP: kernel 89.6 s mean, predict wall 99.4 s mean / 110.6 s max, residual 0.278 s mean / 0.338 s max (cap 0.4 s)
- Smoke test: passed=True duration 45877.061945000154 ms, worker passes 7 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
