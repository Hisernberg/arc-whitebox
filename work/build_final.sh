#!/bin/bash
# usage: build_final.sh <ens.json> <out_dir> [leaf=8] [first=5]  -> V32 estimator (lone L2) with leaf/first baked, validated
ens=$1; out=$2; leaf=${3:-8}; first=${4:-5}; shift 4 2>/dev/null; extra="$@"
cd /home/user/arc-whitebox
SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
mkdir -p $out
python3 work/make_v31.py --embed $ens --out $out/v31_tmp.py > /dev/null
python3 work/make_v32.py $out/v31_tmp.py $out/v32_tmp.py > /dev/null
python3 work/make_variant.py $out/v32_tmp.py $out/estimator.py V32_LONE_LEV=2 V26_STRASSEN_MIN=$leaf V28_STRASSEN_FIRST=$first $extra > /dev/null || { echo "bake failed"; exit 1; }
rm -f $out/v31_tmp.py $out/v32_tmp.py; rm -rf $out/__pycache__
cd $SK && uv run whest validate --estimator /home/user/arc-whitebox/$out/estimator.py --format plain 2>&1 | grep -q "Validation passed" && echo "built $out (leaf $leaf, first $first $extra) OK" || echo "built $out VALIDATION FAILED"
