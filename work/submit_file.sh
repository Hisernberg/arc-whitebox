#!/bin/bash
# usage: submit_file.sh <1|2> <estimator.py> <label> "<description>"   (1 = nabid_nur key, 2 = multi_agent key); starts a watcher
acct=$1; est=$2; label=$3; desc=$4
cd /home/user/arc-whitebox
[ "$acct" = "2" ] && export AICROWD_API_KEY=$(cat work/.aicrowd_key2) || export AICROWD_API_KEY=$(cat work/.aicrowd_key)
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
cd $SK && out=$(uv run whest submit --estimator /home/user/arc-whitebox/$est --yes --format plain --description "$desc" 2>&1 | grep "submission id"); cd /home/user/arc-whitebox
sid=$(echo "$out" | grep -o "[0-9]\{6\}")
echo "$(date -u +%H:%M) acct$acct $label: ${out:-FAILED}" | tee -a work/runs/submissions_day3.log
[ -n "$sid" ] && setsid nohup work/watch_sub.sh $sid $label "$est" "$desc" > work/runs/watch_$sid.log 2>&1 &
