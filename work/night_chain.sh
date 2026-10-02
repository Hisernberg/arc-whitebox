#!/bin/bash
# tonight: when the full-split dump is (nearly) complete, train 3 CDF-GRU members on the full split with ALL 100 mini
# MLPs held out (clean estimate), ensemble-evaluate, embed, sanity-run, then submit right after the UTC day rolls over.
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
until [ "$(ls work/feats/featf_*.npz 2>/dev/null | wc -l)" -ge 950 ] || [ "$(date -u +%H)" -ge 19 ]; do sleep 120; done
echo "$(date -u +%H:%M) full feats: $(ls work/feats/featf_*.npz | wc -l); training"
source work/lean_env.sh
for sd in 1 2 3; do
  OMP_NUM_THREADS=2 python work/gru_corr.py --full --hold-mini --hidden 64 --epochs 10 --inner 4 --seed $sd --act cdf --lr 5e-4 --wd 1e-5 --out work/gru_full_s$sd.npz > work/runs/gru_full_s$sd.log 2>&1
  echo "$(date -u +%H:%M) seed $sd: $(grep BEST work/runs/gru_full_s$sd.log)"
done
OMP_NUM_THREADS=2 python work/gru_corr.py --full --hold-mini --hidden 64 --act cdf --eval work/gru_full_s1.npz,work/gru_full_s2.npz,work/gru_full_s3.npz > work/runs/gru_full_ens.log 2>&1
ratio=$(grep "ENSEMBLE holdout" work/runs/gru_full_ens.log | sed -n 's/.*mean ratio \([0-9.]*\).*/\1/p')
echo "$(date -u +%H:%M) ensemble holdout (100 mini) ratio: $ratio"
mkdir -p work/sub09_v31f
uv run --project $SK python work/export_gru.py work/gru_full_s1.npz work/gru_full_s2.npz work/gru_full_s3.npz work/gru_full_ens.json
python3 work/make_v31.py --embed work/gru_full_ens.json --out work/sub09_v31f/estimator.py
rm -rf work/sub09_v31f/__pycache__
cd $SK && V26_STRASSEN=0 OMP_NUM_THREADS=2 uv run whest run --estimator /home/user/arc-whitebox/work/sub09_v31f/estimator.py --dataset hf://aicrowd/arc-whestbench-public-2026@v2-phase2 --split mini --n-mlps 2 --runner local --no-residual-wall-time-limit --wall-time-limit 900 --format json > /home/user/arc-whitebox/work/runs/v31f_sanity.json 2> /home/user/arc-whitebox/work/runs/v31f_sanity.err
cd /home/user/arc-whitebox && uv run --project $SK python work/cmp_runs.py work/runs/v31f_sanity.json
echo "$(date -u +%H:%M) READY work/sub09_v31f (ratio $ratio); waiting for the UTC day change"
until [ "$(date -u +%H:%M)" \< "00:40" ] && [ "$(date -u +%H)" -eq 0 ]; do sleep 60; done
if python3 -c "import sys; sys.exit(0 if float('$ratio') < 0.99 else 1)"; then
  cd $SK && out=$(uv run whest submit --estimator /home/user/arc-whitebox/work/sub09_v31f/estimator.py --yes --format plain --description "V31f: V29 (504aldo MIT) + 3-member GRU corrector ensemble (CDF gates, hidden 64) trained on the full public split (~950 MLPs), all 100 mini MLPs held out: final-layer MSE ratio $ratio; model embedded" 2>&1 | grep "submission id")
  echo "$out"; sid=$(echo "$out" | grep -o "[0-9]\{6\}")
  cd /home/user/arc-whitebox && nohup work/watch_sub.sh $sid v31f-gru-ens3-full "work/sub09_v31f/estimator.py" "V31f: V29 + 3-member per-layer GRU corrector ensemble (normal-CDF gates, hidden 64) trained on the full public split with all 100 mini-split MLPs held out (held-out final-layer MSE ratio $ratio vs V29); model embedded as a JSON literal." > work/runs/watch_$sid.log 2>&1 &
  echo "$(date -u +%H:%M) SUBMITTED $sid"
else
  echo "$(date -u +%H:%M) ratio $ratio >= 0.99: NOT submitting"
fi
