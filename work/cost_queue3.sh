#!/bin/bash
cd /home/user/arc-whitebox
while pgrep -f "[c]ost_queue2.sh" > /dev/null || pgrep -f "[c]ost_queue.sh" > /dev/null; do sleep 20; done
work/cost_queue.sh /home/user/arc-whitebox/work/estimator_v32.py v32 "V31_GRU_OFF=1 V32_LONE_LEV=2" "V31_GRU_OFF=1 V32_LONE_LEV=2 V26_STRASSEN_MIN=16"
