#!/bin/bash
# at 00:03 UTC (new daily quota): submit candidate A (work/sub11_A) and, if present, B (work/sub11_B); watchers archive them
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
until grep -q "A BUILT" work/runs/prep_final.log; do sleep 60; done
until [ "$(date -u +%H)" -eq 0 ] && [ "$(date -u +%M)" -ge 3 ]; do sleep 30; done
ratio=$(grep "ensemble holdout" work/runs/night_chain.log | tail -n 1 | sed -n 's/.*ratio: \([0-9.]*\).*/\1/p')
for v in A B; do
  d=work/sub11_$v; [ -f $d/estimator.py ] || continue
  desc=$(cat $d/DESCRIPTION 2>/dev/null || echo "V32 final $v: V29 (504aldo MIT) + Strassen-priced lone join products (level 2, leaf 16) + 3-member GRU corrector ensemble trained on the full public split (mini held out, ratio $ratio); model embedded")
  cd $SK && out=$(uv run whest submit --estimator /home/user/arc-whitebox/$d/estimator.py --yes --format plain --description "$desc" 2>&1 | grep "submission id"); cd /home/user/arc-whitebox
  echo "$(date -u +%H:%M) $v: $out"; sid=$(echo "$out" | grep -o "[0-9]\{6\}")
  [ -n "$sid" ] && nohup work/watch_sub.sh $sid final-$v-v32-gru-full "$d/estimator.py" "$desc" > work/runs/watch_$sid.log 2>&1 &
  sleep 90
done
