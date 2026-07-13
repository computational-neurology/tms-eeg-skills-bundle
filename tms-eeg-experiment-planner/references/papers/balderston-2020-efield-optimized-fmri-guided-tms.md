---
type: paper-card
id: balderston-2020-efield-optimized-fmri-guided-tms
title: A generalized workflow for conducting electric field-optimized, fMRI-guided, transcranial magnetic stimulation
year: 2020
authors: Balderston, Roberts, Beydler, Deng, Radman, Luber, Lisanby, Ernst, Grillon
journal: Nature Protocols 15(11):3595-3614
doi: 10.1038/s41596-020-0387-4
pmc: PMC (available 2021-05-15); NIHMS manuscript nihms-1696933
code: https://github.com/balders2/tms_targeting
tags:
  - fmri-guided-targeting
  - efield
  - coil-orientation
  - coil-position
  - neuronavigation
  - simnibs
  - roi
use_for:
  - turning an fMRI-defined ROI into a subject-specific navigated TMS target
  - iterative E-field optimization of coil yaw/handle orientation
  - constraining single-subject fMRI peaks with a group-level ROI mask
confidence: seed-card
---

## Why This Matters For The Agent

This is the end-to-end methodological guideline for the question "I have an fMRI-defined
ROI, how do I turn it into a navigated, E-field-optimized TMS target for one subject?" It
couples functional localization (where to stimulate) with iterative SimNIBS E-field modeling
(which coil orientation induces the most current in the ROI), then hands both to
neuronavigation. It is the primary reference behind the planner's field-simulation and
coil-position/orientation cards.

## Pipeline Summary (Balderston et al. 2020)

Total time ~24 h (E-field models must run between MRI and TMS; single-session scan+stim is
not possible).

1. **Target definition (~1 h).** Operationally define the ROI as a binary mask in standard
   (e.g., MNI) space from group-level fMRI contrasts, a meta-analysis tool (NeuroSynth), or
   an anatomical atlas. The mask *constrains* where single-subject fMRI peaks are accepted —
   critical because single-subject fMRI is noisy, especially in frontal cortex.
2. **Data collection (~2 h).** High-res T1 (+optional T2, <1 mm iso) for tissue segmentation,
   a diffusion scan (<2 mm iso, single-shell, >=30 dir) for anisotropic conductivity, and
   task-based or resting-state EPI to localize the function of interest.
3. **Structural processing / head model (~24 h).** SimNIBS `mri2mesh` builds the segmented,
   meshed head model; `dwi2cond` converts DWI to conductivity tensors (optional; skip -> assume
   isotropic). Register the group-level ROI mask into the subject's native, surface-aligned T1
   space (build the head model *before* registering EPI/mask so volume and surface data agree).
4. **Functional processing / single-subject site (~2-4 h).** `afni_proc.py` runs standard fMRI
   preprocessing + first-level GLM. Extract the peak-activation voxel, but only *within* the ROI
   mask; save the stimulation site as coordinates, a text file, and a small spherical ROI NIfTI
   for neuronavigation.
5. **E-field modeling (~20-30 min per model).** In SimNIBS, load the mesh + coil definition
   file, place the coil at the fMRI site, and iterate the E-field model across yaw (handle)
   orientations — default 24 orientations at 15-degree increments around a circle perpendicular
   to the scalp — outputting a normalized E-field NIfTI per orientation.
6. **Target/orientation selection (~30 min).** Resample E-fields to EPI resolution and sample
   induced current inside the target ROI for each orientation (`3dmaskave`). Build a
   doughnut-shaped orientation mask (current-in-ROI as a function of yaw), plot a polar graph,
   and pick the yaw vector that induces the largest E-field in the ROI. Sampling across the
   whole ROI is more stable across subjects than sampling only at the 5-mm site.
7. **Neuronavigation (~15 min).** Load the T1, the fMRI-peak sphere, the yaw-vector line, and
   the orientation mask into the navigation system (files are NIfTI, Brainsight-tested,
   broadly compatible). Set x/y/z from the cortical target, roll/pitch perpendicular to the
   skin, and yaw aligned to the selected vector; visually confirm the target, then stimulate
   while the subject performs the localizer task.

Core idea: fMRI fixes only 3 of the 6 coil degrees of freedom (x, y, z); the remaining
roll/pitch/yaw — especially yaw — are set by E-field modeling, under the working assumption
that maximizing induced current in the ROI maximizes the stimulation effect.

## Planning Rules Extracted

- Constrain noisy single-subject fMRI peaks with an a priori group/anatomical/meta-analytic ROI
  mask; do not use unconstrained single-subject peaks.
- Treat coil yaw/handle orientation as an optimization variable, not a fixed 45 degrees; search
  it with iterative E-field modeling (default 24 x 15-degree).
- Match ROI sampling size to the target claim (small sphere for a focal patch, whole-ROI for a
  region); prefer whole-ROI sampling for cross-subject stability.
- Budget 24-48 h between MRI and TMS; plan E-field models in parallel to save time.
- Build the head model before registering EPI/mask, and visually inspect every spatial
  transform (RAS vs surface-RAS mismatches are a common failure).
- E-field magnitude vs. tangential-component optimization is an open choice; the workflow is
  agnostic and either metric can be substituted in SimNIBS.

## Related Cards

`targeting/neuronavigation-and-efield.md`; `targeting/coil-orientation-and-intensity.md`;
`repos/simnibs.md`; `repos/slicertms.md`; `repos/navinibs.md`;
`papers/janssen-2015-coil-orientation-efield.md`;
`papers/richter-2013-optimal-coil-orientation.md`.
