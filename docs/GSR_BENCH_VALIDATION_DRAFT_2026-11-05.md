# SBT GSR/EDA bench validation protocol — DRAFT v0.1 (2026-11-05)

**Scope:** test **electronic acquisition and data provenance only**, using calibrated passive **resistors** before any participant measurements. No human test, device electrical-safety approval, manufactured glove, clinical diagnosis, or Bluetooth hardware demonstration is implied. This plan needs owner/technical approval before it becomes a formal acceptance procedure.

## Sources and assumptions

- Primary metrology source: Geršak & Drnovšek (2020), DOI [10.1371/journal.pone.0228949](https://doi.org/10.1371/journal.pone.0228949). The **100 kΩ ⇔ 10 µS** calibration state, variable resistance/simulator approach and dynamic SCR-shaped stimuli are **reported facts of their test setup**, not SBT test outcomes.
- Primary glove source: Lanatà et al. (2012), DOI [10.1007/s11517-012-0921-9](https://doi.org/10.1007/s11517-012-0921-9). A real Lycra glove with integrated electrodes was tested; motion was not validated. Electrode electrical and mechanical feasibility must be validated independently.
- The numerical resistor matrix below is an **SBT engineering proposal derived by Ohm's law**, not a published or owner-approved pass/fail standard.

## Stage 0 — fixture/data preparation (before hardware energization)

1. Record meter calibration certificate/traceability or absence thereof. Measure and record the *actual* resistance, reference uncertainty, rated dissipation, temperature and wiring arrangement for every test resistor. Do not label uncalibrated resistors as reference standards.
2. Store immutable test fixture IDs, acquisition software and simulated/measured source field, firmware version, sample unit, session timestamps, battery state and environmental conditions. Treat `SIMULATED` and `MEASURED` as non-interchangeable.
3. Obtain a circuit-specific engineering safety review of bias voltage, fault current limiting, battery charging isolation, ESD and surge paths. **Do not connect to people** on the basis of this bench protocol.
4. Use a switch/fixture with documented parasitics or an electrically isolated multiplexer as a later option; confirm no short-circuit hazardous transient is introduced. Keep the first tests passive, bench-only.

## Stage 1 — candidate fixed reference matrix

Conductance **G (µS) = 1,000,000 / R (Ω)** for purely resistive loads.

| Nominal passive reference | Expected conductance | Test condition |
| --- | ---: | --- |
| Open circuit | ~0 µS | Invalid contact/disconnect behavior |
| 1 MΩ | 1 µS | Low conductance point |
| 500 kΩ | 2 µS | Additional low point |
| 200 kΩ | 5 µS | Mid point |
| 100 kΩ | 10 µS | Primary 2020-paper-inspired calibration point |
| 50 kΩ | 20 µS | High point in initial proposed range |

**Important:** `0 Ω` is not a required stage-1 stimulus. All states, including open circuit, require bounded input protection before connection. Choose additional loads only after measurement range requirements are agreed. If actual meter value is R_actual, compute expected G from R_actual rather than nominal R.

## Stage 2 — bench-only acquisition and validation

- For every calibrated load, record raw EDA time series and reference metadata; perform **at least three independently restarted runs**. Candidate observation intervals: **60 seconds** per stable state, plus one **10-minute** run at 100 kΩ to characterize warm-up and drift. These durations are *proposed*, not a validated standard.
- Store expected G, measured mean, signed and absolute error in µS, relative error in % (only for nonzero G), RMS noise and peak-to-peak noise, time trend/temperature, dropout and contact flags. Report uncertainty contributions from the reference, ADC calibration, bias, sampling and repeatability separately.
- Introduce *known* switching steps (e.g. 100 kΩ ⇔ 200 kΩ) and measure response time, settling behavior, missing samples, saturation, fault/recovery and erroneous contact-status flags. Never hide missing samples by interpolation.
- **Dynamic stage (future):** replay synthetic 0.25 / 0.5 µS SCR-shaped changes and 5 / 10 / 20 events/min only with a validated simulator/electrical fixture. Do not claim such a generator currently exists in SBT.
- **Mobile stage (later):** evaluate BLE packet_seq + monotonic sample tick + session_id + gap flags; verify loss/reconnect with actual Android and iOS devices. Software-only simulation may test parsing, but not RF behavior.

## Proposed acceptance criteria (not yet signed or proven)

| Criterion | Measurable pass/fail plan | Status |
| --- | --- | --- |
| Static conductance error | Candidate target **≤1% of expected G** for each stable calibrated resistor, *subject to reference uncertainty and cost/technology tradeoffs*. Alternative target may be agreed after bench capability is known. | **PROPOSAL ONLY, NOT APPROVED** |
| Stable signal noise | RMS / peak-to-peak in µS measured over 60 s with temperature and bandwidth recorded; threshold **TBD** before formal test. | SPECIFICATION GAP |
| 10 min drift | Absolute and relative µS drift against 100 kΩ recorded; threshold **TBD** before formal test. | SPECIFICATION GAP |
| Step response | Record time to 95% and sample loss for each 100/200 kΩ transition; latency limit **TBD**. | SPECIFICATION GAP |
| Open circuit | Must explicitly flag `CONTACT_LOST` / invalid output; **never silently interpret as a physiological SCR**. | SOFTWARE BEHAVIOR PROPOSAL |
| Data provenance | Every export includes `source=SIMULATED|MEASURED` and reference/calibration/version IDs; no fabricated `MEASURED` samples. | **TESTABLE SOFTWARE CONTRACT** |
| Safety review | Written review of fault currents, isolation, charging configuration, intended use and privacy before a human touches an electrode. | **HARD BLOCKER** |

## LGW handoff / acceptance

A bounded LGW software assignment may first implement a **bench data contract and synthetic load fixtures** without any physical device or human measurement. The resulting code must pass deterministic tests for conversion, sequence continuity, open-circuit flagging, gap handling, and CSV/JSON round-trip. The LGW job must be explicitly approved and read-back verified (task ID, commit and test report). See `docs/LGW_BENCH_SOFTWARE_TASK_2026-11-05.md`.

**Go/no-go before physical PCB or glove procurement:** test-fixture/reference uncertainty defined, calibrated analog measurement path selected, explicit current/fault/charging protections reviewed, comparator baseline agreed, and customer pilot value stated. No CE/MDR/Zyto or human-fit claims based solely on LeapSpace.
