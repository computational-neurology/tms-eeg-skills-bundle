---
type: repo-card
id: campy-tms
title: CAMpy-TMS
source_url: https://github.com/kolascoco/CAMpy-TMS
language: Python (Jupyter notebook plus module)
status: in progress — not calibrated, not validated against TAAC
tags:
  - masking
  - auditory
  - tooling
---

## Role In The Skill

A Python alternative to TAAC for generating TMS click masking noise, usable without MATLAB. Entry point is `masking_noise_player.ipynb`, run top to bottom; the synthesis lives in `masking_audio.py`. A recorded single TMS pulse ships in `assets/` as a template, and output audio plus configuration are written to `generated/`. A TAAC reproduction is kept separately under `in progress/`.

Offer it when a user wants a scriptable or MATLAB-free masking workflow. Default to `repos/taac.md` when the user needs a validated tool.

## What It Does

`build_masking_track` loads a click recording, resamples it, isolates the largest transient with `_extract_click_event` (peak ±2-30 ms), generates the noise bed, optionally schedules and renders discrete clicks, then mixes, normalises, and writes 16-bit PCM.

Two noise modes: `white`, and `click-shaped` (the default), which shapes noise to the click's spectrum by FFT magnitude smoothing.

Click scheduling has two modes, both Bernoulli-filtered by `click_probability`:

- **Single-pulse** — jittered opportunities at 0.05-20 Hz with ±45% timing jitter per interval.
- **Rhythmic** — trains of `pulses_per_train` (1-1000) at `rhythmic_frequency_hz` (0.1-50), separated by `inter_train_interval_s`.

Key defaults: `sample_rate` 44100, `duration_s` 10.0, `volume` 0.20, `noise_mode` "click-shaped", `seed` 20260810. The `seed` gives reproducible noise across sessions.

## How It Differs From TAAC

| | TAAC | CAMpy-TMS |
|---|---|---|
| Click component | real recorded clicks concatenated at jittered intervals | noise spectrally matched to the click via FFT magnitude smoothing |
| Broadband spread | eleven resampled copies of the click (≈ ×0.3 to ×2.0) | spectral shaping |
| Recording rate | 96 kHz | 44.1 kHz default |
| Click scheduling | jittered inter-click interval only | probabilistic or rhythmic trains, Bernoulli-filtered |
| SPL | validated on a head-and-torso simulator, exposure hours published | explicitly uncalibrated |
| Validation | psychophysical `n = 20`, electrophysiological `n = 1` | none yet |

The spectral-versus-transient distinction is substantive. TAAC's masker contains real click transients; click-shaped noise matches the click's spectrum but not its temporal sharpness. Part of the rationale for masking an impulsive sound is that the masker should itself contain impulsive events, so the two are not interchangeable until tested against each other.

## Failure Modes

- **Digital volume is not calibrated dB SPL.** Start at low hardware volume and validate the complete headphone and masking chain before any participant use. There is no built-in hearing-safety limit beyond clipping at ±1.0.
- **Rhythmic mode carries a specific risk for single-pulse studies.** A periodic click train in the gamma range drives an auditory steady-state response, maximal at frontocentral electrodes — exactly where N100/P200 are measured. A masker built that way can inject the confound it is meant to suppress. Use rhythmic mode only to match an actually rhythmic stimulation protocol, and keep `click_probability` below 1 so the periodicity is broken.
- Treating it as equivalent to TAAC before the reproduction under `in progress/` has been checked.
- Using the shipped `assets/` template click instead of a recording from the user's own stimulator and coil.

## Planning Use

Suitable for prototyping, for scripted or reproducible noise generation, and for workflows without a MATLAB licence. For a protocol where masking efficacy has to be defensible, either use TAAC or validate CAMpy output against it, and in both cases verify with the EEG criterion in `design/auditory-masking.md`.

## Related Cards

`design/auditory-masking.md`; `repos/taac.md`; `papers/russo-2022-taac.md`.
