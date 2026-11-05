# LGW candidate task: SBT bench-only GSR data contract — 2026-11-05

**Status:** TASK SPECIFICATION ONLY — NOT DISPATCHED / NOT STARTED. Project: independent SBT; canonical repository: `tamaspota/SBT`. Executor: LGW only after owner-authorized bounded dispatch and safe-environment verification.

## Goal

Implement the smallest deterministic **software-only** test harness around the SBT existing Python synthetic GSR generator, using a calibrated-resistor fixture *data model*. It must not suggest physical sensor hardware or human contact exists.

## Required preliminary reads

- `AGENTS.md`, `docs/CURRENT_STATE.md`, `docs/DECISIONS.md`, `docs/VALIDATION_PLAN.md`, `docs/SOFTWARE_MVP.md`
- `research/Q4_Q8_EVIDENCE_REVIEW_2026-11-05.md`
- `docs/GSR_BENCH_VALIDATION_DRAFT_2026-11-05.md`
- Inspect actual existing prototype scripts and tests *before* editing.

## Allowed scope

1. Define synthetic fixture states for OPEN and 1 MΩ, 500 kΩ, 200 kΩ, 100 kΩ, 50 kΩ as **candidate** test loads.
2. Implement exact conversion and labeled `SIMULATED` synthetic conductance records: `G_uS=1_000_000/R_ohm`. Do not mark them `MEASURED`.
3. Add monotonically increasing sample times, sequence IDs, `CONTACT_LOST`/data gap flags and CSV/JSON export that preserves units, source, calibration-reference ID and fixture metadata.
4. Keep the test harness local and offline; no API keys, Cloudflare, external services, protected ZYTO protocols, or medical data.
5. Add automated tests with fixed inputs for open, unit conversion, sample-gap behavior, metadata roundtrips and no false `MEASURED` states.

## Acceptance criteria

- Code and tests confined to existing SBT repo; no duplicate repository.
- Deterministic automated tests pass and fail meaningfully when intentionally broken.
- `1e6/100000 = 10.0 µS`, `1e6/200000 = 5.0 µS`, `1e6/50000 = 20.0 µS` in synthetic fixture; open circuit explicitly flags invalid contact without division by zero.
- Test data/source metadata unambiguously identify **synthetic** provenance. No code path silently interpolates missing data.
- Final read-back lists dispatch/task ID, git commit(s), exact test commands/results and any changed canonical state/decision/log docs.
- Nothing is called a validated hardware measurement, sensor accuracy, electrical safety result, ZYTO protocol compatibility or diagnostic output.

## Not authorized

Physical circuit operation, acquisition from a person, PCB fabrication, patient data sharing, supplier communication, private repo visibility/access changes, unreviewed production dependencies or paid cloud resources. If an implementation step requires approval, stop and surface the issue.

## Next action for owner

Approve and dispatch as a bounded LGW coding task when appropriate, after checking current LGW availability and that no overlapping SBT work is running. Drafting this file does **not** dispatch work.
