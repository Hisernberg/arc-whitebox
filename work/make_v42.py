#!/usr/bin/env python3
"""V42: LT corrector with cross-neuron inputs. On top of a V41 build: when the model has x2=True, each layer's
inputs also get the previous layer's features carried through W and W*W (16 extra columns, order
[f@W, f@W^2] for f in LT_XF). Usage: make_v42.py <v41_src.py> <lt_x2.json> <dst.py>"""
import re, sys
src, ltj, dst = sys.argv[1:4]
s = open(src).read()
m = re.search(r'^GRU_JSON = r""".*?"""', s, flags=re.M)
assert m, "GRU_JSON literal not found"
s = s[:m.start()] + 'GRU_JSON = r"""' + open(ltj).read().strip() + '"""' + s[m.end():]
a = '    assert int(d["F"]) == len(LT_FE) + 1, "LT feature count mismatch"\n    g = {"kind": "lt", "sig_mu": 1.0}\n'
assert s.count(a) == 1
s = s.replace(a, '    g = {"kind": "lt", "sig_mu": 1.0, "x2": bool(d.get("x2", False))}\n'
                 '    assert int(d["F"]) == len(LT_FE) + 1 + (2 * len(LT_XF) if g["x2"] else 0), "LT feature count mismatch"\n')
a = 'def _lt_from_dict(d):\n'
assert s.count(a) == 1
s = s.replace(a, 'LT_XF = ["var", "phi", "Phi", "K3v", "K4v", "pred", "g_post", "e_b"]   # V42: carried-forward inputs\n\n\n' + a)
a = '        X = fnp.stack(cols, axis=1)                                               # (n, F)\n        Z = fnp.sign(X)'
assert s.count(a) == 1
s = s.replace(a, '''        if g["x2"]:
            pv = gst.get("prev")
            W2 = W * W if pv is not None else None
            for k in LT_XF:
                v = pv.get(k) if pv is not None else None
                if v is None:
                    cols.append(fnp.zeros(n, dtype=f32)); cols.append(fnp.zeros(n, dtype=f32))
                else:
                    cols.append(W @ v); cols.append(W2 @ v)
            gst["prev"] = fd
        X = fnp.stack(cols, axis=1)                                               # (n, F)
        Z = fnp.sign(X)''')
open(dst, "w").write(s)
print("V42 written", dst)
