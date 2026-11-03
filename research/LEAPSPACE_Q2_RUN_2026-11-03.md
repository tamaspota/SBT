# SBT – LeapSpace Q2: EDA/GSR analog front end and bench verification

- **Task:** `LS-SBT-Q2-20261103-01`
- **Status:** `RESULT_RECEIVED / INITIAL_DOI_SPOTCHECK / SCIENTIFIC_ACCEPTANCE_PENDING` (owner ran LeapSpace and archived the 17-page PDF in SBT Drive/03/Leadspace). Q1 was delivered separately and remains only partially source-verified.
- **Date:** 2026-11-03
- **Scope:** independent battery-operated EDA/GSR front end; not a ZYTO protocol clone or clinically diagnostic product.
- **Length:** 492 characters (LeapSpace UI 500-character input limit).

## Receipt and initial evidence review – 2026-11-03 22:01 (owner report)

- **Source file:** [Battery-powered EDA/GSR analog front-end design – 17-page LeapSpace PDF](https://drive.google.com/file/d/1KKNjZOZKnmPfxfRne-vsvCK1_udLJ-sT/view?usp=drivesdk) in [SBT Drive/03/Leadspace](https://drive.google.com/drive/folders/1a_X07p0qbQVS43aQKWwnH-vdXhkrKm7c). 437687 bytes, uploaded around 21:01:36 UTC; PDF metadata creation at 21:01:32 UTC. Reported 22:01 CET local-time header.
- **Source conversation printed in PDF:** https://www.sciencedirect.com/leapspace/conversation/875038fb-6fcb-4922-890a-ce8d9fe648f0.
- **Verified content:** all-page extract read. PDF visually inspected for the page-10 bench protocol table. Classical ~0.5-V fixed-voltage DC skin conductance method described as baseline; AC/polarity reversal promising for reduced polarization drift; constant-current vs constant-voltage matched comparator data insufficient; AFE ADC/reference, ESD, current limiting, safety/isolation, contact detection and full BLE power budget underreported.
- **Bench-test PROPOSALS ONLY:** calibrated resistors about 10 kΩ–1 MΩ; precision R + RC interface surrogates; 5-minute noise records; 30–60-minute drift; at least 3–5 repeats/load; <=1% pure-resistor static relative accuracy suggested as *project candidate*, not accepted standard or measured SBT result. All quantitative criteria need predefinition, calibration traceability, reference tolerances and safety approval before tests.
- **Independent checks (selected):** Romero-Ante et al. (2025) DOI [10.3390/s25123603](https://doi.org/10.3390/s25123603) on wearable AC excitation (ten healthy participants), Pabst et al. (2017) DOI [10.1111/psyp.12803](https://doi.org/10.1111/psyp.12803) comparing DC and 20-Hz AC, Ogorevc et al. (2013) DOI [10.1016/j.measurement.2013.06.024](https://doi.org/10.1016/j.measurement.2013.06.024) on metrological evaluation. Bibliographic/abstract source check, **not** independent replication.
- **BIBLIOGRAPHY QUALITY WARNING:** PDF entry #20 incorrectly dates Frisanco et al. `2099`; original Nature article DOI [10.1038/s41598-022-26016-1](https://doi.org/10.1038/s41598-022-26016-1) is **2022** and concerns VR/physiological response, not wearable EDA AFE circuitry. The PDF also itself says source DOI strings were not surfaced despite printing a references section with DOI links. Verify citations and claim mapping, not just count DOI-like strings.
- **Status:** `LS-SBT-Q2-20261103-01 = RESULT_RECEIVED / INITIAL_DOI_SPOTCHECK / SCIENTIFIC_ACCEPTANCE_PENDING`. **No** bench device tested, human-use approval, or selected final analog circuit.

## Exact copy/paste prompt

> Review primary studies with verified DOIs on battery-powered EDA/GSR analog front ends for BLE wearables. Compare constant-voltage vs constant-current excitation, electrode polarization, ADC/reference accuracy, input protection, contact detection, noise, drift and power draw. Provide a cited trade-off table and a bench-only protocol with calibrated resistors, sampling requirements and numerical accuracy/noise/drift acceptance proposals. Flag safety gaps; no human tests or medical claims.

## Instructions for execution
Start a normal (non-temporary) LeapSpace conversation; switch on **Deep research**. Avoid `Project only` if it prevents external literature access. Run once as a bounded question; export original report with DOI/reference list, figures and caveats to the existing SBT/03/Leadspace Drive folder: https://drive.google.com/drive/folders/1a_X07p0qbQVS43aQKWwnH-vdXhkrKm7c

Do not submit personal ZYTO/health records, client details or proprietary material. No request to intentionally evade quota controls or to trigger excessive parallel Deep Research runs.

## Review/acceptance criteria (after return)
1. Sources clearly identify actual **EDA/GSR front ends** separately from ECG/EMG/bioimpedance methods; primary DOIs and methods can be independently checked.
2. Compare excitation topology (constant voltage/current), electrode polarization, ADC/reference, sensor/electrode contact detection, power, interference, and protective current limits. No invented numeric safety limits.
3. Include source-backed architecture/block diagram or, if not present, explicitly record as missing; component/BOM selection remains a separate engineering decision.
4. Define a **bench-only** test matrix with traceable resistive/conductance references, expected raw units, calibration/linearity, noise, drift, warm-up, timestamps and data gaps. Quantitative thresholds must be labeled as literature-reported vs proposed project criteria.
5. Separate `VERIFIED`, `INFERENCE`, `UNVERIFIED`, report contradictory results; do not treat Deep Research text alone as acceptance evidence.
6. Do not use on humans until independent electrical safety and privacy review; no ZYTO diagnosis/interoperability claims.

## Follow-up
When the user supplies the exported result or its exact Drive URL, verify cited DOI records and essential methods, update `research/EVIDENCE_AUDIT_2026-11-03.md`, `docs/CURRENT_STATE.md` and the relevant session log. Do not mark Q2 `RESULT_RECEIVED` until the actual file is read and source-checked.
