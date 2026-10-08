# Submission #334742 — d8-K1-v42lp4-e2

| Field | Value |
|---|---|
| Submission ID | 334742 |
| URL | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/334742> |
| Status | GRADED |
| Created (UTC) | 2026-10-08T00:22:19Z |
| Adjusted score (leaderboard) | 4.0230663367605875e-09 |
| Raw final-layer MSE | 1.9649280602607177e-08 |
| Participant | koushik_rudra |
| Grading message | <p>Graded successfully</p> |

## What was submitted

koushik_rudra: V42+LP4, warm-up 2 calls

## Grading summary (from the evaluation report)

- Public aggregate: adjusted 4.023e-09, raw final-layer MSE 1.965e-08, all-layers MSE 8.71e-09, mean multiplier 0.20481575964142393, failed MLPs 0
- FLOPs per MLP: mean 4.4888e+11 (0.2041 x B), min 0.2006 x B, max 0.2147 x B
- Grader timing per MLP: kernel 99.9 s mean, predict wall 110.5 s mean / 118.7 s max, residual 0.301 s mean / 0.368 s max (cap 0.4 s)
- Smoke test: passed=True duration 45539.25108000021 ms, worker passes 5 / failures 0
- MLPs completed: 98 / 100

## Files

- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).
- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment).
- `estimator.py` — the exact single-file estimator that was packaged and submitted.
