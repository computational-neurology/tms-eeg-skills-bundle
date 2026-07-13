---
type: targeting-card
id: neuronavigation-and-efield
title: Neuronavigation And E-Field Planning
tags:
  - neuronavigation
  - efield
  - simnibs
  - slicertms
  - nexstim
---

## Purpose

Use neuronavigation and E-field modeling to improve target precision, reproducibility, and reporting.

## Planning Rules

- Use neuronavigation when comparing sessions, targets, subjects, or source-level TEPs.
- Save target coordinates, coil pose, coil orientation/current direction, head registration quality, and deviations.
- Use E-field simulation when individual anatomy, target depth/orientation, or dose estimates matter. This is especially important for non-motor targets (e.g., DLPFC), where a universal coil orientation is not available and orientation should follow individual gyral anatomy and the induced E-field (Gomez-Tames et al. 2018; see `targeting/coil-orientation-and-intensity.md`).
- If the lab has a Nexstim system, distinguish on-board real-time E-field navigation from offline simulation. Nexstim NBS / SmartFocus nTMS publicly describes MRI-based 3D rendering, multi-sphere E-field modeling, and dynamic recalculation of E-field location/orientation/magnitude as the coil is moved, turned, or tilted.
- E-field/neuronavigation improves target reporting but does not guarantee clean TEPs.
- Combine anatomical/E-field targeting with online TEP and artifact QC.

## Tool Roles

| Tool | Role |
|---|---|
| SimNIBS | individualized E-field simulation and dose/target planning |
| Nexstim NBS / SmartFocus / Eximia-style systems | commercial on-board E-field navigated TMS with real-time coil/E-field visualization during stimulation |
| SlicerTMS | visualization / Slicer-based TMS targeting and E-field/fiber display workflows |
| NaviNIBS | open-source neuronavigation, tracking, registration, and electrode digitization context |

## Nexstim / eXimia Notes

Older papers may refer to Nexstim Eximia/eXimia, while current public Nexstim pages emphasize NBS and SmartFocus nTMS. When the user says "eXima", interpret this as likely Nexstim Eximia/eXimia-style E-field navigated TMS, but verify the local system name/version before writing methods text.

For TMS-EEG planning, treat Nexstim on-board E-field navigation as an acquisition-time guidance and documentation tool. It can help maintain the estimated maximum E-field location, orientation, and magnitude over individual MRI anatomy while the operator adjusts coil position. It should be paired with online TEP/artifact QC because accurate E-field targeting does not by itself exclude muscle, auditory/somatosensory, pulse, decay, or lead-configuration artifacts.

## fMRI-Guided, E-Field-Optimized Targeting

When the target is an fMRI-defined ROI, follow the generalized workflow in
`papers/balderston-2020-efield-optimized-fmri-guided-tms.md`: constrain single-subject fMRI
peaks with a group-level ROI mask, then iterate SimNIBS E-field models across coil yaw (default
24 orientations at 15-degree steps) to pick the orientation that maximizes induced current in
the ROI, and export the target sphere, yaw-vector line, and orientation mask as NIfTI files for
neuronavigation. This is the reference pipeline for coupling fMRI localization with E-field
simulation and neuronavigation.

## Output Rule

For target planning, return both an anatomical/E-field plan and a physiological/online-QC plan.

## Sources

Lioumis and Rosanova 2022; Gomez-Tames et al. 2018 (`papers/gomez-tames-2018-atlas-optimal-coil-orientation.md`); Balderston et al. 2020 (`papers/balderston-2020-efield-optimized-fmri-guided-tms.md`); Nexstim technology and TMS-EEG pages; local SlicerTMS troubleshooting note; SimNIBS, Nexstim, NaviNIBS, and SlicerTMS repo cards.
