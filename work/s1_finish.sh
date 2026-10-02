#!/bin/bash
# S1 finisher: once every member has completed 3 epochs (best checkpoint is saved on improvement), stop the trainers,
# evaluate the ensemble on the 100 held-out mini MLPs, export, build V32 (lone L2, leaf 16), submit, watch, mark S1 DONE
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
source work/lean_env.sh
until [ "$(grep -c '^ep   2' work/runs/gru_full_s1.log work/runs/gru_full_s2.log work/runs/gru_full_s3.log | awk -F: '{s+=$2} END {print s}')" -ge 3 ] || [ "$(ps -eo args | grep -c '[g]ru_corr.py --full --hold-mini --hidden 64')" -eq 0 ]; do sleep 30; done
pkill -f "[g]ru_corr.py --full --hold-mini --hidden 64"; sleep 3
for sd in 1 2 3; do echo "$(date -u +%H:%M) seed $sd: $(grep '^ep' work/runs/gru_full_s$sd.log | tail -n 1 | cut -c1-110)" >> work/runs/today_chain.log; done
OMP_NUM_THREADS=4 python work/gru_corr.py --full --hold-mini --act cdf --eval work/gru_full_s1.npz,work/gru_full_s2.npz,work/gru_full_s3.npz > work/runs/gru_full_ens.log 2>&1
ratio=$(grep "ENSEMBLE holdout" work/runs/gru_full_ens.log | sed -n 's/.*mean ratio \([0-9.]*\).*/\1/p')
echo "$(date -u +%H:%M) S1 ensemble holdout (100 mini) ratio: $ratio" >> work/runs/today_chain.log
uv run --project $SK python work/export_gru.py work/gru_full_s1.npz work/gru_full_s2.npz work/gru_full_s3.npz work/gru_full_ens.json
n=$(ls work/feats/featf_*.npz | wc -l)
work/build_v32.sh work/gru_full_ens.json work/sub12_S1 2 16 submit "V32-S1: V29 (504aldo MIT) + Strassen-priced lone join products (level 2, leaf 16) + 3-member per-layer GRU corrector ensemble (CDF gates, hidden 64, 3 epochs) trained on $n full-split MLPs with all 100 mini MLPs held out (held-out final-layer MSE ratio $ratio vs V29); model embedded" >> work/runs/today_chain.log 2>&1
echo "$(date -u +%H:%M) S1 DONE" >> work/runs/today_chain.log
