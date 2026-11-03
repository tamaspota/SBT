# SBT — Mobile GSR / EDA Sensor Project

**State (2026-11-03): engineering feasibility / concept, not a validated hardware product.**

An independent battery-powered galvanic skin response (GSR / electrodermal activity) sensor project. Planned mobile connectivity: BLE and Android/iOS; candidate physical forms: handheld unit, compact wearable and electrode glove.

## Origin

The idea was documented by Póta Tamás in a **10 November 2022** email to Tamás Sebestény ("Zyto hand cradle"). That historical proposal already considered a new electronic device, phone interface, wireless transmission, battery power and external manufacturing. In 2026 the idea is being reconsidered as a bounded prototype project; no interoperability with proprietary ZYTO software has been proven.

## Start here

- [Current state](docs/CURRENT_STATE.md)
- [Product concept and alternatives](docs/PRODUCT_CONCEPT.md)
- [Architecture sketch](docs/ARCHITECTURE.md)
- [Validation plan](docs/VALIDATION_PLAN.md)
- [LeapSpace research brief — prepared, not executed](research/LEAPSPACE_BRIEF_2026-11-03.md)
- [Mobile software MVP plan](docs/SOFTWARE_MVP.md)
- [Paid pilot customer-discovery questions](docs/CUSTOMER_PILOT_QUESTIONS.md)
- [Decisions](docs/DECISIONS.md)
- [Synthetic sensor telemetry](prototype/simulated_gsr.py) — **not real sensor measurements**.
- [Tests](tests/test_simulated_gsr.py)

## Exclusions and responsibility

There is no available ZYTO firmware/protocol specification, no finished PCB, no human-use validation and no proven medical diagnostic capability. The target is a physically verifiable GSR signal, not recreation of ZYTO virtual wellness scores. Clinical claims require independent evidence and proper regulatory review.

**Do not upload personal ZYTO reports, patient files or credentials to this repository**, even if it later becomes private. These files are stored separately in the owner-controlled SBT Google Drive folder.

## Review path

First validate measurement requirements and sensor architecture, then prototype safely, confirm Android/iOS transport, compare the mechanical concepts, and only then investigate manufacturing partners and a paid feasibility pilot.
