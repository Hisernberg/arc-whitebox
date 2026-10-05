# Submission #334040 — d4-N7-pair18-21f-leaf16

| Field | Value |
|---|---|
| Submission ID | 334040 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334040> |
| Status | GRADED |
| Created (UTC) | 2026-10-04T20:07:09Z |
| Adjusted score (leaderboard) | 4.731701734760877e-09 |
| Raw final-layer MSE | 1.968749355540922e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

SAFE nomination candidate: the 334034 pair (12-epoch s18 + final-weight-8 s21, held-out 0.9180) at Strassen leaf 16 (wall ~92 s vs ~111 s at leaf 8 under load); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.732e-09, raw final-layer MSE 1.969e-08, all-layers MSE 8.596e-09, mean multiplier 0.2403745732396601, failed MLPs 0
- FLOPs per MLP: mean 5.2811e+11 (0.2402 x B), min 0.2399 x B, max 0.2443 x B
- Grader timing per MLP: kernel 73.4 s mean, predict wall 84.1 s mean / 90.9 s max, residual 0.304 s mean / 0.312 s max (cap 0.4 s)
- Smoke test: passed=True duration 29123.89107600029 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
