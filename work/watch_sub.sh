#!/bin/bash
# usage: watch_sub.sh <submission_id> <label> <estimator_path> "<note>"  -- poll until graded/failed, then archive
sid=$1; label=$2; est=$3; note=$4
cd /home/user/arc-whitebox
KEY=$(cat work/.aicrowd_key)
while true; do
  st=$(curl -sS -m 30 -H "Authorization: Token $KEY" "https://www.aicrowd.com/api/v1/submissions/$sid" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('grading_status_cd') or d.get('status') or '')" 2>/dev/null)
  echo "$(date -u +%H:%M) $sid $st"
  case "$st" in graded|failed|GRADED|FAILED) break;; esac
  sleep 60
done
lab=$label; [ "$st" = "failed" ] || [ "$st" = "FAILED" ] && lab="${label}-failed"
uv run --project /tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit python work/archive_submission.py $sid $lab --note "$note" --estimator $est
