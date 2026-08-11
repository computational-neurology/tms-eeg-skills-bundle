---
type: artifact-card
id: auditory-somatosensory-confounds
title: Auditory And Somatosensory Confounds
tags:
  - artifact:auditory
  - artifact:somatosensory
  - caution:sensory-confounds
---

## What It Is

TEP activity partly driven by TMS click, scalp sensation, cranial muscle activation, expectation, or sham-control differences.

## Why It Matters

Several TEP components and condition differences can include sensory-evoked contributions rather than direct cortical effects at the target.

## Detection Clues

Similarity to auditory/somatosensory control responses, broad scalp topographies, condition differences in click/sensation, and late components such as N100. Spatial correlation between peripherally evoked potentials and TEPs emerges from roughly 60 ms post-pulse; components earlier than ~60 ms show little spatial overlap and are more likely to reflect direct cortical activity, though the N45 can still carry some sensory contribution (Biabani et al. 2019). The ~60 ms boundary replicated across three non-motor sites and two stimulation intensities in `n = 135` (Biabani et al. 2024), where ≥88% of late-window variance was a single frontocentral component in every condition including non-cortical shoulder stimulation.

## Which Sensation Affects Which Component

Sensory sensitivity is not uniform across sensations. Ranked by influence on late (N100/P200) amplitude (Biabani et al. 2024):

1. **Click sound — dominant.** Larger late TEPs in individuals perceiving louder clicks; removing masking raised late GMFP at parietal (`p < 0.0001`) and premotor (`p = 0.04`).
2. **Scalp muscle twitch — weaker but real.** Effects at ~80-90 ms and ~220-280 ms; only the `>250 ms` effect survived once sound was controlled for.
3. **Discomfort — marginal**, narrow windows.
4. **Pain — no significant effect on TEP magnitude.** Do not treat pain ratings as a proxy for sensory contamination.

Masking efficacy is site-dependent, so the *size* of any masking effect reflects how well masking was working at that site rather than how much auditory input that site generates. At prefrontal cortex, removing masking changed nothing (`p = 0.32`) because white-noise masking was already failing there — this is not evidence of low auditory contamination. Ask for four separate ratings (sound, twitch, discomfort, pain) rather than one combined discomfort score.

## Mitigation Options

Masking noise, realistic sham, sensory control conditions, active control targets, trial-level covariates, contrast/subtraction strategies such as auditory ERP subtraction when justified, and cautious interpretation. Among ICA, linear regression, and SSP-SIR for sensory-component removal, SSP-SIR offers the best tradeoff: it suppresses sensory contributions while better preserving non-sensory signal, whereas ICA broadly reduces all TEP peaks and linear regression distorts early source topographies (Biabani et al. 2019). When using SSP-SIR for this purpose, confirm that the projected PCs match peripheral-evoked-potential topographies rather than projecting blindly.

## Pipeline Implications

Preprocessing cannot solve poor controls. Keep condition labels separate and avoid removing sensory components without a defined analysis goal. By default, do not reject auditory/somatosensory-related ICA components; handle them through masking, appropriate condition contrasts, or justified subtraction/modeling.

## Interpretation Caveats

Do not present active-vs-sham TEP differences as direct cortical excitability unless sensory confounds are addressed. Masking reduces but cannot eliminate auditory input: even at maximal masking intensity, subjects still perceive the TMS click (Biabani et al. 2019). Perceptual masking success does not guarantee equivalent neural confounds — N45, N100, and P180 were larger at 90% RMT than at perceptually indistinguishable realistic sham despite active masking (Gordon et al. 2018). Reporting of perceived sensory experience remains rare across the literature, which limits cross-study auditing of sensory control.

Distinguish two claims that are often conflated. That peripherally evoked potentials (PEPs) **overlap and add to** TEPs is well supported, and PEPs can dominate later components. Whether sensory input additionally **modulates (interacts with)** the direct cortical response is a separate question: using saturated and individually PEP-matched shams, no significant PEP–TEP interaction was found within ~110 ms post-stimulation for M1 or SMA, supporting removal of PEPs by matched-sham subtraction (Gordon et al. 2026). The practical implication is that a well-matched sham can be subtracted to isolate the cortical TEP, but this does not license treating un-subtracted late components as artifact-free cortical activity, and the null-interaction result should not be over-extended beyond the tested window or targets.

Do not extend "early TEPs are more cortically specific" into "early TEPs are clean". In the same dataset, residual TMS-evoked scalp muscle activity survived ICA in 62.1% of individuals after prefrontal stimulation and 34.5% after premotor, distorting early topographies while leaving site-specificity itself intact (Biabani et al. 2024). Early-window cleanliness is a separate question from early-window sensory specificity, and must be checked separately — see `artifacts/overcleaning-and-ica-risk.md`.

## Sources

Biabani et al. 2019; `papers/biabani-2024-sensory-inputs-three-sites.md`; Gordon et al. 2018; Gordon et al. 2026; `papers/methodological-choices-matter.md`; TMS click masking workflow.
