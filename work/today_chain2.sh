#!/bin/bash
# S2: after S1 is submitted, train 2 hidden-96 members on the (larger) full-split dumps, 5-member ensemble with S1's
# three, V32 (lone L2, leaf 16) build -> submit -> watch
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
until grep -q "S1 DONE" work/runs/today_chain.log; do sleep 60; done
source work/lean_env.sh
echo "$(date -u +%H:%M) S2 training on $(ls work/feats/featf_*.npz | wc -l) full-split MLPs"
for sd in 4 5; do
  OMP_NUM_THREADS=3 python work/gru_corr.py --full --hold-mini --hidden 96 --epochs 6 --inner 2 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_full96_s$sd.npz > work/runs/gru_full96_s$sd.log 2>&1
  echo "$(date -u +%H:%M) seed $sd (h96): $(grep BEST work/runs/gru_full96_s$sd.log)"
done
OMP_NUM_THREADS=3 python work/gru_corr.py --full --hold-mini --act cdf --eval work/gru_full_s1.npz,work/gru_full_s2.npz,work/gru_full_s3.npz,work/gru_full96_s4.npz,work/gru_full96_s5.npz > work/runs/gru_full_ens5.log 2>&1
ratio=$(grep "ENSEMBLE holdout" work/runs/gru_full_ens5.log | sed -n 's/.*mean ratio \([0-9.]*\).*/\1/p')
echo "$(date -u +%H:%M) S2 5-member ensemble holdout (100 mini) ratio: $ratio"
uv run --project $SK python work/export_gru.py work/gru_full_s1.npz work/gru_full_s2.npz work/gru_full_s3.npz work/gru_full96_s4.npz work/gru_full96_s5.npz work/gru_full_ens5.json
n=$(ls work/feats/featf_*.npz | wc -l)
work/build_v32.sh work/gru_full_ens5.json work/sub13_S2 2 16 submit "V32-S2: V29 (504aldo MIT) + Strassen-priced lone join products (level 2, leaf 16) + 5-member per-layer GRU corrector ensemble (CDF gates; 3 x hidden 64 + 2 x hidden 96) trained on up to $n full-split MLPs with all 100 mini MLPs held out (held-out final-layer MSE ratio $ratio vs V29); model embedded"
echo "$(date -u +%H:%M) S2 DONE"
