#!/bin/bash
# when the day chain has produced the ensemble JSON and submitted V31: build + submit V32 (lone L2, leaf 16) with the same ensemble
cd /home/user/arc-whitebox
until [ -f work/gru_m100_ens.json ] && grep -q "SUBMITTED\|NOT submitting" work/runs/day_chain2.log; do sleep 30; done
sleep 30
echo "$(date -u +%H:%M) ensemble ready: $(grep 'ensemble holdout' work/runs/day_chain2.log)"
work/build_v32.sh work/gru_m100_ens.json work/sub10_v32 2 16 submit
