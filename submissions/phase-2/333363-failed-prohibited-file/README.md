# Submission #333363 — FAILED Phase 2 submission (Prohibited file in submission)

| Field | Value |
|-------|-------|
| **Submission ID** | 333363 |
| **AICrowd URL** | <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions/333363> |
| **Status** | ❌ FAILED |
| **Round** | Phase 2 (round id 1429) |
| **Created at (UTC)** | 2026-10-01T15:56:44Z |
| **Primary score (MSE)** | — |
| **Secondary score** | — |
| **Participant** | koushik_rudra (id 518412) |
| **Country** | Bangladesh |
| **Team** | (solo — no team) |
| **Grading message** | <p>Error : Prohibited file in submission</p> |

## Description provided at submission time

> V29 baseline (504aldo, MIT) + kappa4 lambda table scale 0.95->1.00 (re-validated on 4 public mini-split MLPs, mean raw -0.35%)

## Grading summary

- **Smoke test**: FAILED (duration — ms; worker passes —/— failures)
- **Config snapshot**:
  - n_mlps = 100
  - depth = 16
  - width = 1024
  - flop_budget = 2199023255552.0 FLOPs/MLP
- **Progress**:
  - Total MLPs: 100
  - Completed:  0
  - In flight:  0
  - Failed:     100
  - % complete: 100.0
- **Per-MLP outcomes** (from results.per_mlp):
  - Completed: 0
  - Failed/other: 0
  - Average FLOPs used per MLP: —
  - Average participant predict wall time per MLP: —
- **Session ID**: sess-a8046bb5cebb
- **Started at**: 2026-10-01T15:57:06Z
- **Updated at**: 2026-10-01T15:57:06Z
- **Completed at**: 2026-10-01T15:57:06Z

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
