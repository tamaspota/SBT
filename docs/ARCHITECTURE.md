# Proposed architecture — not yet implemented

## Updated architectural candidate — 2026-11-05 (not implemented)

Owner proposes to replace the first-product *phone-dependent* architecture below with a **self-contained appliance**:

```text
Skin electrodes -> protected EDA AFE -> ADC / calibration / quality flags
  -> local interface to Raspberry Pi-class computer (interface TBD)
  -> locally rendered touchscreen UI (candidate 3–10 inch, responsive)
  -> local raw EDA session storage / export
  -> optional wireless/back-end ONLY after independent need and test
```

Compute candidates **Pi 4B or Pi Zero 2 W**; no choice, power budget, driver, real-time sampling/latency, touchscreen adaptation or battery safety verified. Prefer keeping deterministic acquisition on a bounded dedicated front end; check whether a separate MCU is needed after actual sampling and jitter requirements. 3D-printed housing is an enclosure concept, not an assembled device. Defer Android/iOS native-app support as first MVP. The prior BLE-to-smartphone diagram remains historical, not the currently prioritized path.

Research/bench priorities unchanged: calibrated passive resistor tests, correct raw-EDA units, timestamp/quality/traceable calibration and no human use before electrical safety/privacy review. Licensing or pay-per-measurement requires security and commercial review, not assumed code functionality.

```
Skin electrodes / contact sensing
  -> protected low-current measurement AFE
  -> filtered ADC / reference / self-test
  -> low-power BLE MCU + battery monitoring
  -> BLE GATT: timestamp, raw conductance, quality, battery, firmware version
  -> phone app (iOS / Android): plot, export, consent, local history
  -> optional encrypted backend after explicit need and privacy assessment
```

No assertion is made about the circuitry, data rate or protocol inside a ZYTO Hand Cradle: unavailable until documented and legally verified. USB 2.0 supply in a historical email is an observation, not a design specification.

### Protocol concept
- Units: conductance in microsiemens (uS) or resistance in ohms with explicit calibration metadata.
- Timestamp: monotonic sample counter plus device tick; app may attach UTC on receipt.
- Quality flags: contact_lost, saturation, motion_suspected, calibration_invalid.
- BLE link is best-effort: sequence numbers and retransmission / gap detection to be designed.

### Privacy and compliance
No human sensor streams or personal reports go to public GitHub. Default is on-device storage with consent. Medical claims, electrical safety, radio compliance, cybersecurity and data protection must be evaluated before productization.
