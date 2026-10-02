#!/usr/bin/env python3
"""Archive an AIcrowd submission into submissions/phase-2/<id>-<label>/ with
submission-metadata.json, submission-report.json (evaluation JSON) and README.md.
Usage: archive_submission.py <submission_id> <label> [--note "text"] [--estimator path]
"""
import json, os, sys, urllib.request, shutil, datetime

API_KEY = os.environ.get("AICROWD_API_KEY", "acb8a247bedc2e090a454bed42d62d61")
SLUG = "arc-white-box-estimation-challenge-2026"
ROOT = "/home/user/arc-whitebox/submissions/phase-2"
B = 2 ** 41

GQL = ("query($id: ID!){ submission(id: $id){ id createdAt status gradingMessage score scoreSecondary "
       "participant{ id name } team{ name } round{ id name } evaluation } }")


def rails(sid):
    req = urllib.request.Request(f"https://www.aicrowd.com/api/v1/submissions/{sid}",
                                 headers={"Authorization": f"Token {API_KEY}"})
    return json.load(urllib.request.urlopen(req, timeout=60))


def graphql(sid):
    body = json.dumps({"query": GQL, "variables": {"id": str(sid)}}).encode()
    req = urllib.request.Request("https://www.aicrowd.com/graphql", data=body,
                                 headers={"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req, timeout=120))["data"]["submission"]


def main():
    sid, label = sys.argv[1], sys.argv[2]
    note = ""
    est = None
    args = sys.argv[3:]
    while args:
        a = args.pop(0)
        if a == "--note":
            note = args.pop(0)
        elif a == "--estimator":
            est = args.pop(0)
    r = rails(sid)
    g = graphql(sid)
    ev = g.pop("evaluation", None)
    if isinstance(ev, str):
        try:
            ev = json.loads(ev)
        except Exception:
            pass
    folder = os.path.join(ROOT, f"{sid}-{label}")
    # remove any older folder for the same id (status label may change)
    for d in os.listdir(ROOT) if os.path.isdir(ROOT) else []:
        if d.startswith(f"{sid}-") and d != f"{sid}-{label}":
            shutil.rmtree(os.path.join(ROOT, d))
    os.makedirs(folder, exist_ok=True)
    meta = {
        "id": str(sid), "status": (g.get("status") or r.get("grading_status_cd") or "").upper(),
        "score_primary": g.get("score"), "score_secondary": g.get("scoreSecondary"),
        "description": note, "createdAt": g.get("createdAt"), "participant": g.get("participant"),
        "round": g.get("round"), "team": g.get("team"),
        "aicrowd_url": f"https://www.aicrowd.com/challenges/{SLUG}/submissions/{sid}",
        "rails_metadata": r, "archived_at": datetime.datetime.utcnow().isoformat() + "Z",
    }
    json.dump(meta, open(os.path.join(folder, "submission-metadata.json"), "w"), indent=2)
    if ev is not None:
        json.dump(ev, open(os.path.join(folder, "submission-report.json"), "w"), indent=1)
    if est and os.path.exists(est):
        shutil.copy(est, os.path.join(folder, "estimator.py"))
    # README
    lines = [f"# Submission #{sid} — {label}", ""]
    lines += ["| Field | Value |", "|---|---|",
              f"| Submission ID | {sid} |", f"| URL | <{meta['aicrowd_url']}> |",
              f"| Status | {meta['status']} |", f"| Created (UTC) | {meta['createdAt']} |",
              f"| Adjusted score (leaderboard) | {meta['score_primary']} |",
              f"| Raw final-layer MSE | {meta['score_secondary']} |",
              f"| Participant | {(meta['participant'] or {}).get('name')} |",
              f"| Grading message | {r.get('grading_message', '').strip()} |", ""]
    if note:
        lines += ["## What was submitted", "", note, ""]
    if isinstance(ev, dict) and ev.get("results") and ev["results"].get("per_mlp"):
        res = ev["results"]
        agg = (res.get("aggregates") or {}).get("public", {})
        pm = res["per_mlp"]
        tel = [m["telemetry"] for m in pm if m.get("telemetry")]
        fl = [t["flops_used"] for t in tel if t.get("flops_used")]
        kw = [t.get("flopscope_server_kernel_wall_s") for t in tel if t.get("flopscope_server_kernel_wall_s") is not None]
        rw = [t.get("residual_wall_time_s") for t in tel if t.get("residual_wall_time_s") is not None]
        pw = [t.get("participant_predict_wall_s") for t in tel if t.get("participant_predict_wall_s") is not None]
        smoke = ev.get("smoke_test_result") or {}
        lines += ["## Grading summary (from the evaluation report)", ""]
        lines += [f"- Public aggregate: adjusted {agg.get('adjusted_final_layer_score')}, raw final-layer MSE {agg.get('final_layer_mse')}, "
                  f"all-layers MSE {agg.get('all_layers_mse')}, mean multiplier {agg.get('mean_score_multiplier')}, failed MLPs {agg.get('n_failed_mlps')}"]
        if fl:
            lines += [f"- FLOPs per MLP: mean {sum(fl) / len(fl):.4e} ({sum(fl) / len(fl) / B:.4f} x B), min {min(fl) / B:.4f} x B, max {max(fl) / B:.4f} x B"]
        if kw:
            lines += [f"- Grader timing per MLP: kernel {sum(kw) / len(kw):.1f} s mean, predict wall {sum(pw) / len(pw):.1f} s mean / {max(pw):.1f} s max, residual {sum(rw) / len(rw):.3f} s mean / {max(rw):.3f} s max (cap 0.4 s)"]
        lines += [f"- Smoke test: passed={smoke.get('passed')} duration {smoke.get('duration_ms')} ms, worker passes {smoke.get('worker_passes')} / failures {smoke.get('worker_failures')}",
                  f"- MLPs completed: {ev.get('progress', {}).get('mlps_completed')} / {ev.get('progress', {}).get('total_mlps')}", ""]
    lines += ["## Files", "", "- `submission-metadata.json` — Rails + GraphQL record (id, status, scores, participant, round).",
              "- `submission-report.json` — full evaluation report (per-MLP telemetry, public per-MLP scores, smoke test, runtime environment)."]
    if est and os.path.exists(est):
        lines += ["- `estimator.py` — the exact single-file estimator that was packaged and submitted."]
    open(os.path.join(folder, "README.md"), "w").write("\n".join(lines) + "\n")
    print("archived", folder, meta["status"], meta["score_primary"], meta["score_secondary"])


if __name__ == "__main__":
    main()
