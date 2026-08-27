---
type: repo-card
id: pcist
title: PCIst (Perturbational Complexity Index, state transitions)
source_url: https://github.com/renzocom/PCIst
author: Renzo Comolatti (renzo.com@gmail.com)
license: GPL-3.0
language: Python and MATLAB
tags:
  - metric:pci
  - complexity
  - tooling
---

## Role In The Skill

Reference implementation of **PCIst**, the sensor-level perturbational complexity index. Use it when a user wants to compute perturbational complexity without source reconstruction. It does **not** compute PCI-LZ — that requires a source-modeling pipeline this library does not provide.

## Layout

- `PCIst/pci_st.py` — Python module (~415 lines), the main implementation
- `PCIst.m` — MATLAB equivalent
- `setup.py` — packaging

Depends on NumPy/SciPy-level scientific Python only; no MNE or EEGLAB dependency.

## API

```python
from PCIst import pci_st
pci = pci_st.calc_PCIst(evoked, times, **par)
```

`calc_PCIst(signal_evk, times, full_return=False, **par)` takes a 2D `(channels, times)` **trial-averaged** array and a 1D `times` array in milliseconds with negative baseline values. It returns a float; with `full_return=True` it returns a dict including `dNST` (the per-component decomposition), `signal_svd`, `eigenvalues`, `var_exp`, and `snrs` — useful for QC.

Internally it runs `preprocess_signal()`, then the two published steps: `dimensionality_reduction()` and `state_transition_quantification()`. Both accept parameters through the same `**par` dict.

Published parameter sets:

```python
# TMS/EEG
par = {'baseline_window': (-400, -50), 'response_window': (0, 300), 'k': 1.2,
       'min_snr': 1.1, 'max_var': 99, 'embed': False, 'n_steps': 100}

# SPES/SEEG
par = {'baseline_window': (-250, -50), 'response_window': (10, 600), 'k': 1.2,
       'min_snr': 1.1, 'max_var': 99, 'embed': False, 'n_steps': 100, 'avgref': False}
```

Other exposed options: `max_thr_p`, time-delay embedding (`embed`, `L`, `tau`), `resample`, `avgref`, `baseline_corr`, `n_components`.

## Usage Notes

- Input must be the **averaged** TEP, not epochs.
- `times` is in milliseconds, matching the window parameters.
- If the input contains NaN, `calc_PCIst` prints a message and returns `0` — a silent-looking failure that is easy to mistake for a genuine low-complexity result. Check for NaN before calling, and treat an exact `0.0` as suspect.
- Use `full_return=True` for QC: inspect how many components survived `min_snr`, and how `dNST` distributes across them. PCIst is the product of component count and mean per-component transitions, so a value can be low for two very different reasons.

## Failure Modes

- Applying the PCI-LZ cutoff `0.31` to a PCIst value. Different scale entirely.
- Porting a cutoff across montages — the published thresholds are montage-specific and sensitivity drops as channel count falls.
- Computing PCIst on data cleaned differently from the benchmark and comparing absolute values.
- Feeding in data with residual muscle artefact, which is high-dimensional and transition-rich and therefore inflates PCIst.
- Treating an exact zero as a real measurement rather than the NaN guard.

## Related Cards

`steps/pci.md`; `papers/comolatti-2019-pcist.md`; `papers/casarotto-2024-pci-mcs-eeg-dissociation.md`; `repos/tmseegpy.md`.
