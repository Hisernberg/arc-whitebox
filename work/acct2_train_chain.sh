#!/bin/bash
# second account, later variants (need CPU after S3's members finish):
#  V1: + 2 tanh-activation members (h64, 3 epochs, mini held out) -> 9-member mixed ensemble, leaf 16
#  V2: + 2 all-data members (full + mini, no holdout, 3 fixed epochs) -> 11-member ensemble, leaf 16
cd /home/user/arc-whitebox
export AICROWD_API_KEY=$(cat work/.aicrowd_key2)
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
source work/lean_env.sh
until grep -q "S3 DONE" work/runs/today_chain3.log; do sleep 60; done
M7="work/gru_full_s1.npz,work/gru_full_s2.npz,work/gru_full_s3.npz,work/gru_full96_s4.npz,work/gru_full96_s5.npz,work/gru_full128_s6.npz,work/gru_full128_s7.npz"
echo "$(date -u +%H:%M) V1 training (tanh members)"
for sd in 8 9; do
  OMP_NUM_THREADS=2 setsid nohup python work/gru_corr.py --full --hold-mini --hidden 64 --epochs 3 --inner 2 --seed $sd --act tanh --lr 5e-4 --wd 1e-5 --out work/gru_fulltanh_s$sd.npz > work/runs/gru_fulltanh_s$sd.log 2>&1 &
done
wait
M9="$M7,work/gru_fulltanh_s8.npz,work/gru_fulltanh_s9.npz"
OMP_NUM_THREADS=4 python work/gru_corr.py --full --hold-mini --act cdf --eval $M9 > work/runs/gru_full_ens9.log 2>&1
r9=$(grep "ENSEMBLE holdout" work/runs/gru_full_ens9.log | sed -n 's/.*mean ratio \([0-9.]*\).*/\1/p')
echo "$(date -u +%H:%M) 9-member mixed ensemble holdout ratio: $r9"
uv run --project $SK python work/export_gru.py $(echo $M9 | tr ',' ' ') work/gru_full_ens9.json
work/build_v32.sh work/gru_full_ens9.json work/sub20_A2_mix9 2 16 submit "Acct2 V32 mixed-9: lone level 2, leaf 16 + 9-member GRU corrector ensemble (7 CDF-gated members of S3 + 2 tanh-gated members), full split, 100 mini held out (ratio $r9); model embedded"
echo "$(date -u +%H:%M) V2 training (all-data members)"
for sd in 10 11; do
  OMP_NUM_THREADS=2 setsid nohup python work/gru_corr.py --full --holdout 0 --hidden 64 --epochs 3 --inner 2 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_all_s$sd.npz > work/runs/gru_all_s$sd.log 2>&1 &
done
wait
M11="$M9,work/gru_all_s10.npz,work/gru_all_s11.npz"
uv run --project $SK python work/export_gru.py $(echo $M11 | tr ',' ' ') work/gru_full_ens11.json
work/build_v32.sh work/gru_full_ens11.json work/sub21_A2_all11 2 16 submit "Acct2 V32 all-data-11: lone level 2, leaf 16 + 11-member GRU corrector ensemble (the mixed 9 + 2 members trained on all 710 public MLPs without holdout, 3 epochs); model embedded"
echo "$(date -u +%H:%M) ACCT2 TRAIN CHAIN DONE"
