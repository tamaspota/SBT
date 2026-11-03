# SBT – LeapSpace Q2: EDA/GSR analog front end and bench verification

- **Task:** `LS-SBT-Q2-20261103-01`
- **Status:** `PREPARED / NOT SUBMITTED` (owner manually runs LeapSpace Deep Research and archives full result). Q1 was delivered separately and remains only partially source-verified.
- **Date:** 2026-11-03
- **Scope:** independent battery-operated EDA/GSR front end; not a ZYTO protocol clone or clinically diagnostic product.
- **Length:** 492 characters (LeapSpace UI 500-character input limit).

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
