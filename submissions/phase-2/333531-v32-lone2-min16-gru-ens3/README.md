# Submission #333531 — v32-lone2-min16-gru-ens3

| Field | Value |
|---|---|
| Submission ID | 333531 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333531> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T11:48:27Z |
| Adjusted score (leaderboard) | 4.912983576601519e-09 |
| Raw final-layer MSE | 2.0339595643292796e-08 |
| Participant | nabid_nur |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V32: V29 + Strassen pricing of the join's lone dense products (level cap 2, smallest leaf 16; local steady cost vs V29 see work/runs/cost_v32_*) + the 3-member per-layer GRU corrector ensemble of the V31 submission (normal-CDF gates, hidden 48, trained on 80 mini MLPs, 20 held out); model embedded as a JSON literal.

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.913e-09, raw final-layer MSE 2.034e-08, all-layers MSE 8.637e-09, mean multiplier 0.24166138296814096, failed MLPs 0
- FLOPs per MLP: mean 5.2955e+11 (0.2408 x B), min 0.2400 x B, max 0.2556 x B
- Grader timing per MLP: kernel 73.4 s mean, predict wall 84.4 s mean / 92.5 s max, residual 0.312 s mean / 0.343 s max (cap 0.4 s)
- Smoke test: passed=True duration 29098.87771299873 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
