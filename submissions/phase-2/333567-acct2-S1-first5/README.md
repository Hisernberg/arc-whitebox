# Submission #333567 — acct2-S1-first5

| Field | Value |
|---|---|
| Submission ID | 333567 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333567> |
| Status | GRADED |
| Created (UTC) | 2026-10-02T15:25:58Z |
| Adjusted score (leaderboard) | 4.779540708808576e-09 |
| Raw final-layer MSE | 1.9830208302096252e-08 |
| Participant | multi_agent |
| Grading message | <p>Graded successfully</p> |

## What was submitted

Acct2 V32-S1 first-call L5: as nabid_nur's S1 (lone level 2, leaf 16, 3-member full-split GRU ensemble, ratio 0.9252) but the first predict of each worker also runs Strassen level 5 (V28_STRASSEN_FIRST=5); model embedded

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.78e-09, raw final-layer MSE 1.983e-08, all-layers MSE 8.605e-09, mean multiplier 0.2410541309170185, failed MLPs 0
- FLOPs per MLP: mean 5.2960e+11 (0.2408 x B), min 0.2406 x B, max 0.2450 x B
- Grader timing per MLP: kernel 77.3 s mean, predict wall 88.5 s mean / 100.3 s max, residual 0.320 s mean / 0.342 s max (cap 0.4 s)
- Smoke test: passed=True duration 28984.368066005118 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
