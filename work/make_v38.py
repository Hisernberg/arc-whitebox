#!/usr/bin/env python3
"""V38 = V37 + late-only deeper Strassen: after the first V37_NEARLY predicts (where the grader
residual sits near 0.27 s, against 0.37 s on the first ones) the leaf floor drops to V38_MIN_LATE and
the lone join products go to level V38_LONE_LATE. The early calls keep the V37 settings.
Usage: make_v38.py <v37_in.py> <out.py>"""
import sys
src = open(sys.argv[1]).read()
def rep(old, new, n=1):
    global src
    c = src.count(old)
    assert c == n, (c, old[:90])
    src = src.replace(old, new)
a = src.index('LP_LATE = int(_os.environ.get("V37_LP_LATE"'); b = src.index("\n", a) + 1
src = src[:b] + ('MIN_EARLY = STRASSEN_MIN\n'
                 'MIN_LATE = int(_os.environ.get("V38_MIN_LATE", "6"))      # V38: leaf floor after the early calls\n'
                 'LONE_LATE = int(_os.environ.get("V38_LONE_LATE", "6"))    # V38: lone level after the early calls\n') + src[b:]
rep('''        self._lev_lone = LONE_EARLY if early else LONE_LEV
''', '''        self._lev_lone = LONE_EARLY if early else LONE_LATE
        global STRASSEN_MIN
        STRASSEN_MIN = MIN_EARLY if early else MIN_LATE   # V38: read by _ok / level at call time
''')
open(sys.argv[2], "w").write(src)
print("ok")
