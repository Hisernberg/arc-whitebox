#!/bin/bash
# second account, revised: V1 = 3-member tanh ensemble (seeds 8-10); V2 = 3-member all-data ensemble (seeds 11-13,
# full + mini, no holdout, 3 fixed epochs). Both built as V32 with leaf 8 + first-call level 5 (grader-verified knobs).
cd /home/user/arc-whitebox
export AICROWD_API_KEY=$(cat work/.aicrowd_key2)
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
source work/lean_env.sh
finish() {  # <ens.json> <out_dir> <label> <description>
  work/build_v32.sh $1 $2 2 8 >> work/runs/acct2_chain2.log 2>&1
  python3 work/make_variant.py $2/estimator.py $2/est_tmp.py V28_STRASSEN_FIRST=5 && mv $2/est_tmp.py $2/estimator.py && rm -rf $2/__pycache__
  cd $SK && ok=$(uv run whest validate --estimator /home/user/arc-whitebox/$2/estimator.py --format plain 2>&1 | grep -c "Validation passed"); cd /home/user/arc-whitebox
  [ "$ok" = "1" ] || { echo "$(date -u +%H:%M) $3: validation FAILED, not submitting"; return; }
  cd $SK && out=$(uv run whest submit --estimator /home/user/arc-whitebox/$2/estimator.py --yes --format plain --description "$4" 2>&1 | grep "submission id"); cd /home/user/arc-whitebox
  echo "$(date -u +%H:%M) $3: $out"; sid=$(echo "$out" | grep -o "[0-9]\{6\}")
  [ -n "$sid" ] && setsid nohup work/watch_sub.sh $sid $3 "$2/estimator.py" "$4" > work/runs/watch_$sid.log 2>&1 &
}
# --- V1: tanh-3 ---
until [ "$(grep -l 'saved' work/runs/gru_fulltanh_s8.log work/runs/gru_fulltanh_s9.log work/runs/gru_fulltanh_s10.log 2>/dev/null | wc -l)" -ge 3 ]; do sleep 60; done
for sd in 8 9 10; do echo "$(date -u +%H:%M) tanh seed $sd: $(grep BEST work/runs/gru_fulltanh_s$sd.log)"; done
OMP_NUM_THREADS=4 python work/gru_corr.py --full --hold-mini --act tanh --hidden 64 --eval work/gru_fulltanh_s8.npz,work/gru_fulltanh_s9.npz,work/gru_fulltanh_s10.npz > work/runs/gru_fulltanh_ens.log 2>&1
r=$(grep "ENSEMBLE holdout" work/runs/gru_fulltanh_ens.log | sed -n 's/.*mean ratio \([0-9.]*\).*/\1/p'); echo "$(date -u +%H:%M) tanh-3 ensemble holdout ratio: $r"
uv run --project $SK python work/export_gru.py work/gru_fulltanh_s8.npz work/gru_fulltanh_s9.npz work/gru_fulltanh_s10.npz work/gru_fulltanh_ens.json
finish work/gru_fulltanh_ens.json work/sub20_A2_tanh3 acct2-tanh3 "Acct2 V32 tanh-3: lone level 2, leaf 8, first-call level 5 + 3-member tanh-gated GRU corrector ensemble (hidden 64) trained on 630 full-split MLPs, 100 mini held out (ratio $r); model embedded"
# --- V2: all-data-3 ---
echo "$(date -u +%H:%M) all-data members training"
for sd in 11 12 13; do
  OMP_NUM_THREADS=1 setsid nohup python work/gru_corr.py --full --holdout 0 --hidden 64 --epochs 3 --inner 2 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_all_s$sd.npz > work/runs/gru_all_s$sd.log 2>&1 &
done
until [ "$(grep -l 'saved' work/runs/gru_all_s11.log work/runs/gru_all_s12.log work/runs/gru_all_s13.log 2>/dev/null | wc -l)" -ge 3 ]; do sleep 60; done
uv run --project $SK python work/export_gru.py work/gru_all_s11.npz work/gru_all_s12.npz work/gru_all_s13.npz work/gru_all_ens.json
finish work/gru_all_ens.json work/sub21_A2_all3 acct2-alldata3 "Acct2 V32 all-data-3: lone level 2, leaf 8, first-call level 5 + 3-member CDF-gated GRU corrector ensemble (hidden 64) trained on all 730 public MLPs (full + mini, no holdout, 3 fixed epochs); model embedded"
echo "$(date -u +%H:%M) ACCT2 CHAIN2 DONE"
