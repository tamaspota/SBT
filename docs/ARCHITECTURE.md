# Proposed architecture — not yet implemented

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
