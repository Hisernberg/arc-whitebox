#!/usr/bin/env python3
"""Bake knob values into a copy of an estimator: every `_os.environ.get("NAME", "default")`
whose NAME is given on the command line gets its default replaced (the grader passes no env).
Usage: make_variant.py <src.py> <dst.py> NAME=VALUE [NAME=VALUE ...]"""
import re, sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src).read()
for kv in sys.argv[3:]:
    name, val = kv.split("=", 1)
    pat = re.compile(r'_os\.environ\.get\("%s",\s*"[^"]*"\)' % re.escape(name))
    n = len(pat.findall(s))
    if n != 1:
        sys.exit(f"{name}: expected exactly one environ.get, found {n}")
    s = pat.sub('_os.environ.get("%s", "%s")' % (name, val), s)
    print(f"baked {name}={val}")
open(dst, "w").write(s)
