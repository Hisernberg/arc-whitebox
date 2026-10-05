#!/bin/bash
# today's chain v2: 3 CDF-GRU members (hidden 48, early-stopped on the same 20 held-out mini MLPs) -> ensemble eval ->
# embed -> sanity run -> submit if the ensemble's held-out ratio < 0.99
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
source work/lean_env.sh
for sd in 1 2 3; do
  OMP_NUM_THREADS=2 python work/gru_corr.py --hidden 48 --epochs 60 --holdout 20 --seed $sd --split-seed 1 --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_m100_s$sd.npz > work/runs/gru_m100_s$sd.log 2>&1
  echo "$(date -u +%H:%M) seed $sd: $(grep BEST work/runs/gru_m100_s$sd.log)"
done
OMP_NUM_THREADS=2 python work/gru_corr.py --holdout 20 --split-seed 1 --act cdf --hidden 48 --eval work/gru_m100_s1.npz,work/gru_m100_s2.npz,work/gru_m100_s3.npz > work/runs/gru_m100_ens.log 2>&1
ratio=$(grep "ENSEMBLE holdout" work/runs/gru_m100_ens.log | sed -n 's/.*mean ratio \([0-9.]*\).*/\1/p')
echo "$(date -u +%H:%M) ensemble holdout ratio: $ratio"
mkdir -p work/sub04_v31m
uv run --project $SK python work/export_gru.py work/gru_m100_s1.npz work/gru_m100_s2.npz work/gru_m100_s3.npz work/gru_m100_ens.json
python3 work/make_v31.py --embed work/gru_m100_ens.json --out work/sub04_v31m/estimator.py
rm -rf work/sub04_v31m/__pycache__
cd $SK && V26_STRASSEN=0 OMP_NUM_THREADS=2 uv run whest run --estimator /home/user/arc-whitebox/work/sub04_v31m/estimator.py --dataset hf://aicrowd/arc-whestbench-public-2026@v2-phase2 --split mini --n-mlps 2 --runner local --no-residual-wall-time-limit --wall-time-limit 900 --format json > /home/user/arc-whitebox/work/runs/v31m_sanity.json 2> /home/user/arc-whitebox/work/runs/v31m_sanity.err
cd /home/user/arc-whitebox && uv run --project $SK python work/cmp_runs.py work/runs/v31m_sanity.json
if python3 -c "import sys; sys.exit(0 if float('$ratio') < 0.99 else 1)"; then
  cd $SK && out=$(uv run whest submit --estimator /home/user/arc-whitebox/work/sub04_v31m/estimator.py --yes --format plain --description "V31: V29 (504aldo MIT) + 3-member GRU corrector ensemble (CDF gates, hidden 48, early-stopped; trained on 80 mini-split MLPs, 20 held out: final-layer MSE ratio $ratio), model embedded" 2>&1 | grep "submission id")
  echo "$out"; sid=$(echo "$out" | grep -o "[0-9]\{6\}")
  cd /home/user/arc-whitebox && nohup work/watch_sub.sh $sid v31-gru-ens3-mini "work/sub04_v31m/estimator.py" "V31: V29 + 3-member per-layer GRU corrector ensemble (normal-CDF gates, hidden 48, early-stopped on the held-out set) trained on 80 mini-split MLPs with 20 held out (held-out final-layer MSE ratio $ratio vs V29); model embedded as a JSON literal; suite-shape gate + setup dry run." > work/runs/watch_$sid.log 2>&1 &
  echo "$(date -u +%H:%M) SUBMITTED $sid"
else
  echo "$(date -u +%H:%M) ensemble ratio $ratio >= 0.99: NOT submitting"
fi
