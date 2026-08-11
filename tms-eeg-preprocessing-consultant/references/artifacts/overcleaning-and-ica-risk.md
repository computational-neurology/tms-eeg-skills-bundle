---
type: artifact-card
id: overcleaning-and-ica-risk
title: Overcleaning And ICA Risk
tags:
  - caution:overcleaning
  - step:ica
---

## What It Is

Loss or distortion of real evoked activity due to aggressive component rejection, projection, filtering, or interpolation.

## Why It Matters

TMS-EEG preprocessing can create plausible-looking waveforms while removing condition-relevant signal. Systematic comparisons indicate that ICA-using pipelines tend to produce smaller TEP amplitudes across all peaks, including early (N15/P30) and late (N100/P180) components, not only in windows adjacent to artifact. This points to a global suppressive effect of ICA-based cleaning that is not restricted to artifact-contaminated latencies.

## Detection Clues

Large pre/post changes in TEP morphology, removed components with evoked timing, rank loss, and condition-specific cleaning effects. Note that varying a single decay-suppression method (FastICA vs. SOUND vs. model-based detrending) can change both early TEP amplitude and topography even when late windows converge (Rogasch et al. 2022); systematic topography shifts compromise source interpretation.

## Undercleaning Is The Mirror Risk

ICA also fails in the other direction, and at measurable rates. After a two-pass FastICA pipeline, TMS-evoked scalp muscle activity was still visible in the uncleaned 5-15 ms window in 62.1% of individuals following prefrontal stimulation, 34.5% following premotor, and 0% following parietal (Biabani et al. 2024). Corroborating signs at prefrontal: the first principal component of early TEPs explained only 44% of variance versus 89% premotor and 72% parietal, and spatial correlation between the muscle and no-muscle subgroups dropped sharply across the first ~80 ms.

The mechanism is known — the high amplitude and time-locked nature of muscle artifact violates ICA's assumptions, so components can be incompletely separated in either direction. Rate of failure scales with how lateral and how muscle-rich the target is.

**Reusable QC design.** Split participants by presence or absence of visible muscle activity in the *uncleaned* 5-15 ms epochs, then compare cleaned group-level TEPs and spatial correlations between subgroups. If cleaned results diverge, the cleaning is not doing what it claims. Biabani et al. used this both to quantify distortion and to show that site-specificity of early TEPs was *not* an artifact of it, by re-running on the `n = 9` subgroup with no visible muscle at any site. Start the window at 5 ms — amplifiers may be offline for up to 5 ms post-TMS and pulse ringing persists at that latency.

## Mitigation Options

Transparent component decisions, before/after plots (compare topographies, not only amplitudes), conservative thresholds, sensitivity checks (vary rejected-component count and SSP-SIR projection count), and explicit retained-rank reporting. For frontal and lateral targets, add the muscle vs no-muscle subgroup check above before interpreting early-window topographies or source estimates.

## Pipeline Implications

Every cleaning step needs QC and a record of decisions. When comparing results across studies, account for the systematic ICA amplitude-suppression effect before attributing amplitude differences to physiology.

## Interpretation Caveats

Null results after heavy cleaning may reflect preprocessing suppression rather than absence of cortical response; large early responses in ICA-light pipelines may reflect residual artifact. Amplitude comparisons across studies with different cleaning strategies are not straightforward.

## Sources

`papers/methodological-choices-matter.md` (systematic pipeline comparison); `papers/rogasch-designing-comparing-cleaning.md`; `papers/atti-2024-ica-accuracy.md`; `papers/rogasch-2014-ica-artifacts-network-properties.md`; `papers/biabani-2024-sensory-inputs-three-sites.md` (residual-muscle rates and the subgroup QC design).
