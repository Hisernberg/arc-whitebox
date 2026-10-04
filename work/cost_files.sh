#!/bin/bash
# usage: cost_files.sh <dir> ...   -> local Strassen-on run (2 MLPs, 1 thread) per estimator; report in work/runs/costf_<dir>.json
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
for d in "$@"; do
  cd $SK && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 uv run whest run --estimator /home/user/arc-whitebox/$d/estimator.py --dataset hf://aicrowd/arc-whestbench-public-2026@v2-phase2 --split mini --n-mlps 2 --runner local --no-residual-wall-time-limit --wall-time-limit 1800 --format json > /home/user/arc-whitebox/work/runs/costf_$(basename $d).json 2>/dev/null
  echo "$(date -u +%H:%M) done $d"
done
