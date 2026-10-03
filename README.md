# arc-whitebox

A personal archive of my submissions to the **ARC White-Box Estimation Challenge 2026**
(also known as **WhestBench 2026**), organized by AICrowd for the Alignment Research Center.

## Repository contents

| Path | Description |
|------|-------------|
| `challenge-info.md`        | What the challenge is, rules, scoring, and timeline. |
| `submissions/`             | All my submissions to this challenge, one folder per submission. |
| `submissions/README.md`    | How the per-submission folders are organized. |

## My participation at a glance

- **AICrowd username**: `koushik_rudra` (participant ID `518412`)
- **Country**: Bangladesh
- **Solo participant** (no team)
- **Challenge**: ARC White-Box Estimation Challenge 2026 (`arc-white-box-estimation-challenge-2026`, challenge ID 1174)
- **Submissions**: 6 in total — all in **Phase 2** (round id 1429), Aug 22 – Oct 17, 2026
- **Best score**: **MSE = 4.6890e-09** on submission `#333790` (graded 2026-10-03 16:35 UTC, `nabid_nur` account, team Hydrion-Labs): V32 with Strassen leaf 8 and first-call level 5 + a 3-member GRU corrector ensemble trained for 8 epochs on 630 full-split MLPs (raw −7.4% vs V29, cost −6.4%); previous bests 4.7050e-09 (`#333578`), 4.8035e-09 (`#333564`), 4.9130e-09 (`#333531`), 5.1987e-09 (`#333530`), 5.3113e-09 (`#333508`), 5.3936e-09 (`#333364`, koushik_rudra account)
- **Iteration trajectory** (graded submissions only, oldest → newest):
  - `#333177` (2026-09-30 17:22 UTC): MSE = 9.950e-09
  - `#333323` (2026-10-01 10:30 UTC): MSE = 5.418e-09
  - `#333330` (2026-10-01 11:11 UTC): MSE = 5.406e-09
  - `#333364` (2026-10-01 16:00 UTC): **MSE = 5.394e-09** ← best
  - `#333467` (2026-10-02 06:39 UTC, `nabid_nur` account): MSE = 5.418e-09 (V29 verbatim baseline; leaderboard rank 82 of 248 on 2026-10-02)

A ~1.85× improvement across four graded submissions in two days, all built on the
public `504aldo, MIT` V29 baseline with kappa4 lambda-table scaling.

## Important note about submission source code

The actual estimator source code for each submission lives on **AIcrowd's private
GitLab** (`gitlab.aicrowd.com`), pushed there as a git tag (`submission-*`) via the
`aicrowd` CLI. The source is **not** included in this repository, because:

1. AIcrowd does not expose submission source code through their public REST/GraphQL
   APIs (only the grading report and metadata).
2. Each participant has access to their own submission via their own git credentials,
   via `aicrowd challenge init` / `aicrowd submission create` workflows.

To retrieve the source for any submission listed here, clone your own copy of the
challenge starter kit and check out the corresponding `submission-<description>` git
tag, or use the AICrowd CLI's submission inspection commands.

This repository contains, for every submission:
- `submission-report.json` — the full grading evaluation JSON (this is exactly the
  file AICrowd's "Download report.json" button produces on the submission detail
  page; it includes per-MLP telemetry: FLOPs used, wall time, error codes, smoke
  test results, etc.).
- `submission-metadata.json` — submission ID, status, score, round, participant,
  description, grading message from AICrowd's Rails API.
- `README.md` — human-readable context for that submission.

See [`submissions/README.md`](submissions/README.md) for folder layout.
