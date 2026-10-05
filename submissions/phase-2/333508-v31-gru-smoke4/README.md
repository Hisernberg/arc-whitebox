# Submission #333508 — v31-gru-smoke4

| Field | Value |
|---|---|
| Submission ID | 333508 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333508> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T09:26:14Z |
| Adjusted score (leaderboard) | 5.311332090550101e-09 |
| Raw final-layer MSE | 2.087158179620019e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V31 pipeline test 4: tanh-GRU corrector gated to the 1024x16 suite shape, setup-time dry run of the step at n=8, model embedded as a JSON literal.

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 5.311e-09, raw final-layer MSE 2.087e-08, all-layers MSE 8.669e-09, mean multiplier 0.25458955475287437, failed MLPs 0
- FLOPs per MLP: mean 5.5810e+11 (0.2538 x B), min 0.2530 x B, max 0.2675 x B
- Grader timing per MLP: kernel 63.0 s mean, predict wall 69.7 s mean / 78.4 s max, residual 0.192 s mean / 0.206 s max (cap 0.4 s)
- Smoke test: passed=True duration 21754.04890200025 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
