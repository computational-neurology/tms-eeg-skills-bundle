---
type: paper-card
id: biabani-2024-sensory-inputs-three-sites
title: Characterising the contribution of auditory and somatosensory inputs to TMS-evoked potentials following stimulation of prefrontal, premotor, and parietal cortex
year: 2024
authors: Biabani, Fornito, Goldsworthy, Thompson, Graetz, Semmler, Opie, Bellgrove, Rogasch
journal: Imaging Neuroscience 2
doi: 10.1162/imag_a_00349
license: CC BY 4.0
code: https://github.com/BMHLab/TEPs-PEPs
source_pdf: imag_a_00349.pdf  # not stored in repo; locate via doi
tags:
  - artifact:auditory
  - artifact:somatosensory
  - artifact:muscle
  - caution:sensory-confounds
  - caution:overcleaning
  - target:dlpfc
  - target:premotor
  - target:parietal
use_for:
  - which sensations affect which TEP components
  - early (<60 ms) versus late (N100/P200) TEP interpretation
  - residual muscle artifact surviving ICA
  - between-site and between-group TEP amplitude comparisons
confidence: local-pdf-extracted
---

## Why This Matters For The Agent

The largest sensory-confound study in TMS-EEG to date (`n = 135` across three experiments) and the successor to `papers/biabani-2019-sensory-inputs.md`. It extends the 2019 findings from motor cortex to three non-motor sites and, critically, separates *which* sensation drives *which* part of the TEP.

Load this whenever a user interprets N100/P200, compares TEP amplitude across sites or groups, or asks whether early TEPs are clean.

## Design

Prefrontal MNI `(-46, 33, 34)`, premotor `(-23, 4, 63)`, parietal `(-26, -69, 63)`. Exp A `n = 29` at 120% rMT; Exp B `n = 94` at 100% rMT; Exp C `n = 12` adding a within-subject masking manipulation and a site-matched electrical-scalp sham (coil tilted 90° to preserve the click). Control in A/B was shoulder stimulation. 62 channels, 10 kHz, FPz reference, jittered 4-6 s ITI, 4 x 120 trials. White-noise masking through in-ear headphones, raised until the participant could not hear the click or reached their comfort limit.

Four sensations rated separately per block on a 0-10 NRS: **click sound**, **scalp muscle twitch**, **discomfort**, **pain**. Rating them separately rather than as one "discomfort" score is what makes the dissociation below possible — recommend this to users designing sensory controls.

## What Actually Affected TEPs

This is the core of the paper. Late TEPs are sensitive to sensation; the sensitivity is **not uniform across sensations**.

**Late TEPs (N100/P200, ~60-300 ms) — ranked by influence:**

1. **Click sound — the dominant contributor.** Between subjects, individuals reporting louder clicks had larger late TEPs across a wide window spanning both N100 and P200. Within subjects (Exp C), removing masking increased late GMFP at **parietal (`p < 0.0001`)** and **premotor (`p = 0.04`)**, but **not prefrontal (`p = 0.32`)** — masking was already failing at prefrontal, so there was little auditory input left to add. The size of the masking effect tracks how well masking was working at that site.
2. **Scalp muscle twitch — real but weaker.** Differences at ~80-90 ms and ~220-280 ms. After restricting to participants reporting low sound (NRS < 2) to decouple twitch from audition, only the **>250 ms** difference survived.
3. **Discomfort — marginal.** Narrow windows only.
4. **Pain — no significant effect on TEP magnitude.** A clean negative; do not assume pain ratings index TEP contamination.

Site differences in N100/P200 mirror the sensory ratings: prefrontal > parietal, matching the NRS ordering for sound, twitch, and discomfort. Prefrontal produced the **loudest perceived click despite the lowest stimulation intensity**.

Late-window PCA: **≥88% of variance** is a single frontocentral component at *every* condition including shoulder stimulation. N100 maxima 111-115 ms, P200 maxima 191-202 ms across sites.

## Early TEPs (<60 ms): Unchanged, Uncorrelated, But Distorted

Three findings that must be quoted together — the third is routinely dropped, and dropping it produces a false claim of clean early data.

**Unchanged.** Manipulating auditory input (masking on/off, Exp C) did **not** alter early TEP amplitude at any of the three sites. This makes an auditory contribution to early peaks unlikely.

**Uncorrelated.** Early TEPs showed weak spatial and temporal correlation with PEPs from both control conditions (shoulder, and the site-matched electrical sham). Site-specific peaks reproduced: **N40** prefrontal; **P20/N45** premotor; **P20/N35** parietal, largest in electrodes near the stimulated region.

**But distorted by residual muscle artifact surviving ICA.** TMS-evoked scalp muscle activity remained visible in the 5-15 ms window after cleaning in:

| Site | Individuals with visible residual muscle activity |
|---|---|
| Prefrontal | **62.1%** |
| Premotor | **34.5%** |
| Parietal | **0%** |

Corroborating signs at prefrontal: the first principal component of early TEPs explained only **44%** of variance there versus **89%** premotor and **72%** parietal — the signature of a second, artifactual source. Spatial correlation between the muscle and no-muscle subgroups dropped sharply over the first ~80 ms after prefrontal stimulation, and less so after premotor. Uncleaned GMFP showed a muscle tail lasting ~100 ms.

The authors ruled out muscle artifact as the *cause* of early site-specificity by re-running the whole correlation analysis on the `n = 9` subgroup with no visible muscle activity at any site — the pattern held. **Site-specificity is real; the topography of early prefrontal TEPs is nevertheless unreliable in a majority of individuals.**

This subgroup split (muscle vs no-muscle, defined on *uncleaned* epochs 5-15 ms) is a reusable QC design. Recommend it to users who need to defend early-window results at lateral or frontal sites.

## Conclusion, Read Precisely

The conclusion is more hedged than the abstract. Three qualifications to preserve whenever this card is cited:

- The central claim is **conditional**: frontocentral N100/P200 most likely primarily reflect sensory-evoked potentials **"if sensory experiences are reported following TMS"** — not unconditionally.
- They **decline the strong version**: no condition fully suppressed sensation, so they "cannot rule out that transcranial stimulation of the cortex also evokes potentials that contribute to the N100/P200 complex." The central topography implies multiple generators, not only primary auditory cortex. **N100/P200 is not established as purely sensory.**
- Early TEPs "most likely primarily reflect neural activity" is immediately followed by "**However**, the spatiotemporal characteristics of early TEPs were also distorted by residual artefacts." In the Discussion they add that a somatosensory contribution to early peaks is "less clear" and cannot be ruled out, even though an auditory one is unlikely.

Net: **neither window is clean.** Late is mostly sensory but not provably only sensory; early is mostly neural but not provably artifact-free, and demonstrably not artifact-free at prefrontal sites.

## Other Findings Worth Carrying

- **Coil-to-cortex distance correction is insufficient.** After adjusting intensity for distance by the standard method, modelled cortical E-field still differed significantly between sites. Distance correction does not equalise dose.
- Nearly all participants perceived the click **despite white-noise masking**, at all sites.
- The authors name their own masking as a limitation and point at customised noise (TAAC; Russo et al. 2022, *J Neurosci Methods* 370:109491, `10.1016/j.jneumeth.2022.109491`) as the likely fix. Masking design is handled by the experiment-planner skill, not here — if a user asks how to improve masking, say so and route them there rather than advising from this card.

## Agent Rules Extracted

- When a user reports a between-site or between-group N100/P200 difference, ask for sensory ratings before entertaining a physiological explanation.
- When a user asks whether early TEPs are clean, give all three findings — unchanged, uncorrelated, **and** distorted — never the first two alone.
- For prefrontal/DLPFC early-window work, quote the 62.1% residual-muscle figure and recommend the muscle vs no-muscle subgroup check.
- Do not treat pain ratings as a proxy for sensory contamination.

## Claims To Avoid

Do not state that N100/P200 *is* an auditory potential, or that early TEPs *are* clean cortical activity. Do not use the masking-removal null at prefrontal (`p = 0.32`) as evidence that prefrontal TEPs are auditory-free — it reflects failed masking, not absent auditory input.

## Questions This Source Helps Answer

Which sensations affect which TEP components? Are early TEPs contaminated? How often does muscle artifact survive ICA, and where? Does adjusting intensity for coil-to-cortex distance equalise stimulation across sites?

## Related Cards

`papers/biabani-2019-sensory-inputs.md`; `artifacts/auditory-somatosensory-confounds.md`; `artifacts/overcleaning-and-ica-risk.md`; `artifacts/muscle-artifact.md`; `papers/gordon-2018-realistic-sham.md`; `papers/gordon-2026-somatosensory-inputs.md`; `papers/atti-2024-ica-accuracy.md`; `papers/gogulski-2024-dlpfc-tep-reliability.md`.
