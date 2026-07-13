---
type: artifact-appearance-card
id: muscle-artifact-appearance
title: Muscle Artifact Appearance
artifact_type: muscle
tags:
  - muscle-artifact
  - emg
  - early-artifacts
  - target-risk
  - itep
load_with:
  - references/artifacts/target-specific-artifact-risks.md
  - references/routing/target-risk-routing.md
source_cards:
  - references/guidelines/recommendations-good-practice.md
---

## What It Looks Like

Brief, often biphasic EMG-like activity after the TMS pulse. It can resemble a peripheral MEP but usually has very short latency and is time-locked to the TMS pulse. It is commonly strongest over temporal, frontal, jaw, neck, or facial regions, depending on target location and coil position.

In averaged data, time-locked muscle activity may appear as sharp early deflections, or as smeared early activity if its timing varies slightly across trials. In topographies, it often shows a very focal, localized dipolar pattern rather than a broad cortical field.

## Timing Clues

- Very early post-pulse onset: the peak typically emerges just after the TMS-pulse artifact, at latencies later than `~4 ms`.
- Often overlaps the early TEP/i-TEP window.
- May be consistently time-locked if the same scalp muscle or cranial nerve is stimulated on each pulse.

## The Early Peak You See Online Is Not the Participant's Twitch

Keep two different "muscle" signals separate, especially at non-motor targets (e.g., DLPFC) where they are easily conflated:

- **Early muscle-artifact peak (EEG):** the early, bipolar/MEP-like deflection described above, later than `~4 ms` and focal over frontal/temporal/jaw/facial channels. In a low-trial online average it is frequently the *only* time-locked activity visible in the early window, and it can be mistaken for an early cortical/i-TEP response.
- **Felt/visible muscle twitch (behavior):** the participant-facing contraction that causes discomfort. It is a comfort/compliance signal and is often absent at non-motor sites.

These are decoupled: the early EEG peak can be large even when the participant reports no twitch, so "the participant is comfortable" is not evidence that the early window is muscle-free. Judge the early window from the EEG peak itself, not from participant comfort.

## Topography Clues

- Focal, localized, dipolar-looking scalp pattern.
- Often strongest around temporal, frontal, jaw, facial, neck, or inferior scalp channels.
- Target-specific: lateral frontal, temporal, DLPFC, language, and facially proximate targets have higher risk.

## Single-Trial Versus Average Clues

In single trials, muscle artifact often appears as high-frequency EMG-like bursts or sharp biphasic activity. In averages, repeated time-locked muscle activity can become deceptively clean-looking and may be mistaken for an early cortical component.

## Common Confusions

- Muscle artifact versus i-TEP: both can be early and time-locked. Use topography, target risk, coil-position sensitivity, current direction, EMG channels, and sham/control evidence.
- Muscle artifact versus peripheral MEP: scalp/facial muscle artifact can resemble MEP-like biphasic activity but is observed in EEG channels and may occur with very short latency.
- Muscle artifact versus broad cortical response: focal dipolar maps near muscle-rich regions are suspicious.

## Acquisition Checks

- Inspect single trials and topographies during setup.
- Try small coil-position and orientation adjustments if early focal activity is present.
- Consider additional EMG channels for face/jaw/neck or target-specific muscles.
- Reassess target choice if the scientific endpoint depends on early local responses and the target is muscle-contaminated.

## What Not To Conclude

- Do not treat a focal early dipole near temporal/frontal/facial channels as cortical without controls.
- Do not assume averaging solves muscle artifact; time-locked muscle can become more convincing after averaging.

## Sources

Local good-practice note; target-specific artifact risk cards; i-TEP acquisition practice card.
