#!/bin/bash
# ensemble members 2 and 3 (same holdout split as the day chain's seed-1 model), trained after the day chain's model exists
cd /home/user/arc-whitebox
until [ -f work/gru_mini100.npz ]; do sleep 60; done
source work/lean_env.sh
for sd in 2 3; do
  OMP_NUM_THREADS=2 python work/gru_corr.py --hidden 64 --epochs 150 --holdout 20 --seed $sd --split-seed 1 --act cdf --out work/gru_mini100_s$sd.npz > work/runs/gru_mini100_s$sd.log 2>&1
  echo "$(date -u +%H:%M) seed $sd done: $(grep 'ep 149' work/runs/gru_mini100_s$sd.log)"
done
