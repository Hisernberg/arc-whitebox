#!/bin/bash
# wait for >= $1 cached weight files, then run a short GRU training as a pipeline smoke test
cd /home/user/arc-whitebox
while [ "$(ls work/feats/W_*.npy 2>/dev/null | wc -l)" -lt "$1" ]; do sleep 20; done
source work/lean_env.sh
OMP_NUM_THREADS=2 python work/gru_corr.py --epochs 40 --holdout 6 --hidden 48 --out work/gru_smoke.npz
