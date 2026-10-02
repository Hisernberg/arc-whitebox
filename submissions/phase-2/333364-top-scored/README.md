# Submission #333364 — Top-scored Phase 2 submission (MSE = 5.394e-09)

| Field | Value |
|-------|-------|
| **Submission ID** | 333364 |
| **AICrowd URL** | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333364> |
| **Status** | ✅ GRADED |
| **Round** | Phase 2 (round id 1429) |
| **Created at (UTC)** | 2026-10-01T16:00:54Z |
| **Primary score (MSE)** | 5.3936e-09 |
| **Secondary score** | 2.1583858149654133e-08 |
| **Participant** | koushik_rudra (id 518412) |
| **Country** | Bangladesh |
| **Team** | (solo — no team) |
| **Grading message** | <p>Graded successfully</p> |

## Description provided at submission time

> V29 baseline (504aldo, MIT) + kappa4 lambda table scale 0.95->1.00 (mean raw -0.35% on 4 public mini-split MLPs)

## Grading summary

- **Smoke test**: PASSED (duration 21966.65827999999 ms; worker passes 5/0 failures)
- **Config snapshot**:
  - n_mlps = 100
  - depth = 16
  - width = 1024
  - flop_budget = 2199023255552.0 FLOPs/MLP
- **Progress**:
  - Total MLPs: 100
  - Completed:  100
  - In flight:  0
  - Failed:     0
  - % complete: 100.0
- **Per-MLP outcomes** (from results.per_mlp):
  - Completed: 100
  - Failed/other: 0
  - Average FLOPs used per MLP: 5.4796e+11
  - Average participant predict wall time per MLP: 68.34 s
- **Session ID**: sess-47dfe7c7d9ee
- **Started at**: 2026-10-01T16:01:11Z
- **Updated at**: 2026-10-01T16:25:10Z
- **Completed at**: 2026-10-01T16:25:10Z

## Files in this folder

- `submission-report.json` — the full grading evaluation JSON (the same file
  the AICrowd "Download report.json" button produces).
- `submission-metadata.json` — submission record from the Rails API and GraphQL
  (id, status, score, round, challenge, participant, grading message).

## Where is the source code?

The estimator source code is **not** included in this repository. AIcrowd
submissions for this challenge are git-based: the source is pushed to
`gitlab.aicrowd.com` as a git tag (e.g. `submission-<description>`) via the
`aicrowd` CLI, and AIcrowd's public APIs do not expose the source. The
participant owns and can retrieve the source via their own git credentials.
