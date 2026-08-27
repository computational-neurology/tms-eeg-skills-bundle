---
type: paper-card
id: comolatti-2019-pcist
title: A fast and general method to empirically estimate the complexity of brain responses to transcranial and intracranial stimulations
year: 2019
authors: Comolatti, Pigorini, Casarotto, Fecchio, Faria, Sarasso, Rosanova, Gosseries, Boly, Bodart, Ledoux, Brichant, Nobili, Laureys, Tononi, Massimini, Casali
journal: Brain Stimulation 12(5):1280-1289
doi: 10.1016/j.brs.2019.05.013
code: https://github.com/renzocom/PCIst
source_pdf: PIIS1935861X19302207.pdf  # not stored in repo; locate via doi
tags:
  - metric:pci
  - complexity
  - consciousness
use_for:
  - what PCIst is and how it differs from PCI-LZ
  - benchmark values and classification performance
  - montage requirements for PCI
confidence: local-pdf-extracted
---

## Why This Matters For The Agent

The source paper for **PCIst** and the reference for `steps/pci.md` and `repos/pcist.md`. Load it whenever a user computes, reports, or interprets PCIst, or asks how PCI can be obtained without source modeling.

## What PCIst Does

PCI-LZ binarizes source-level TEPs against baseline statistics and compresses with Lempel-Ziv. That requires forward modeling, inverse solution, and permutation statistics at the single-trial level — heavy, hd-EEG-dependent, and not applicable to intracranial signals.

PCIst replaces that with a non-binary, sensor-level procedure in two steps:

1. **Dimensionality reduction** — SVD of the response; principal components retained to account for `≥ 99%` of response strength (mean field power), then components below a minimum SNR removed.
2. **State transition quantification** — per component, distance matrices are built for baseline and response, thresholded at scale `ε`, yielding transition matrices. `ΔNSTn = T_R[NST_res(ε*) − k × NST_base(ε*)]`, maximized over `ε`. `PCIst = Σ ΔNSTn`.

Equivalently `PCIst = N_C × mean(ΔNST)` — the product of **spatial differentiation** (surviving component count) and **temporal complexity** (mean transitions per component). Both are needed for a high value; a spatially rich but temporally flat response scores low, and vice versa.

Unlike PCI-LZ, PCIst is **not upper-bounded by 1**.

## Numbers

Benchmark: `382` TMS/hd-EEG sessions from `108` healthy subjects.

- Wakefulness: `47.89 ± 12.65`
- NREM sleep / anaesthesia (midazolam, xenon, propofol): `14.19 ± 5.26`, `p = 4.7 × 10^-40`
- AUC `0.998` for PCIst versus `0.995` for PCI-LZ on the same data
- Correlation with PCI-LZ: `r = 0.82`, `p < 10^-95`
- Computation: `0.71 ± 0.20 s` versus about `300 s` for PCI-LZ — stated as **~380x faster**, `p < 10^-127`

Brain-injured cohort: `108` patients, `337` TMS/hd-EEG sessions — 16 conscious (5 LIS, 11 EMCS) and 92 severe DOC (43 UWS, 49 MCS). Sensitivity by montage:

| Montage | LIS | EMCS | MCS |
|---|---|---|---|
| hd-EEG (60 ch) | 5/5 (100%) | 11/11 (100%) | 45/49 (91.8%) |
| 10-20 (19 ch) | 100% | 100% | 44/49 (89.8%) |
| 8 channels | 5/5 (100%) | 10/11 (90.9%) | 41/49 (83.7%) |

The **cutoff is derived empirically from the benchmark with a linear classifier, separately per montage** — there is no single universal PCIst threshold, and none of them is 0.31. `PCImax` (maximum across stimulation sites) is the reported per-patient statistic, paralleling the best-capacity logic of the CRS-R.

Intracranial validation: `9` epilepsy patients, `84` SPES/SEEG sessions, `42` stimulation sites. PCIst fell by `47.2%` on average from wakefulness to NREM (`p = 1.4 × 10^-7`), reproducing at the mesoscale what TMS-EEG shows at the macroscale.

## Methodological Points Worth Carrying

- **The benchmark's own preprocessing** was: 60-channel TMS-compatible amplifier, MRI-guided TMS, ~200 stimuli per session, visual rejection, ICA, spherical interpolation of bad channels, bandpass `0.1-45 Hz`, downsample to `725 Hz`, segment `-400` to `400 ms`, average reference, baseline correct `-400` to `-5 ms`. Absolute PCIst values are only comparable to that benchmark if the pipeline is comparable.
- **Masking in the benchmark was capped at `< 85 dB`** — noise tailored to the coil through inserted earphones, titrated within safety limits. Worth noting against the masking evidence held in the experiment-planner skill, where median SPL to fully mask real TMS was `84.1-89.0 dB` depending on noise type. The benchmark data may therefore carry some residual auditory contribution.
- The authors flag this themselves: sensory co-stimulation "can be effectively minimized but depends on many factors, such as coil type and effectiveness of noise masking, and is currently a matter of debate," citing the sensory-confound literature. A key argument for the SPES/SEEG replication is precisely that intracranial stimulation carries no auditory or somatosensory co-stimulation.
- `T_R` normalizes by the number of response samples, making PCIst extensive with signal length but largely independent of sampling rate.

## Claims To Avoid

Do not state a single universal PCIst cutoff, and never apply PCI-LZ's `0.31`. Do not compare absolute PCIst across studies with different montages or cleaning pipelines. Do not describe PCIst as a measure of local cortical excitability — it is a whole-response spatiotemporal complexity measure.

## Questions This Source Helps Answer

How is PCIst computed and how does it differ from the original PCI? What are normal awake versus unconscious values? Can PCI be computed without source modeling, or on a clinical 19-channel montage?

## Related Cards

`steps/pci.md`; `repos/pcist.md`; `papers/casarotto-2024-pci-mcs-eeg-dissociation.md`; `papers/casali-2012-consciousness-effective-connectivity.md`; `papers/massimini-2005-breakdown-effective-connectivity-sleep.md`; `papers/rosanova-2009-natural-frequencies.md`.
