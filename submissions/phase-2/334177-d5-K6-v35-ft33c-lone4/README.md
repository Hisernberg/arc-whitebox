# Submission #334177 — d5-K6-v35-ft33c-lone4

| Field | Value |
|---|---|
| Submission ID | 334177 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334177> |
| Status | GRADED |
| Created (UTC) | 2026-10-05T08:46:46Z |
| Adjusted score (leaderboard) | 4.25454269580438e-09 |
| Raw final-layer MSE | 2.0007478660488686e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

V35 (V34 + leaner Strassen helper: cached buffer/slot views) + GRU fine-tuned on 418 V34 dumps + join lone products at Strassen level 4

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.255e-09, raw final-layer MSE 2.001e-08, all-layers MSE 8.694e-09, mean multiplier 0.21269941578069848, failed MLPs 0
- FLOPs per MLP: mean 4.6614e+11 (0.2120 x B), min 0.2089 x B, max 0.2205 x B
- Grader timing per MLP: kernel 89.2 s mean, predict wall 99.5 s mean / 106.1 s max, residual 0.295 s mean / 0.363 s max (cap 0.4 s)
- Smoke test: passed=True duration 47761.578494002606 ms, worker passes 5 / failures 0
- MLPs completed: 100 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
