# SBT — Q4-R + Q8 primary evidence review — 2026-11-05

**Status:** The two owner-executed LeapSpace reports are **RECEIVED** and have been checked against select original primary sources. `SOURCE_VERIFIED_PARTIAL`, **NOT** `SCIENTIFICALLY_ACCEPTED`, `HARDWARE_VALIDATED` or `MEDICAL_CLAIM_APPROVED`. Source PDF files stay in private/collaborator Drive, not copied to public GitHub.

## Receipt, provenance and issue status

- **Q4-R:** [Electrodermal activity wearable textile gloves](https://drive.google.com/file/d/1VAcpQh8jITp01oSUaZwF6MuxLJK1EUDO/view), created 2026-11-05 11:20:57 UTC; 10-page report; research session URL printed in PDF: https://www.sciencedirect.com/leapspace/conversation/10845ac2-8a6d-4d2f-bcb6-80327495ed93
- **Q8:** [Reproducible EDA instrument test methods](https://drive.google.com/file/d/1x_ZXhDxgN5rpOwNG1Fjl8SSUnA-a82gU/view), created 2026-11-05 11:24:25 UTC; 10-page report; research session URL printed in PDF: https://www.sciencedirect.com/leapspace/conversation/11fa28fc-07b2-4562-9680-9b18d8e95ef4
- **LeapSpace access restriction:** owner-provided screenshot shows `We detected unusual activity` after manual prompt use. The owner says work was possible through Q8 and further jobs were blocked; provider cause/rate limit not known. Don't infer automated user behavior or attempt to evade detection. No Q9–Q11 result received as of the checked Drive listing.
- Archival folder: https://drive.google.com/drive/folders/1a_X07p0qbQVS43aQKWwnH-vdXhkrKm7c

## Q4-R: independent primary-paper cross-check

**Paper:** Lanatà A., Valenza G., Scilingo E. P., (2012), *A novel EDA glove based on textile-integrated electrodes for affective computing*, `Medical & Biological Engineering & Computing`, DOI [10.1007/s11517-012-0921-9](https://doi.org/10.1007/s11517-012-0921-9). [PubMed PMID 22711069](https://pubmed.ncbi.nlm.nih.gov/22711069/); [open institutional record](https://flore.unifi.it/handle/2158/1192174).

**Source-supported setup and measured results (full primary text checked, not copied):**
- A **real Lycra glove** with integrated fingertip electrodes, not merely loose textile contact pads. Four fingertips equipped, but index and middle fingers were used in the experimental measurement (original **Fig. 1**, *Methods* §2.2).
- Textile electrode area **1 × 1 cm**; fibers **80% polyester + 20% stainless steel** (*Methods* §2.3.1 and *Results* §3.1). These are attributes of *that paper's* prototype, not an approved SBT BOM.
- The authors used **0.5 V DC** for EDR acquisition, and a **Biopac MP35 reference sampling at 1 kHz** to compare textile versus conventional Ag/AgCl electrode signals. Crossed-finger electrode placement and low-pass filtering were part of the comparison (*Methods* §§2.1, 2.3.2).
- Reported **Spearman correlation** for textile vs standard electrode EDR: tonic **0.957 ± 0.024**, phasic **0.995 ± 0.001**, whole crossed-finger EDR **0.960 ± 0.031** (*Results* §3.1). These normalized waveform correlations do **not** establish absolute conductance bias, electrical safety or movement stability of the future SBT prototype.
- **35 healthy participants aged 21–24** were enrolled in a *separate affective-image classification experiment* using the glove (*Methods* §2.4.1). **Do not misattribute N=35 to the electrode-agreement comparison**, whose subject N is not demonstrated by that number.
- The authors explicitly said examining **motion-artifact effects during dynamic tasks was future work** (*Discussion*). Hence no validated walking/hand-flexion artifact budget can be inferred from this study.

**Correction to LeapSpace:** Q4-R PDF confirms a 2012 glove study but reports that its DOI, N and design specifics are not recoverable from its evidence set. These are **not unavailable in the original source**; several are directly extractable as above. The paper is useful proof of a historical concept but does not certify the planned SBT glove.

**Open Q4 limitations:** no comparator Bland–Altman limits, no demonstrated multi-size fit/force sensitivity, no quantified movement artifact across participants, and no approved human-use safety process for an SBT design. Continue `Q9` (motion/contact) when the provider restriction permits, but bench fixture evaluation can be scoped now.

## Q8: independent primary-paper cross-check

**Paper:** Geršak G. & Drnovšek J. (2020), *Electrodermal activity patient simulator*, `PLoS ONE`, DOI [10.1371/journal.pone.0228949](https://doi.org/10.1371/journal.pone.0228949), [full open HTML with figures](https://pmc.ncbi.nlm.nih.gov/articles/PMC7001969/), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32023317/).

**Source-supported circuit and test facts:**
- A programmable, optically controlled variable resistance with an **artificial conductive-finger hand** was built to emulate EDA **SCL** and **SCR**. This is a *simulator/test fixture*, not a validated wearable sensor architecture.
- **100 kΩ fixed resistor = 10 µS** built-in calibration condition (original **Fig. 9**). The original also shows a **54 kΩ ≈ 18.5 µS** fixed comparison (Fig. 4), and reviewer-added measurements for **10 µS** and **4.5 µS** fixed states (original peer-review material).
- Simulator range: approximately **up to 20 µS**, with proposed SCR amplitudes **0.25 µS and 0.5 µS**, frequencies **5, 10 and 20 per minute** (**Figs. 5, 10–11**). Exact output depends on optocoupler limitations and selected device.
- The authors describe **after-transient output stability ~0.05 µS** in one prototype evaluation and optocoupler **latency up to 100 ms**. They note light-dependent resistance and temperature sensitivity as limitations, so these are **reported case-specific performance**, not SBT or industry pass/fail values.
- The original paper includes a discussion of error/uncertainty against simulated output. Without copying their specific apparatus and reference calibration, no general **SBT measurement accuracy** can be inferred.

**Correction to LeapSpace:** Q8 PDF states the two seeded DOIs' paper methods could not be recovered and concludes every requested datum is unverifiable from its *retrieved record*. The PLOS open primary full text demonstrably includes the 100 kΩ condition, simulator architecture, dynamic waveform settings, and figures. This is a **retrieval/coverage failure** of the specific LeapSpace run, not evidence that no metrology methods exist.

**Second seeded DOI:** Montgomery et al., EmotiBit (2024), DOI [10.1016/j.measen.2024.101075](https://doi.org/10.1016/j.measen.2024.101075), [publisher abstract](https://www.sciencedirect.com/science/article/pii/S2665917424000515). Bibliographic identity and physiological device-comparator objective verified. Its exact resistor-sweep calibration and specific error percentages have **not** been checked against full methods/figures, so keep `SOURCE_PENDING` for these claims.

## Decision impact

1. **Feasible concept:** A real glove-based EDA sensor has precedent; does **not** eliminate contact/mechanical/ambient artifact risk or prove SBT diagnostic value.
2. **Smallest verifiable engineering action:** use physical precision resistance standards, and only after that a controlled artificial dynamic EDA stimulus for *bench-only* repeatability tests. See `docs/GSR_BENCH_VALIDATION_DRAFT_2026-11-05.md`.
3. **Status:** Q4-R and Q8 both `RESULT_RECEIVED / SELECTIVE_PRIMARY_SOURCE_CHECK_PASSED / FULL_ACCEPTANCE_PENDING`. Q9, Q10, Q11 remain prepared/not received. No further Deep Research launched.
4. **Safety and privacy:** no human contact or charging-connected subject measurements without electrical safety and data protection review; proprietary ZYTO software and personal medical reports remain outside public repo and external AI systems.
