# SBT EDA / GSR research evidence audit (2026-11-03)

**Status:** Initial independent, citation-level verification. NOT a completed LeapSpace systematic review and NOT a finished medical / electronics validation. Owner-directed handoff was reviewed from `tamaspota/TRE/docs/SBT_LEAPSPACE_HANDOFF_2026-11-03.md`.

## Scope and provenance

- Four research prompts Q1-Q4 are prepared in `research/LEAPSPACE_BRIEF_2026-11-03.md`, but no accepted SBT-specific LeapSpace result with full bibliography, methods, data and expert review was located in the SBT repository or SBT Drive/03 at this checkpoint.
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
