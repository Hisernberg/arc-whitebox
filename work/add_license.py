#!/usr/bin/env python3
"""Prepend the attribution header (504aldo's MIT copyright and permission notice) to a built
estimator, in place. Comment-only: the code is unchanged. Idempotent.
Usage: add_license.py <estimator.py> [...]"""
import sys
lic = open("/home/user/arc-whitebox/work/LICENSE_504aldo.txt").read().strip().splitlines()
head = ["# Attribution: this estimator builds on the factorized K=3 cumulant-propagation estimator by",
        "# 504aldo (https://github.com/504aldo/whest-p2-cumulant-k3, forum topic 18218), used under the",
        "# MIT licence below (its version history runs up to V29). Changes labelled V31 and later are our",
        "# own: GRU corrector, Strassen-priced join products, dead-ReLU pruning, shared scratch buffers,",
        "# leaner Strassen helper, warm-up schedule.",
        "#"] + [("# " + l).rstrip() for l in lic] + ["", ""]
for p in sys.argv[1:]:
    s = open(p).read()
    if s.startswith("# Attribution: this estimator builds on"):
        continue
    open(p, "w").write("\n".join(head) + s)
    print("licensed", p)
