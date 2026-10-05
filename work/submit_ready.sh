#!/bin/bash
# when the day chain reports READY: submit work/sub04_v31m if the held-out final-layer ratio < 0.99, then watch/archive
cd /home/user/arc-whitebox
until grep -q "READY" work/runs/day_chain.log; do sleep 30; done
ratio=$(grep "ep 149" work/runs/gru_mini100.log | sed -n 's/.*holdout \([0-9.]*\).*/\1/p')
echo "$(date -u +%H:%M) ready; holdout ratio $ratio"
if python3 -c "import sys; sys.exit(0 if float('$ratio') < 0.99 else 1)"; then
  SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
  cd $SK && out=$(uv run whest submit --estimator /home/user/arc-whitebox/work/sub04_v31m/estimator.py --yes --format plain --description "V31: V29 (504aldo MIT) + per-layer GRU corrector (CDF gates, hidden 64, trained on 80 mini-split MLPs, 20 held out: final-layer MSE ratio $ratio), model embedded" 2>&1 | grep "submission id")
  echo "$out"; sid=$(echo "$out" | grep -o "[0-9]\{6\}")
  cd /home/user/arc-whitebox && nohup work/watch_sub.sh $sid v31-gru-mini100 work/sub04_v31m/estimator.py "V31: V29 + per-layer GRU corrector (normal-CDF gates, hidden 64, 150 epochs) trained on 80 mini-split MLPs with 20 held out (held-out final-layer MSE ratio $ratio vs V29); model embedded as a JSON literal; suite-shape gate + setup dry run." > work/runs/watch_$sid.log 2>&1 &
else
  echo "holdout ratio $ratio >= 0.99: NOT submitting"
fi
