# Current state — 2026-11-03

## 2026-11-03 latest research receipt — Q1 report delivered

- The owner placed a **14-page LeapSpace research PDF (46 references)** in [Drive SBT/03 / Leadspace](https://drive.google.com/drive/folders/1a_X07p0qbQVS43aQKWwnH-vdXhkrKm7c). This is a real research output, replacing the earlier status of `no SBT Q1 PDF located`; [source PDF](https://drive.google.com/file/d/12q_RhdfrQzGpxOQ2Hcd0noWhSUeH7EWr/view?usp=drivesdk).
- `LS-SBT-Q1-20261103-01`: `RESULT_RECEIVED / PARTIAL_SOURCE_REVIEW / SCIENTIFIC_ACCEPTANCE_PENDING`. Selected DOI abstracts and publisher/university bibliographic records checked; not all references, sample sizes or complete paper methods independently reviewed.
- Main direction to **test**, not a fixed engineering decision: finger/palm reference, textile finger/glove concept, and dry wrist comfort candidate. Glove-specific live movement equivalence is not proven; numeric bench go/no-go criteria and electrical safety plan remain open.
- Audit detail: `research/EVIDENCE_AUDIT_2026-11-03.md`; original Q1 handoff and result receipt: `research/LEAPSPACE_Q1_RUN_2026-11-03.md`. Q2-Q4 remain planning stage.
- No new SBT mobile firmware/app, hardware benchmark, consumer health claim, LGW run result, business contract or ZYTO interoperability established by the PDF.

## 2026-11-03 — CURRENT COORDINATION UPDATE (LATEST OWNER DIRECTIVE)

- Owner now explicitly requests **TRE ChatGPT to coordinate the next SBT research, bounded development task definition/review, and commercial validation from the present conversation**. This updates the 20:44 owner routing note **only for coordination**. SBT is still an **independent product/project** and `tamaspota/SBT` remains the technical authority; the repo is not folded into TRE.
- LGW remains the **designated technical executor**, but actual accepted LGW task IDs, commits and tests are not verified in this session. TRE must not assume a job has started or bypass LGW dispatch/safety.
- First evidence review is saved in `research/EVIDENCE_AUDIT_2026-11-03.md`: two wrist/palm studies and methodological guidance checked via DOI/abstract, one artifact paper has a 2026 editor's note requiring review. No complete SBT LeapSpace report accepted.
- Existing Q1 LeapSpace "Retrieved references: 0" is a search failure, **not** negative evidence. No validated glove-comparator study, safe electronic front-end, real BLE/mobile application, commercial buyer or ZYTO interface has been established.
- Nine additional screenshots were received in chat, but not individually accessible as files in the connected file list; their contents are not interpreted or treated as verified scientific results.
- Next: verify additional research exports and DOI paper methods; select bench-only sensor measurement contract and ask SBT collaborators the minimum paid pilot problem/acceptance; hand a bounded approved implementation packet to LGW only when needed.

## 2026-11-03 20:44 CET — OWNER CORRECTION: SBT IS A SEPARATE PROJECT (CURRENT)

- SBT is an **independent project**, intended to have its own ChatGPT Project context. Its creation/configuration in ChatGPT has **not been verified in this session**; do not claim a new ChatGPT Project was created by this repository edit.
- **SBT owns its research, hardware/firmware, mobile software design, technical decisions, tests and day-to-day project coordination.** Canonical technical memory and source: `tamaspota/SBT`.
- **LGW is the owner-designated SBT technical executor / workstream.** The owner reports LGW is working on SBT; no LGW task ID, run status, output, approval or performance result was independently verified here. Actual execution must comply with `tamaspota/local-gpu-helper` dispatch, safety and permission gates.
- **TRE remains involved only as a cross-project business/commercial partner** for SBT customer discovery, paid-pilot qualification, offer/conversion preparation and agreed handoffs. TRE does **not own or replace** the SBT project or direct its general technical work.
- Shared collaborator-safe docs belong to owner-controlled SBT Drive/03; sensitive ZYTO reports, medical data and private files remain segregated. Public/private GitHub and collaborator access must be checked before changing them; no visibility or sharing change is authorized by this log.
- Research/LeapSpace input and validated evidence stay attributable to SBT. The older TRE-only project-routing instruction below is **superseded** by this later, explicit owner instruction.
- Next action: when the separate SBT ChatGPT Project exists, bootstrap it from this CURRENT_STATE, DECISIONS, AGENTS.md and research/LEAPSPACE_BRIEF_2026-11-03.md; reconcile any LGW work by verified task IDs/commits before marking it complete.

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

## 2026-11-03 — Historical TRE handoff (SUPERSEDED at 20:44 CET)

**Historical owner direction, since superseded:** coordinate SBT product and research development **only through the TRE ChatGPT project**. This does not move SBT source code into the TRE repo: `tamaspota/SBT` remains canonical for technical implementation, tests, scientific acceptance and project decisions; TRE drives feasibility, user/payer discovery, research review and task routing; Drive SBT/03 remains the partner-facing workspace. LGW is not independently authorized to START SBT code tasks from its own chat; it may be a bounded TRE-selected executor only after normal LGW admission and resource safety.

**LeapSpace observed limitation:** owner created SBT and PhD projects, but reports new project conversations disappearing/losing project continuity; screenshot also shows SBT recent conversations, so persistence failure is **reported, not independently reproduced**. Composer restricts input to 500 characters. One Q1 EDA query returned `Retrieved references: 0`; no conclusions on EDA literature or electrode superiority may be drawn. Do not rely on the LeapSpace project for durable research history; export and verify original studies/DOIs externally. TRE handoff including exact prompt: [tamaspota/TRE/docs/SBT_LEAPSPACE_HANDOFF_2026-11-03.md](https://github.com/tamaspota/TRE/blob/main/docs/SBT_LEAPSPACE_HANDOFF_2026-11-03.md).

**Current technical stage unchanged:** independent, non-diagnostic mobile GSR/EDA bench feasibility only. No sensor design selected, validated prototype, commercial customer, Deep Research evidence, BLE build or ZYTO compatibility proven by this handoff. Next research gate is reproducible electrode comparison with a falsifiable, safe bench/volunteer protocol, reviewed DOI literature and customer pilot acceptance criteria.

