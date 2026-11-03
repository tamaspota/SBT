# SBT mobile sensor concept — v0.1

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
