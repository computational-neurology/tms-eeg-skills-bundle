---
type: template
id: preregistration-methods-template
title: TMS-EEG Preregistration And Methods Template
tags:
  - preregistration
  - methods
  - reporting
reporting_standard: TMS-RAT v1.0 — Székely et al. (2026) Brain Stimulation 19:103155, https://doi.org/10.1016/j.brs.2026.103155; tool at https://tms-rat.org
---

# TMS-EEG Methods Skeleton

Write against **TMS-RAT v1.0** (Székely et al. 2026, <https://doi.org/10.1016/j.brs.2026.103155>; items at <https://tms-rat.org/?page=rat&version=1.0>) — the 72-item prospective version. Do **not** write against v1.1: that is the 50-item retrospective subset, built by removing items the literature reports inconsistently, and writing to it drops inter-trial interval, pulse count, and participant-level intensity.

TMS-RAT is validated only on afferent-conditioning/MEP studies and has no EEG acquisition or TEP-measures section, so sections A–H cover roughly half of what a TMS-EEG Methods section needs. See `references/guidelines/reporting-tms-rat-mapping.md` for the gap list. A parallel Methods-text generator (in development) is at <https://tms-rat.org/?page=generator>.

## Targeting

TMS will be delivered to [target]. The target will be defined using [individual MRI/template/function/localizer]. Coil position and orientation will be monitored with [neuronavigation system]. The planned current direction is [direction], with acceptable deviations defined as [criterion].

## Intensity Selection

Stimulation intensity will be set using [RMT/active motor threshold/E-field/online TEP threshold/combined rule]. For non-motor targets, RMT will be treated as [starting calibration/safety reference] rather than a complete guarantee of target activation. Online TEP and artifact checks will be used to confirm whether the chosen parameters produce usable responses.

## Coil Orientation And E-Field Planning

Candidate coil orientations will be chosen based on [anatomy/E-field simulation/prior literature/online response]. If E-field modeling is used, the head model, coil model, conductivity assumptions, and optimization criterion will be reported.

## EEG Acquisition

EEG will be recorded using [system] at [sampling frequency]. Trigger synchronization will be performed using [method]. Lead routing and electrode contact will be inspected before acquisition to reduce pulse, recharge, and decay artifacts.

## Online Quality Control

Before the main block, [number] setup pulses will be used to inspect raw traces, pulse/recharge artifacts, decay, muscle activity, and online TEP averages. The planned go/no-go criteria are [criteria]. Setup changes will be logged.

## Sham And Sensory Controls

The control condition will be [sham/control]. Auditory masking will be [method], and scalp sensation will be controlled or measured using [method]. Sensory ratings and blinding checks will be collected [schedule].

## Trial Count

The planned number of trials per condition is [number]. The target number of usable trials after rejection is [number]. If online artifact rates exceed [criterion], acquisition will be paused and setup will be inspected.

## Stimulation Parameters To State Numerically

Inter-trial interval, total number of pulses delivered, and stimulation intensity both as %MSO and relative to the participant's threshold will each be reported as explicit numbers rather than by implication. These correspond to TMS-RAT items `G1`, `G2`, `F2` and `F3`, which are the least reliably reported items in the TMS literature (Gwet's AC1 = 0.56, 0.40, 0.58 and 0.20 respectively) and were excluded from TMS-RAT v1.1 for that reason. Quantitative values will include both a measure of central tendency and a measure of dispersion.

## Reporting Completeness

Reporting will follow TMS-RAT v1.0 (Székely et al., 2026). The completed tool sheet and its output `.csv` will be submitted as supplementary material, with any items scored partial or missing listed alongside the reason. Items with no TMS-RAT equivalent — EEG amplifier and acquisition settings, blanking and saturation handling, trigger synchronisation and measured latency, reference and ground, impedance, lead routing relative to the coil, pulse interpolation window, preprocessing pipeline and version, TEP analysis windows, and trials delivered versus retained — will be reported explicitly.

## i-TEP Or Early-Response Addendum

If immediate or very early TEPs are analyzed, acquisition will additionally report sampling frequency, synchronization method, lead configuration, pulse/recharge/removal windows, early artifact QC, and current-direction or control conditions. Early responses will not be interpreted as clean cortical activity unless artifact and control evidence support that interpretation.
