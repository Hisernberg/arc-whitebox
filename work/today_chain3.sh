#!/bin/bash
# S3: after S2 is submitted, train 2 hidden-128 members (seeds 6, 7) on the full-split dumps (mini held out), 7-member
# ensemble with S2's five, V32 (lone L2, leaf $(cat work/S3_LEAF)) build -> submit -> watch
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
until grep -q "S2 DONE" work/runs/today_chain2.log; do sleep 60; done
source work/lean_env.sh
echo "$(date -u +%H:%M) S3 training on $(ls work/feats/featf_*.npz | wc -l) full-split MLPs"
for sd in 6 7; do
  OMP_NUM_THREADS=4 python work/gru_corr.py --full --hold-mini --hidden 128 --epochs 5 --inner 2 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_full128_s$sd.npz > work/runs/gru_full128_s$sd.log 2>&1
  echo "$(date -u +%H:%M) seed $sd (h128): $(grep BEST work/runs/gru_full128_s$sd.log)"
done
M="work/gru_full_s1.npz,work/gru_full_s2.npz,work/gru_full_s3.npz,work/gru_full96_s4.npz,work/gru_full96_s5.npz,work/gru_full128_s6.npz,work/gru_full128_s7.npz"
OMP_NUM_THREADS=4 python work/gru_corr.py --full --hold-mini --act cdf --eval $M > work/runs/gru_full_ens7.log 2>&1
ratio=$(grep "ENSEMBLE holdout" work/runs/gru_full_ens7.log | sed -n 's/.*mean ratio \([0-9.]*\).*/\1/p')
echo "$(date -u +%H:%M) S3 7-member ensemble holdout (100 mini) ratio: $ratio"
uv run --project $SK python work/export_gru.py $(echo $M | tr ',' ' ') work/gru_full_ens7.json
leaf=$(cat work/S3_LEAF); n=$(ls work/feats/featf_*.npz | wc -l)
work/build_v32.sh work/gru_full_ens7.json work/sub14_S3 2 $leaf submit "V32-S3: V29 (504aldo MIT) + Strassen-priced lone join products (level 2, leaf $leaf) + 7-member per-layer GRU corrector ensemble (CDF gates; 3 x h64 + 2 x h96 + 2 x h128) trained on up to $n full-split MLPs with all 100 mini MLPs held out (held-out final-layer MSE ratio $ratio vs V29); model embedded"
echo "$(date -u +%H:%M) S3 DONE"
