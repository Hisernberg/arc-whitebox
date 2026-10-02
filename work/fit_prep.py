#!/usr/bin/env python3
"""Prepare the fitted transported-correction dataset from V29 feature dumps.

For every mini-split MLP i with work/feats/feat_i.npz, stream its weights from the parquet
shards, build per-layer per-neuron features H_l (n, F), transport them linearly to the final
layer with T_m(s) = Phi_m * (s @ W_m)  (first-order sensitivity of the post-ReLU mean to a
mean shift of the previous layer), and save G = [T_{l->15} H_l] (16, n, F) with the final
error e15 = truth15 - pred15 to work/feats/G_i.npz.  Also records the transport validation
(regression of e_m on T_m e_{m-1}) and the born-error decomposition.
Usage: fit_prep.py [start stop]"""
import glob, os, sys, time
import numpy as np
import pyarrow.parquet as pq

FE = "/home/user/arc-whitebox/work/feats"
n = 1024


def iter_rows():
    shards = sorted(glob.glob(os.path.expanduser(
        "~/.cache/huggingface/hub/datasets--aicrowd--arc-whestbench-public-2026/snapshots/*/data/mini-*.parquet")))
    i = 0
    for sh in shards:
        pf = pq.ParquetFile(sh)
        for batch in pf.iter_batches(batch_size=1, columns=["mlp_name", "weights"]):
            yield i, batch.to_pylist()[0]
            i += 1


def herm(a):
    """probabilists' Hermite He_0..He_4 of alpha."""
    return [np.ones_like(a), a, a * a - 1, a ** 3 - 3 * a, a ** 4 - 6 * a * a + 3]


def features(d, l):
    """Per-neuron feature dict at layer l from a feature dump (missing keys -> zeros)."""
    def g(k):
        kk = f"L{l:02d}_{k}"
        return d[kk].astype(np.float64) if kk in d.files else np.zeros(n)
    mu, var, alpha, phi, Phi = g("mu_pre"), g("var"), g("alpha"), g("phi"), g("Phi")
    sig = np.sqrt(np.maximum(var, 1e-12))
    chi = sig * phi                      # sigma * pdf(alpha): the natural scale of mean corrections
    D3, g4 = g("D3"), g("g4row")         # pre-activation kappa3 / regenerated kappa4 diagonals
    s3 = D3 / sig ** 3                   # skewness
    k4 = g4 / sig ** 4                   # excess kurtosis (regenerated)
    He = herm(alpha)
    F = {}
    for hi, h in enumerate(He):
        F[f"chi_He{hi}"] = chi * h
        F[f"chi_s3_He{hi}"] = chi * s3 * h
        F[f"chi_k4_He{hi}"] = chi * k4 * h
        F[f"chi_s3sq_He{hi}"] = chi * s3 * s3 * h
    F["chi_s3k4"] = chi * s3 * k4
    F["K3v"], F["K4v"], F["g_post"] = g("K3v"), g("K4v"), g("g_post")
    F["s3c"] = g("s3c")
    F["k22row"], F["k21row"], F["k21col"] = g("k22row"), g("k21row"), g("k21col")
    cs, cq = g("coff_sum"), g("coff_sq")
    F["chi_csum"], F["chi_csq"] = chi * cs, chi * cq
    F["chi_csq_He1"], F["chi_csq_He2"] = chi * cq * He[1], chi * cq * He[2]
    F["chi_d21row"], F["chi_d21col"] = chi * g("d21_rowsum"), chi * g("d21_colsum")
    F["chi_d21abs"], F["chi_d21sq"] = chi * g("d21_abs"), chi * g("d21_sq")
    F["chi_d21Tabs"] = chi * g("d21T_abs")
    F["pred"] = g("pred")
    F["mu"], F["Phi"], F["phi"] = mu, Phi, phi
    F["sig"] = sig
    return F


def main():
    start = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    stop = int(sys.argv[2]) if len(sys.argv) > 2 else 10 ** 9
    names = None
    for i, row in iter_rows():
        if i < start or not os.path.exists(f"{FE}/feat_{i:04d}.npz"):
            continue
        if i >= stop:
            break
        out = f"{FE}/G_{i:04d}.npz"
        if os.path.exists(out):
            continue
        t0 = time.time()
        d = np.load(f"{FE}/feat_{i:04d}.npz")
        assert str(d["name"]) == row["mlp_name"], (str(d["name"]), row["mlp_name"])
        W = np.asarray(row["weights"], dtype=np.float32).reshape(16, n, n).astype(np.float64)
        pred, truth = d["pred"].astype(np.float64), d["truth"].astype(np.float64)
        e = truth - pred                                             # (16, n)
        Phi = np.stack([d[f"L{l:02d}_Phi"].astype(np.float64) for l in range(16)])
        # convention check on the first MLP: mu_pre[1] vs truth0 @ W1 vs W1 @ truth0
        if i == start or names is None:
            mu1 = d["L01_mu_pre"].astype(np.float64)
            a = truth[0] @ W[1]; b = W[1] @ truth[0]
            print(f"convention check: corr(mu1, t0@W1)={np.corrcoef(mu1, a)[0, 1]:.6f} corr(mu1, W1@t0)={np.corrcoef(mu1, b)[0, 1]:.6f}", flush=True)

        def T(m, S):  # transport a (n, k) block of layer m-1 mean shifts to layer m post means
            return Phi[m][:, None] * (W[m].T @ S)

        # transport validation + born errors
        born = np.zeros((16, n)); born[0] = e[0]
        val = []
        for m in range(1, 16):
            te = T(m, e[m - 1][:, None])[:, 0]
            a = float(te @ e[m] / max(te @ te, 1e-30))
            r = e[m] - te
            val.append((m, a, float(np.mean(r ** 2) / np.mean(e[m] ** 2))))
            born[m] = r
        # contribution of each layer's born error to e15
        contrib = np.zeros((16, n))
        for l in range(16):
            s = born[l][:, None]
            for m in range(l + 1, 16):
                s = T(m, s)
            contrib[l] = s[:, 0]
        # features and their transports
        Fd = [features(d, l) for l in range(16)]
        names = list(Fd[0].keys())
        Fn = len(names)
        G = np.zeros((16, n, Fn), dtype=np.float32)
        for l in range(16):
            S = np.stack([Fd[l][k] for k in names], axis=1)
            for m in range(l + 1, 16):
                S = T(m, S)
            G[l] = S.astype(np.float32)
        np.savez_compressed(out, G=G, e15=e[15].astype(np.float32), e=e.astype(np.float32), born=born.astype(np.float32),
                            contrib=contrib.astype(np.float32), names=np.array(names), name=str(d["name"]),
                            val=np.array(val), mse=float(d["mse"]))
        cm = np.array([np.mean(contrib[l] ** 2) for l in range(16)])
        print(f"[{i:03d}] {str(d['name']):20s} mse={float(d['mse']):.3e} T-fit a(m=5,10,15)={val[4][1]:.3f},{val[9][1]:.3f},{val[14][1]:.3f} "
              f"born-frac(m=5,10,15)={val[4][2]:.2f},{val[9][2]:.2f},{val[14][2]:.2f} | contrib->e15 by layer (x1e-9): "
              + " ".join(f"{c * 1e9:.1f}" for c in cm) + f" sum-check {np.mean(contrib.sum(0) ** 2) / np.mean(e[15] ** 2):.3f} t={time.time() - t0:.0f}s", flush=True)


if __name__ == "__main__":
    main()
