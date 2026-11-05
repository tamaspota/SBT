# SBT mobile sensor concept — v0.1

## Owner update – 2026-11-05: standalone Pi touchscreen direction

**Candidate first product:** self-contained EDA/GSR measurement appliance, Raspberry Pi compute (Pi 4B or Pi Zero 2 W as **unselected candidates**), integrated touchscreen approx. 3–10 inches, adaptable common software codebase, possible 3D-printed enclosure. The owner decided to **de-prioritize separate Android/iOS native apps** due to long-term maintenance/platform variation; a future mobile companion is optional, not the pilot baseline.

**NOT validated:** Pi model, CPU/RAM footprint, boot/measurement latency, display resolution and drivers, battery capacity/run time, safety during charging, 3D printed ergonomics, BOM, legal/regulatory position, app portability or measurement equivalence. First engineer/bench gate remains traceable resistance–conductance calibration and `SIMULATED` vs `MEASURED` provenance.

**Business model under discussion:** sale of a dedicated appliance, optional software license or free base software with paid measurements/services. Pricing/payment/measurement entitlement and privacy regulatory implications require real customer validation; no commitment has been made.

The following 2022 historical origin and v0.1 phone/BLE alternatives remain **historical possibilities**, superseded for first-product planning by this owner direction. See `docs/DECISIONS.md` D-011.

## Historical origin

Tamás Póta's own November 2022 email already proposed replacing the legacy USB Windows Hand Cradle with a battery-powered mobile Android device, Bluetooth or Wi-Fi communications, a potentially self-contained unit and a rebuilt independent software layer. No teardown or validated ZYTO protocol was documented then. The current owner adds a wearable / glove option and iOS compatibility to the development hypotheses.

## Alternatives

A. **Handheld**: contact pads touched with fingers or palm; easiest bench validation.

B. **Compact wearable**: Fitbit-like size, not Fitbit physiological equivalence. GSR requires electrodes at suitable skin contact locations, so wrist-only electrodes may show different signal quality; validate placement before selecting.

C. **Glove**: integrated finger or palmar dry electrodes, adjustable fit, potentially higher contact consistency, but motion artefact, washing, hygiene, sourcing and manufacturing complexity.

## Minimum plausible pilot

- Independent electrodermal conductance sensing, not a cloned ZYTO analyser.
- Battery operation during measurement, electrical protections, safe low-current front-end subject to formal engineering verification.
- BLE with documented raw readings, timestamps and signal-quality bits.
- A basic Android/iOS viewer and local export. No medical interpretation.
- Repeatability and stability recorded against reference resistance/conductance conditions and human-use protocol with consent.

## Decision gates

G0 requirements and lawful interface rights; G1 electronics bench performance; G2 phone connection; G3 ergonomics; G4 customer-funded pilot and manufacturing readiness. No production claims before those gates.
