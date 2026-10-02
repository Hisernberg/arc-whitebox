# Submission #333323 — Graded Phase 2 submission (MSE = 5.418e-09)

| Field | Value |
|-------|-------|
| **Submission ID** | 333323 |
| **AICrowd URL** | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333323> |
| **Status** | ✅ GRADED |
| **Round** | Phase 2 (round id 1429) |
| **Created at (UTC)** | 2026-10-01T10:30:13Z |
| **Primary score (MSE)** | 5.4182e-09 |
| **Secondary score** | 2.1326515771136202e-08 |
| **Participant** | koushik_rudra (id 518412) |
| **Country** | Bangladesh |
| **Team** | (solo — no team) |
| **Grading message** | <p>Graded successfully</p> |

## Description provided at submission time

> K3 cumulant propagation V29 (504aldo MIT baseline)

## Grading summary

- **Smoke test**: PASSED (duration 21841.016397000003 ms; worker passes 5/0 failures)
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
  - Average FLOPs used per MLP: 5.5717e+11
  - Average participant predict wall time per MLP: 67.83 s
- **Session ID**: sess-041173e57ff3
- **Started at**: 2026-10-01T10:32:24Z
- **Updated at**: 2026-10-01T10:56:02Z
- **Completed at**: 2026-10-01T10:56:02Z

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
