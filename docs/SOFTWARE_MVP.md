# Mobile GSR companion software — MVP design v0.1

**Status:** SPEC ONLY as of 2026-11-03. No mobile app or BLE device has been implemented. The current Python prototype generates explicitly synthetic GSR/EDA samples.

## Purpose
A smartphone companion to an **independent** BLE GSR/EDA sensor. First customer value: reliable raw-signal capture, signal quality visibility, local session history and usable share/export. No ZYTO-proprietary algorithm replication, physiological diagnosis, generic "stress diagnosis" or unvalidated biomarker scores.

## User flows
1. **Connect:** find a test sensor, verify protocol revision, show battery/connection status.
2. **Measure:** display live skin conductance (uS), contact quality, duration and gaps; manual start/stop.
3. **Review:** plot time series; annotate movement/contact changes without health conclusions.
4. **Export:** local CSV or JSON containing device and firmware versions, units, monotonic timestamps, quality flags and explicit simulated-vs-real source.
5. **Erase/share:** session deletion and user-authorized sharing only. No default upload.

## Architecture options — not yet selected
- **First demonstration:** reuse existing synthetic Python generator and a basic local simulator/viewer with known-good test fixtures; **no new backend**.
- **Phone app:** evaluate a cross-platform option (e.g. Flutter) vs native Android/iOS after iOS BLE requirements and existing codebases are assessed. No framework choice is final.
- **Device protocol:** BLE GATT with characteristic definitions, timestamps, sequence numbers, rate/units and quality flag semantics frozen only after bench tests; optional USB-C later.
- **Data model:** `session_id`, `device_id` (privacy-safe), `schema_version`, `firmware_version`, `timestamp_ms`, `eda_uS`, `quality_flags[]`, `source: SIMULATED|MEASURED`, sampling metadata, calibration-reference identifier, and explicit consent state for sharing.

## Implementation slices (smallest demonstrable path)
**M0 — software-only demonstration** (no health measurements): simulated stream, live chart, quality flag and CSV/JSON export. Demonstrate with no cloud and no customer account.
**M1 — hardware integration:** tested BLE sensor stream, timestamps/reconnect, measurement-gap reporting, explicit hardware vs simulated data, iOS and Android test matrix.
**M2 — repeatable data capture:** local history, session metadata, consent, reproducible export/import and firmware compatibility.
**M3 — optional customer workflow:** consent-controlled sharing, a simple practitioner review view and neutral, non-diagnostic report only if external customer evidence justifies it.

## Acceptance tests — must be defined with customer
- Synthetic vs measured data unambiguous in UI/export.
- Known artificial gap appears as missing data, never silently interpolated or treated as a biological response.
- Export/import roundtrip retains sequence, timestamp, value, unit and quality flags.
- BLE reconnect and iOS/Android support require real-device testing; simulator tests alone do not prove them.
- No claim of ZYTO connectivity without a permitted API and on-device validation.

## Dependencies / decision gates
Customer discovery → selected use case / lawful interface → bench signal metrics → BLE+mobile proof → funded pilot → production, if justified. Determine licensing/IP ownership of Adri's existing software separately; do not assume it can be copied or integrated.

## Compliance boundary
Medical-purpose claims may trigger EU MDR software/device qualification. Bluetooth electronics may trigger EU RED/CE and privacy/cybersecurity requirements. This is a review gate, not a compliance certification. References:
- https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32017R0745
- https://single-market-economy.ec.europa.eu/sectors/electrical-and-electronic-engineering-industries-eei/radio-equipment-directive-red_en
- https://zyto.com/faq/
