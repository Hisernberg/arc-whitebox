#!/bin/bash
# sequential Strassen-on cost runs (2 MLPs each, 1 BLAS thread): usage cost_queue.sh <estimator> <tag> "ENV=VAL ..." ...
est=$1; shift; tagbase=$1; shift
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
cd $SK
for cfg in "$@"; do
  tag=${tagbase}_$(echo "$cfg" | tr ' =' '__')
  env $cfg OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 uv run whest run --estimator $est --dataset hf://aicrowd/arc-whestbench-public-2026@v2-phase2 --split mini --n-mlps 2 --runner local --no-residual-wall-time-limit --wall-time-limit 1800 --format json > /home/user/arc-whitebox/work/runs/cost_$tag.json 2> /home/user/arc-whitebox/work/runs/cost_$tag.err
  echo "$(date -u +%H:%M) done $tag"
done
