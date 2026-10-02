# Submissions

One folder per submission, named `<submission-id>-<short-label>` to keep the
listing stable when statuses change.

| Folder | Submission ID | Status | MSE | Created (UTC) | Description |
|--------|---------------|--------|-----|---------------|-------------|
| `333467-graded/`               | 333467 | ✅ GRADED  | 5.418e-09    | 2026-10-02 06:39:28 | V29 verbatim (504aldo, MIT) re-submitted from the `nabid_nur` account as the Phase 2 baseline; raw 2.133e-08, 0.2534 x B, grader kernel 62.5 s, residual 0.183 s mean |
| `333364-top-scored/`           | 333364 | ✅ GRADED  | **5.394e-09** | 2026-10-01 16:00:54 | V29 baseline (504aldo, MIT) + kappa4 lambda table scale 0.95→1.00 (mean raw -0.35% on 4 public mini-split MLPs) |
| `333330-graded/`               | 333330 | ✅ GRADED  | 5.406e-09    | 2026-10-01 11:11:03 | V29 + R_OLD2 192 cost trim |
| `333323-graded/`               | 333323 | ✅ GRADED  | 5.418e-09    | 2026-10-01 10:30:13 | K3 cumulant propagation V29 (504aldo MIT baseline) |
| `333177-graded/`               | 333177 | ✅ GRADED  | 9.950e-09    | 2026-09-30 17:22:57 | (no description provided) |
| `333363-failed-prohibited-file/` | 333363 | ❌ FAILED | — | 2026-10-01 15:56:44 | V29 baseline (504aldo, MIT) + kappa4 lambda table scale 0.95→1.00 (re-validated). Failure: "Prohibited file in submission" |
| `333166-failed-eval-error/`    | 333166 | ❌ FAILED | — | 2026-09-30 16:29:17 | (no description provided). Failure: "Evaluation error" |

Account note: submissions up to #333364 were graded under the `koushik_rudra` participant;
#333467 onwards are graded under `nabid_nur` (the API key used from 2026-10-02). The grader is
deterministic, so an identical estimator gives an identical adjusted score on either account.

## Folder layout (per submission)

Each submission folder contains:

- `README.md` — human-readable context: what was submitted, what the score was,
  what the description said, what the grading report tells us.
- `submission-report.json` — the full grading evaluation JSON, exactly the file
  AICrowd's "Download report.json" button produces. Contains:
  - `schema_version`, `session_id`, `submission_id`, `state`, `phase`
  - `started_at`, `updated_at`, `completed_at`
  - `config_snapshot` — `n_mlps`, `depth`, `width`, `flop_budget`
  - `progress` — `total_mlps`, `mlps_completed`, `mlps_in_flight`, `mlps_failed`, `pct_complete`
  - `workers` — per-worker state
  - `smoke_test_result` — pass/fail, duration, worker_passes, errors
  - `results.per_mlp[]` — per-MLP telemetry: `mlp_index`, `mlp_name`, `state`,
    `telemetry.flops_used`, `telemetry.participant_predict_wall_s`,
    `telemetry.flopscope_server_kernel_wall_s`, `budget_exhausted`, `time_exhausted`,
    `error_code`, `error_message`, `traceback_index`
- `submission-metadata.json` — submission ID, status, score (primary + secondary),
  challenge ID, round ID, created_at, grading_message (from AICrowd Rails API),
  plus GraphQL-derived fields (participant, round, team, description).

The grading reports for the two FAILED submissions are much shorter — they
record the smoke-test failure that aborted the run before any MLPs were scored.
