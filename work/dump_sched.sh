#!/bin/bash
# full-split feature dumps: one now (rows 0-549), a second when the mini dump has finished (rows 550-1099)
cd /home/user/arc-whitebox
until [ -f work/truth_all.npz ]; do sleep 10; done
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
FEAT_SRC=full nohup uv run --project $SK python work/feat_dump.py 0 550 > work/runs/featf_0_550.log 2>&1 &
while pgrep -f "[f]eat_dump.py 0 100" > /dev/null; do sleep 30; done
FEAT_SRC=full nohup uv run --project $SK python work/feat_dump.py 550 1100 > work/runs/featf_550_1100.log 2>&1 &
wait
