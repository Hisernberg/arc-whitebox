# ARC White-Box Estimation Challenge 2026 (WhestBench)

> Official challenge page: <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026>

## What the challenge is

Organized by the **Alignment Research Center** in partnership with AIcrowd, the
ARC White-Box Estimation Challenge (WhestBench) is a contest in **compute-efficient
white-box mechanistic estimation**.

Given the weights of a randomly initialized **ReLU MLP**, build an **estimator**
(executable code) that predicts each neuron's **expected post-ReLU activation**
under standard-normal inputs, more accurately than running the network on a
comparable number of sampled inputs.

The eventual goal is white-box estimation for trained networks. WhestBench
starts with randomly initialized networks, a tractable setting in which to
develop the algorithmic toolkit that mechanistic estimation — and the safety
questions motivating it — will eventually need.

## Task

- **Input**: Weights of a random ReLU MLP + a fixed FLOP budget.
- **Output**: Per-neuron expected post-ReLU activation means for every hidden layer.
- **Metric**: Final-layer MSE against a high-budget Monte Carlo reference.
- **Reference compute**: ~3.36 × 10¹⁶ FLOPs/MLP.
- **Participant budget**: ~2.20 × 10¹² FLOPs/MLP (~15,000× compute gap).
- **Grader**: CPU-only, 1 core (2 vCPU) for participant code, 7-core `flopscope`
  backend, 8 GB RAM, no network, hard cap 120 s per MLP.
- **Daily limit**: 10 submissions per team per UTC day in Phase 2.
- **Final ranking**: Fresh private rerun of each team's up-to-two nominated
  submissions, per phase.

## Timeline

| Phase | Window (UTC) | Status |
|-------|--------------|--------|
| Warm-Up Round | 2026-05-28 → 2026-06-17 | completed |
| Phase 1       | 2026-06-18 → 2026-08-10 | completed |
| Phase 2       | 2026-08-22 → 2026-10-17 23:59 | **live** |

## Prize pool

$150,000 USD ARV — split into $50K (Phase 1) + $100K (Phase 2), with both
placement prizes and algorithmic-novelty prizes.

## Network shape (Phase 2)

- 16 layers, width 1024 (i.e. 16 × 1024 prediction matrix per MLP).
- 100 MLPs per grading run (50 public + 50 private).

## My approach (per submission descriptions)

All four graded Phase 2 submissions build on the **`504aldo, MIT` V29 public
baseline** — a published reference implementation in the WhestBench community —
and tune it with **kappa4 lambda-table scaling** at scale 0.95 → 1.00. Earlier
submissions explored `R_OLD2 192 cost trim` and `K3 cumulant propagation` variants
on the same baseline. Net effect over four submissions: ~1.85× MSE reduction
(9.95e-09 → 5.39e-09).

## Useful links

- Challenge page: <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026>
- My submissions: <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/submissions?q%5Bparticipant_name_equals%5D=koushik_rudra>
- My profile: <https://www.aicrowd.com/participants/koushik_rudra>
- Leaderboard: <https://www.aicrowd.com/challenges/arc-white-box-estimation-challenge-2026/leaderboards>
- Companion paper (Wilson Wu, Victor Lecomte, Michael Winer, George Robinson, Jacob Hilton, Paul Christiano): "Estimating the expected output of wide random MLPs more efficiently than sampling", arXiv:2605.05179
- WhestBench Explorer: linked from the challenge page
- flopscope (compute metering): <https://github.com/AIcrowd/flopscope>
