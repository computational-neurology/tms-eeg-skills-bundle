---
type: targeting-card
id: coil-orientation-and-intensity
title: Coil Orientation, Position, And Intensity
tags:
  - coil-orientation
  - coil-position
  - intensity
---

## Purpose

Choose coil orientation, position, and intensity to maximize interpretable target engagement while minimizing muscle and sensory artifacts.

## Planning Rules

- Do not automatically apply a 45-degree coil orientation. The 45-degree
  posterolateral-to-anteromedial convention is a practical rule for the primary motor cortex
  (M1); it is not a universal standard for other cortical areas.
- A common optimal orientation across subjects is only well supported at M1 and primary
  somatosensory cortex (S1). For non-motor targets (e.g., DLPFC and other frontal, parietal,
  or temporal sites), individual gyral folding varies enough that the optimal orientation is
  subject-specific and should be individualized (Gomez-Tames et al. 2018).
- Set orientation from the individual anatomy and the resulting E-field distribution: aim for
  an induced current approximately perpendicular to the target sulcal wall / gyral crown, then
  refine with online TEP/artifact monitoring.
- Rotate the coil and use online TEP/artifact monitoring to find a clearer early response with lower artifact.
- Small coil rotations or slight position changes can improve early TEP amplitude without increasing intensity.
- For non-motor targets, the signal you actually watch while rotating/repositioning the coil is usually the early *muscle-artifact peak*: a bipolar/MEP-like deflection appearing after the TMS-pulse artifact at latencies later than `~4 ms`, focal over frontal/temporal/jaw/facial channels. It is often the only time-locked activity visible in the low-trial online average, and it is distinct from the participant's felt/visible muscle twitch (a comfort issue, and typically absent at non-motor sites). Judge orientation/position by whether this early bipolar peak *shrinks*, not only by whether the participant is comfortable; a clean early window with no felt twitch can still contain a large early muscle-artifact peak.
- Do not assume the optimal coil sits at the nearest scalp point; expect a several-mm position
  shift (mean ~5.5 mm), larger for deeper/farther targets (Gomez-Tames et al. 2018).
- RMT is a useful starting point, especially for M1, but not a final standard for non-motor targets.
- For i-TEPs, small coil shifts may be needed to remove scalp muscle contamination.

## Procedure

1. Define initial orientation from anatomy, E-field model, literature, or motor mapping.
2. Run low-trial online TEP checks.
3. Compare early local TEP amplitude, topography, discomfort, and muscle artifact.
4. Adjust orientation and position iteratively within safety/targeting constraints.
5. Lock settings only after online QC is acceptable.

## Model-Based Orientation Search

To set the initial orientation from a simulation rather than a fixed 45-degree default, use the
iterative E-field approach in `papers/balderston-2020-efield-optimized-fmri-guided-tms.md`:
sweep coil yaw (default 24 orientations at 15-degree steps) in SimNIBS and choose the yaw that
maximizes induced current in the target ROI, then refine with online TEP/artifact QC. fMRI
fixes only the x/y/z position; roll/pitch/yaw still need to be planned. See
`targeting/neuronavigation-and-efield.md`.

Tools that support individualized orientation and E-field visualization:

- Nexstim NBS / SmartFocus nTMS neuronavigation with real-time E-field visualization
  (`repos/nexstim-efield-navigation.md`).
- NIBS-style E-field modeling tools, primarily SimNIBS (`repos/simnibs.md`).
- SlicerTMS for real-time visualization and navigation (`repos/slicertms.md`).

## Output Rule

When advising orientation/intensity, provide an initial setting, a search procedure, and a stopping rule based on online TEP quality and artifact profile.

## Sources

Richter et al. 2013; Janssen et al. 2015; Gomez-Tames et al. 2018 (`papers/gomez-tames-2018-atlas-optimal-coil-orientation.md`); Balderston et al. 2020 (`papers/balderston-2020-efield-optimized-fmri-guided-tms.md`); Adank et al. 2018; Casarotto et al. 2022; local good-practice note.
