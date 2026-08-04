---
type: template
id: experiment-protocol-template
title: TMS-EEG Experiment Protocol Template
tags:
  - protocol
  - experiment-planning
  - preregistration
  - reporting
reporting_standard: TMS-RAT v1.0 — Székely et al. (2026) Brain Stimulation 19:103155, https://doi.org/10.1016/j.brs.2026.103155; tool and item definitions at https://tms-rat.org
---

# TMS-EEG Experiment Protocol

Fields tagged `[A1]`, `[E5]` and similar map to items of the **TMS Reporting Assessment Tool v1.0** (TMS-RAT; Székely et al. 2026, <https://doi.org/10.1016/j.brs.2026.103155>; item definitions at <https://tms-rat.org/?page=rat&version=1.0>). Fields tagged `[EEG-ext]` have no TMS-RAT item — TMS-RAT is validated only on afferent-conditioning/MEP studies and has no EEG acquisition or TEP-measures section. See `references/guidelines/reporting-tms-rat-mapping.md`.

Quantitative fields marked `[quant]` require **both** a measure of central tendency and a measure of dispersion to count as fully reported.

## Study Aim

- Primary question:
- Primary TEP/EEG outcome:
- Secondary outcomes:
- Hypothesized direction or contrast:

## Participant And Safety Plan

- Population/source `[C2]`:
- Number of experiments or studies `[C1]`:
- Number of independent groups `[C3]`:
- Age `[A1] [quant]`:
- Sex, n per category `[A2]`:
- Handedness `[A3]`:
- Height `[A4] [quant]`:
- Weight `[A5] [quant]`:
- Inclusion criteria:
- Exclusion criteria — neurological/psychiatric/behavioural `[B3]`, medical/systemic `[B4]`:
- TMS safety screen:
- Medication screening `[B1]`:
- CNS-active substance screening `[B2]`:
- Sleep/alertness assessment `[B6]`:
- Cognitive state assessment `[B5]`:
- Participant posture `[B7]`:
- Stopping criteria:

## Session Design

- General TMS protocol `[C4]`:
- Time of day `[C5]`:
- Session duration and interval between sessions `[C6]`:
- How participant attention was maintained `[C7]`:

## Target Definition

- Target region / target location in CNS `[E3]`:
- Coordinate system:
- Target source:
- Individual MRI available:
- Functional/localizer data available:
- Coil location on the skin `[E2]`:
- Neuronavigation system `[E1]`:
- Backup target rule:

## E-Field And Navigation Plan

- E-field modeling tool:
- Head model:
- Coil model:
- Candidate coil orientations:
- Optimization criterion:
- Acceptable deviation from target:
- Saved evidence:

## Stimulation Parameters

- Stimulator make and model `[D1]`:
- Coil shape and model `[D2]`:
- Coil diameter `[D3]`:
- Pulse waveform `[D4]`:
- Coil orientation `[E4]`:
- Induced current direction `[E5]`:
- How coil stability was maintained `[E6]`:
- Intensity method — how intensity was set `[F1]`:
- Machine intensity, %MSO `[F2] [quant]`:
- Participant intensity relative to threshold `[F3] [quant]`:
- Threshold location `[H1]`, type `[H2]`, criterion `[H3]`, algorithm `[H4]`:
- Threshold values `[H5] [quant]`:
- TEP threshold or online response criterion `[EEG-ext]`:
- Inter-trial interval `[G1]`:
- Planned pulses/trials per condition `[G2]`:
- Expected usable trials after rejection `[EEG-ext]`:

> `[F3]`, `[G1]` and `[G2]` are among the worst-reported items in the TMS literature (Gwet's AC1 = 0.20, 0.56 and 0.40 respectively) and were cut from TMS-RAT v1.1 for that reason. State them explicitly and numerically — never by implication.

## EEG Acquisition

All fields in this section are `[EEG-ext]` — TMS-RAT has no EEG acquisition section.

- EEG amplifier make and model:
- Acquisition software and version:
- Sampling frequency:
- Acquisition filter settings:
- Blanking / sample-and-hold / saturation handling:
- Synchronization method and measured trigger latency:
- TMS-compatible settings:
- Electrode type, material, size:
- Montage:
- Reference:
- Ground:
- Skin preparation:
- Impedance/contact target:
- Lead routing plan relative to coil:
- Channels near coil requiring special inspection:

## Sham And Sensory Control

- Sham/control type `[C8]`:
- Auditory masking — noise type, level, verification `[C9]` + `[EEG-ext]` detail:
- Scalp sensation control `[C9]`:
- Foam/spacer/contact plan:
- Sensory ratings:
- Order/randomization:
- Blinding check:

## Online TEP And Acquisition QC

- Online averaging window:
- Setup trials:
- Early response criterion:
- Artifact go/no-go criteria:
- Decay/recharge inspection:
- Muscle artifact inspection:
- Save screenshots/logs:

## Target-Specific Risks

- Muscle risk:
- Auditory/somatosensory risk:
- Eye/face/neck artifact risk:
- i-TEP risk:
- Planned mitigation:

## Analysis-Relevant Reporting

All fields in this section are `[EEG-ext]` — the nearest TMS-RAT items (`M3`, `M4`) are scoped to somatosensory evoked potentials and were cut from v1.1.

- Pulse interpolation/removal window planned:
- Baseline window:
- TEP components or features of interest:
- TEP values, amplitude and latency `[quant]`:
- GMFA/LMFP windows:
- Planned ROI/channels:
- Preprocessing pipeline and version:
- Trials delivered versus retained:
- Artifact rejection criteria:
- Deviations to log:

## Reporting Checklist Output

- TMS-RAT v1.0 sheet completed (<https://tms-rat.org/?page=rat&version=1.0>):
- Completed sheet and output `.csv` attached as supplementary material:
- Items marked partial or missing, with reason:

## Session Outputs

- Navigation export:
- TMS device log:
- EEG raw file:
- Event markers:
- Online QC notes:
- Sensory/control ratings:
- Deviations/adverse events:
