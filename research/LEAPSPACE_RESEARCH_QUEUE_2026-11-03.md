# SBT – LeapSpace research queue (2026-11-03)

**Owner:** Póta Tamás. **Project:** standalone SBT. **Technical record:** `tamaspota/SBT`. **Partner-facing working area:** SBT Drive/03. **Research-output archive:** https://drive.google.com/drive/folders/1a_X07p0qbQVS43aQKWwnH-vdXhkrKm7c

## Execution rules

- Run **one** LeapSpace Deep Research job at a time, when convenient. No background execution/automation has been set up.
- Use a **normal, non-temporary conversation**, enable `Deep research`, and select external literature search rather than `Project only` if those modes conflict.
- Copy **only the exact English prompt** of the desired task. Each prompt is under the observed 500-character input limit.
- Export full PDF with bibliography to the existing SBT research archive, keeping the original title/date. Add the Drive link when reporting completion. No project-only source list or claims of finished research from prompt creation.
- The research tool is a literature synthesis system, **not an electronics design approval or a medical certification authority**. Independently check primary papers/standards, DOI, methods, N and quantitative results; mark conflicts. No proprietary ZYTO data or personal medical files in LeapSpace.
- Record each run as `PREPARED` → `RESULT_RECEIVED` → `SOURCE_CHECKED_PARTIAL` → `SCIENTIFICALLY_ACCEPTED` only after evidence review. Stop/restrict use if the provider reports quota/rate-limit constraints; no attempts to evade them.

## AKTUÁLIS ÁLLAPOT – 2026-11-05 (az alábbi november 3-i állapot történeti)

**7 PDF / 6 téma:** Q1, Q2, Q3, Q5 (két önálló eredmény), Q6 és Q7 ténylegesen megvan a [Leadspace Drive-mappában](https://drive.google.com/drive/folders/1a_X07p0qbQVS43aQKWwnH-vdXhkrKm7c). **Q4 nincs kész PDF-ként archiválva.** Az új Q3/Q5/Q6/Q7 jelentések státusza `RESULT_RECEIVED / SOURCE_AUDIT_PENDING`, nem `SCIENTIFICALLY_ACCEPTED`. A pontos PDF-linkek és a kutatási hiányosságok: [2026-11-05 bizonyítékaudit](LEAPSPACE_AUDIT_2026-11-05.md).

**Módszer:** egyetlen aktív, kézzel indított Deep Research-kérdés egyszerre; nincs megerősített korlátlan kvóta. A források eredeti DOI-ját, mintaelemszámát, módszerét és állított mérési határértékeit külön ellenőrizni kell. Személyes ZYTO-riportokat nem küldünk a szolgáltatónak.

### Javasolt következő kutatások (Q4-R és Q8–Q11)

#### Q4-R – Kész GSR-kesztyű mérési bizonyítéka [P0] (467/500 karakter)

**Állapot:** `PREPARED / NOT_SUBMITTED`

> Find primary EDA/GSR trials that tested a complete wearable textile glove, not just textile patches on fingers. Start with DOI 10.3390/bios8030079 and 10.1109/SEGAH54908.2022.9978571; check whether either tested a finished glove. For each true glove trial give DOI, N, Ag/AgCl comparator, material, electrode layout, fit/pressure, movement and quantitative agreement. If no direct comparison exists, say so. Propose bench contact tests; do not imply human-use safety.

#### Q8 – Reprodukálható GSR referencia-mérőpad [P0] (441/500 karakter)

**Állapot:** `PREPARED / NOT_SUBMITTED`

> Using primary metrology papers DOI 10.1371/journal.pone.0228949 and 10.1016/j.measen.2024.101075, extract reproducible EDA instrument test methods. List actual reference-resistor values, tolerances, simulator circuit, sample rate, reference meter, bias, noise, drift, time constants and uncertainty. Give page/table/figure identifiers and check each DOI/claim. Separate reported results from SBT project acceptance proposals; no human tests.

#### Q9 – Mozgási műtermék és kontaktushiba [P1] (463/500 karakter)

**Állapot:** `PREPARED / NOT_SUBMITTED`

> Find primary field studies measuring contact-loss and motion artifacts in wrist, palm and finger EDA during walking, hand use and sleep. For each give DOI, N, reference measurement, electrode geometry, raw sampling, movement labeling and quantified false SCR events or missed events. Distinguish measured rates from assumptions. Propose quality flags, an artifact-labeled dataset schema and non-diagnostic acceptance tests; explicitly report missing ground truth.

#### Q10 – Hivatalos EU jog és szabványalkalmazhatóság [P1] (480/500 karakter)

**Állapot:** `PREPARED / NOT_SUBMITTED`

> Using current official EU MDR, RED, EMC, RoHS, Batteries Regulation and GDPR texts plus authoritative IEC/EN catalogs, determine which rules may apply to a battery BLE EDA research/wellness wearable vs a medical-purpose device. Cite exact article/annex and current standard edition with source URL. List RF, skin-contact, charging, leakage/fault, cybersecurity and data tests; mark conditional applicability and unknowns. Do not invent legal exemptions or safe current thresholds.

#### Q11 – SCL/SCR jelkinyerés szoftveres validációja [P2] (493/500 karakter)

**Állapot:** `PREPARED / NOT_SUBMITTED`

> Compare validated open-source algorithms for separating tonic SCL and phasic SCR in wearable EDA recordings (4-32 Hz). Seek original benchmark papers with DOI and available datasets/code; report filtering delay, events missed, motion-artifact sensitivity, inter-subject variability, computational cost and ground-truth limitations. Recommend a minimum offline, on-phone non-diagnostic pipeline preserving raw values and contact-quality flags. Include reproducible tests and uncertainty labels.

**Eredmény:** a teljes PDF forrásjegyzékkel az eredeti [SBT Leadspace Drive-mappába](https://drive.google.com/drive/folders/1a_X07p0qbQVS43aQKWwnH-vdXhkrKm7c), majd forrásellenőrzés és GitHub-naplózás. Nem futtatunk újra Q3/Q5/Q6/Q7 általános kérdéseket változatlan formában.

---

## TÖRTÉNETI állapot – 2026-11-03

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
