# Submissions

One folder per submission, named `<submission-id>-<short-label>` to keep the
listing stable when statuses change.

| Folder | Submission ID | Status | MSE | Created (UTC) | Description |
|--------|---------------|--------|-----|---------------|-------------|
| `334890-d8-C2-rb-lam090-r192/` | 334890 | ✅ GRADED | 4.066e-09 | 2026-10-08 | koushik_rudra Track C nominee: robust + LAM 0.90 + R_OLD2 192 (pred ~4.02): slightly worse than 4.063. Raw 1.990e-08 |
| `334889-d8-C1-l5-lam090-r192/` | 334889 | ✅ GRADED | 4.023e-09 | 2026-10-08 | koushik_rudra Track C: L5 + LAM 0.90 + R_OLD2 192 (pred 3.98–3.99): no change (raw 1.988e-08 up, C/B down) |
| `334765-d8-R3-rb-e2-a1/` | 334765 | ✅ GRADED | 4.063e-09 | 2026-10-08 | nabid_nur: robust V42 + warm-up 2 — nominee (pred 4.0627) |
| `334759-d8-R3-rb-e2-a2/` | 334759 | ✅ GRADED | 4.063e-09 | 2026-10-08 | multi_agent: robust V42 + warm-up 2 — nominee (pred 4.06–4.065). Wall max 105.9 s, residual max 0.338 s, 0 failures |
| `334758-d8-R3-rb-e2-a3/` | 334758 | ✅ GRADED | 4.063e-09 | 2026-10-08 | koushik_rudra: robust V42 + warm-up 2 — nominee. Wall max 105.1 s, residual max 0.345 s, 0 failures |
| `334751-d8-N2-v42lp4-e2/` | 334751 | ✅ GRADED | **4.023e-09** | 2026-10-08 | nabid_nur: V42 + LP4 + warm-up 2 — new best (pred 4.02–4.03). Wall max 112.5 s, 0 failures |
| `334750-d8-M2-v42lp4-e2/` | 334750 | ✅ GRADED | **4.023e-09** | 2026-10-08 | multi_agent: V42 + LP4 + warm-up 2 — new best (pred 4.02–4.03) |
| `334749-d8-K2-v42lp4-e1/` | 334749 | ✅ GRADED | 0.0320 | 2026-10-08 | koushik_rudra: warm-up on 1 call/worker — **2 MLPs (30, 31) TIME_EXHAUSTED**; warm-up 1 is too aggressive |
| `334743-d8-N1-v42lp4-e3/` | 334743 | ✅ GRADED | **4.030e-09** | 2026-10-08 | nabid_nur: V42 + LP4, warm-up on 3 calls/worker — new best (pred 4.025–4.03). C/B 0.2043 (10 early MLPs), wall max 117.2 s; 3 MLPs cut by the grader near the end (TIME_EXHAUSTED at ~109 s with ~1 s overhead), score unaffected |
| `334742-d8-K1-v42lp4-e2/` | 334742 | ✅ GRADED | **4.023e-09** | 2026-10-08 | koushik_rudra: V42 + LP4, warm-up on 2 calls/worker — new best (pred 4.02–4.03). C/B 0.2041 (7 early MLPs), wall max 118.7 s; 2 grader-side cuts as above |
| `334741-d8-M1-v42lp4/` | 334741 | ✅ GRADED | **4.036e-09** | 2026-10-08 | multi_agent: V42 + LP4 carry — new best (pred ~4.04). C/B 0.2043, wall max 118.4 s, 0 failures |
| `334643-d7-V42lp4-a1/` | 334643 | ✅ GRADED | **4.036e-09** | 2026-10-07 | nabid_nur: V42 + join products at Strassen level 4 — new best. Raw 1.965e-08, C/B 0.2043 (9 early-level MLPs), wall max 116.5 s, 0 failures |
| `334642-d7-V42lp4-a3/` | 334642 | ✅ GRADED | 4.051e-09 | 2026-10-07 | koushik_rudra: same file as 334643; C/B 0.2047 (15 early-level MLPs: grader spread comes from how many MLPs hit the per-worker warm-up schedule). Wall max 112.3 s, 0 failures |
| `334632-d7-V42rb-a2/` | 334632 | ✅ GRADED | 4.080e-09 | 2026-10-07 | multi_agent: V42 on the robust build (nominee). Raw 1.965e-08, C/B 0.2065, wall max 107.1 s, 0 failures |
| `334631-d7-V42-a2/` | 334631 | ✅ GRADED | 4.052e-09 | 2026-10-07 | multi_agent: V42 on L5 — new best. Raw 1.966e-08, C/B 0.2052, wall max 114.1 s, 0 failures |
| `334630-d7-V42rb-a1/` | 334630 | ✅ GRADED | 4.073e-09 | 2026-10-07 | nabid_nur: V42 on the robust build (nominee). Raw 1.965e-08, C/B 0.2064, wall max 110.6 s, 0 failures |
| `334629-d7-V42-a1/` | 334629 | ✅ GRADED | **4.045e-09** | 2026-10-07 | nabid_nur: V42 (LT + cross-neuron inputs) on L5 — new best; predicted 4.02–4.03. Raw 1.965e-08, C/B 0.2051, wall max 118.5 s, 0 failures |
| `334628-d7-V42rb-a3/` | 334628 | ✅ GRADED | 4.073e-09 | 2026-10-07 | koushik_rudra: V42 on the robust build (nominee). Raw 1.965e-08, C/B 0.2063, wall max 103.0 s, 0 failures |
| `334627-d7-V42-a3/` | 334627 | ✅ GRADED | **4.045e-09** | 2026-10-07 | koushik_rudra: V42 on L5 — new best; predicted 4.02–4.03. Raw 1.965e-08, C/B 0.2052, wall max 116.5 s, 0 failures |
| `334571-d7-A2-v41-lt-robust/` | 334571 | ✅ GRADED | 4.092e-09 | 2026-10-07 | multi_agent: V41 LT on the robust build (nominee). Raw 1.977e-08, C/B 0.2060, wall max 107.4 s, 0 failures |
| `334570-d7-A2-v41-lt/` | 334570 | ✅ GRADED | **4.063e-09** | 2026-10-07 | multi_agent: V41 LT on L5 + age gate 8 — new best. Raw 1.977e-08, C/B 0.2045, wall max 118.6 s, 0 failures |
| `334569-d7-A1-v41-lt-robust/` | 334569 | ✅ GRADED | 4.092e-09 | 2026-10-07 | nabid_nur: V41 LT on the robust build (nominee). Raw 1.977e-08, C/B 0.2060, wall max 108.0 s, 0 failures |
| `334568-d7-A1-v41-lt/` | 334568 | ✅ GRADED | **4.063e-09** | 2026-10-07 | nabid_nur: V41 LT on L5 + age gate 8 — new best. Raw 1.977e-08, C/B 0.2045, wall max 116.8 s, 0 failures |
| `334557-d7-K4-v41-lt-robust-ao7/` | 334557 | ✅ GRADED | 4.093e-09 | 2026-10-07 | koushik_rudra: V41 LT corrector on the robust build, age gate 7. Raw 1.995e-08, C/B 0.2041, wall max 106.7 s, 0 failures |
| `334556-d7-K3-v41-lt-repeat/` | 334556 | ✅ GRADED | **4.063e-09** | 2026-10-07 | koushik_rudra: V41 LT corrector (replaces GRU) on L5 + age gate 8 — **new best**. Raw 1.977e-08, C/B 0.2045, wall max 113.7 s, 0 failures |
| `334555-d7-K2-v41-lt-robust/` | 334555 | ✅ GRADED | 4.092e-09 | 2026-10-07 | koushik_rudra: V41 LT corrector on the robust lone-level-4 build (nominee). Raw 1.977e-08, C/B 0.2060, wall max 109.1 s, 0 failures |
| `334554-d7-K1-v41-lt/` | 334554 | ✅ GRADED | 0.0204 | 2026-10-07 | koushik_rudra: same file as 334556; **1 network over the 120 s wall limit** (119.7 s). C/B 0.2044 |
| `334393-d6-K5-allft-ao8/` | 334393 | ✅ GRADED | 4.133e-09 | 2026-10-06 | koushik_rudra: best build (lone L5 + age gate 8) on the account that had failed it; passed, but wall max 118.5 s (limit 120). Raw 2.012e-08, C/B 0.2044, 0 failures |
| `334355-d6-N3-rb-pair-nominee/` | 334355 | ✅ GRADED | 4.160e-09 | 2026-10-06 | nabid_nur: robust + 2-member corrector (nominee copy), wall max 105.8 s. Raw 2.023e-08, C/B 0.2046, 0 failures |
| `334354-d6-K4-rb-pair-nominee/` | 334354 | ✅ GRADED | 4.160e-09 | 2026-10-06 | koushik_rudra: robust + 2-member corrector (nominee copy), wall max 111.3 s. Raw 2.023e-08, C/B 0.2046, 0 failures |
| `334345-d6-N2-rb-lp2/` | 334345 | ✅ GRADED | 4.17e-09 | 2026-10-06 | nabid_nur: robust + join level 2 (wall max 105 s, safest). Raw 2.029e-08, C/B 0.2056, 0 failures |
| `334344-d6-M2-rb-pair/` | 334344 | ✅ GRADED | 4.16e-09 | 2026-10-06 | multi_agent: robust + 2-member corrector (best robust). Raw 2.023e-08, C/B 0.2058, 0 failures |
| `334343-d6-K3-rb-ageold2-8/` | 334343 | ✅ GRADED | 4.162e-09 | 2026-10-06 | koushik_rudra: robust + age gate 8. Raw 2.012e-08, C/B 0.2069, 0 failures |
| `334338-d6-K2-lic-robust-allft/` | 334338 | ✅ GRADED | 4.161e-09 | 2026-10-06 | koushik_rudra: robust licensed all-data build. Raw 2.03e-08, C/B 0.2051, 0 failures |
| `334329-d6-N1-allft-ageold2-8/` | 334329 | ✅ GRADED | 4.133e-09 | 2026-10-06 | nabid_nur: nested-tier age gate 8: neutral. Raw 2.012e-08, C/B 0.2055, 0 failures |
| `334328-d6-M1-allft-rfb3/` | 334328 | ✅ GRADED | 4.143e-09 | 2026-10-06 | multi_agent: D21 feedback rank 3: worse than rank 2. Raw 2.022e-08, C/B 0.2050, 0 failures |
| `334327-d6-K1-lic-v37-allft/` | 334327 | ✅ GRADED | 0.02995 | 2026-10-06 | koushik_rudra: the 4.133e-09 build: **2 networks over the 120 s wall limit** on a slow grader (identical build passed on the other accounts). Raw 0.02995, C/B 0.2359, 2 failures |
| `334282-d5-N10-lic-robust-allft/` | 334282 | ✅ GRADED | 4.161e-09 | 2026-10-05 | nabid_nur: robust licensed nominee (lone level 4), wall max 108.2 s. Raw 2.03e-08, C/B 0.2051, 0 failures |
| `334281-d5-M10-lic-robust-allft/` | 334281 | ✅ GRADED | 4.161e-09 | 2026-10-05 | multi_agent: robust licensed nominee (lone level 4), wall max 109.5 s. Raw 2.03e-08, C/B 0.2051, 0 failures |
| `334280-d5-M9-lic-v37-allft/` | 334280 | ✅ GRADED | 4.133e-09 | 2026-10-05 | multi_agent: licensed all-data corrector build (lone level 5). Raw 2.03e-08, C/B 0.2037, 0 failures |
| `334265-d5-N9-lic-v37-allft/` | 334265 | ✅ GRADED | 4.133e-09 | 2026-10-05 | nabid_nur: licensed V37 + join level 3 + rank 2 + **GRU fine-tuned on ~1000 MLPs** (held-out 0.913). **Best score**. Raw 2.03e-08, C/B 0.2037, 0 failures |
| `334261-d5-M8-lic-robust-l4lp3rfb2/` | 334261 | ✅ GRADED | 4.174e-09 | 2026-10-05 | multi_agent: robust licensed nominee (lone level 4). Raw 2.036e-08, C/B 0.2051, 0 failures |
| `334260-d5-N8-lic-v37lp3-rfb2/` | 334260 | ✅ GRADED | 4.149e-09 | 2026-10-05 | nabid_nur: licensed copy of the 334221 build. Raw 2.035e-08, C/B 0.2039, 0 failures |
| `334240-d5-N7-lic-robust-l4lp3rfb2/` | 334240 | ✅ GRADED | 4.188e-09 | 2026-10-05 | nabid_nur: robust nomination build: lone products at level 4 (wall median 101 s, max 113 s) + join level 3 + rank 2, MIT notice shipped. Raw 2.037e-08, C/B 0.2057, 0 failures |
| `334239-d5-M7-lic-v37lp3-rfb2/` | 334239 | ✅ GRADED | 4.145e-09 | 2026-10-05 | multi_agent: the 334221 build with 504aldo's MIT notice shipped (prize-eligible copy of the best). Raw 2.036e-08, C/B 0.2037, 0 failures |
| `334230-d5-N6-v37lp4-rfb2-ft33f/` | 334230 | ✅ GRADED | 0.01509 | 2026-10-05 | nabid_nur: join level 4 + rank 2: **1 MLP over the 120 s wall limit** (max 119.5 s on the rest), catastrophic score; level 4 is too slow on the grader. Raw 0.01509, C/B 0.2198, 1 failures |
| `334227-d5-M6-v37lp3-rfb2-ft33f/` | 334227 | ✅ GRADED | 4.145e-09 | 2026-10-05 | multi_agent: the 334221 build. Raw 2.036e-08, C/B 0.2037, 0 failures |
| `334221-d5-N5-v37lp3-rfb2-ft33f/` | 334221 | ✅ GRADED | 4.145e-09 | 2026-10-05 | nabid_nur: V37 + join level 3 + D21 feedback rank 2. **Best score**. Raw 2.036e-08, C/B 0.2037, 0 failures |
| `334220-d5-M5-v37lp3-rfb4-ft33f/` | 334220 | ✅ GRADED | 4.157e-09 | 2026-10-05 | multi_agent: V37 + join level 3 + D21 feedback rank 4. Raw 2.024e-08, C/B 0.2055, 0 failures |
| `334215-d5-N4-v37-rfb2-ft33f/` | 334215 | ✅ GRADED | 4.156e-09 | 2026-10-05 | nabid_nur: V37 + D21 feedback rank 2 (C/B -2.7%, GRU unchanged). Raw 2.036e-08, C/B 0.2042, 0 failures |
| `334213-d5-M4-v37-rfb4-ft33f/` | 334213 | ✅ GRADED | 4.166e-09 | 2026-10-05 | multi_agent: V37 + D21 feedback rank 4 (C/B -1.8%, GRU unchanged). Raw 2.022e-08, C/B 0.2061, 0 failures |
| `334209-d5-N3-v37-ft33i/` | 334209 | ✅ GRADED | 4.198e-09 | 2026-10-05 | nabid_nur: V37 + ft33i GRU (all 598 dumps): raw 1.992e-08 but C/B +0.5% (the corrector shifts the pruning). Raw 1.992e-08, C/B 0.2109, 0 failures |
| `334208-d5-M3-v37lp3-ft33f/` | 334208 | ✅ GRADED | 4.182e-09 | 2026-10-05 | multi_agent: V37 + join products at Strassen level 3 after the first 5 MLPs. Raw 1.999e-08, C/B 0.2093, 0 failures |
| `334205-d5-N2-v37-ft33f/` | 334205 | ✅ GRADED | 4.192e-09 | 2026-10-05 | nabid_nur: V37 + ft33f (same build as 334198). Raw 1.999e-08, C/B 0.2098, 0 failures |
| `334204-d5-M2-v37-ft33f/` | 334204 | ✅ GRADED | 4.192e-09 | 2026-10-05 | multi_agent: V37 + ft33f (same build as 334198). Raw 1.999e-08, C/B 0.2098, 0 failures |
| `334203-d5-N1-v36-ft33c-lone5/` | 334203 | ✅ GRADED | 4.222e-09 | 2026-10-05 | nabid_nur: V36 lone level 5 + ft33c (same build as 334182). Raw 1.998e-08, C/B 0.2113, 0 failures |
| `334202-d5-M1-v36-ft33c-lone5/` | 334202 | ✅ GRADED | 4.222e-09 | 2026-10-05 | multi_agent: V36 lone level 5 + ft33c (same build as 334182). Raw 1.998e-08, C/B 0.2113, 0 failures |
| `334198-d5-K10-v37-ft33f-lone5-lp2/` | 334198 | ✅ GRADED | 4.192e-09 | 2026-10-05 | koushik_rudra: V37 (join products at Strassen level 2 after the first 5 MLPs) + ft33f. Raw 1.999e-08, C/B 0.2098, 0 failures |
| `334188-d5-K9-v36-ft33f-lone5/` | 334188 | ✅ GRADED | 4.227e-09 | 2026-10-05 10:04 | koushik_rudra: as 334182 with the continued fine-tune ft33f (held-out 0.9165 on 53, 0.9067 on 143 unseen MLPs). Raw 2.001e-08, C/B 0.2113: same as 334182 within noise; residual max 0.376 s (first 5 MLPs), wall max 116.8 s |
| `334187-d5-K8-v36-ft33e-lone4/` | 334187 | ✅ GRADED | 4.285e-09 | 2026-10-05 09:49 | koushik_rudra: V36 lone level 4 + ft33e (held-out 0.920 on 53 MLPs). Raw 2.015e-08: worse than ft33c on the grader set, so a 53-MLP held-out gap of 0.2% is noise |
| `334182-d5-K7-v36-ft33c-lone5/` | 334182 | ✅ GRADED | **4.225e-09** | 2026-10-05 09:24 | koushik_rudra: V36 (V35 + cached Strassen quadrant views; bit-identical) + ft33c GRU + lone products at level 5. Raw 1.998e-08, C/B 0.2115; residual median 0.268 s, max 0.382 s (first MLPs); wall max 116.8 s (thin margin). **New best** |
| `334177-d5-K6-v35-ft33c-lone4/` | 334177 | ✅ GRADED | **4.255e-09** | 2026-10-05 08:46 | koushik_rudra: V35 (V34 + leaner Strassen helper: one-dict buffer fast path, cached slot views; bit-identical) + ft33c GRU + lone products at level 4. Raw 2.001e-08, C/B 0.2127; residual median 0.293 s (was 0.349) with the max 0.363 s on the first MLPs (cache warm-up). **New best** |
| `334176-d5-K5-v34-ft33c-lone3/` | 334176 | ✅ GRADED | 4.304e-09 | 2026-10-05 08:13 | koushik_rudra: V34 + GRU fine-tuned on 418 V34 dumps (held-out 0.9218) + lone level 3. Raw 2.000e-08, C/B 0.2153, residual max 0.368 s |
| `334170-d5-K4-v34-ft33pair/` | 334170 | ✅ GRADED | 4.392e-09 | 2026-10-05 07:36 | koushik_rudra: V34 + 2-member GRU fine-tuned on V34 features (held-out 0.9206). Raw 1.9996e-08 (best raw today) but C/B 0.2196: the second member's cost cancels its accuracy gain |
| `334168-d5-K3-v34-ft33a-lone3/` | 334168 | ✅ GRADED | **4.340e-09** | 2026-10-05 07:12 | koushik_rudra: V34 + fine-tuned GRU (0.9247) + join lone products at Strassen level 3. Raw 2.013e-08, C/B 0.2157 (−1.3%), residual max 0.364 s (+0.036), wall max 106 s. **New koushik_rudra best** |
| `334161-d5-K2-v34-ft33ep3/` | 334161 | ✅ GRADED | 4.381e-09 | 2026-10-05 06:34 | koushik_rudra: V34 + GRU fine-tuned on 142 V34 feature dumps (held-out 0.961 → 0.925). Raw 2.006e-08 (−3.4% vs 334146), C/B 0.2184; ties the account's previous best |
| `334146-d5-K1-v34-AB-e12/` | 334146 | ✅ GRADED | 4.534e-09 | 2026-10-05 05:33 | koushik_rudra: V34 = dead-ReLU pruning (transport + hub/old tier, live sizes 896/960), shared Strassen scratch (estimator peak 6.9 GB), dense join products, D21 feedback rank 8, leaf 8 + single e12 GRU (not retrained). Raw 2.076e-08, C/B 0.2184 (−7.4% vs V32), residual max 0.327 s, wall max 99.8 s, 0 failures. Telemetry run: the GRU only gives a 0.961 ratio on V34 features (0.922 on V32) |
| `334069-d4-N8-soup21-20/` | 334069 | ✅ GRADED | 4.664e-09 | 2026-10-04 22:25 | nabid_nur: pair of weight-averaged final-weight-8 members soup21 + soup20. Raw 1.971e-08 |
| `334070-d4-N9-pair17-21f/` | 334070 | ✅ GRADED | 4.677e-09 | 2026-10-04 22:25 | nabid_nur: pair 12-epoch s17 + final-weight-8 s21. Raw 1.977e-08 |
| `334071-d4-N10-soup21-s17/` | 334071 | ✅ GRADED | 4.672e-09 | 2026-10-04 22:25 | nabid_nur: pair soup21 + 12-epoch s17 (wall max 113.7 s). Raw 1.975e-08 |
| `334072-d4-M8-soup21-a0.94/` | 334072 | ✅ GRADED | 4.665e-09 | 2026-10-04 22:25 | multi_agent: single soup21, correction scaled 0.94. Raw 1.977e-08 |
| `334073-d4-M9-soup21-s18/` | 334073 | ✅ GRADED | 4.658e-09 | 2026-10-04 22:25 | multi_agent: pair soup21 + 12-epoch s18; ties the nabid_nur best. Raw 1.968e-08 |
| `334074-d4-M10-s17-a0.88/` | 334074 | ✅ GRADED | 4.678e-09 | 2026-10-04 22:25 | multi_agent: single 12-epoch s17 scaled 0.88. **Wall max 119.0 s, 1 s under the 120 s cap**. Raw 1.983e-08 |
| `334037-d4-N6-pair20-21f-a0.93/` | 334037 | ✅ GRADED | 4.666e-09 | 2026-10-04 19:43 | nabid_nur: pair s20 + s21 (final-weight-8), correction scaled by 0.93. Raw 1.972e-08 |
| `334040-d4-N7-pair18-21f-leaf16/` | 334040 | ✅ GRADED | 4.732e-09 | 2026-10-04 20:07 | nabid_nur: SAFE nomination candidate, the 334034 pair at leaf 16. Same raw (1.969e-08), cost +1.6 percent; wall max 90.9 s and residual max 0.312 s vs 111.1 s / 0.373 s at leaf 8 |
| `334036-d4-M7-single21f-a0.9/` | 334036 | ✅ GRADED | 4.665e-09 | 2026-10-04 19:42 | multi_agent: single final-weight-8 member s21 with its correction scaled by 0.9. Raw 1.978e-08 vs 1.981e-08 unscaled (334035): the held-out-fitted scale transfers to the public board |
| `334031-d4-M4-single21/` | 334031 | ✅ GRADED | 4.668e-09 | 2026-10-04 19:03 | multi_agent: single final-weight-8 member s21, epoch-8 checkpoint (held-out 0.9218). Raw 1.979e-08 |
| `334032-d4-M5-pair17-21-leaf16/` | 334032 | ✅ GRADED | 4.744e-09 | 2026-10-04 19:04 | multi_agent: SAFE variant, the 334030 pair at leaf 16. Same raw (1.974e-08), cost +1.6%, but more wall-time margin under load (see README for the numbers) |
| `334034-d4-N5-pair18-21f/` | 334034 | ✅ GRADED | 4.658e-09 | 2026-10-04 19:32 | nabid_nur: pair 12-epoch s18 + fully trained final-weight-8 s21 (held-out 0.9180). **Best nabid_nur score**. Raw 1.969e-08 |
| `334035-d4-M6-single21f/` | 334035 | ✅ GRADED | 4.674e-09 | 2026-10-04 19:32 | multi_agent: single fully trained final-weight-8 member s21 (held-out 0.9212). Raw 1.981e-08 |
| `334030-d4-N4-pair17-21/`      | 334030 | ✅ GRADED  | 4.670e-09    | 2026-10-04 19:03 | nabid_nur: pair 12-epoch s17 + final-weight-8 s21 (epoch-8 checkpoint), held-out 0.9180. Raw 1.974e-08: same as the other pairs within 0.1% on the public 50 |
| `334011-d4-N1-e12x2/`          | 334011 | ✅ GRADED  | **4.667e-09** | 2026-10-04 16:53 | nabid_nur: 2-member 12-epoch GRU ensemble (held-out 0.9187), V32 lone L2, leaf 8, first-call L5. Raw 1.972e-08. Best so far |
| `334012-d4-N2-e12x2-lam1/`     | 334012 | ✅ GRADED  | 4.687e-09    | 2026-10-04 16:53 | nabid_nur: as 334011 + lambda scale 1.00. Raw 1.981e-08 (+0.4%): the corrector is tuned to the default chain, so chain knobs hurt |
| `334013-d4-M1-e12x1/`          | 334013 | ✅ GRADED | **4.654e-09** | 2026-10-04 16:53 | multi_agent: single 12-epoch GRU member (held-out 0.9223), V32 lone L2, leaf 8, first-call L5. Raw 1.973e-08 (same as the pair on the public 50), cost 0.2359 x B. Best so far |
| `334014-d4-M2-e12x2-lam1-r192/` | 334014 | ✅ GRADED | 4.701e-09 | 2026-10-04 16:54 | multi_agent: 2-member 12-epoch ensemble + lambda 1.00 + nested rank 192. Raw 2.015e-08 (+2.2%) for cost −1.3%: worse |
| `334020-d4-N3-e12x3/`          | 334020 | ⚠️ GRADED  | 8.08e-02 | 2026-10-04 17:43 | nabid_nur: 3-member 12-epoch ensemble at leaf 8. **4 of 100 networks hit the time limits** (wall 108–120 s, residual 0.405 s) under today's grader load and fell back to zero. Lesson: each corrector member adds ~720 server round-trips; keep ≤2 members at leaf 8 |
| `334021-d4-M3-e12x2-r192/`     | 334021 | ✅ GRADED | 4.671e-09 | 2026-10-04 17:43 | multi_agent: 2-member 12-epoch ensemble + nested rank 192. Raw 2.002e-08 (+1.5%) for cost −1.3%: slightly worse than 334011, so rank 192 is out too |
| `333790-day3-N1-long3/`        | 333790 | ✅ GRADED  | **4.689e-09** | 2026-10-03 15:52 | nabid_nur: V32 leaf 8 + first-call L5 + 3-member 8-epoch CDF GRU ensemble (the 333605 recipe; grader is deterministic, same score). Best so far on this account |
| `333791-day3-N2-long2/`        | 333791 | ✅ GRADED  | **4.676e-09** | 2026-10-03 15:52 | nabid_nur: V32 leaf 8 + first-call L5 + 2-member 8-epoch CDF GRU ensemble. Same raw as 3 members (1.976e-08), one member less cost. Best so far |
| `333792-day3-M1-long2/`        | 333792 | ✅ GRADED | 4.676e-09 | 2026-10-03 15:53 | multi_agent: identical file to 333791 (2-member 8-epoch ensemble); identical score, confirming the grader is deterministic across accounts |
| `333793-day3-M2-long1/`        | 333793 | ✅ GRADED | 4.674e-09 | 2026-10-03 15:53 | multi_agent: single 8-epoch CDF GRU member (held-out 0.924). Raw 1.981e-08 (+0.3% vs 2 members), cost −0.3%: one or two members is the sweet spot |
| `333605-acct2-long3/` | 333605 | ✅ GRADED | 4.689e-09 | 2026-10-02 19:22 | multi_agent: V32 leaf 8 + first-call L5 + 3-member CDF GRU ensemble trained for 8 epochs (held-out 0.921). Raw 1.976e-08 |
| `333589-acct2-tanh3/`          | 333589 | ✅ GRADED | 4.734e-09 | 2026-10-02 17:03 | multi_agent: V32 leaf 8 + first-call L5 + 3-member tanh-gated GRU ensemble (held-out 0.935). Raw 2.000e-08 (tanh members worse than CDF's 1.983e-08), the cost knobs compensate |
| `333596-acct2-alldata3/`       | 333596 | ✅ GRADED | 4.729e-09 | 2026-10-02 18:02 | multi_agent: V32 leaf 8 + first-call L5 + 3-member CDF GRU ensemble trained on all 730 public MLPs (no holdout, 3 fixed epochs). Raw 1.992e-08: slightly worse than the early-stopped S1 members (1.983e-08) |
| `333578-sub14_S3-v32/`         | 333578 | ✅ GRADED  | **4.705e-09** | 2026-10-02 16:34 | **S3**: V32 with leaf 8 + first-call level 5 (both grader-verified) + the 3-member full-split GRU ensemble of S1 (held-out 0.925). Raw 1.983e-08, cost 0.2373 x B. Best so far |
| `333572-sub18_A2S2_leaf8-v32/` | 333572 | ✅ GRADED | 4.779e-09 | 2026-10-02 15:56 | multi_agent: S2 (5 members) with leaf 8. Worse than the 3-member 333566 (4.734e-09): extra members only add cost |
| `333571-sub13_S2-v32/`         | 333571 | ✅ GRADED  | 4.855e-09    | 2026-10-02 15:53 | **S2**: V32 (lone level 2, leaf 16) + 5-member GRU ensemble (3 x h64 + 2 x h96), 630 full-split MLPs, 100 mini held out at ratio 0.926. Same raw as S1 (1.984e-08) but +1% cost from the two extra members: ensembling is saturated at 3 |
| `333567-acct2-S1-first5/`      | 333567 | ✅ GRADED | 4.780e-09 | 2026-10-02 15:25 | multi_agent: S1 with the first predict of each worker at Strassen level 5 (V28_STRASSEN_FIRST=5): cost −0.5% vs S1, same raw; passed 100/100 |
| `333566-sub16_A2S1_leaf8-v32/` | 333566 | ✅ GRADED | 4.734e-09 | 2026-10-02 15:25 | multi_agent: S1 with smallest leaf 8 (cost 0.2388 x B); same raw as S1 (1.983e-08). Best score on that account |
| `333564-sub12_S1-v32/`         | 333564 | ✅ GRADED  | **4.804e-09** | 2026-10-02 15:22 | **S1**: V32 (lone level 2, leaf 16) + 3-member GRU ensemble (hidden 64) trained on 630 full-split MLPs, 100 mini held out at ratio 0.925. Raw 1.983e-08 (−7.0% vs V29). Best so far |
| `333557-acct2-v32-leaf8-gru-ens3/` | 333557 | ✅ GRADED | 4.855e-09 | 2026-10-02 14:40 | **multi_agent account**: 333531's recipe with smallest Strassen leaf 8 (cost 0.2388 x B, −1.2%), same raw 2.033e-08; residual stayed under the cap |
| `333531-v32-lone2-min16-gru-ens3/` | 333531 | ✅ GRADED | **4.913e-09** | 2026-10-02 11:48 | **V32**: V31 ensemble + Strassen pricing of the join's lone dense products (level cap 2, leaf 16). Same raw as 333530 (2.034e-08), cost 0.2416 x B (−5.5%). Best so far |
| `333530-v31-gru-ens3-mini/`    | 333530 | ✅ GRADED  | **5.199e-09** | 2026-10-02 11:44 | **V31 ensemble**: V29 + 3-member per-layer GRU corrector ensemble (CDF gates, hidden 48, early-stopped; trained on 80 mini MLPs, 20 held out at ratio 0.955). Raw 2.034e-08 (−4.6% vs V29), cost unchanged. Best so far |
| `333509-v31-gru-cdf-smoke5/`   | 333509 | ✅ GRADED  | 5.584e-09    | 2026-10-02 09:28 | V31 with a normal-CDF GRU (hidden 48) trained on only 20 mini MLPs (local held-out ratio 1.025): raw 2.193e-08, +2.8% worse than V29, matching the local held-out estimate |
| `333508-v31-gru-smoke4/`       | 333508 | ✅ GRADED  | **5.311e-09** | 2026-10-02 09:26 | **V31**: V29 + per-layer GRU corrector (tanh, hidden 48, trained on only 20 mini MLPs), model embedded, suite-shape gate + setup dry run. Raw 2.087e-08 (−2.2% vs V29), cost unchanged. First graded learned-corrector submission |
| `333489-v31-gru-smoke-failed/`  | 333489 | ❌ FAILED | — | 2026-10-02 08:44 | V31 pipeline test 1: V29 + GRU corrector (hidden 48, 20 mini MLPs) from gru_model.json. Smoke test failed: FLOPSCOPE_SERVER_ERROR |
| `333492-v31-gru-smoke2-failed/` | 333492 | ❌ FAILED | — | 2026-10-02 08:52 | V31 pipeline test 2 (defensive GRU step). Smoke test failed: FLOPSCOPE_SERVER_ERROR |
| `333497-v31-gru-smoke3-failed/` | 333497 | ❌ FAILED | — | 2026-10-02 09:02 | V31 pipeline test 3 (model embedded, contiguous readout). Smoke test failed: FLOPSCOPE_SERVER_ERROR |
| `333493-bisect-b1-hooks-only/` | 333493 | ✅ GRADED  | 5.420e-09    | 2026-10-02 08:56 | Bisection B1: V29 + per-layer feature-recording hooks only (GRU disabled). Raw identical to V29 |
| `333494-bisect-b2-load-only/`  | 333494 | ✅ GRADED  | 5.440e-09    | 2026-10-02 08:56 | Bisection B2: V29 + feature hooks + GRU model loaded in setup (step disabled). Grader-identical raw; the +0.4% is first-call Strassen-level scheduling, not the load |
| `333467-graded/`               | 333467 | ✅ GRADED  | 5.418e-09    | 2026-10-02 06:39:28 | V29 verbatim (504aldo, MIT) re-submitted from the `nabid_nur` account as the Phase 2 baseline; raw 2.133e-08, 0.2534 x B, grader kernel 62.5 s, residual 0.183 s mean |
| `333364-top-scored/`           | 333364 | ✅ GRADED  | **5.394e-09** | 2026-10-01 16:00:54 | V29 baseline (504aldo, MIT) + kappa4 lambda table scale 0.95→1.00 (mean raw -0.35% on 4 public mini-split MLPs) |
| `333330-graded/`               | 333330 | ✅ GRADED  | 5.406e-09    | 2026-10-01 11:11:03 | V29 + R_OLD2 192 cost trim |
| `333323-graded/`               | 333323 | ✅ GRADED  | 5.418e-09    | 2026-10-01 10:30:13 | K3 cumulant propagation V29 (504aldo MIT baseline) |
| `333177-graded/`               | 333177 | ✅ GRADED  | 9.950e-09    | 2026-09-30 17:22:57 | (no description provided) |
| `333363-failed-prohibited-file/` | 333363 | ❌ FAILED | — | 2026-10-01 15:56:44 | V29 baseline (504aldo, MIT) + kappa4 lambda table scale 0.95→1.00 (re-validated). Failure: "Prohibited file in submission" |
| `333166-failed-eval-error/`    | 333166 | ❌ FAILED | — | 2026-09-30 16:29:17 | (no description provided). Failure: "Evaluation error" |

Account note: the `nabid_nur` account appears on the public leaderboard under its team name **Hydrion-Labs** (rank 50 at 4.8e-09 on 2026-10-02 16:10 UTC); the `multi_agent` account (used from 14:40 UTC for the riskier cost variants, key supplied by the owner) is listed separately.
Account note: submissions up to #333364 were graded under the `koushik_rudra` participant;
#333467 onwards are graded under `nabid_nur` (the API key used from 2026-10-02). The grader is
deterministic, so an identical estimator gives an identical adjusted score on either account.

## Folder layout (per submission)

Each submission folder contains:

- `README.md` — human-readable context: what was submitted, what the score was,
  what the description said, what the grading report tells us.
- `submission-report.json` — the full grading evaluation JSON, exactly the file
  AICrowd's "Download report.json" button produces. Contains:
  - `schema_version`, `session_id`, `submission_id`, `state`, `phase`
  - `started_at`, `updated_at`, `completed_at`
  - `config_snapshot` — `n_mlps`, `depth`, `width`, `flop_budget`
  - `progress` — `total_mlps`, `mlps_completed`, `mlps_in_flight`, `mlps_failed`, `pct_complete`
  - `workers` — per-worker state
  - `smoke_test_result` — pass/fail, duration, worker_passes, errors
  - `results.per_mlp[]` — per-MLP telemetry: `mlp_index`, `mlp_name`, `state`,
    `telemetry.flops_used`, `telemetry.participant_predict_wall_s`,
    `telemetry.flopscope_server_kernel_wall_s`, `budget_exhausted`, `time_exhausted`,
    `error_code`, `error_message`, `traceback_index`
- `submission-metadata.json` — submission ID, status, score (primary + secondary),
  challenge ID, round ID, created_at, grading_message (from AICrowd Rails API),
  plus GraphQL-derived fields (participant, round, team, description).

The grading reports for the two FAILED submissions are much shorter — they
record the smoke-test failure that aborted the run before any MLPs were scored.
