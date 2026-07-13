---
type: paper-card
id: gomez-tames-2018-atlas-optimal-coil-orientation
title: Atlas of optimal coil orientation and position for TMS - A computational study
year: 2018
authors: Gomez-Tames, Hamasaka, Laakso, Hirata, Ugawa
journal: Brain Stimulation 11(4):839-848
doi: 10.1016/j.brs.2018.04.011
tags:
  - coil-orientation
  - coil-position
  - efield
  - target:dlpfc
  - target:m1
  - personalized-targeting
use_for:
  - why 45 degrees is an M1/S1 convention, not a universal rule
  - justifying individualized coil orientation for non-motor targets (e.g., DLPFC)
  - E-field-perpendicular-to-sulcal-wall orientation principle
confidence: seed-card
---

## Why This Matters For The Agent

This is the evidence that a single "correct" coil orientation does not generalize across the
cortex. From 518,616 simulated scenarios (2401 scalp positions x 12 coil angles x 18 realistic
head models), the authors show a common optimal coil angle across subjects exists only at
primary motor (M1) and primary somatosensory (S1) cortex. For all other regions - including
frontal cortex, where the DLPFC sits - individual gyral folding varies enough that the optimal
orientation is subject-specific. Use this card to strengthen any answer that would otherwise
default to "use 45 degrees."

## Key Findings

- The optimal induced-current direction is approximately perpendicular to the gyral crown /
  sulcal wall in all cortical areas (optimal angle follows the anatomical shape of the hand
  motor area, R^2 = 0.91).
- A universal optimal coil orientation applicable to most subjects is feasible only at M1 and
  S1; motor and sensory areas show the highest cross-subject agreement in optimal angle.
- Frontal, parietal, and temporal regions have complicated, variable folding between
  individuals, so a common angle is not available and personalized optimization is preferable.
- Maximum E-field strength is consistently higher in M1/S1 (and gyral crowns) than in other
  areas; E-field decays with cortex-scalp distance (approximately cubic).
- The optimal coil position deviates on average 5.5 +/- 1.6 mm from the nearest scalp point;
  the deviation is smallest at motor/sensory/occipital areas and larger where cortex-scalp
  distance is greater (parietal, temporal).

## Planning Rules Extracted

- Do not automatically apply a 45-degree coil orientation outside M1/S1; treat it as a
  motor-cortex convention, not a universal standard.
- For non-motor targets such as DLPFC, individualize orientation to the subject's gyral anatomy
  and resulting E-field distribution (aim for current approximately perpendicular to the target
  sulcal wall).
- Prefer E-field simulation / navigated targeting over a fixed angle when the target is frontal
  or otherwise anatomically variable.
- Do not assume the optimal coil sits at the nearest scalp point; expect a several-mm position
  shift, larger for deeper/farther targets.

## Related Cards

`targeting/coil-orientation-and-intensity.md`; `targeting/neuronavigation-and-efield.md`;
`targets/dlpfc.md`; `repos/simnibs.md`; `repos/nexstim-efield-navigation.md`;
`repos/slicertms.md`; `papers/richter-2013-optimal-coil-orientation.md`;
`papers/janssen-2015-coil-orientation-efield.md`;
`papers/balderston-2020-efield-optimized-fmri-guided-tms.md`.
