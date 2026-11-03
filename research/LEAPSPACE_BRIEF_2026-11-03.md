# SBT | LeapSpace Deep Research delegation — 2026-11-03

**Status:** Prepared, NOT submitted to LeapSpace. Owner: Póta Tamás. Source-of-truth: this GitHub repository; editable business/team briefing: owner-controlled Google Drive SBT/03 folder.

## Revenue / user problem
Explore a **paid SBT feasibility pilot** with a real practitioner/customer for an independent, battery-powered mobile electrodermal activity (EDA / GSR) measurement device and companion phone software. Interest and spending commitment remain **unconfirmed**. Define customer-facing value beyond "runs on a phone" and beyond existing ZYTO products.

## Verified vs proposed
- Historical (owner's email, 2022-11-10/11): independent device, phone connection and battery-powered operation were proposed; no working build or communications protocol was demonstrated.
- 2026-11-03 owner proposal: small wearable (Fitbit-size aspiration) or textile glove in addition to a handheld design. No mechanical or electrode configuration selected.
- ZYTO's current public material describes the **USB-connected Hand Cradle as a GSR sensor**, and **its wellness output is not diagnostic**. Source: https://zyto.com/hand-cradle/ and https://zyto.com/faq/
- ZYTO also markets mobile software, including ZYTO Link. Therefore novelty cannot be claimed solely from smartphone access. Source: https://zyto.com/about/
- No third-party ZYTO SDK, API rights, device internals, raw protocol or ownership of Adri's existing software has been verified. Do not assume integration.
- This is a **non-diagnostic independent research prototype**. Never upload personal ZYTO reports, medical/lab results or identifiable subject data to research services.

## Research scope and questions
**A. Sensor location / electrodes.** Compare palmar or finger contacts, wrist-worn dry electrodes, and textile glove electrodes for signal quality, stability, skin contact, movement artefacts, ergonomics, hygiene and reproducibility. Include studies with DOI and conflicting results.

**B. Measurement design.** Compare EDA/GSR front-end methods: constant-voltage vs constant-current, reference resistors and calibration, low-noise ADC, electrode impedance/contact checks, power management, BLE/USB-C, electrical and radio safety. Separate literature-supported components from proposed engineering choices.

**C. Measurement interpretation and validity.** Identify what continuous EDA alone can reliably quantify, confounders (temperature, skin condition, motion, individual baseline), stress inference limitations, and what the evidence does NOT support. No disease or virtual-biomarker diagnosis.

**D. Practical go/no-go.** Recommend a minimum bench reference and 1–2 portable designs worth prototyping, **not a production BOM**. Identify a falsifiable engineering demonstration, commercial differentiators, and evidence needed for legal/product claims.

## Copy/paste Deep Research prompts
Run each as a **separate LeapSpace Deep Research question**. Use trustworthy primary papers with DOI (or explicitly mark unavailable) and report contradictory/negative findings. Do not paste private repository contents or client health data.

**Q1 — electrode placement (<= 500 chars)**
> For a non-diagnostic mobile electrodermal-activity (EDA/GSR) sensor, compare finger/palm, wrist dry electrodes and textile glove electrodes. Find primary validation studies, with DOI, on signal quality, motion artifacts, calibration, contact stability and between-subject variability. Recommend a minimal falsifiable bench and volunteer protocol. Distinguish evidence from engineering assumptions.

**Q2 — analog sensing (<= 500 chars)**
> Review peer-reviewed designs for low-power, battery-powered EDA/GSR sensor front ends with BLE phone connectivity. Compare excitation, analog protection, ADC and reference strategy, calibration, noise/drift, skin-contact indicators and safe human-use constraints. Return evidence-backed design trade-offs and a reproducible bench validation plan, with DOI and explicit unknowns.

**Q3 — interpretation limits (<= 500 chars)**
> What can raw wearable electrodermal activity reliably measure or infer? Review validation of skin conductance features, motion-artifact handling and any stress-related inference, especially under real-world movement. Identify confounders, false positives, and unsupported disease/organ/nutrient claims. Summarize primary peer-reviewed evidence with DOI and negative findings.

**Q4 — research/commercial decision (<= 500 chars)**
> For a practitioner-facing independent GSR/EDA mobile sensor, what literature-backed evidence supports handheld vs compact wearable vs glove deployment? Compare measurement quality, ease of calibration, human effort, usability, privacy and repeatability. Propose a small, falsifiable feasibility pilot and explicit kill criteria. Cite primary literature with DOI; do not infer ZYTO software compatibility.

## Expected output / acceptance
1. One decision summary: **handheld / wearable / glove**, scoring evidence strength and practical readiness.
2. Reference matrix (paper, year, DOI, electrode location, sample size, gold standard, metrics, limitations).
3. A minimal GSR/EDA electronics validation protocol with explicit test setup and predefined failure conditions.
4. A 5–10 point risks/unknowns register, tagged `EVIDENCE`, `INFERENCE`, or `UNVERIFIED`.
5. Suggested measurable pilot acceptance criteria, **not** a claim of health diagnosis or ZYTO compatibility.
6. Export research report to private Drive SBT/03 and note review decision in repository after owner/scientific review.

## Useful starting primary sources (do not treat as full review)
- Poh et al., IEEE TBME (2010), DOI 10.1109/TBME.2009.2038487. https://pubmed.ncbi.nlm.nih.gov/20172811/
- van der Mee et al., Int. J. Psychophysiol. (2021), DOI 10.1016/j.ijpsycho.2021.08.003. https://www.sciencedirect.com/science/article/pii/S0167876021008461
- Kong et al., Comput. Biol. Med. (2024), DOI 10.1016/j.compbiomed.2024.109139. https://pubmed.ncbi.nlm.nih.gov/39270456/

## Handoff and decision gate
LeapSpace supplies **research evidence**, not verified firmware, electrical safety certification, owner approval or completed development. Software implementation and tests belong to this repository, with bounded implementation agents as appropriate. SBT customer / contractual / IP scope must be agreed before committing to a full platform or manufacturing.
