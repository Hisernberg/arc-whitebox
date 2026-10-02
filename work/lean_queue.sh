#!/bin/bash
# Sequential lean-chain experiments. Usage: lean_queue.sh <dumps> <tag1>=<cfg1> [<tag2>=<cfg2> ...]
source /home/user/arc-whitebox/work/lean_env.sh
cd /tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/lean
dumps=$1; shift
for item in "$@"; do
  tag=${item%%=*}; cfg=${item#*=}
  echo "=== $tag  cfg=$cfg  dumps=$dumps  $(date -u +%H:%M:%S)"
  python g_regen_probe.py "$dumps" "$cfg" > /home/user/arc-whitebox/work/lean_runs/$tag.log 2>&1
  grep "MEAN\|mse_final" /home/user/arc-whitebox/work/lean_runs/$tag.log | tail -4
done
echo "queue done $(date -u +%H:%M:%S)"
