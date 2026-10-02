#!/bin/bash
# usage: build_v32.sh <ens.json> <out_dir> <LONE_LEV> <STRASSEN_MIN> [submit]
# V31 (GRU embedded) -> V32 (lone products) -> bake knobs -> validate -> 2-MLP dense sanity -> optional submit
ens=$1; out=$2; lev=$3; smin=$4; sub=$5; desc=${6:-"V32: V29 (504aldo MIT) + Strassen-priced lone join products (level $3, leaf $4) + GRU corrector ensemble; model embedded"}
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
mkdir -p $out
python3 work/make_v31.py --embed $ens --out $out/v31_tmp.py | tail -1
python3 work/make_v32.py $out/v31_tmp.py $out/v32_tmp.py | tail -1
python3 work/make_variant.py $out/v32_tmp.py $out/estimator.py V32_LONE_LEV=$lev V26_STRASSEN_MIN=$smin
rm -f $out/v31_tmp.py $out/v32_tmp.py; rm -rf $out/__pycache__
cd $SK && uv run whest validate --estimator /home/user/arc-whitebox/$out/estimator.py --format plain 2>&1 | grep -c "Validation passed"
V26_STRASSEN=0 OMP_NUM_THREADS=2 uv run whest run --estimator /home/user/arc-whitebox/$out/estimator.py --dataset hf://aicrowd/arc-whestbench-public-2026@v2-phase2 --split mini --n-mlps 2 --runner local --no-residual-wall-time-limit --wall-time-limit 900 --format json > /home/user/arc-whitebox/work/runs/sanity_$(basename $out).json 2>/dev/null
cd /home/user/arc-whitebox && uv run --project $SK python work/cmp_runs.py work/runs/sanity_$(basename $out).json
if [ "$sub" = "submit" ]; then
  cd $SK && res=$(uv run whest submit --estimator /home/user/arc-whitebox/$out/estimator.py --yes --format plain --description "$desc" 2>&1 | grep "submission id")
  echo "$res"; sid=$(echo "$res" | grep -o "[0-9]\{6\}")
  cd /home/user/arc-whitebox && nohup work/watch_sub.sh $sid $(basename $out)-v32 "$out/estimator.py" "$desc" > work/runs/watch_$sid.log 2>&1 &
  echo "$(date -u +%H:%M) SUBMITTED $sid"
fi
