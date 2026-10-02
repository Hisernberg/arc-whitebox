#!/bin/bash
# after the mini dump ends: two full-split dumps (2 BLAS threads each) over disjoint row ranges
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
while pgrep -f "[f]eat_dump.py 0 100" > /dev/null; do sleep 30; done
echo "$(date -u +%H:%M) mini dump finished; starting full dumps"
FEAT_SRC=full OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 nohup uv run --project $SK python work/feat_dump.py 0 550 > work/runs/featf_0_550.log 2>&1 &
sleep 5
FEAT_SRC=full OMP_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 nohup uv run --project $SK python work/feat_dump.py 550 1100 > work/runs/featf_550_1100.log 2>&1 &
wait
