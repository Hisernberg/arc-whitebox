#!/bin/bash
# usage: archive_pending.sh <args-file>  -- one pass (no polling loop): archive every listed submission that has
# finished grading; lines are "<sid>|<label>|<estimator>|<note>". Prints what is still pending.
cd /home/user/arc-whitebox
KEY=$(cat work/.aicrowd_key)
while IFS='|' read -r sid lab est note; do
  ls -d submissions/phase-2/$sid-* >/dev/null 2>&1 && continue
  st=$(curl -sS -m 30 -H "Authorization: Token $KEY" "https://www.aicrowd.com/api/v1/submissions/$sid" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('grading_status_cd') or d.get('status') or '')" 2>/dev/null)
  case "$st" in
    graded|GRADED) l=$lab;;
    failed|FAILED) l="$lab-failed";;
    *) echo "$sid $lab pending ($st)"; continue;;
  esac
  uv run --project /tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit python work/archive_submission.py $sid $l --note "$note" --estimator $est
done < "$1"
