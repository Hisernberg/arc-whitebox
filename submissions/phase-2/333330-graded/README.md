# Submission #333330 — Graded Phase 2 submission (MSE = 5.406e-09)

| Field | Value |
|-------|-------|
| **Submission ID** | 333330 |
| **AICrowd URL** | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333330> |
| **Status** | ✅ GRADED |
| **Round** | Phase 2 (round id 1429) |
| **Created at (UTC)** | 2026-10-01T11:11:03Z |
| **Primary score (MSE)** | 5.4062e-09 |
| **Secondary score** | 2.163471538807471e-08 |
| **Participant** | koushik_rudra (id 518412) |
| **Country** | Bangladesh |
| **Team** | (solo — no team) |
| **Grading message** | <p>Graded successfully</p> |

## Description provided at submission time

> V29 + R_OLD2 192 cost trim

## Grading summary

- **Smoke test**: PASSED (duration 21089.002077999794 ms; worker passes 5/0 failures)
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
  - Average participant predict wall time per MLP: 66.56 s
- **Session ID**: sess-890fa6fb051a
- **Started at**: 2026-10-01T11:11:21Z
- **Updated at**: 2026-10-01T11:34:29Z
- **Completed at**: 2026-10-01T11:34:29Z

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
