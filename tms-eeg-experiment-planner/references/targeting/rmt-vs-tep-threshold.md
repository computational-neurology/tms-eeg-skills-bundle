---
type: targeting-card
id: rmt-vs-tep-threshold
title: RMT Versus TEP Threshold
tags:
  - rmt
  - tep-threshold
  - intensity
---

## Purpose

Help the agent reason about stimulation intensity when RMT, E-field dose, online TEP amplitude, and artifact ceiling may disagree.

## Key Distinction

RMT indexes corticospinal excitability for motor cortex. TEP quality indexes EEG-observable target response and artifact burden. They are related only indirectly and may diverge, especially outside M1.

## Planning Rules

- Use RMT as a safety and starting reference, not as the sole intensity rule for non-motor TMS-EEG.
- For non-motor targets, adjust intensity based on online TEP visibility, artifact profile, discomfort, and safety limits.
- Treat early local TEP amplitude as a QC variable. Local notes suggest about `8-10 uV` peak-to-peak in `8-50 ms` near the coil as a practical acquisition target, not a universal threshold.
- If increasing intensity improves late N100/P200 but not early local response, suspect sensory contamination.
- For non-motor targets, treat the early muscle-artifact peak as an intensity ceiling. This is the bipolar/MEP-like deflection appearing after the TMS-pulse artifact at latencies later than `~4 ms`, focal over frontal/temporal/jaw/facial channels; it grows with intensity and is frequently the only time-locked activity visible in the online average. Do not raise intensity on the basis that "the participant is not twitching" — the felt muscle twitch and this early EEG muscle-artifact peak are separate signals, and at non-motor sites the peak can be large while no twitch is felt. Increase intensity only while this early bipolar peak stays low enough that the planned early window remains interpretable.
- Retune auditory masking whenever intensity changes.

## Matching Intensity Across Stimulation Sites

Correcting intensity for coil-to-cortex distance is standard practice and **does not equalise cortical dose**. Applying the usual distance adjustment across prefrontal, premotor, and parietal targets still left modelled cortical E-field significantly different between sites (Biabani et al. 2024) — the authors state directly that the commonly used coil-to-cortex correction is insufficient for matching TMS-evoked E-fields between sites.

If a study compares TEPs across sites, either model the E-field per individual (T1+T2 head model, FEM; SimNIBS in that study) and normalise the outcome measure by peak E-field, or accept that dose is unmatched and state it as a limitation. Do not present distance-corrected %rMT as equalised stimulation.

Note also that perceived click loudness does not follow intensity: prefrontal stimulation produced the **loudest** perceived click at the **lowest** stimulation intensity of the three sites. Intensity is not a proxy for sensory burden.

## Output Rule

Report intensity as a decision chain: initial RMT/E-field estimate, online TEP response, artifact/discomfort ceiling, and final locked value. When comparing sites, add the dose-matching method and whether cortical E-field was modelled or assumed.

## Sources

Local good-practice note; rt-TEP tool paper; DLPFC reliability/excitability cards in preprocessing skill; `papers/biabani-2024-sensory-inputs-three-sites.md` (distance correction insufficient; sensory burden versus intensity).
