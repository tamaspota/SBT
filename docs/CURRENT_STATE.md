# Current state — 2026-11-03

- Project: SBT independent mobile GSR/EDA sensor concept, originating in Póta Tamás's November 2022 email to Tamás Sebestény.
- Technical owner: Póta Tamás. External stakeholders: Sebestény Tamás and Tilli Adrienne, subject to access and collaboration approval.
- Repository initially public; no confidential measurement data belongs here.
- Stage: discovery / bench feasibility, NOT a working prototype, NOT a clinically validated instrument.
- Physical design under study: compact handheld / Fitbit-size wearable / textile glove; these are alternatives, not a selected production design.
- First use case: smartphone-compatible, battery-powered GSR recording, BLE transport and user-controlled export.
- Open: customer requirements, existing hardware measurements, ZYTO interface rights, sensing topology, safety/EMC, Android/iOS BLE feasibility, wearability, calibration and manufacturing quote.
- Next gate: independently validate basic GSR signal quality against bench reference before enclosure/China manufacturing commitments.
- Evidence: 2022-11-10/11 archived subject 'Zyto hand cradle'; 2026-11-03 meeting photos and proprietary ZYTO report (private Drive only).

## Next action

1. Define 3 explicit mechanical concepts and their electrode placements.
2. Prototype a safe, isolated, current-limited sensor front end on bench; document requirements before PCB layout.
3. Record raw EDA with timestamp, contact-quality and calibration metadata.
4. Run repeatability / signal-quality tests; assess BLE on mobile.
5. Solicit specific customer requirements and quote a paid feasibility pilot.

## 2026-11-03 evening: research and software package prepared

- The user clarified that **Google Drive SBT/03 is the partner-facing collaborative workspace**; this repository remains the technical versioned source and may currently be public. The private SBT/01, /02 and /04 health records are not partner-shared.
- LeapSpace (Elsevier) is the **scientific literature/research lane**, not assumed to have GitHub or hardware/code execution access. No Deep Research run has been started or completed by this update.
- Research prompts and evidence-acceptance contract: `research/LEAPSPACE_BRIEF_2026-11-03.md`.
- Complete Android/iOS software is a proposed **phase-wise MVP**, not an implemented or committed product. Scope: independent BLE raw EDA capture, contact quality, local session logs, export; no diagnosis or ZYTO virtual-item reverse engineering. See `docs/SOFTWARE_MVP.md`.
- Commercial first gate: next meeting should yield an explicit customer pain, written pilot acceptance criteria, and payer/budget hypothesis (see `docs/CUSTOMER_PILOT_QUESTIONS.md`).
- External evidence: https://zyto.com/hand-cradle/ (GSR / USB); https://zyto.com/about/ (existing ZYTO mobile offerings). Do not market mobile-only as novel.
- Next: owner launches independent LeapSpace queries, shares exported report with team via private SBT/03; review primary sources and choose lowest-cost bench GSR test before coding full mobile app.

- 2026-11-03 partner-facing editable Google Doc, created and verified under SBT/03: https://docs.google.com/document/d/1T9da1qlidI-9XIGKy2es-zZx0JvZz3y1ia3Ph8rnRk8/edit (includes research queries, software phases, and customer gate). This is a derived collaboration copy, not evidence that LeapSpace ran.
