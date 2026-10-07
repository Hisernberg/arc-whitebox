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

### Submission accounts

Submissions go to all three accounts, 10 per account per UTC day (30 a day), following
[`DAILY_PLAN.md`](DAILY_PLAN.md):

| Account | Team | Best score so far |
|---------|------|-------------------|
| `nabid_nur` | Hydrion-Labs | **4.045e-09** (`#334629`, V42 LT + cross-neuron inputs); robust nominee 4.073e-09 (`#334630`) |
| `multi_agent` | — | **4.063e-09** (`#334570`, V41 LT corrector); robust nominee 4.092e-09 (`#334571`) |
| `koushik_rudra` (participant ID `518412`) | — | **4.045e-09** (`#334627`, V42 LT + cross-neuron inputs); robust nominee 4.073e-09 (`#334628`) |

- **Challenge**: ARC White-Box Estimation Challenge 2026 (`arc-white-box-estimation-challenge-2026`, challenge ID 1174)
- **Submissions**: 59 archived under `submissions/phase-2/`, all in **Phase 2** (round id 1429), Aug 22 – Oct 17, 2026
- **Score history (all accounts)**: 4.156e-09 (`#334215`, nabid_nur), 4.166e-09 (`#334213`, multi_agent), 4.182e-09 (`#334208`), 4.192e-09 (`#334198`/`#334204`/`#334205`), 4.225e-09 (`#334182`), 4.255e-09 (`#334177`), 4.304e-09 (`#334176`), 4.340e-09 (`#334168`), 4.381e-09 (`#334161`), 4.6544e-09 (`#334013`, multi_agent), 4.6582e-09 (`#334034`, nabid_nur), 5.3936e-09 (`#333364`)
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
