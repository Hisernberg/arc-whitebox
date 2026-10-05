#!/bin/bash
# after the night chain's READY: build final candidate A = V32 (lone L2, leaf 16) + full-split GRU ensemble; validate + dense sanity (no submit)
cd /home/user/arc-whitebox
until grep -q "READY" work/runs/night_chain.log; do sleep 60; done
echo "$(date -u +%H:%M) night chain READY: $(grep 'ensemble holdout' work/runs/night_chain.log | tail -n 1)"
work/build_v32.sh work/gru_full_ens.json work/sub11_A 2 16
echo "$(date -u +%H:%M) A BUILT"
