# Submission #333530 — v31-gru-ens3-mini

| Field | Value |
|---|---|
| Submission ID | 333530 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333530> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T11:44:34Z |
| Adjusted score (leaderboard) | 5.198689667342865e-09 |
| Raw final-layer MSE | 2.034363014047358e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V31: V29 + 3-member per-layer GRU corrector ensemble (normal-CDF gates, hidden 48, early-stopped on the held-out set) trained on 80 mini-split MLPs with 20 held out (held-out final-layer MSE ratio 0.9550 vs V29); model embedded as a JSON literal; suite-shape gate + setup dry run.

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 5.199e-09, raw final-layer MSE 2.034e-08, all-layers MSE 8.636e-09, mean multiplier 0.2556530380544245, failed MLPs 0
- FLOPs per MLP: mean 5.6044e+11 (0.2549 x B), min 0.2541 x B, max 0.2686 x B
- Grader timing per MLP: kernel 62.2 s mean, predict wall 69.2 s mean / 72.1 s max, residual 0.203 s mean / 0.206 s max (cap 0.4 s)
- Smoke test: passed=True duration 21239.684349000072 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
