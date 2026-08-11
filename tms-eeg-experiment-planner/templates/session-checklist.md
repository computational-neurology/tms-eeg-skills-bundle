---
type: template
id: session-checklist
title: TMS-EEG Session Checklist
tags:
  - checklist
  - acquisition
  - online-qc
---

# TMS-EEG Session Checklist

## Before Participant Arrives

- Confirm protocol version and condition order.
- Confirm TMS safety equipment and emergency procedure.
- Confirm EEG amplifier, trigger cable, TMS device, neuronavigation, and masking audio.
- Load target coordinates, MRI/head model, coil model, and planned orientations.
- Prepare all neuronavigation steps possible before arrival: MRI upload, brain segmentation, fiducial setup, target import, coil model selection, and planned evidence exports.
- Confirm storage paths and participant ID convention.

## Participant Setup

- Complete safety screening and consent.
- Record sleep, caffeine, medication, and relevant state variables.
- Prepare cap placement and identify digitization landmarks without disturbing electrode contact.
- Keep electrode contact stable under and around target.
- Route leads away from coil; reduce loops, slack, and cable tension. Keep wires near the coil approximately perpendicular to the coil main axis when feasible, not parallel.
- Check impedance/contact quality and gel bridges. Use skin preparation together with the minimum gel needed to achieve reliable contact.

## Navigation And Stimulation Setup

- Register head to MRI or template.
- Verify target, coil orientation, current direction, and handle angle.
- Measure RMT when relevant.
- Choose starting intensity.
- Test candidate orientations/intensities if the protocol allows optimization.
- Save target and coil setup evidence.

## Click Recording (Only When Setup Changed)

Skip if the existing click recording still matches the stimulator, coil, and intensity.

- **Safety first: microphone and all metal objects out of the magnetic field.** Metal within the field can be thrown violently.
- Omnidirectional microphone, no filtering or distortion in the chain, ~25 cm laterally to the coil.
- Record at 96 kHz, deliver a few pulses, crop from the sharp transient to return-to-baseline.
- Re-record whenever the stimulator, coil, or (device-dependent) intensity changes.

## Sensory Control Setup

- Fit in-ear earphones and masking audio.
- Tune masking after stimulation intensity is chosen, **under real TMS — not sham**. Real stimulation needs roughly 6 dB more masking than sham.
- Titrate by raising volume until the participant detects no click across 10 consecutive pulses, with jittered inter-pulse intervals.
- Verify masking by inspecting the online average for N100/P200 — absence of the AEP complex is the reliable criterion, not self-report. For participants who cannot report perception, this is the only available check.
- Add foam/spacer or scalp-contact control if planned.
- Run sham/control setup checks.
- Record tolerability and perceived loudness/scalp sensation.
- Note total planned noise exposure time against hearing-safety limits for long sessions.

## Online QC Before Main Block

- Deliver setup pulses and inspect raw EEG.
- Check pulse, recharge, decay, and amplifier recovery.
- Inspect muscle contamination near face/temporal/neck channels.
- Average a small setup block when possible.
- Confirm early local response and topography if relevant.
- Decide go/no-go or adjust target/orientation/intensity/cables.

## Main Acquisition

- Monitor target drift and coil angle.
- Monitor EEG trace, trigger timing, and rejection rate.
- Recheck masking and comfort after intensity, coil, or target changes, and re-verify the AEP check.
- Pause if decay, muscle, or synchronization artifacts appear.
- Log all deviations and adjustments.

## End Of Session

- Save EEG, markers, navigation, TMS device logs, and QC screenshots.
- Digitize landmarks/electrode positions after stimulation and recording when feasible, to avoid perturbing channels or spreading gel before acquisition.
- Export sensory ratings and condition notes.
- Record final usable-trial estimate.
- Document adverse events or tolerability issues.
- Back up raw data before preprocessing.
