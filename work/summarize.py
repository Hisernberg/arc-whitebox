#!/usr/bin/env python3
"""Summarize a `whest run --format json` report: raw, C/B, residual, wall, failures."""
import json
import sys

B = 2 ** 41


def main(path):
    d = json.load(open(path))
    per = d.get("per_mlp", [])
    print(f"== {path}")
    top = {k: d[k] for k in d if not isinstance(d[k], (dict, list))}
    for k in ("adjusted_final_layer_score", "final_layer_mse", "all_layers_mse",
              "mean_score_multiplier", "mean_effective_compute", "n_mlps"):
        if k in top:
            print(f"  {k}: {top[k]}")
    rows = []
    for m in per:
        raw = m.get("final_layer_mse")
        fl = m.get("flops_used") or m.get("effective_compute")
        rows.append((m.get("mlp_name") or m.get("mlp_index"), raw, fl, m.get("residual_wall_time_s"),
                     m.get("wall_time_s"), m.get("budget_exhausted"), m.get("residual_wall_time_exhausted"),
                     m.get("time_exhausted"), m.get("error_code")))
    for r in rows:
        name, raw, fl, res, wall, be, re_, te, ec = r
        cb = (fl / B) if fl else None
        print(f"  {str(name)[:24]:24s} raw={raw!s:12.12s} C/B={cb if cb is None else round(cb, 4)!s:7s} "
              f"resid={res if res is None else round(res, 3)!s:6s} wall={wall if wall is None else round(wall, 1)!s:6s} "
              f"fail={be or re_ or te or ec}")
    raws = [r[1] for r in rows if r[1] is not None and not (r[5] or r[6] or r[7] or r[8])]
    if raws:
        print(f"  mean raw over {len(raws)} ok MLPs: {sum(raws) / len(raws):.4e}")


if __name__ == "__main__":
    for p in sys.argv[1:]:
        main(p)
