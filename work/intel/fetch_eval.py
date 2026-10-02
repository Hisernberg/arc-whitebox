#!/usr/bin/env python3
"""Fetch AIcrowd submission evaluation reports via the public GraphQL endpoint."""
import json, sys, urllib.request

Q = "query($id: ID!){ submission(id: $id){ id createdAt status gradingMessage score scoreSecondary participant{ name } team{ name } round{ name } evaluation } }"

def fetch(sid):
    body = json.dumps({"query": Q, "variables": {"id": str(sid)}}).encode()
    req = urllib.request.Request("https://www.aicrowd.com/graphql", data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        d = json.load(r)
    return d["data"]["submission"]

if __name__ == "__main__":
    for sid in sys.argv[1:]:
        try:
            s = fetch(sid)
        except Exception as e:
            print(sid, "ERR", e); continue
        ev = s.pop("evaluation", None)
        if isinstance(ev, str):
            try: ev = json.loads(ev)
            except Exception: pass
        json.dump({"meta": s, "evaluation": ev}, open(f"eval_{sid}.json", "w"))
        agg = ((ev or {}).get("results") or {}).get("aggregates", {}).get("public", {}) if isinstance(ev, dict) else {}
        print(sid, s.get("participant", {}).get("name") if s.get("participant") else None, (s.get("team") or {}).get("name"), s["status"], s["score"], s["scoreSecondary"], "mult", agg.get("mean_score_multiplier"), "fail", agg.get("n_failed_mlps"))
