---
type: target-card
id: dlpfc
title: DLPFC TMS-EEG Planning
tags:
  - target:dlpfc
  - muscle-artifact
  - sensory-confounds
---

## Planning Focus

DLPFC is scientifically important but artifact-sensitive. Target subregion, coil orientation, muscle artifact, masking, and sensory controls should be planned before acquisition.

## Risks

- craniofacial and scalp muscle artifacts
- auditory/somatosensory confounds
- weak early local TEP
- target-specific reliability differences
- interpreting N100/P200 as direct cortical activation

## Coil Orientation

Do not automatically use a 45-degree coil orientation for DLPFC. The 45-degree convention is a
practical rule for M1; a common optimal orientation across subjects is only well supported at
M1 and primary somatosensory cortex. DLPFC sits in frontal cortex, where gyral folding is
variable between individuals, so the optimal orientation is subject-specific (Gomez-Tames et
al. 2018).

Set DLPFC orientation from the individual anatomy and the resulting E-field distribution - aim
for an induced current approximately perpendicular to the target sulcal wall / gyral crown -
then refine with online TEP/artifact monitoring. Tools that help with individualized targeting
and E-field visualization:

- Nexstim NBS / SmartFocus nTMS neuronavigation with real-time E-field visualization
  (`repos/nexstim-efield-navigation.md`).
- NIBS-style E-field modeling tools, primarily SimNIBS (`repos/simnibs.md`).
- SlicerTMS for real-time visualization and navigation (`repos/slicertms.md`).

See `targeting/coil-orientation-and-intensity.md` and `targeting/neuronavigation-and-efield.md`
for the full orientation/position workflow.

## Expected Burden, Quantified

Prefrontal cortex is the worst of the commonly studied non-motor sites on every sensory and artifact axis simultaneously (Biabani et al. 2024, `n = 135`, prefrontal vs premotor vs parietal):

| | Prefrontal | Premotor | Parietal |
|---|---|---|---|
| Residual muscle artifact surviving ICA | **62.1%** of individuals | 34.5% | 0% |
| Perceived click loudness | highest (despite **lowest** intensity) | mid | mid |
| Twitch / discomfort / pain ratings | highest | mid | lowest |
| White-noise masking effectiveness | worst | good | best |
| N100/P200 amplitude | largest | mid | smallest |
| Early-TEP PC1 variance explained | **44%** | 89% | 72% |

Two planning consequences. First, expect roughly **two in three participants** to carry residual muscle artifact into the cleaned early window here — budget for it at acquisition (coil angle and position adjustment, online inspection of the 5-15 ms window) rather than planning to remove it with ICA afterwards. Second, the largest N100/P200 at this site is partly a sensory effect, not a physiological one: it tracks the sensory ratings, so a DLPFC-versus-other-site amplitude difference is expected from sensation alone.

Early TEPs at this site remain **site-specific and unaltered by auditory masking** — the site-specificity is real, confirmed on the subgroup with no visible muscle activity — but their **topography is unreliable in the majority of individuals**. Plan an early-window analysis here only with a pre-registered muscle vs no-muscle subgroup check on uncleaned epochs.

## Practical Advice

Use online TEP monitoring to find a target/orientation with interpretable early local responses and manageable muscle artifact. Record blinks before DLPFC sessions when ICA will be used. Consider backup medial/posterior or lower-muscle target options if anterior/lateral DLPFC is too contaminated.

For muscle artifact, inspect single trials and short averages for a focal high-frequency, biphasic/MEP-like response near frontal, temporal, jaw, or facial channels. If this dominates the first `10-20 ms`, plan in advance whether preprocessing will remove/interpolate the earliest interval or use projection/SSP-SIR-style recovery; do not design an endpoint that depends on samples you expect to interpolate.

**The early muscle-artifact peak is not the participant's muscle twitch — track them separately.** DLPFC is a non-motor target, so on most pulses there is no visible/felt limb or facial twitch to warn you. The thing you can actually see is the *muscle-artifact peak in the EEG*: an early, bipolar/MEP-like deflection that emerges after the TMS-pulse artifact, at latencies later than `~4 ms`, and is strongest over frontal/temporal/jaw/facial channels. In the low-trial online average this early bipolar peak is frequently the *only* time-locked activity you can see — the genuine early local TEP is smaller and often buried under it. Do not read that peak as cortical activation, and do not assume "the participant was comfortable / did not twitch" means the early window is muscle-free: the felt twitch is a comfort/compliance issue, whereas this early bipolar peak is an EEG contaminant that masquerades as an early cortical (i-TEP) response and must be minimized (coil rotation/position, intensity) or handled in preprocessing on its own terms.

## Sources

Gogulski 2024 DLPFC reliability/mapping; Gomez-Tames et al. 2018 coil-orientation atlas (`papers/gomez-tames-2018-atlas-optimal-coil-orientation.md`); Maki 2011 muscle projection; Biabani et al. 2019; `papers/biabani-2024-sensory-inputs-three-sites.md` (site-burden table); local good-practice note.
