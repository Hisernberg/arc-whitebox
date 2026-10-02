#!/bin/bash
# second account, V3: the S1 recipe trained longer (8 epochs, 3 members, mini held out), leaf 8 + first-call L5
cd /home/user/arc-whitebox
export AICROWD_API_KEY=$(cat work/.aicrowd_key2)
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
source work/lean_env.sh
until [ "$(grep -l 'saved' work/runs/gru_all_s11.log work/runs/gru_all_s12.log work/runs/gru_all_s13.log 2>/dev/null | wc -l)" -ge 3 ]; do sleep 60; done
sleep 120
echo "$(date -u +%H:%M) long-3 training"
for sd in 14 15 16; do
  OMP_NUM_THREADS=1 setsid nohup python work/gru_corr.py --full --hold-mini --hidden 64 --epochs 8 --inner 2 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_long_s$sd.npz > work/runs/gru_long_s$sd.log 2>&1 &
done
until [ "$(grep -l 'saved' work/runs/gru_long_s14.log work/runs/gru_long_s15.log work/runs/gru_long_s16.log 2>/dev/null | wc -l)" -ge 3 ]; do sleep 60; done
for sd in 14 15 16; do echo "$(date -u +%H:%M) long seed $sd: $(grep BEST work/runs/gru_long_s$sd.log)"; done
OMP_NUM_THREADS=4 python work/gru_corr.py --full --hold-mini --act cdf --hidden 64 --eval work/gru_long_s14.npz,work/gru_long_s15.npz,work/gru_long_s16.npz > work/runs/gru_long_ens.log 2>&1
r=$(grep "ENSEMBLE holdout" work/runs/gru_long_ens.log | sed -n 's/.*mean ratio \([0-9.]*\).*/\1/p'); echo "$(date -u +%H:%M) long-3 ensemble holdout ratio: $r"
uv run --project $SK python work/export_gru.py work/gru_long_s14.npz work/gru_long_s15.npz work/gru_long_s16.npz work/gru_long_ens.json
work/build_v32.sh work/gru_long_ens.json work/sub22_A2_long3 2 8 >> work/runs/acct2_chain3.log 2>&1
python3 work/make_variant.py work/sub22_A2_long3/estimator.py work/sub22_A2_long3/est_tmp.py V28_STRASSEN_FIRST=5 && mv work/sub22_A2_long3/est_tmp.py work/sub22_A2_long3/estimator.py && rm -rf work/sub22_A2_long3/__pycache__
cd $SK && ok=$(uv run whest validate --estimator /home/user/arc-whitebox/work/sub22_A2_long3/estimator.py --format plain 2>&1 | grep -c "Validation passed"); cd /home/user/arc-whitebox
desc="Acct2 V32 long-3: lone level 2, leaf 8, first-call level 5 + 3-member CDF-gated GRU corrector ensemble (hidden 64) trained for 8 epochs on 630 full-split MLPs, 100 mini held out (ratio $r); model embedded"
if [ "$ok" = "1" ]; then
  cd $SK && out=$(uv run whest submit --estimator /home/user/arc-whitebox/work/sub22_A2_long3/estimator.py --yes --format plain --description "$desc" 2>&1 | grep "submission id"); cd /home/user/arc-whitebox
  echo "$(date -u +%H:%M) acct2-long3: $out"; sid=$(echo "$out" | grep -o "[0-9]\{6\}")
  [ -n "$sid" ] && setsid nohup work/watch_sub.sh $sid acct2-long3 work/sub22_A2_long3/estimator.py "$desc" > work/runs/watch_$sid.log 2>&1 &
fi
echo "$(date -u +%H:%M) ACCT2 CHAIN3 DONE"
