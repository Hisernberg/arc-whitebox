#!/bin/bash
# usage: run_cost.sh <tag> <n_mlps> [ENV=VAL ...]   -- cost run: Strassen on, graded caps off (cost is deterministic)
tag=$1; n=$2; shift 2
cd /tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
env "$@" uv run whest run --estimator /home/user/arc-whitebox/work/estimator_v29.py \
  --dataset hf://aicrowd/arc-whestbench-public-2026@v2-phase2 --split mini --n-mlps $n --runner local \
  --no-residual-wall-time-limit --wall-time-limit 600 --profile --format json \
  > /home/user/arc-whitebox/work/runs/$tag.json 2> /home/user/arc-whitebox/work/runs/$tag.err
echo "$tag done"
