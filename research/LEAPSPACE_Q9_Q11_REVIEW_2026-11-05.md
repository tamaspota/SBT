# SBT – LeapSpace Q9–Q11 receipt, review and research gate — 2026-11-05

**Status:** Delivered and content-reviewed, not methodologically/source accepted. The three reports are from the user's manual LeapSpace runs, archived in the existing SBT Drive/03/Leadspace research folder. **The broad planned Q1–Q11 Deep Research campaign is complete as source collection**; this is not completed bench/hardware, regulatory or algorithm validation. The 12 PDF files cover 11 question IDs, with Q5 duplicated and Q4 replaced by Q4-R. Provider's unusual-activity restriction was reported before and is not evidence that the user used automation.

## New results and source-side claims

| Question | Original PDF (Drive) | What the report supports at synthesis level | What remains unproven |
| --- | --- | --- | --- |
| **Q9** – motion/contact artefacts | [Electrodermal activity artifact measurement](https://drive.google.com/file/d/1hGfSL-0aKVym78WZjmuVTum6A8XVQZ6R/view) (2026-11-05, 19-page exported report) | Differentiates *invalid signal segments*, *false/missed SCR events* and *contact loss*. Reports published approaches using manually labeled/moving-hand segments and sleep/PSG comparators. Quality flags and labels by ground-truth strength are indicated. | The report explicitly could **not** identify a complete cross-site wrist/palm/finger DOI+N+reference+movement+sampling matrix with verified event-level false/missed SCR rates. Reported example segment or sleep/wake classification accuracy is **not SCR event-level false-positive accuracy**; DOI/statistics not independently verified. |
| **Q10** – EU safety/regulatory boundary | [Regulatory compliance for wearable health devices](https://drive.google.com/file/d/17wXd5AbGCziWYIqmreh_GyPlFVtuyJz3/view) (2026-11-05, 19-page exported report) | Identifies a decision fork by **intended purpose/claims**: nonmedical research/wellness vs medical purpose; potential RED/RF/EMC, batteries, restricted materials and GDPR data controls alongside possible MDR qualification. | The report itself **does not deliver the full exact article/annex mappings, current harmonized EN/IEC standard editions/OJEU status or authoritative official URLs** for every law/standard. This is not a classification, certification or safe current limit. Device design and intended-use statement must be frozen first, then legal/electrical safety specialists check official sources. |
| **Q11** – SCL/SCR software decomposition | [Electrodermal activity signal-processing algorithms](https://drive.google.com/file/d/1j6bOfoPY6FUe35rw6zrGkTElxUHfxbNG/view) (2026-11-05, 16-page exported report) | Reviews Ledalab-style CDA/DDA, cvxEDA, SparsEDA, Bayesian/state-space and learned models. Recommends preserving **raw EDA and time/quality metadata**, then optional offline decomposition with explicit uncertainty and no clinical interpretation. | No common head-to-head event-level mobile benchmark with missed SCR, false SCR, delay, battery/CPU and independent physiological ground truth; open-source code reproducibility not fully established. The described results are secondary report claims, not an accepted SBT algorithm choice. |

**Evidence grading:** `REPORT_RECEIVED / CONTENT_REVIEWED / PRIMARY_DOI_METHOD_AUDIT_OPEN` for Q9–Q11. Previous partial primary source checks exist for Q1, Q2, Q4-R, Q8, but those checks alone do not imply full program signoff.

## Current 12-PDF archive (do not mirror copyrighted full reports into the public repository)

- Q1: https://drive.google.com/file/d/12q_RhdfrQzGpxOQ2Hcd0noWhSUeH7EWr/view
- Q2: https://drive.google.com/file/d/1KKNjZOZKnmPfxfRne-vsvCK1_udLJ-sT/view
- Q3: https://drive.google.com/file/d/1GC40Ul-DkzL2Ho5TqMjfpQnlhOSkg9Wt/view
- Q4-R: https://drive.google.com/file/d/1VAcpQh8jITp01oSUaZwF6MuxLJK1EUDO/view
- Q5a: https://drive.google.com/file/d/1OhxtHEvJpv6SwtTaAh8krecjjcT7SrdW/view
- Q5b: https://drive.google.com/file/d/1CdzFYiswRqOrgmF_Y0CoplivzkVoX4Nm/view
- Q6: https://drive.google.com/file/d/1mgRIVGUoEWGauDK976oTUPQ1ejOth9mv/view
- Q7: https://drive.google.com/file/d/1kh6z9VEtyfPobOTXzWMuyaw8_m8xppCU/view
- Q8: https://drive.google.com/file/d/1x_ZXhDxgN5rpOwNG1Fjl8SSUnA-a82gU/view
- Q9: https://drive.google.com/file/d/1hGfSL-0aKVym78WZjmuVTum6A8XVQZ6R/view
- Q10: https://drive.google.com/file/d/17wXd5AbGCziWYIqmreh_GyPlFVtuyJz3/view
- Q11: https://drive.google.com/file/d/1j6bOfoPY6FUe35rw6zrGkTElxUHfxbNG/view

## Recommendation: stop broad Deep Research; work through measurable engineering gates

1. **G0 / Pilot intended use:** Write a single sentence describing **non-diagnostic** sensor purpose and ask Adri/Sebestény Tamás what exact real-world pain, measurable deliverable, budget/willingness to pay and approval would make a bench feasibility pilot valuable. No external email or business commitment without owner approval.
2. **G1 / Software-only reference fixture:** Bounded LGW task already specified in [LGW_BENCH_SOFTWARE_TASK_2026-11-05.md](../docs/LGW_BENCH_SOFTWARE_TASK_2026-11-05.md), **NOT DISPATCHED**. Implement/test resistance-to-conductance simulation and raw telemetry/quality flags as a deterministic local harness (without any human measurements).
3. **G2 / Bench metrology:** Adopt or amend [GSR_BENCH_VALIDATION_DRAFT_2026-11-05.md](../docs/GSR_BENCH_VALIDATION_DRAFT_2026-11-05.md) with traceable resistor/reference-meter uncertainty, defined gain/noise/drift pass/fail limits, and engineer-reviewed excitation/current protections. Only then evaluate a physical front end on passive references. Numeric criteria in draft are **proposed**, not approved.
4. **G3 / Raw-first mobile data model:** Implement loss/reconnect/quality flags and on-device storage of raw µS and monotonic time. Defer cvxEDA/SparsEDA selection and learned models until benchmark metrics and clean data exist. Simulation is not a working BLE/mobile product.
5. **G4 / Glove/wrist human safety:** No testing on humans until a documented electrical safety and privacy assessment. Industrialization/CE, medical uses, ZYTO integration and proprietary protocols require their own approval and evidence.

## Remaining targeted evidence tasks without further LeapSpace

- For Q9: select original primary controlled artifact study and verify DOI, N, labels, setup and event confusion matrix **if the future device's use case requires event-level SCR analysis**; otherwise implement honest invalid-segment flags and defer full SCR event validation.
- For Q10: obtain official EUR-Lex RED/MDR/RoHS/Battery/GDPR texts, applicable latest OJEU/harmonized standards list, and product-specific intended-use/regulatory assessment. This is a legal/engineering compliance gate, not a general AI literature search.
- For Q11: choose one reproducible offline baseline only after calibration/raw data contract, validate against labeled synthetic and controlled reference data, then profile a target Android/iOS phone. No need to select a model now.

**Decision:** `NO_ADDITIONAL_GENERAL_LEAPSPACE_RUN_NEEDED_FOR_BENCH_MVP`. Further research only if a scoped test, specialist regulatory review, manufacturer question or customer pilot gate exposes an explicit blocker.
