---
type: design-card
id: auditory-masking
title: Auditory Click Masking
tags:
  - masking
  - auditory
  - sensory-confounds
  - safety:hearing
use_for:
  - designing and tuning TMS click masking
  - choosing a masking noise type
  - verifying that masking actually worked
  - hearing-safety exposure planning
---

## Purpose

Prevent the auditory evoked potential (AEP) from contaminating the TEP, at the design and acquisition stage. Masking is the alternative to removing the AEP offline, and it is the better one — offline AEP removal by ICA assumes the cortical responses to TMS and to its click are independent and superpose linearly without interaction (Russo et al. 2022). Masking makes that assumption unnecessary.

## Build The Masker From Your Own Click

Generic white noise is not a masker for your click. The TMS click varies significantly across **stimulators**, across **coils**, and sometimes across **intensities**. Record your own, and re-record after any major change to the setup.

Recording procedure (Russo et al. 2022):

- Omnidirectional microphone, no filtering or distortion in the chain.
- Positioned approximately `25 cm laterally` to the coil.
- `96 kHz` sampling, 24-bit.
- Deliver a few TMS pulses into a low-noise, low-reverberation room.
- Cut the audiotrack from the sharp transient until the signal returns to baseline.

> **Safety.** The microphone and every metal object must be outside the magnetic field. Metallic parts within the field can be thrown violently. Treat mic placement as a safety check, not a convenience.

## Noise Architecture

A customised masker mixes two components:

- **Click-based noise (CBN)** — your recorded click, concatenated into a sequence with pseudo-random spacing. Inter-click interval = a fixed latency plus a uniform random draw between a minimum and maximum, in samples.
- **White-based noise (WBN)** — randomly generated white noise, independently resampled to trade high against low frequencies.

The two are mixed by an explicit **white-to-click ratio**, then scaled by a noise volume independent of system volume.

**Broadband shuffling** is the option that produced the best-performing noises: the original click is mixed with eleven resampled copies of itself (factors ≈ ×0.3 to ×2.0), spreading energy across the spectrum around the true click. It deliberately disables separate frequency tuning, which shrinks the parameter space and the time needed to tune per participant.

Two further options: **intensity shuffling** (each click randomly attenuated by a uniform draw up to a set maximum) and **spatial shuffling** (inter-aural delay randomising the virtual source location). Spatial shuffling was **not tested** in the validation study — treat as unvalidated.

Save the parameter set so the same noise can be reproduced across sessions.

## Why Customised Noise Wins

Minimum sound pressure level required to mask the click, `n = 20` (Russo et al. 2022):

| Condition | White noise | Adapted noise | Customised CN1 | Customised CN2 |
|---|---|---|---|---|
| Sham TMS | 81.6 dB | 85.4 dB | **78.3** | **79.0** |
| Real TMS | 87.1 dB | 89.0 dB | **84.1** | **82.9** |

Customised noise masked at lower SPL in **100% of subjects** — 4.1-5.6 dB below white noise and 7.5-7.8 dB below adapted noise, equivalent to a **61-83% reduction in sound intensity**. All pairwise comparisons were significant except CN1 versus CN2.

This matters for hearing safety in long sessions. Maximum permissible exposure at the measured levels:

| Noise | NIOSH | OSHA |
|---|---|---|
| White noise | 5 h | 12 h |
| Adapted noise | 3 h | 9 h |
| CN1 | 10 h | 13 h |
| CN2 | 13 h | 21 h |

## Validate On Real TMS, Never On Sham

**Real TMS requires roughly 6 dB more masking than sham TMS** for the same noise (CN1: 84.1 vs 78.3 dB; condition effect `F(1,19) = 22.18, p < 0.001`). The explanation is bone conduction — during real stimulation the coil vibrates perpendicular to the scalp with a larger contact area.

Consequence: **masking titrated during a sham or coil-tilted setup will under-mask the real condition.** Titrate under real stimulation, at the intensity and coil position you will actually use.

## Titration Procedure

- Deliver pulses at a jittered inter-pulse interval (2000-2300 ms in the validation study).
- Raise volume progressively until the participant cannot detect any click across **10 consecutive pulses**.
- Randomise the order of noise types and conditions to avoid entrainment and sorting effects.
- Re-tune whenever stimulation intensity, coil, or target changes.
- Deliver through in-ear earphones, which also attenuate ambient sound.

## Verify That It Worked

Self-report is the weak check. **The most reliable criterion is the absence of the N100/P200 AEP complex in the EEG** (Russo et al. 2022). In their electrophysiological demonstration, noise off produced a clear N100 at 96 ms and P200 at 196 ms; with customised noise both were abolished and the participant reported hearing nothing.

Practical workflow:

- Run a short sham or setup block with masking on and inspect the online average for N100/P200.
- Pair with online TEP visualisation (`online-qc/rt-tep-monitoring.md`) so masking efficacy is checked in the same loop as coil and intensity tuning.
- For participants who cannot report perception — disorders of consciousness, infants, non-compliant patients — the EEG criterion is the **only** available check. Plan for it rather than relying on asking.

Note the limits of both checks: perceptual masking success does not guarantee equivalent neural confounds (see `design/sham-and-sensory-controls.md`), and masking reduces but has not been shown to abolish auditory input in every setup.

## Site Dependence

Masking efficacy is not uniform across stimulation sites. White-noise masking failed to prevent click perception in nearly all participants across prefrontal, premotor, and parietal targets, and was **least successful at prefrontal cortex** (`papers/biabani-2024-sensory-inputs-three-sites.md`). Prefrontal produced the loudest perceived click *despite the lowest stimulation intensity*, so intensity is not a proxy for auditory burden. Tune and verify masking per site, not once per participant.

## Tooling

- `repos/taac.md` — TAAC, MATLAB, published and validated.
- `repos/campy-tms.md` — CAMpy-TMS, Python, in progress and uncalibrated.

## Output Rule

When advising on masking, specify: the noise source (recorded from which stimulator and coil), the noise type, the titration criterion, the condition under which titration was performed (must be real TMS), the verification method, and the re-tuning triggers. Report SPL if it was measured, and state plainly if it was not.

## Sources

`papers/russo-2022-taac.md` (Russo et al. 2022, TAAC); `papers/biabani-2024-sensory-inputs-three-sites.md` (site-dependent masking failure); `papers/gordon-2018-realistic-sham.md`; `papers/casarotto-2022-rt-tep-tool.md`; `design/sham-and-sensory-controls.md`.
