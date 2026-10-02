#!/bin/bash
# today's chain: 100 mini feats -> train GRU (hold out 20) -> export -> sub04 folder -> 2-MLP local sanity run
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
until [ "$(ls work/feats/feat_*.npz | wc -l)" -ge 100 ]; do sleep 60; done
echo "$(date -u +%H:%M) 100 mini feats ready; training"
source work/lean_env.sh
OMP_NUM_THREADS=2 python work/gru_corr.py --hidden 64 --epochs 150 --holdout 20 --seed 1 --act cdf --out work/gru_mini100.npz > work/runs/gru_mini100.log 2>&1
echo "$(date -u +%H:%M) training done: $(grep 'ep 149' work/runs/gru_mini100.log)"
mkdir -p work/sub04_v31m
uv run --project $SK python work/export_gru.py work/gru_mini100.npz work/gru_mini100.json
python3 work/make_v31.py --embed work/gru_mini100.json --out work/sub04_v31m/estimator.py
rm -rf work/sub04_v31m/__pycache__
cd $SK && V26_STRASSEN=0 OMP_NUM_THREADS=2 uv run whest run --estimator /home/user/arc-whitebox/work/sub04_v31m/estimator.py --dataset hf://aicrowd/arc-whestbench-public-2026@v2-phase2 --split mini --n-mlps 2 --runner local --no-residual-wall-time-limit --wall-time-limit 900 --format json > /home/user/arc-whitebox/work/runs/v31m_sanity.json 2> /home/user/arc-whitebox/work/runs/v31m_sanity.err
cd /home/user/arc-whitebox && uv run --project $SK python work/cmp_runs.py work/runs/v31m_sanity.json
echo "$(date -u +%H:%M) READY: work/sub04_v31m"
