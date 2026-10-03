#!/bin/bash
# day-3 submissions as each training batch lands (nabid_nur = acct 1, multi_agent = acct 2)
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
source work/lean_env.sh
ratio() { python - "$1" <<'PY'
import sys, numpy as np; d = np.load(sys.argv[1], allow_pickle=False); print("%.4f" % float(d["best_ratio"]) if "best_ratio" in d.files else "n/a")
PY
}
rank() {  # prints the given npz paths sorted by best_ratio (ascending)
  for f in "$@"; do echo "$(ratio $f) $f"; done | sort -n | awk '{print $2}'
}
exp() { uv run --project $SK python work/export_gru.py "$@" > /dev/null 2>&1; }
# ---------- batch A: 12-epoch members ----------
until grep -q "A done" work/runs/day3_train_chain.log; do sleep 60; done
A=($(rank work/gru_e12_s17.npz work/gru_e12_s18.npz work/gru_e12_s19.npz)); rA=$(ratio ${A[0]})
exp ${A[0]} ${A[1]} ${A[2]} work/gru_e12_3.json; exp ${A[0]} work/gru_e12_1.json; exp ${A[0]} ${A[1]} work/gru_e12_2.json
work/build_final.sh work/gru_e12_3.json work/sub33_e12_3 8 5; work/build_final.sh work/gru_e12_1.json work/sub34_e12_1 8 5
work/build_final.sh work/gru_e12_2.json work/sub35_e12_2 8 5; work/build_final.sh work/gru_e12_3.json work/sub36_e12_3_leaf16 16 5
work/submit_file.sh 1 work/sub33_e12_3/estimator.py day3-N3-e12x3 "V32 (lone L2, leaf 8, first-call L5) + 3-member CDF GRU ensemble trained 12 epochs (best member held-out $rA); model embedded"
sleep 5; work/submit_file.sh 1 work/sub34_e12_1/estimator.py day3-N4-e12x1 "V32 (lone L2, leaf 8, first-call L5) + single best 12-epoch CDF GRU member (held-out $rA); model embedded"
sleep 5; work/submit_file.sh 2 work/sub35_e12_2/estimator.py day3-M3-e12x2 "V32 (lone L2, leaf 8, first-call L5) + 2 best 12-epoch CDF GRU members; model embedded"
sleep 5; work/submit_file.sh 2 work/sub36_e12_3_leaf16/estimator.py day3-M4-e12x3-leaf16 "V32 (lone L2, leaf 16, first-call L5) + 3-member 12-epoch CDF GRU ensemble; model embedded"
# ---------- batch B: final-layer weight 8 ----------
until grep -q "B done" work/runs/day3_train_chain.log; do sleep 60; done
B=($(rank work/gru_fw8_s20.npz work/gru_fw8_s21.npz work/gru_fw8_s22.npz)); rB=$(ratio ${B[0]})
MIX=($(rank work/gru_e12_s17.npz work/gru_e12_s18.npz work/gru_e12_s19.npz work/gru_fw8_s20.npz work/gru_fw8_s21.npz work/gru_fw8_s22.npz work/gru_long_s14.npz work/gru_long_s15.npz work/gru_long_s16.npz))
exp ${B[0]} ${B[1]} ${B[2]} work/gru_fw8_3.json; exp ${B[0]} ${B[1]} work/gru_fw8_2.json; exp ${B[0]} work/gru_fw8_1.json; exp ${MIX[0]} ${MIX[1]} ${MIX[2]} work/gru_mix3.json
work/build_final.sh work/gru_fw8_3.json work/sub37_fw8_3 8 5; work/build_final.sh work/gru_mix3.json work/sub38_mix3 8 5
work/build_final.sh work/gru_fw8_2.json work/sub39_fw8_2 8 5; work/build_final.sh work/gru_fw8_1.json work/sub40_fw8_1 8 5
work/submit_file.sh 1 work/sub37_fw8_3/estimator.py day3-N5-fw8x3 "V32 (lone L2, leaf 8, first-call L5) + 3-member CDF GRU ensemble trained with final-layer loss weight 8 (best member held-out $rB); model embedded"
sleep 5; work/submit_file.sh 1 work/sub38_mix3/estimator.py day3-N6-mix3 "V32 (lone L2, leaf 8, first-call L5) + the 3 best held-out members across the 8-epoch, 12-epoch and final-weight-8 runs; model embedded"
sleep 5; work/submit_file.sh 2 work/sub39_fw8_2/estimator.py day3-M5-fw8x2 "V32 (lone L2, leaf 8, first-call L5) + 2 best final-weight-8 CDF GRU members; model embedded"
sleep 5; work/submit_file.sh 2 work/sub40_fw8_1/estimator.py day3-M6-fw8x1 "V32 (lone L2, leaf 8, first-call L5) + single best final-weight-8 CDF GRU member; model embedded"
# ---------- batch C: hidden 48 ----------
until grep -q "C done" work/runs/day3_train_chain.log; do sleep 60; done
C=($(rank work/gru_h48_s23.npz work/gru_h48_s24.npz work/gru_h48_s25.npz)); rC=$(ratio ${C[0]})
exp ${C[0]} ${C[1]} ${C[2]} work/gru_h48_3.json; exp ${C[0]} ${C[1]} work/gru_h48_2.json; exp ${C[0]} work/gru_h48_1.json
work/build_final.sh work/gru_h48_3.json work/sub41_h48_3 8 5; work/build_final.sh work/gru_h48_2.json work/sub42_h48_2 8 5
work/build_final.sh work/gru_h48_3.json work/sub43_h48_3_leaf16 16 5; work/build_final.sh work/gru_h48_1.json work/sub44_h48_1 8 5
work/submit_file.sh 1 work/sub41_h48_3/estimator.py day3-N7-h48x3 "V32 (lone L2, leaf 8, first-call L5) + 3-member hidden-48 CDF GRU ensemble, 8 epochs (best member held-out $rC); model embedded"
sleep 5; work/submit_file.sh 1 work/sub42_h48_2/estimator.py day3-N8-h48x2 "V32 (lone L2, leaf 8, first-call L5) + 2 best hidden-48 CDF GRU members; model embedded"
sleep 5; work/submit_file.sh 2 work/sub43_h48_3_leaf16/estimator.py day3-M7-h48x3-leaf16 "V32 (lone L2, leaf 16, first-call L5) + 3-member hidden-48 CDF GRU ensemble; model embedded"
sleep 5; work/submit_file.sh 2 work/sub44_h48_1/estimator.py day3-M8-h48x1 "V32 (lone L2, leaf 8, first-call L5) + single best hidden-48 CDF GRU member; model embedded"
# ---------- batch D: all-data, 8 epochs ----------
until grep -q "D done" work/runs/day3_train_chain.log; do sleep 60; done
exp work/gru_all8_s26.npz work/gru_all8_s27.npz work/gru_all8_s28.npz work/gru_all8_3.json; exp work/gru_all8_s26.npz work/gru_all8_s27.npz work/gru_all8_2.json; exp work/gru_all8_s26.npz work/gru_all8_1.json
ALL=($(rank work/gru_e12_s17.npz work/gru_e12_s18.npz work/gru_e12_s19.npz work/gru_fw8_s20.npz work/gru_fw8_s21.npz work/gru_fw8_s22.npz work/gru_long_s14.npz work/gru_long_s15.npz work/gru_long_s16.npz work/gru_h48_s23.npz work/gru_h48_s24.npz work/gru_h48_s25.npz))
exp ${ALL[0]} ${ALL[1]} work/gru_best2.json
work/build_final.sh work/gru_all8_3.json work/sub45_all8_3 8 5; work/build_final.sh work/gru_best2.json work/sub46_best2 8 5
work/build_final.sh work/gru_all8_2.json work/sub47_all8_2 8 5; work/build_final.sh work/gru_all8_1.json work/sub48_all8_1 8 5
work/submit_file.sh 1 work/sub45_all8_3/estimator.py day3-N9-all8x3 "V32 (lone L2, leaf 8, first-call L5) + 3-member CDF GRU ensemble trained 8 epochs on all 730 public MLPs (no holdout); model embedded"
sleep 5; work/submit_file.sh 1 work/sub46_best2/estimator.py day3-N10-best2 "V32 (lone L2, leaf 8, first-call L5) + the 2 best held-out members of the day across all runs; model embedded"
sleep 5; work/submit_file.sh 2 work/sub47_all8_2/estimator.py day3-M9-all8x2 "V32 (lone L2, leaf 8, first-call L5) + 2 CDF GRU members trained 8 epochs on all 730 public MLPs; model embedded"
sleep 5; work/submit_file.sh 2 work/sub48_all8_1/estimator.py day3-M10-all8x1 "V32 (lone L2, leaf 8, first-call L5) + 1 CDF GRU member trained 8 epochs on all 730 public MLPs; model embedded"
echo "$(date -u +%H:%M) DAY3 SUBMIT CHAIN DONE"
