---
type: guideline-card
id: reporting-tms-rat-mapping
title: TMS-RAT Reporting Standard And Its TMS-EEG Mapping
tags:
  - reporting
  - methods
  - preregistration
  - checklist
  - transparency
source_paper: Székely O, Holmes N P, Ashton J, Breuer F, Chen H-Y, Di Chiaro N V, Duport A, Frangou P, Gwynne L, Hassan U, Lowe C J, Mathias B, Peng N, Pepper J L, Phylactou P, Szymanska M A, Tamè L (2026). Development and validation of the transcranial magnetic stimulation reporting assessment tool (TMS-RAT). Brain Stimulation 19:103155.
doi: https://doi.org/10.1016/j.brs.2026.103155
tool_site: https://tms-rat.org
tool_v1_0: https://tms-rat.org/?page=rat&version=1.0
tool_v1_1: https://tms-rat.org/?page=rat&version=1.1
guidance_pdf: https://tms-rat.org/docs/TMS_Reporting_Assessment_Tool_v1.0_Guidance.pdf
generator: https://tms-rat.org/?page=generator
github: https://github.com/TMSMultiLab/TMSMultiLab/wiki
osf_preregistration: https://osf.io/tywn8
license: paper is CC BY-NC-ND 4.0
validation_scope: afferent conditioning / MEP-recording studies only — NOT validated for TMS-EEG
use_for:
  - writing a TMS-EEG Methods section or preregistration
  - reporting-completeness questions and reviewer responses
  - deciding which reporting items a TMS-EEG protocol must state explicitly
---

## Source

Everything below refers to the **TMS Reporting Assessment Tool (TMS-RAT)**, published as Székely et al. (2026), *Brain Stimulation* 19:103155, <https://doi.org/10.1016/j.brs.2026.103155>. The tool itself, the item definitions, and the ~16,500-word guidance document live at <https://tms-rat.org>, not in the paper. Point users at the site; do not reproduce the guidance document (CC BY-NC-ND, no derivatives).

## Load This Card When

The user asks about reporting, checklists, Methods-section writing, preregistration completeness, reviewer requests for missing methods detail, or names TMS-RAT or the Chipchase checklist.

## The v1.0 / v1.1 Trap — Read First

TMS-RAT ships in two versions with **different jobs**, and picking the wrong one causes a real error.

| Version | Items | Sections | Job |
|---|---|---|---|
| **v1.0** | 72 | 13 (A–M) | **Prospective** — writing your own Methods |
| **v1.1** | 50 | 12 | **Retrospective** — rating published papers in reviews/meta-analyses |

v1.1 is the version with the headline reliability figures (Gwet's AC1 = 0.78, range 0.60–0.99; test–retest AC1 = 0.82, range 0.65–1.0), so it is the tempting one to grab. **Do not write to v1.1.** It was built by deleting 22 items that raters could not reliably agree were reported — including the entire Single Pulse section. Writing to v1.1 means systematically omitting inter-trial interval, number of pulses, and participant-level intensity.

**Always use v1.0 for prospective reporting.** Use v1.1 only when scoring somebody else's paper.

## Validation Scope — State This Whenever Citing

TMS-RAT was developed and validated on **333 afferent-conditioning studies recording MEPs**. The authors state explicitly that it "has not been validated outside the afferent conditioning literature or on studies not recording motor evoked potentials," and name TMS-EEG and TMS-fMRI as requiring additional items in future versions.

Use it as reporting guidance. Never present it as a validated TMS-EEG standard.

Neither version measures methodological quality or risk of bias — only completeness of reporting. A completeness score is not a quality score.

## Which Sections Apply To TMS-EEG

**Apply directly:** `A` Participant Bio · `B` Participant State · `C` Design · `D` Hardware · `E` Locations · `F` Intensity · `G` Single Pulse · `H` Motor Threshold (only when a motor threshold is used for dosing).

**Do not apply** unless the study also records MEPs: `I` Motor Variables · `J` EMG & Muscles · `K` Afferent Stimulation · `L` Conditioning.

**Structural template only:** `M` SEP. Its EEG items are scoped to somatosensory evoked potentials (M2 is "EEG montage *for SEP recording*"), and M3/M4 were cut from v1.1. Useful as a shape to copy, not as coverage.

**Unvalidated, and inconsistent between sources:** the live site serves a 14th section `N` Repetitive (rTMS burst/train parameters, 8 items on-site); the paper describes the rTMS section as 9 items and excluded from validation. Do not assert an item count for `N`; check the OSF supplement if it matters.

## The Numbers Worth Quoting

Field-wide reporting completeness measured with v1.1 is **≈53%**, improving at **β = 0.29%/year** (95% CI 0.12–0.47).

Item-level agreement (Gwet's AC1) for the items closest to TMS-EEG practice:

| Item | AC1 | In v1.1? |
|---|---|---|
| F3 Participant intensity (relative to threshold) | **0.20** | cut |
| G2 Number of pulses | 0.40 | cut |
| G3 Evoked response, raw units | 0.46 | cut |
| C8 Control condition | 0.54 | cut |
| G1 Trial-to-trial interval | 0.56 | cut |
| F2 Machine intensity (%MSO) | 0.58 | cut |
| E1 Head and brain neuronavigation | 0.60 | kept |
| E3 Target location in CNS | 0.64 | kept |
| C9 Sensory attenuation | 0.80 | kept |
| E5 Coil current direction | 0.81 | kept |

**Interpret these correctly.** A low AC1 means raters could not agree *whether the paper reported the item* — it is evidence that the literature reports it inconsistently, **not** that the item is unimportant. The authors make this point themselves. The naïve reading ("cut = optional") is exactly backwards for TMS-EEG: inter-trial interval, trial count, and intensity are among the most consequential parameters we have.

Use this as the evidence base when telling a user to state ISI, trial count, and intensity explicitly rather than by implication.

*Note: Table 3 of the paper prints two confidence intervals whose lower bound exceeds the point estimate (C9 and C2). Cite the point estimates; omit those two CIs.*

## The TMS-EEG Gap

TMS-RAT has no item for the following, all of which a TMS-EEG paper must report:

| Required for TMS-EEG | Nearest TMS-RAT analogue |
|---|---|
| EEG amplifier make/model and software version | J1/J2 (EMG-scoped) |
| Sampling rate and acquisition filter settings | J7 (EMG-scoped) |
| Blanking / sample-and-hold / saturation handling | *none* |
| Reference and ground electrode placement | M2 (SEP-scoped) |
| Impedance or contact target | *none* |
| Electrode type, material, size | J4 (EMG-scoped) |
| Lead routing and orientation relative to coil | *none* |
| Trigger synchronisation method and measured latency | *none* |
| Auditory masking: noise type, level, verification | C9, too coarse |
| Sham type and sensory matching | C8, too coarse |
| Pulse artifact removal/interpolation window | *none* |
| Preprocessing pipeline and version | *none* |
| TEP components, analysis windows, GMFA/LMFP | M3/M4 (SEP-scoped, both cut) |
| Trials delivered vs retained, rejection criteria | G2 (delivered only, cut) |
| Online rt-TEP QC and go/no-go criteria | *none* |

Six of these have no analogue anywhere in the tool. The bundle's own `../templates/experiment-protocol-template.md` already covers all fifteen.

## Proposed TMS-EEG Extension — Ours, Not The Tool's

The following two sections are **this bundle's proposal**, built on the tool's own structure. They are not part of published TMS-RAT and must never be cited as such. They exist because the authors name this extension as needed future work.

**EEG acquisition** — modelled item-for-item on Section J: amplifier make/model; acquisition software and version; skin preparation; electrode type, material and size; montage, reference and ground; sampling rate and acquisition filters. Then the items J has no counterpart for: blanking/sample-and-hold/saturation handling; impedance target; lead routing relative to the coil; trigger synchronisation method and measured latency.

**TEP measures** — modelled on Section M: TEP components or features of interest; TEP values with central tendency and dispersion. Then: pulse interpolation/removal window; baseline window; GMFA/LMFP windows; ROI or channel selection; preprocessing pipeline and version; trials delivered versus retained; rejection criteria.

## Reporting Conventions Worth Enforcing

- **Quantitative items require both** a measure of central tendency (mean or median) **and** a measure of dispersion (SD, SE, CI, IQR, or range). Central tendency alone counts as partial reporting only. This applies to age, height, weight, machine intensity, participant intensity, threshold values, and evoked-response values — and, by extension, to any TEP amplitude or latency reported.
- Scoring is three-level: missing `0`, partial `0.5`, full `1`. TMS-RAT dropped the older Chipchase "reported versus controlled" binary because uptake was poor (only 31% of reviews used it) and it was hard to operationalise.
- The paper recommends attaching the completed sheet and output `.csv` as supplementary material at submission.

## Behaviour Rules

- Use **v1.0** for prospective/writing questions; **v1.1** only for retrospective rating.
- When walking a user through Methods, cover sections A–H plus the two extension sections above; skip I–L unless MEPs are recorded.
- When an item was cut from v1.1, explain *why* (reporting inconsistency, not irrelevance).
- Never report a completeness percentage as a quality judgement.
- Link users to <https://tms-rat.org> for the item definitions and guidance document, and to the geneRATor (<https://tms-rat.org/?page=generator>, in development) for Methods-text generation. Do not reproduce the guidance document.
- State the validation-scope limitation any time the tool is recommended for a TMS-EEG study.

## Related Cards

`../templates/experiment-protocol-template.md`; `../templates/preregistration-methods-template.md`; `guidelines/recommendations-good-practice.md`; `design/study-design-checklist.md`; `design/sham-and-sensory-controls.md`; `papers/hernandez-pavon-2023-recommendations-open-issues.md`.
