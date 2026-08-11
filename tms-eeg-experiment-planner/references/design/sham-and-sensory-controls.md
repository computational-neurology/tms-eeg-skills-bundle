---
type: design-card
id: sham-and-sensory-controls
title: Sham, Auditory Masking, And Somatosensory Controls
tags:
  - sham
  - masking
  - sensory-confounds
---

## Purpose

Design controls that separate cortical TMS-evoked activity from click, scalp sensation, vibration, expectation, and muscle artifacts.

## Required Decisions

- realistic sham type and coil placement
- auditory masking noise and retuning when intensity changes
- mechanical vibration/scalp sensation control
- foam/spacer or sham coil setup if used
- active control target when scientific question requires it
- whether sensory-only control trials are needed

## Methodological Rules

- Sensory controls are design-level safeguards; preprocessing cannot fully fix poor controls.
- If early local TEP is weak, late N100-P200 activity may be dominated by auditory/sensory contamination.
- If using sham subtraction, check whether sham/control PEPs resemble real-TMS PEPs closely enough for the intended interpretation.
- Consider individualized PEP matching or PEP saturation logic when somatosensory subtraction is central to the study design.
- For tactile-feeling studies, collect subjective ratings that separate scalp sensation, click loudness, unpleasantness, perceived tactile quality, and perceived location.
- Titrate auditory masking under **real TMS, never under sham** — real stimulation requires roughly 6 dB more masking because of bone conduction through the vibrating coil. Retune whenever intensity, coil, or target changes.
- Report sham and masking parameters clearly.

## Auditory Masking

Masking has its own card: `design/auditory-masking.md`, covering how to record your own click, noise design, titration, hearing-safety exposure, and how to verify masking worked. Load it for any question about masking noise, click perception, or AEP contamination.

Two points that belong here because they constrain sham design:

- A sham condition used to titrate masking will **under-mask the real condition**. Titrate on real TMS.
- Verify masking by the **absence of N100/P200 in the EEG**, not by asking the participant. Perceptual masking success does not guarantee equivalent neural confounds — N45, N100, and P180 differed between active stimulation and a perceptually indistinguishable realistic sham despite active masking (Gordon et al. 2018).

## Output Rule

When advising interpretation-sensitive designs, propose at least one auditory and one somatosensory control strategy, plus how the control will be checked online.

## Sources

Gordon et al. 2018; Grasin 2019 realistic sham; Gordon et al. 2026 somatosensory inputs; `papers/russo-2022-taac.md`; `papers/biabani-2024-sensory-inputs-three-sites.md`; `design/auditory-masking.md`; local good-practice note.
