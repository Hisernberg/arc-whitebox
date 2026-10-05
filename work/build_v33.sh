#!/bin/bash
# usage: build_v33.sh <ens.json> <out_dir> <leaf> [KNOB=VAL ...]  -> V31(embed) -> V32 -> V33 -> knobs baked -> validated
ens=$1; out=$2; leaf=$3; shift 3
cd /home/user/arc-whitebox; SK=/tmp/claude-0/-home-user-arc-whitebox/828b687d-6a50-5b7c-872b-6b10df70baf6/scratchpad/whest-starterkit
mkdir -p $out
python3 work/make_v31.py --embed $ens --out $out/a.py > /dev/null && python3 work/make_v32.py $out/a.py $out/b.py > /dev/null && python3 work/make_v33.py $out/b.py $out/c.py > /dev/null || { echo "generate failed"; exit 1; }
python3 work/make_variant.py $out/c.py $out/estimator.py V32_LONE_LEV=2 V26_STRASSEN_MIN=$leaf V28_STRASSEN_FIRST=5 "$@" > /dev/null || { echo "bake failed"; exit 1; }
rm -f $out/a.py $out/b.py $out/c.py; rm -rf $out/__pycache__
cd $SK && uv run whest validate --estimator /home/user/arc-whitebox/$out/estimator.py --format plain 2>&1 | grep -q "Validation passed" && echo "built $out (leaf $leaf $@) OK" || echo "VALIDATION FAILED $out"
