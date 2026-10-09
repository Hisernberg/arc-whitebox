# Submission #334929 — C-lam090

| Field | Value |
|---|---|
| Submission ID | 334929 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334929> |
| Status | GRADED |
| Created (UTC) | 2026-10-09T02:16:23Z |
| Adjusted score (leaderboard) | 4.043493473777762e-09 |
| Raw final-layer MSE | 1.974912471780499e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Track C: sub121 (L5+LP4+warm-up 2) with LAM_SCALE 0.90 alone (8-MLP paired: raw -0.6%, 6/8 MLPs better; R_OLD2 192 rejected +0.8% raw). pred ~4.00e-09

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.043e-09, raw final-layer MSE 1.975e-08, all-layers MSE 8.791e-09, mean multiplier 0.20481575964142393, failed MLPs 0
- FLOPs per MLP: mean 4.4854e+11 (0.2040 x B), min 0.2007 x B, max 0.2147 x B
- Grader timing per MLP: kernel 100.7 s mean, predict wall 111.7 s mean / 119.5 s max, residual 0.309 s mean / 0.369 s max (cap 0.4 s)
- Smoke test: passed=True duration 45311.64114799958 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
