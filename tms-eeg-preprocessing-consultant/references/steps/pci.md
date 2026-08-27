---
type: step-card
id: pci
title: PCI — Nature, Interpretation, And Computation
tags:
  - metric:pci
  - step:analysis
  - complexity
  - consciousness
use_for:
  - what PCI actually measures
  - explaining why PCI increased or decreased
  - designing a TMS-EEG study around PCI
  - computing PCI-LZ or PCIst
---

## 1. What PCI Measures

PCI operationalises one specific claim: a system capable of consciousness must be simultaneously **integrated** (it responds as a whole, so a local perturbation propagates beyond the stimulated site) and **differentiated** (the response is not stereotyped, so many distinguishable spatiotemporal states occur). Either property alone is cheap. A single synchronised slow wave is integrated but not differentiated. Independent noise in every channel is differentiated but not integrated. PCI is high only when both hold at once.

This is why it is a **perturbational** measure. Spontaneous EEG shows what the network is doing; PCI shows what the network *can do* when pushed. That distinction is the reason PCI is not redundant with spectral EEG — in minimally conscious patients, PCI exceeded threshold regardless of whether the background EEG was mildly or severely abnormal, and did not correlate with delta (`rho = .11`) or alpha power (`rho = -.04`) at all (`papers/casarotto-2024-pci-mcs-eeg-dissociation.md`).

What PCI is **not**: it is not a measure of local excitability at the stimulated site, not a measure of response amplitude, and not a graded index of how conscious someone is. It is a whole-response spatiotemporal complexity measure with a detection threshold.

## 2. The Formula Is A Product — Use That

For PCIst the structure is explicit:

```
PCIst = N_C × mean(ΔNST)
        ↑        ↑
   spatial    temporal
differentiation complexity
```

`N_C` is the number of principal components surviving dimensionality reduction and the SNR filter — how many independent spatial patterns the response contains. `mean(ΔNST)` is the average number of significant state transitions per component, over and above baseline — how much each pattern actually does over time.

**A product falls if either factor falls.** This is the single most useful interpretive move available: before explaining a PCI change, decompose it. Call `calc_PCIst(..., full_return=True)` and inspect `dNST` (per-component contributions), `snrs`, and `var_exp`.

- Fewer components, similar transitions → the response became **spatially stereotyped**. The perturbation is producing one correlated pattern across the cortex.
- Similar components, fewer transitions → the response became **temporally stereotyped**. Spatial structure survives but each pattern does little.
- Both fell → global breakdown, the classic unconsciousness signature.

Two studies can report the same PCI drop for opposite reasons. Reporting the decomposition, not just the scalar, is what makes a PCI result interpretable.

## 3. Explaining A Decrease

**The established mechanism is cortical bistability** — the tendency of cortical neurons to plunge into a silent OFF-period after an initial activation. The OFF-period truncates the chain of causal interactions, so the response collapses into a stereotyped high-amplitude slow wave: few independent components, few transitions, low PCI. The same bistability generates the delta activity seen in spontaneous EEG, which is why slow waves and low complexity travel together without one causing the other.

Genuine low-PCI states: NREM sleep, anaesthesia (propofol, midazolam, xenon), unresponsive wakefulness syndrome, and **perilesional cortex**, where focal injury produces local sleep-like intrusions.

**But a low PCI has a differential diagnosis, and most entries are technical, not physiological:**

| Cause | How to distinguish |
|---|---|
| Genuine complexity loss (bistability) | Response present, high amplitude, stereotyped slow wave; decomposition shows both factors low |
| **Stimulation failed** | Online TEP below the `10 µV` peak-to-peak criterion in the first `50 ms`; no local response |
| **Target over or near a lesion** | Known from structural imaging; such sites are not expected to respond at all |
| **Too few trials** | Response not extracted from spontaneous variability; check trial count against `120-150` |
| **Over-cleaning** | ICA suppresses TEP amplitude globally (`artifacts/overcleaning-and-ica-risk.md`); compare pre/post cleaning |
| **Arousal drop mid-session** | Eyes closed, drowsiness; requires arousal monitoring to detect after the fact |
| **NaN in the input** | `calc_PCIst` returns exactly `0.0` — treat an exact zero as a bug, not a result |

A low PCI is therefore **weak evidence**, because genuine complexity loss and acquisition failure look identical in the scalar. Rule out the technical causes before offering a physiological reading.

## 4. Explaining An Increase

Genuine increases: recovery of consciousness after brain injury, emergence from anaesthesia, wakefulness versus NREM, and dissociative states where consciousness is present but disconnected — REM sleep and dreaming, ketamine anaesthesia, locked-in syndrome. The last group is the point of the measure: PCI stays high in people who cannot report or respond but are conscious.

**The dangerous direction is that artefact also raises PCI.** PCIst rewards exactly what artefact provides:

| Inflating source | Why it inflates |
|---|---|
| **Residual muscle artefact** | High-dimensional (many independent spatial patterns) and transition-rich (fast, jagged) — it scores on both factors at once |
| **Sensory co-stimulation** | Auditory and somatosensory input adds a response chain unrelated to the cortical perturbation; the measured complexity is partly of the sensory pathway |
| **Under-cleaning generally** | Ocular, line-noise, and high-frequency contamination all add spurious transitions |
| **Too few trials** | A noisy average carries transitions that do not survive proper averaging |

A high PCI in a lateral or frontal target deserves a residual-muscle check before it is believed — see `papers/biabani-2024-sensory-inputs-three-sites.md` for how often muscle survives ICA (62.1% at prefrontal). A high PCI with poor masking deserves scepticism about the auditory contribution; auditory masking is a design-side matter handled by the experiment-planner skill.

**Asymmetry worth internalising: a low PCI is easy to fake by failing, a high PCI is easy to fake by contaminating.** Neither direction is self-validating.

## 5. What PCI Does Not Track

State these whenever a user wants PCI to do more than it does:

- **Behavioural severity.** `PCImax` did not correlate with best total CRS-R (`rho = -.07, p = .65`).
- **Level within a diagnostic category.** It could not separate MCS+ from MCS− (`AUC = 52.2%`).
- **Alpha power or arousal-related spectral change.** PCI is unchanged by eyes opening despite the alpha reduction that causes.
- **Local cortical excitability.** That is what early TEP amplitude at the target indexes, and it is a different question.

PCI is a detection measure for capacity, not a graded or prognostic one.

## 6. Using PCI In TMS-EEG

**Design.** The reported statistic is `PCImax`, the maximum across stimulation sites — this parallels the best-capacity logic of the CRS-R, so use **at least two sites**. Within-subject and longitudinal designs are the defensible use; absolute cross-study comparison is not, because PCI inherits every preprocessing choice upstream of it.

**Acquisition criteria** (from clinical practice in `papers/casarotto-2024-pci-mcs-eeg-dissociation.md`) — PCI is acquisition-limited and no preprocessing recovers a failed recording:

- Targets **away from structural lesions**; sites over or adjacent to lesions do not respond.
- Targets placed to **avoid lateral scalp muscle** — e.g. ~1 cm lateral to midline over superior frontal gyrus (BA6/BA8) and superior parietal lobule (BA7).
- **Online amplitude criterion:** adjust location, orientation, and intensity until peak-to-peak exceeds `10 µV` in the first `50 ms` at the channel nearest the target, averaged over 20 trials. Use rt-TEP feedback.
- **`120-150` trials per site**, to extract the deterministic response from spontaneous variability — most critical where high-amplitude slow waves dominate.
- **Arousal monitoring** throughout, with a defined re-arousal protocol.
- **Auditory masking**, verified.

**Reporting.** Give the metric (PCI-LZ or PCIst), the full parameter set, the montage, trial count, number of sites, cutoff provenance, and — ideally — the `N_C` / `mean(ΔNST)` decomposition rather than the scalar alone.

## 7. Computing It — Two Different Metrics

"PCI" names two measures with different algorithms, scales, and cutoffs. Establish which one the user means before answering anything else.

| | **PCI-LZ** (Casali 2013) | **PCIst** (Comolatti 2019) |
|---|---|---|
| Level | Estimated **cortical sources** | **Sensor** space |
| Core operation | Binarise vs baseline stats, Lempel-Ziv compress | SVD, then recurrence-based state transitions |
| Source modeling | **Required** | **Not required** |
| Range | Normalised, bounded `≤ 1` | **Not upper-bounded** |
| Typical values | bounded `0-1`; individual `PCImax` near the cutoff, e.g. `0.34` and `0.40` in MCS | benchmark means `14.19 ± 5.26` (unconscious) to `47.89 ± 12.65` (awake) |
| Cutoff | `PCI* = 0.31` | Empirical, **montage-specific**, not 0.31 |
| Time per session | `~300 s` | `0.71 ± 0.20 s` — **~380x faster** |

They correlate at `r = 0.82` and classify equivalently (AUC `0.998` vs `0.995`), but **the numbers are not interchangeable**.

**The most common error is applying `0.31` to a PCIst value.** PCIst's awake benchmark mean is `47.89 ± 12.65`; 0.31 is meaningless on that scale. If a user quotes 0.31, confirm they computed PCI-LZ with source reconstruction.

**PCIst cutoffs are montage-specific.** Thresholds were re-derived per setup, and sensitivity falls with channel count:

| Montage | LIS | EMCS | MCS |
|---|---|---|---|
| hd-EEG (60 ch) | 5/5 (100%) | 11/11 (100%) | 45/49 (91.8%) |
| 10-20 (19 ch) | 100% | 100% | 44/49 (89.8%) |
| 8 channels | 5/5 (100%) | 10/11 (90.9%) | 41/49 (83.7%) |

Do not port a cutoff across montages, amplifiers, or pipelines without re-deriving it.

**PCIst code** (`repos/pcist.md`), published TMS-EEG parameters:

```python
from PCIst import pci_st
par = {'baseline_window': (-400, -50), 'response_window': (0, 300),
       'k': 1.2, 'min_snr': 1.1, 'max_var': 99,
       'embed': False, 'n_steps': 100}
pci = pci_st.calc_PCIst(evoked, times, **par)

# for interpretation, always prefer:
out = pci_st.calc_PCIst(evoked, times, full_return=True, **par)
out['PCI'], out['dNST'], out['snrs'], out['var_exp']
```

`evoked` is a 2D `(channels, times)` **trial-averaged** array; `times` is 1D in milliseconds with negative baseline. Parameters: `max_var=99` keeps components explaining 99% of response mean field power; `min_snr=1.1` drops low-SNR components; `k` (>1) weights baseline against response transitions, controlling noise sensitivity; `n_steps` sets the resolution of the search for the threshold maximising ΔNST.

Intracranial SPES/SEEG uses different windows — `baseline_window=(-250,-50)`, `response_window=(10,600)`, `avgref=False`.

PCI-LZ has no equivalent drop-in library here; it needs a source-modeling pipeline (forward model, inverse solution, bootstrap statistics for significant cortical activations, then normalised Lempel-Ziv complexity).

## 8. Claims To Avoid

Do not apply the PCI-LZ cutoff to PCIst or quote a single universal PCIst threshold. Do not compare absolute PCI across studies with different montages or cleaning pipelines. Do not present PCI as tracking severity, predicting outcome, or measuring local excitability. Do not report a bare scalar when the decomposition is available. Do not read a low PCI as loss of complexity until acquisition failure has been excluded.

## Related Cards

`papers/comolatti-2019-pcist.md`; `papers/casarotto-2024-pci-mcs-eeg-dissociation.md`; `repos/pcist.md`; `papers/casali-2012-consciousness-effective-connectivity.md`; `papers/massimini-2005-breakdown-effective-connectivity-sleep.md`; `papers/rosanova-2009-natural-frequencies.md`; `steps/gmfa-lmfp-computation.md`; `artifacts/overcleaning-and-ica-risk.md`; `papers/biabani-2024-sensory-inputs-three-sites.md`.
