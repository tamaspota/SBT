# SBT – LeapSpace research queue (2026-11-03)

**Owner:** Póta Tamás. **Project:** standalone SBT. **Technical record:** `tamaspota/SBT`. **Partner-facing working area:** SBT Drive/03. **Research-output archive:** https://drive.google.com/drive/folders/1a_X07p0qbQVS43aQKWwnH-vdXhkrKm7c

## Execution rules

- Run **one** LeapSpace Deep Research job at a time, when convenient. No background execution/automation has been set up.
- Use a **normal, non-temporary conversation**, enable `Deep research`, and select external literature search rather than `Project only` if those modes conflict.
- Copy **only the exact English prompt** of the desired task. Each prompt is under the observed 500-character input limit.
- Export full PDF with bibliography to the existing SBT research archive, keeping the original title/date. Add the Drive link when reporting completion. No project-only source list or claims of finished research from prompt creation.
- The research tool is a literature synthesis system, **not an electronics design approval or a medical certification authority**. Independently check primary papers/standards, DOI, methods, N and quantitative results; mark conflicts. No proprietary ZYTO data or personal medical files in LeapSpace.
- Record each run as `PREPARED` → `RESULT_RECEIVED` → `SOURCE_CHECKED_PARTIAL` → `SCIENTIFICALLY_ACCEPTED` only after evidence review. Stop/restrict use if the provider reports quota/rate-limit constraints; no attempts to evade them.

## Status at creation

| ID | Status | Output |
| --- | --- | --- |
| Q1 | `RESULT_RECEIVED / PARTIAL_SOURCE_REVIEW` | [Electrode comparison, 14-page PDF](https://drive.google.com/file/d/12q_RhdfrQzGpxOQ2Hcd0noWhSUeH7EWr/view) |
| Q2 | `RESULT_RECEIVED / INITIAL_DOI_SPOTCHECK / ACCEPTANCE_PENDING` | [EDA/GSR AFE, 17-page PDF](https://drive.google.com/file/d/1KKNjZOZKnmPfxfRne-vsvCK1_udLJ-sT/view) |
| Q3–Q7 | `PREPARED / NOT_SUBMITTED` | Exact prompts below |

## Prepared prompts (copy individually)

### Q3 — EDA-jel értelmezhetősége és határai [P1]

**Status:** `PREPARED / NOT_SUBMITTED`. **Focus:** Raw EDA signals vs stress/disease inference. **Length:** 458 characters.

> Review primary studies on what raw wearable EDA/GSR can validly measure or infer. Compare tonic SCL, phasic SCR, stress/arousal estimates, motion artifacts, temperature and individual baseline effects. Report DOI, sample size, reference methods, error rates, negative findings and reproducibility. Distinguish physiological observation from diagnosis; identify unsupported disease, organ and nutrient claims. Propose non-diagnostic software reporting limits.

**Required acceptance:** Source table with verified bibliographic identities, citations and methods; explicitly state gaps, negative evidence and uncertainties; compare against SBT Q1/Q2. No medical diagnosis claims or assertions that a proposed design has passed electrical safety testing.

### Q4 — Textilkesztyű, érintkezés és mozgás [P1]

**Status:** `PREPARED / NOT_SUBMITTED`. **Focus:** Glove-specific evidence rather than extrapolating finger sites. **Length:** 446 characters.

> Find primary EDA/GSR studies directly testing textile finger or glove electrodes against Ag/AgCl reference sensors. Compare material, electrode size/spacing, contact pressure, hydration, hand motion, fit and repeatability. Verify DOI, sample size and actual glove vs finger-only methodology; report negative findings. Design a bench contact fixture and a proposed volunteer comparison with measurable metrics, pending safety and privacy approval.

**Required acceptance:** Source table with verified bibliographic identities, citations and methods; explicitly state gaps, negative evidence and uncertainties; compare against SBT Q1/Q2. No medical diagnosis claims or assertions that a proposed design has passed electrical safety testing.

### Q5 — Mérőlabor: referenciaellenállás és RC-phantom [P1]

**Status:** `PREPARED / NOT_SUBMITTED`. **Focus:** Quantitative bench calibration with prior thresholds. **Length:** 477 characters.

> Find primary EDA/GSR metrology papers on calibrated-resistor and RC skin-electrode phantoms. Compare constant-voltage DC, constant-current DC and AC/polarity-reversal front ends on accuracy, noise, drift, polarization, contact loss and response time. Verify DOI and experimental methods; distinguish published limits from proposed targets. Produce a reproducible bench-only test matrix with reference tolerances, sample rates, durations and go/no-go thresholds. No human tests.

**Required acceptance:** Source table with verified bibliographic identities, citations and methods; explicitly state gaps, negative evidence and uncertainties; compare against SBT Q1/Q2. No medical diagnosis claims or assertions that a proposed design has passed electrical safety testing.

### Q6 — BLE, Android/iOS és adatminőség [P2]

**Status:** `PREPARED / NOT_SUBMITTED`. **Focus:** Data model, timestamps, dropouts and offline user consent. **Length:** 454 characters.

> Review evidence and official Bluetooth, Android and iOS documentation for reliable BLE transport of wearable EDA/GSR data. Compare GATT profiles, timestamps, sequence numbers, packet loss, reconnection, background restrictions, power and offline storage. Propose a minimal cross-platform phone app data contract and test matrix with measurable accuracy, gap and battery criteria. Cite primary technical docs and studies; mark unverified interoperability.

**Required acceptance:** Source table with verified bibliographic identities, citations and methods; explicitly state gaps, negative evidence and uncertainties; compare against SBT Q1/Q2. No medical diagnosis claims or assertions that a proposed design has passed electrical safety testing.

### Q7 — Elektromos biztonság, EU RED/MDR és adatvédelem [P1]

**Status:** `PREPARED / NOT_SUBMITTED`. **Focus:** Intended-use and compliance decisions, not certification. **Length:** 473 characters.

> Assess EU requirements for a battery-powered BLE skin-conductance research/wellness wearable, contrasting non-medical intended use with possible medical device claims. Use official EU MDR, RED, EMC and privacy sources plus relevant IEC safety standards. Identify when each rule applies, skin-contact current/fault risks, charging isolation and required test evidence. Deliver a compliance decision tree and unresolved questions, not certification or invented safety limits.

**Required acceptance:** Source table with verified bibliographic identities, citations and methods; explicitly state gaps, negative evidence and uncertainties; compare against SBT Q1/Q2. No medical diagnosis claims or assertions that a proposed design has passed electrical safety testing.

## Integration gates

1. Q3 limits what the planned mobile app may claim from raw EDA signals. Q4 focuses on the still-unverified finished-glove measurement hypothesis. Q5 converts the Q2 AFE result into bench metrology; Q7 addresses safety/regulatory boundaries; Q6 evaluates BLE/mobile transport after basic sensor assumptions are made.
2. Q1/Q2 PDF outputs are retained on Drive. Do not re-upload copyrighted full research papers into the public repository. Only the author's prompts, references, review status and non-sensitive evidence summaries belong here.
3. SBT code and technical testing stay in this repository; LGW tasks require scoped acceptance criteria and verified task IDs/commits before being declared complete. TRE supports customer/pilot validation but does not replace SBT project ownership.
