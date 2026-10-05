# Submission #333566 — sub16_A2S1_leaf8-v32

| Field | Value |
|---|---|
| Submission ID | 333566 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333566> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T15:25:53Z |
| Adjusted score (leaderboard) | 4.734321605788398e-09 |
| Raw final-layer MSE | 1.9830417663513343e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Acct2 V32-S1 leaf-8: V29 (504aldo MIT) + Strassen-priced lone join products (level 2, leaf 8) + 3-member GRU corrector ensemble (CDF, hidden 64) trained on full-split MLPs, 100 mini held out (ratio 0.9252); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.734e-09, raw final-layer MSE 1.983e-08, all-layers MSE 8.606e-09, mean multiplier 0.23890564169776554, failed MLPs 0
- FLOPs per MLP: mean 5.2310e+11 (0.2379 x B), min 0.2369 x B, max 0.2530 x B
- Grader timing per MLP: kernel 83.8 s mean, predict wall 95.3 s mean / 101.3 s max, residual 0.328 s mean / 0.344 s max (cap 0.4 s)
- Smoke test: passed=True duration 28924.416683999993 ms, worker passes 6 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
