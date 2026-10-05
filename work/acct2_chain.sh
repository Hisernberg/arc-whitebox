#!/bin/bash
# second account (multi_agent): for each finished stage, submit the leaf-8 counterpart of the ensemble; for S1 also a
# leaf-16 + first-call-level-5 variant. Uses AICROWD_API_KEY from work/.aicrowd_key2 (build_v32.sh inherits it).
cd /home/user/arc-whitebox
export AICROWD_API_KEY=$(cat work/.aicrowd_key2)
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
submit_variant() {  # <estimator.py> <label> <description>
  cd $SK && out=$(uv run whest submit --estimator /home/user/arc-whitebox/$1 --yes --format plain --description "$3" 2>&1 | grep "submission id"); cd /home/user/arc-whitebox
  echo "$(date -u +%H:%M) $2: $out"; sid=$(echo "$out" | grep -o "[0-9]\{6\}")
  [ -n "$sid" ] && setsid nohup work/watch_sub.sh $sid $2 "$1" "$3" > work/runs/watch_$sid.log 2>&1 &
  sleep 60
}
# --- S1 ---
until grep -q "S1 DONE" work/runs/today_chain.log; do sleep 60; done
r1=$(grep "S1 ensemble holdout" work/runs/today_chain.log | tail -n 1 | sed -n 's/.*ratio: \([0-9.]*\).*/\1/p')
work/build_v32.sh work/gru_full_ens.json work/sub16_A2S1_leaf8 2 8 submit "Acct2 V32-S1 leaf-8: V29 (504aldo MIT) + Strassen-priced lone join products (level 2, leaf 8) + 3-member GRU corrector ensemble (CDF, hidden 64) trained on full-split MLPs, 100 mini held out (ratio $r1); model embedded"
mkdir -p work/sub17_A2S1_first5 && python3 work/make_variant.py work/sub12_S1/estimator.py work/sub17_A2S1_first5/estimator.py V28_STRASSEN_FIRST=5 && submit_variant work/sub17_A2S1_first5/estimator.py acct2-S1-first5 "Acct2 V32-S1 first-call L5: as nabid_nur's S1 (lone level 2, leaf 16, 3-member full-split GRU ensemble, ratio $r1) but the first predict of each worker also runs Strassen level 5 (V28_STRASSEN_FIRST=5); model embedded"
# --- S2 ---
until grep -q "S2 DONE" work/runs/today_chain2.log; do sleep 60; done
r2=$(grep "S2 5-member ensemble holdout" work/runs/today_chain2.log | tail -n 1 | sed -n 's/.*ratio: \([0-9.]*\).*/\1/p')
work/build_v32.sh work/gru_full_ens5.json work/sub18_A2S2_leaf8 2 8 submit "Acct2 V32-S2 leaf-8: lone level 2, leaf 8 + 5-member GRU corrector ensemble (3 x h64 + 2 x h96, full split, 100 mini held out, ratio $r2); model embedded"
# --- S3 ---
until grep -q "S3 DONE" work/runs/today_chain3.log; do sleep 60; done
r3=$(grep "S3 7-member ensemble holdout" work/runs/today_chain3.log | tail -n 1 | sed -n 's/.*ratio: \([0-9.]*\).*/\1/p')
work/build_v32.sh work/gru_full_ens7.json work/sub19_A2S3_leaf8 2 8 submit "Acct2 V32-S3 leaf-8: lone level 2, leaf 8 + 7-member GRU corrector ensemble (3 x h64 + 2 x h96 + 2 x h128, full split, 100 mini held out, ratio $r3); model embedded"
echo "$(date -u +%H:%M) ACCT2 CHAIN DONE"
