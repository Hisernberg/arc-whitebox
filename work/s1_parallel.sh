#!/bin/bash
# S1 members in parallel (detached), then the finisher: ensemble eval -> export -> V32 build -> submit -> watcher -> "S1 DONE"
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
source work/lean_env.sh
echo "$(date -u +%H:%M) S1 training (parallel) on $(ls work/feats/featf_*.npz | wc -l) full-split MLPs" >> work/runs/today_chain.log
for sd in 1 2 3; do
  OMP_NUM_THREADS=1 setsid nohup python work/gru_corr.py --full --hold-mini --hidden 64 --epochs 6 --inner 2 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_full_s$sd.npz > work/runs/gru_full_s$sd.log 2>&1 &
done
wait
for sd in 1 2 3; do echo "$(date -u +%H:%M) seed $sd: $(grep BEST work/runs/gru_full_s$sd.log)" >> work/runs/today_chain.log; done
OMP_NUM_THREADS=3 python work/gru_corr.py --full --hold-mini --hidden 64 --act cdf --eval work/gru_full_s1.npz,work/gru_full_s2.npz,work/gru_full_s3.npz > work/runs/gru_full_ens.log 2>&1
ratio=$(grep "ENSEMBLE holdout" work/runs/gru_full_ens.log | sed -n 's/.*mean ratio \([0-9.]*\).*/\1/p')
echo "$(date -u +%H:%M) S1 ensemble holdout (100 mini) ratio: $ratio" >> work/runs/today_chain.log
uv run --project $SK python work/export_gru.py work/gru_full_s1.npz work/gru_full_s2.npz work/gru_full_s3.npz work/gru_full_ens.json
n=$(ls work/feats/featf_*.npz | wc -l)
work/build_v32.sh work/gru_full_ens.json work/sub12_S1 2 16 submit "V32-S1: V29 (504aldo MIT) + Strassen-priced lone join products (level 2, leaf 16) + 3-member per-layer GRU corrector ensemble (CDF gates, hidden 64) trained on $n full-split MLPs with all 100 mini MLPs held out (held-out final-layer MSE ratio $ratio vs V29); model embedded" >> work/runs/today_chain.log 2>&1
echo "$(date -u +%H:%M) S1 DONE" >> work/runs/today_chain.log
