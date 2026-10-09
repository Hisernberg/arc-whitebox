#!/bin/bash
# usage: cost_sweep.sh <est> <tag> [ENV=VAL ...] -- local whest run on 2 mini MLPs, warm-up schedule off (V37_NEARLY=0)
est=$1; tag=$2; shift 2
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
OUT=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/sweep
cd $SK && env V37_NEARLY=0 "$@" uv run whest run --estimator $est --dataset hf://aicrowd/arc-whestbench-public-2026@v2-phase2 \
  --split ${SPLIT:-mini} --n-mlps ${NM:-2} --runner local --no-residual-wall-time-limit --wall-time-limit 600 --format json > $OUT/$tag.json 2> $OUT/$tag.err
python3 -c "
import json;d=json.load(open('$OUT/$tag.json'))['results']
print('$tag', 'raw %.4e'%d['final_layer_mse'], 'C/B %.4f'%d['mean_compute_utilization'], 'score %.4e'%d['adjusted_final_layer_score'])" >> $OUT/summary.txt
