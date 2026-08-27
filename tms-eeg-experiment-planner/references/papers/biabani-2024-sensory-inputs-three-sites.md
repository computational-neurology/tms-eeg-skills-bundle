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
  - design:sensory-controls
  - design:sham
  - target:dlpfc
  - target:premotor
  - target:parietal
  - intensity
  - caution:sensory-confounds
use_for:
  - planning sensory controls and what to rate
  - anticipating site-specific sensory and muscle burden
  - intensity matching across stimulation sites
  - deciding whether a planned early-window analysis is viable at a given site
confidence: local-pdf-extracted
---

## Why This Matters For The Agent

`n = 135` across three experiments, three non-motor sites. The largest sensory-confound dataset in TMS-EEG. For planning, it answers three questions: what to measure, what to expect at each site, and whether a planned early-window analysis will survive at that site.

## Design Worth Copying

Four sensations rated **separately** per block on a 0-10 NRS: **click sound**, **scalp muscle twitch**, **discomfort**, **pain**. Rating them separately rather than as a single discomfort score is what allowed the dissociation below. Recommend four separate scales, collected after every block, in any protocol comparing sites, conditions, or groups.

Two control conditions, with different weaknesses:

- **Shoulder stimulation** (acromioclavicular joint, contralateral positioning matched to the coil) — non-cortical, but does not match the scalp location of somatosensory input.
- **Site-matched electrical scalp stimulation** with the coil tilted 90° so the click is preserved — fixes the spatial mismatch. Intensity of the electrical stimulus was titrated per individual to match the sensation of real TMS at that site.

Acquisition: 62 channels, 10 kHz, FPz reference, AFz ground, impedance < 5 kΩ, jittered 4-6 s ITI, 4 x 120 trials, foam under the coil, white-noise masking through in-ear headphones raised until the click was inaudible or the comfort limit was reached.

## What Actually Affected TEPs

Late TEPs are sensitive to sensation, but **not uniformly across sensations**:

1. **Click sound — dominant.** Individuals reporting louder clicks had larger late TEPs across a window spanning N100 and P200. Removing masking increased late GMFP at **parietal (`p < 0.0001`)** and **premotor (`p = 0.04`)**, but not **prefrontal (`p = 0.32`)** — because masking was already failing at prefrontal.
2. **Scalp muscle twitch — weaker but real.** Effects at ~80-90 ms and ~220-280 ms; only the **>250 ms** effect survived once sound was controlled for.
3. **Discomfort — marginal.**
4. **Pain — no significant effect.** Do not treat pain ratings as a proxy for contamination.

Site ordering of N100/P200 amplitude follows the sensory ratings: **prefrontal > premotor > parietal**. Prefrontal produced the **loudest perceived click despite the lowest stimulation intensity**.

## Site-Specific Burden To Plan Around

| | Prefrontal | Premotor | Parietal |
|---|---|---|---|
| Residual muscle artifact after ICA | **62.1%** of individuals | 34.5% | **0%** |
| Perceived click loudness | highest | mid | mid |
| Muscle twitch / discomfort / pain ratings | highest | mid | lowest |
| Masking effectiveness | worst | good | best |
| N100/P200 amplitude | largest | mid | smallest |
| Early-TEP PC1 variance explained | **44%** | 89% | 72% |

Prefrontal is worst on every axis simultaneously. Plan lateral/frontal sessions expecting all of it.

## Early TEPs (<60 ms): Unchanged, Uncorrelated, But Distorted

Three findings that belong together. The third is what determines whether an early-window analysis is viable at the planned site.

**Unchanged** by the masking manipulation at any site — an auditory contribution to early peaks is unlikely.

**Uncorrelated** with PEPs from either control condition. Site-specific peaks reproduced: **N40** prefrontal; **P20/N45** premotor; **P20/N35** parietal.

**But distorted by residual muscle artifact surviving ICA** in 62.1% of individuals at prefrontal (see table above). Site-specificity itself is real — re-running the analysis on the `n = 9` subgroup with no visible muscle activity anywhere preserved the pattern — but the early topography at prefrontal is unreliable in most individuals.

**Planning consequence:** if the study depends on early-window topography or source estimates at a lateral frontal site, budget for it at acquisition — coil angle and position adjustment to reduce muscle activation, online inspection of the 5-15 ms window, and a pre-registered muscle vs no-muscle subgroup check on uncleaned epochs. Do not plan to fix it with ICA afterwards.

## Intensity Matching Across Sites

Coil-to-cortex distance differed significantly across sites (prefrontal shortest, premotor longest). Intensity was adjusted for distance using the standard method — and modelled cortical E-field **still differed significantly between sites**. Distance correction does not equalise dose. If cross-site comparison matters, model the E-field per individual (they used SimNIBS FEM on T1+T2) and normalise, or accept that dose is unmatched and say so.

## Conclusion, Read Precisely

Conditional, not absolute: frontocentral N100/P200 most likely primarily reflect sensory-evoked potentials **"if sensory experiences are reported following TMS."** The authors explicitly decline the strong version — no condition fully suppressed sensation, so a cortical contribution to N100/P200 cannot be ruled out. And the early-TEP verdict carries an immediate "however" about residual artefacts.

Neither window is clean. Plan controls accordingly rather than assuming a window is safe.

## Agent Rules Extracted

- Recommend four separate NRS scales (sound, twitch, discomfort, pain) per block whenever sites, conditions, or groups will be compared.
- Warn that white-noise masking failed to prevent click perception in nearly all participants, worst at prefrontal.
- For frontal/lateral targets, raise the 62.1% residual-muscle figure during planning, not after.
- State that distance-corrected intensity does not equalise cortical E-field across sites.

## Claims To Avoid

Do not present N100/P200 as purely auditory, or early TEPs as clean. Do not cite the prefrontal masking-removal null (`p = 0.32`) as evidence of low auditory contamination there — it reflects failed masking.

## Questions This Source Helps Answer

What sensory measures should a protocol collect? Which site will be hardest for sensory control and muscle artifact? Is an early-window analysis realistic at my target? Does distance-adjusted intensity match dose across sites?

## Related Cards

`design/sham-and-sensory-controls.md`; `targets/dlpfc.md`; `targeting/rmt-vs-tep-threshold.md`; `artifacts/target-specific-artifact-risks.md`; `artifact-appearance/muscle-artifact-appearance.md`; `papers/gordon-2018-realistic-sham.md`; `papers/gordon-2026-somatosensory-inputs.md`; `papers/hernandez-pavon-2023-recommendations-open-issues.md`.
