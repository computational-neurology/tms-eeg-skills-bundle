---
type: online-qc-card
id: rt-tep-monitoring
title: Real-Time TEP Monitoring
tags:
  - rt-tep
  - online-qc
  - acquisition
---

## Purpose

Use online TEP visualization before and during formal data collection to maximize cortical activation and minimize artifacts.

## Planning Rules

- Inspect single trials before trusting averages.
- Use 10-30 trial online averages to decide whether the response is large and clean enough.
- Treat early local TEP amplitude and artifact profile as acquisition QC variables.
- Adjust coil orientation, position, intensity, masking, and electrodes before committing to full collection.
- If early local response is weak but late N100/P200 is large, suspect sensory contamination.

## What To Monitor

- pulse/recharge/discharge/decay artifacts
- early muscle-artifact peak (see note below)
- craniofacial muscle bursts
- early local TEP or i-TEP near target channels
- late auditory/somatosensory components
- condition differences in artifacts
- impedance or channel drift

## Early Muscle-Artifact Peak vs. Participant Twitch

For non-motor targets (e.g., DLPFC), the early *muscle-artifact peak* is often the single most prominent thing in the online view, so name it explicitly rather than folding it into "muscle bursts":

- **Appearance:** an early, bipolar/MEP-like deflection that emerges after the TMS-pulse artifact, at latencies later than `~4 ms`, focal over frontal/temporal/jaw/facial channels.
- **Why it matters online:** in a 10-30 trial online average it is frequently the *only* time-locked activity visible in the early window; the genuine early local TEP is smaller and easily hidden beneath it. Do not report it as an early cortical response.
- **Not the same as the felt twitch:** the visible/felt muscle twitch that disturbs the participant is a comfort/compliance signal and is often absent at non-motor sites. This early EEG peak is a separate contaminant that can be large even with no twitch. "The participant is comfortable / did not twitch" does not mean the early window is clean — inspect the EEG peak on its own.
- **Use it as the tuning target:** minimize this early bipolar peak with small coil rotation/position changes and intensity, and decide go/no-go on whether the early window is interpretable once it is accounted for.

## Go/No-Go

Proceed when early response is interpretable for the endpoint, artifacts are manageable, and controls/masking are acceptable. Pause and adjust when artifacts dominate the planned analysis window.

## Sources

Casarotto et al. 2022 rt-TEP tool; local good-practice note.
