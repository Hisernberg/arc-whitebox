#!/bin/bash
# usage: submit_file.sh <1|2> <estimator.py> <label> "<description>"   (1 = nabid_nur / Hydrion-Labs, 2 = multi_agent; koushik_rudra is retired); starts a watcher
acct=$1; est=$2; label=$3; desc=$4
cd /home/user/arc-whitebox
case $acct in 2) export AICROWD_API_KEY=$(cat work/.aicrowd_key2);; 3) echo "account 3 (koushik_rudra) is retired: submit to 1 (nabid_nur) or 2 (multi_agent)"; exit 1;; *) export AICROWD_API_KEY=$(cat work/.aicrowd_key);; esac
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
cd $SK && out=$(uv run whest submit --estimator /home/user/arc-whitebox/$est --yes --format plain --description "$desc" 2>&1 | grep "submission id"); cd /home/user/arc-whitebox
sid=$(echo "$out" | grep -o "[0-9]\{6\}")
echo "$(date -u +%H:%M) acct$acct $label: ${out:-FAILED}" | tee -a ${SUBLOG:-work/runs/submissions_day3.log}
[ -n "$sid" ] && setsid nohup work/watch_sub.sh $sid $label "$est" "$desc" > work/runs/watch_$sid.log 2>&1 &
