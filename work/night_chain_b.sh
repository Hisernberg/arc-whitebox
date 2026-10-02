#!/bin/bash
# candidate B: after the night chain's READY, train 2 more members (hidden 96) on the full split, 5-member ensemble eval,
# build work/sub11_B = V32 (lone L2, leaf $(cat work/B_LEAF)) + 5-member ensemble; no submit (final_submit.sh picks it up)
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
until grep -q "READY" work/runs/night_chain.log; do sleep 60; done
source work/lean_env.sh
for sd in 4 5; do
  OMP_NUM_THREADS=2 python work/gru_corr.py --full --hold-mini --hidden 96 --epochs 10 --inner 4 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_full96_s$sd.npz > work/runs/gru_full96_s$sd.log 2>&1
  echo "$(date -u +%H:%M) seed $sd (h96): $(grep BEST work/runs/gru_full96_s$sd.log)"
done
# 5-member ensemble evaluation (members may differ in hidden size: evaluate per model via --eval with matching --hidden)
OMP_NUM_THREADS=2 python work/gru_corr.py --full --hold-mini --hidden 96 --act cdf --eval work/gru_full96_s4.npz,work/gru_full96_s5.npz > work/runs/gru_full96_ens.log 2>&1
echo "$(date -u +%H:%M) h96 pair: $(grep 'ENSEMBLE holdout' work/runs/gru_full96_ens.log)"
uv run --project $SK python work/export_gru.py work/gru_full_s1.npz work/gru_full_s2.npz work/gru_full_s3.npz work/gru_full96_s4.npz work/gru_full96_s5.npz work/gru_full_ens5.json
leaf=$(cat work/B_LEAF)
work/build_v32.sh work/gru_full_ens5.json work/sub11_B 2 $leaf
echo "V32 final B: V29 (504aldo MIT) + Strassen-priced lone join products (level 2, leaf $leaf) + 5-member GRU corrector ensemble (3 x hidden 64 + 2 x hidden 96) trained on the full public split, mini split held out; model embedded" > work/sub11_B/DESCRIPTION
echo "$(date -u +%H:%M) B BUILT"
