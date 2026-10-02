#!/bin/bash
# like knob_queue.sh but on the patched estimator_v29_x.py; waits for knob_queue.sh to finish first
n=$1; shift
while pgrep -f "[k]nob_queue.sh" > /dev/null; do sleep 30; done
cd /tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
for cfg in "$@"; do
  tag=$(echo "$cfg" | tr ' =' '__')
  env $cfg V26_STRASSEN=0 OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 uv run whest run --estimator /home/user/arc-whitebox/work/estimator_v29_x.py \
    --dataset hf://aicrowd/arc-whestbench-public-2026@v2-phase2 --split mini --n-mlps $n --runner local \
    --no-residual-wall-time-limit --wall-time-limit 900 --format json \
    > /home/user/arc-whitebox/work/runs/knobx_$tag.json 2> /home/user/arc-whitebox/work/runs/knobx_$tag.err
  echo "done $tag $(date -u +%H:%M)"
done
