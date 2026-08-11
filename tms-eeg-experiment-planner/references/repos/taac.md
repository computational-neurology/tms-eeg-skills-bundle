---
type: repo-card
id: taac
title: TAAC (TMS Adaptable Auditory Control)
source_url: https://github.com/iTCf/TAAC
video_tutorial: https://www.youtube.com/watch?v=EsAkS4X-2fA
language: MATLAB
dependencies: Signal Processing Toolbox, Communications System Toolbox
tags:
  - masking
  - auditory
  - tooling
---

## Role In The Skill

The reference tool for generating TMS click masking noise. A single-file MATLAB GUI that records the stimulator- and coil-specific click, builds a masking noise from it, and lets the noise be tuned live against the participant's perception. Published and validated (`papers/russo-2022-taac.md`).

## What It Does

Three steps in the interface:

1. **Acquire** — record the click through a microphone (96 kHz), then crop from the sharp transient to baseline.
2. **Test and play** — `Test noise` builds a short loop that can be manipulated in real time while the participant listens; `Noise start` locks the parameters and plays continuously for the session.
3. **Parameterise** — mix a click-based component (your recorded click, concatenated at jittered intervals) with a white-noise component, set the white-to-click ratio, resample either component up or down in frequency, and set the volume independently of system volume.

`Broadband shuffling` is the option to reach for first: it mixes the click with eleven resampled copies of itself and disables separate frequency tuning, which is both faster to tune and what produced the validated results. Optional `intensity shuffling` and `spatial shuffling` add per-click attenuation and inter-aural delay — spatial shuffling is untested.

Parameter sets save and load, giving reproducible masking across sessions. `Export audio .wav` writes the noise out so it can be played from any device.

## Planning Use

Use when designing masking for any TMS-EEG protocol. Record a fresh click whenever the stimulator, coil, or (for some devices) intensity changes. Tune per participant with the participant in the chair, under real TMS at the intensity you will use.

## Failure Modes

- Recording the click with a microphone or metal object inside the magnetic field — a physical hazard, not just a data problem.
- Recording through a chain that filters or distorts, so the masker is built from the wrong spectrum.
- Reusing a click recording after changing coil or stimulator.
- Titrating masking under sham and assuming it transfers to real TMS — it does not, real TMS needs roughly 6 dB more.
- Accepting self-report as proof of masking without checking the EEG for N100/P200.
- Treating the published SPL values as targets for a different earphone or coil setup.

## Related Cards

`design/auditory-masking.md`; `papers/russo-2022-taac.md`; `repos/campy-tms.md`; `online-qc/rt-tep-monitoring.md`; `repos/rt-tep-tool.md`.
