# SBT EDA / GSR research evidence audit (2026-11-03)

**Status:** Initial source-level verification PLUS returned 2026-11-03 LeapSpace Q1 PDF. Research output received, **partially independently checked, not yet scientifically accepted**. No completed electronics validation. Owner-directed handoff was reviewed from `tamaspota/TRE/docs/SBT_LEAPSPACE_HANDOFF_2026-11-03.md`.

## 2026-11-03 evening update: Q1 LeapSpace report delivered (source-audit stage)

**Original evidence:** [14-page 2026-11-03 LeapSpace Q1 PDF](https://drive.google.com/file/d/12q_RhdfrQzGpxOQ2Hcd0noWhSUeH7EWr/view?usp=drivesdk) in [SBT/03 / Leadspace](https://drive.google.com/drive/folders/1a_X07p0qbQVS43aQKWwnH-vdXhkrKm7c), from an owner-executed run. This is raw research output and is retained **in Drive, not copied to public GitHub**. Local PDF showed 14 pages, creation 2026-11-03 20:27:47 UTC, 46 numbered bibliographic references, and DOI URLs. The original task prompt matches the 494-character `research/LEAPSPACE_Q1_RUN_2026-11-03.md` brief.

**Reported high-level conclusion:** In the report, finger/palm ranks best as the reference site; textile finger electrodes / proposed glove second; dry wrist electrodes third for fidelity-first use. This is a review recommendation, not a comparison of a finished SBT glove versus an SBT wrist device.

**Independently verified anchors (selective; publisher, university or PubMed bibliographic records/abstracts):**

| PDF ref | Study / DOI | Independent check and engineering meaning | Important limit |
| --- | --- | --- | --- |
| [1] | Tsiamyrtzis et al. (2016), `10.1145/2858036.2858536` | University record supports n=23 startle-based EDA site comparison, finger/palm good small-response detectability | Site/method specifics need full methods; not finished SBT prototype evidence |
| [7] | van der Mee et al. (2021), `10.1016/j.ijpsycho.2021.08.003` | PubMed confirms 112 adults / 26 conditions, wrist-palm tonic r=0.31 and ns.SCR r=0.42 | Modest correlation; wrist not interchangeable with palm |
| [14] | Haddad et al. (2018), `10.3390/bios8030079` | PubMed/MDPI confirms dry Ag/AgCl textile EDA on **fingers/hand**, cotton best with correlation 0.913 +/- 0.041 | Not proof of a complete movable glove; actual geometry/fit needs testing |
| [15] | Janka et al. (2022), `10.1109/SEGAH54908.2022.9978571` | Tampere University describes textile **finger** electrode comparison with commercial Ag/AgCl | Glove/sock integration is stated as **future work**, not tested finished glove equivalence |
| [25] | Veeturi et al., 2025 IEEE BSN / 2026 publication, `10.1109/BSN66969.2025.11337617` | PubMed reports a 10-adult mobile EDA circuit comparison with BIOPAC; first 5 gel, next 5 dry textile | Different electrode material groups, limited sample; not direct 3-form-factor design comparison |

**Acceptance check vs user Q1 contract:**

- **PASS:** Relevant 14-page research output received and retained on the designated SBT Drive; proposed ranking, comparative table, reference list and qualitative bench/volunteer protocol present.
- **PARTIAL:** Six-digit reference identifiers [1]–[46] and DOI strings appear at the end, but authorship/DOI/method verification for **10+ specifically relevant primary trials** has not been completed. In many table rows N is expressly `Not surfaced`. The report itself says a genuinely DOI-verified 10+ study matrix cannot be reconstructed from the material, despite the later reference list.
- **PARTIAL:** Textile EDA finger studies provide evidence of feasibility but **not** a controlled finished glove vs palm vs wrist benchmark. Some included works concern ECG, EMG, generic biopotentials or reviews: e.g., report references [5], [17], [19], [21], [39], [44]. These cannot be counted as direct EDA form-factor validation.
- **NOT MET:** Numeric go/no-go thresholds are **not specified**. Terms like "low drift", "materially below", "acceptable agreement" are not testable pass/fail criteria until units, limits, window lengths and reference comparators are fixed in a signed plan.
- **UNVERIFIED:** PDF bibliographic completeness, reference-to-claim mapping and original paper full texts for all 46 references. The LeapSpace PDF's own `High` confidence for a ranking must not be upgraded to project `validated` status without independent review.
- **NEXT GATE:** Resolve at least one glove-specific controlled study if available, paper methods, and bench-only resistor/conductance specification with predefined bias, noise, drift, contact-loss and recovery thresholds, then decide whether the wearable or glove form merits prototyping. Human tests remain blocked on safety/privacy review.

**Project status after this update:** `LS-SBT-Q1-20261103-01 = RESULT_RECEIVED / PARTIAL_SOURCE_REVIEW / ACCEPTANCE_PENDING`; Q2–Q4 not marked run. The historical initial `Retrieved references: 0` attempt remains a separate failed run, not the successful owner-supplied 14-page Q1 output.

## Q2 update – 2026-11-03 22:01: Analog-front-end LeapSpace report received

**Source:** [17-page LeapSpace EDA/GSR AFE PDF](https://drive.google.com/file/d/1KKNjZOZKnmPfxfRne-vsvCK1_udLJ-sT/view?usp=drivesdk) in the designated SBT Drive/03/Leadspace folder. Task `LS-SBT-Q2-20261103-01 = RESULT_RECEIVED / INITIAL_DOI_SPOTCHECK / SCIENTIFIC_ACCEPTANCE_PENDING`.

**Report observations (not validated engineering design):**
- Fixed-voltage DC (~0.5 V) is the conventional EDA baseline under cited methodological guidance; AC/polarity reversal is a research candidate to mitigate polarization drift. It is **not** shown to be universally superior on matched power, noise or complexity.
- Constant-current vs fixed-voltage head-to-head wearable evidence with matched calibrated references was not identified in the report.
- ADC/reference specifications, input protection, isolation, leakage-current limits, contact detection, low-frequency drift and complete BLE power remain underreported; journal reports cannot substitute for electrical safety design review.
- Bench matrix proposed: 10 kΩ–1 MΩ calibrated resistor equivalents, RC-interface emulation, 5-min noise windows, 30–60-min drift windows and 3–5 repeats per load. A <=1% pure-resistance error goal is **proposed only**, not an SBT-approved acceptance standard or tested measurement. Limits for noise, drift, timing and safety still lack quantified acceptance and uncertainty budget.

**Source-level independent spot checks:** DOI [10.3390/s25123603](https://doi.org/10.3390/s25123603) (Romero-Ante et al. 2025, N=10, wearable AC EDA feasibility), DOI [10.1111/psyp.12803](https://doi.org/10.1111/psyp.12803) (Pabst et al., 2017 AC/DC comparison), DOI [10.1016/j.measurement.2013.06.024](https://doi.org/10.1016/j.measurement.2013.06.024) (Ogorevc et al. 2013 metrological uncertainty study). DOI metadata/abstract checked independently; full methods of all other citations **not verified**.

**Detected reference defect:** bibliography entry #20 states year **2099** for Frisanco et al., DOI [10.1038/s41598-022-26016-1](https://doi.org/10.1038/s41598-022-26016-1), but the publisher says **14 December 2022**. The cited paper's VR study includes skin conductance as an outcome, but it is not evidence for GSR AFE circuit metrology. This is a concrete citation quality warning; further source audit mandatory.

**Updated gates:** Q2 report received, only partial source review. Q5 metrology research prepared for quantitative R/RC bench acceptance; Q7 safety/regulatory research prepared for intended-use and current/fault questions. See `research/LEAPSPACE_RESEARCH_QUEUE_2026-11-03.md`. No hardware, electronics tests, medical claims, BLE compatibility or ZYTO integration validated.

## Scope and provenance

- Four research prompts Q1-Q4 are defined in `research/LEAPSPACE_BRIEF_2026-11-03.md`. At the **initial pre-Q1-return checkpoint**, no SBT-specific research PDF was present. A Q1 report was subsequently deposited under SBT Drive/03/Leadspace and is now linked in the dated update below; it remains only partially validated.
- **One owner-reported LeapSpace Q1 run: `Retrieved references: 0`**. It is a retrieval failure, not a negative scientific result. The search scope (`Project only` vs external scholarly corpus) is unresolved. Do not cite it as evidence.
- Nine new screenshot attachments were supplied in the ongoing chat on 2026-11-03, but their individual contents were not exposed as accessible file bytes in the connected conversation-file list. Their claims are **pending review**, not incorporated as verified findings. A source-side export or accessible reattachment is required to cite exact screen content.
- This file does **not** imply that LeapSpace executed a full literature study or LGW completed code/hardware work.

## Verified literature anchor matrix

| ID | Source | Primary vs guidance | What the accessible abstract/full text actually supports | Constraints / next verification |
| --- | --- | --- | --- | --- |
| E01 | Boucsein et al. (2012). DOI [10.1111/j.1469-8986.2012.01384.x](https://doi.org/10.1111/j.1469-8986.2012.01384.x); [PubMed](https://pubmed.ncbi.nlm.nih.gov/22680988/) | Consensus methodological **guideline**, not a new comparative trial | Standard descriptions of EDA methods, palmar electrode conventions, constant-voltage DC approach, calibration, applied voltage/current, electrode geometry, contact/gel, baseline, artifacts, recording conditions. It notes that dry electrodes can exhibit unstable drift as skin hydration evolves. | Establish reference measurement method and protocol before hardware decisions. Guideline date 2012: newer literature may qualify it. |
| E02 | Poh, Swenson & Picard (2010). DOI [10.1109/TBME.2009.2038487](https://doi.org/10.1109/TBME.2009.2038487); [PubMed](https://pubmed.ncbi.nlm.nih.gov/20172811/) | Original wearable sensor experiment | Describes a wrist/forearm-worn EDA device and comparison with a reference EDA system at palmar and distal forearm sites under multiple stressors; supports feasibility of a wearable EDA signal, NOT wrist equivalence in every operating condition. | Full paper methods, actual subject counts, calibration and noise details to be extracted before adopting circuit or performance criteria. |
| E03 | van der Mee et al. (2021). DOI [10.1016/j.ijpsycho.2021.08.003](https://doi.org/10.1016/j.ijpsycho.2021.08.003); [PubMed](https://pubmed.ncbi.nlm.nih.gov/34418464/) | Original **112-adult** controlled study (26 conditions) | Dry-wrist vs wet-palm EDA showed directionally similar responses but **modest** mean within-subject correlations (SCL r=0.31, nonspecific SCR r=0.42); wrist SCL and response frequency were lower. It supports wrist measurement as potentially useful in ambulatory research, NOT interchangeability with palmar EDA. | Lab conditions and devices differ from planned glove/wrist design; no clinical-diagnostic claim. Independent wearable vs palmar acceptance threshold not yet defined. |
| E04 | Kong et al. (2024). DOI [10.1016/j.compbiomed.2024.109139](https://doi.org/10.1016/j.compbiomed.2024.109139); [PubMed](https://pubmed.ncbi.nlm.nih.gov/39270456/) | Original algorithm paper, **follow-up notice** | Research concerns detection of EDA motion/noise artifacts by a 1D U-Net. | **2026-10-15 Editor's Note** exists: [DOI 10.1016/j.compbiomed.2026.111985](https://doi.org/10.1016/j.compbiomed.2026.111985) ([PubMed](https://pubmed.ncbi.nlm.nih.gov/42855346/)). Full text and reason of note NOT verified. Do NOT treat implementation/performance claims as accepted or train a model based on it until clarified. |

**Source-verification method:** consulted original journal/publisher listings and PubMed citation records on 2026-11-03. Direct PDF full-text analysis of E02-E04 and 2026 Editor's Note is not complete. DOI existence verification is not equivalent to reproducing measured results.

## Unresolved evidence gaps and priority

| Gate | Status | Smallest required evidence / acceptance |
| --- | --- | --- |
| P0: LeapSpace exact research result & source trace | **BLOCKED** | Export Q1 result, query and search scope; if it again yields zero sources, repeat via normal scholarly corpus and save canonical DOI/abstract/method metadata |
| P1: Glove vs wrist vs palm | **OPEN** | Identify at least one controlled glove / textile-contact primary study, and tabulate electrode material, skin site, contact pressure, sample size, protocol, artifact metrics and comparison instrument. If no reliable glove study, mark `INSUFFICIENT EVIDENCE` |
| P2: Electrical measurement specification | **OPEN** | Define excitation and current limits from documented safety engineering; bench-only first with reference resistors/conductances, battery/charger isolation, reference ADC, calibration curve, drift and noise |
| P3: Wearable motion, contact and between-user variability | **OPEN** | Pre-register raw timestamped signals, dropout/contact-lost flags, movement test cases, and reference palmar measurements; explicit predefined go/no-go thresholds and consent |
| P4: Software/MVP | **SPEC ONLY** | Existing `prototype/simulated_gsr.py` synthetic generator is not physical sensor evidence. Simulator-to-mobile demo can be built without internet backend; real BLE/phone functionality requires bench device and app tests |
| P5: ZYTO/proprietary interface rights | **UNVERIFIED** | Customer/Adri confirms code ownership, licensing and API/SDK availability. Do not reverse engineer or claim current ZYTO compatibility |
| P6: Commercial pilot | **UNVERIFIED** | Record one specific user problem, decision maker, objective success metric, whether willing to pay, and approved scope/budget; no confirmed order or fixed-price claim |
| P7: Regulatory/ethical scope | **OPEN** | Decide intended use (non-medical research/wellness vs medical) before human work or claims; expert safety/privacy/regulatory review |
| P8: LGW executor evidence | **NOT VERIFIED** | Verify request ID, permission, branch/commit, run logs and test results in local-gpu-helper. User states LGW is working on SBT, which is not completion evidence |
| P9: Chat screenshots | **PENDING READABLE SOURCE** | Nine screenshot items referred by owner in chat. No extracted claims registered without accessible image or reliable source text |

## Immediate minimal validation proposal (NOT human-use approval)

1. **Bench reference:** electrically simulate a set of known resistances/skin conductances before attaching electrodes to a person.
2. **Measurement contract:** require raw microSiemens values, timestamp, sample ID, contact flag, calibration/version metadata and explicit `SIMULATED` vs `MEASURED` provenance.
3. **Repeatability plan:** determine allowable bias/noise/drift after measuring reference sources; numerical thresholds to be agreed **before** tests, not invented now.
4. **Physical form:** compare hand/finger first as conventional benchmark, wrist as research-supported alternative with reduced/altered response, glove only when contact evidence exists. This is a test ordering **inference**, not a final design choice.
5. **Customer gate:** identify actual workflow and willingness to fund a small feasibility assessment before committing to manufacturing or full app development.

## Separation of responsibilities / latest user direction

- **SBT stays a separate product/project and the canonical technical GitHub repository** `tamaspota/SBT`.
- **TRE ChatGPT conversation coordinates the cross-project research review, bounded engineering task packets and commercial validation** as explicitly requested by the owner in the latest message. This does **not** merge SBT into TRE.
- **LGW** may perform bounded approved development/research as an executor; task existence and outputs must be validated by logs/commits. No new LGW START is implied.
- SBT Drive/03 remains the partner-safe working area; SBT Drive/01, /02 and /04 contain personal records and must not be forwarded to LeapSpace or public GitHub.

## Review status

**MAYBE / evidence-gathering**. A mechanically plausible non-diagnostic GSR sensor concept exists, and independent wrist-vs-palm studies exist. There is insufficient evidence for wrist/glove performance equivalence, hardware safety, ZYTO interoperability, completed LeapSpace research or a paying SBT pilot.
