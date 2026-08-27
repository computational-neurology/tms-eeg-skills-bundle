---
type: paper-card
id: casarotto-2024-pci-mcs-eeg-dissociation
title: Dissociations between spontaneous electroencephalographic features and the perturbational complexity index in the minimally conscious state
year: 2024
authors: Casarotto, Hassan, Rosanova, Sarasso, Derchi, Trimarchi, Viganò, Russo, Fecchio, Devalle, Navarro, Massimini, Comanducci
journal: European Journal of Neuroscience 59(5):934-947
doi: 10.1111/ejn.16299
license: CC BY-NC
source_pdf: ejn-2024-casarotto-pci-mcs.pdf  # not stored in repo; locate via doi
tags:
  - metric:pci
  - complexity
  - consciousness
  - clinical
use_for:
  - why PCI is not redundant with spontaneous EEG
  - acquisition requirements for a valid clinical PCI
  - limits of PCI as a graded or prognostic measure
confidence: local-pdf-extracted
---

## Why This Matters For The Agent

Uses **PCI-LZ**, not PCIst — source-level, with the `PCI* = 0.31` cutoff. Two uses for this bundle: it is the clearest statement of what PCI adds over spontaneous EEG, and its methods section is an unusually explicit acquisition checklist for clinical TMS-EEG.

## Design

`40` MCS patients recruited, `39` analysed (one excluded for a skull breach rhythm producing outlier EEG voltage and spectral power); `40` healthy controls recruited, `39` analysed. 28 patients previously reported in Casarotto et al. 2016. Aetiology: vascular `21`, traumatic `11`, anoxic `7`. Best total CRS-R `7-15`; MCS− `24`, MCS+ `15`.

Per participant: ≥5 min spontaneous EEG plus TMS at ≥2 cortical sites in the same session. 62- or 60-channel TMS-compatible amplifiers, 10-20 montage, impedance `< 5 kΩ`.

Spontaneous EEG was classified visually into four categories and quantified as normalized PSD in delta (`0.5-4 Hz`) and alpha (`8-13 Hz`) over a posterior cluster. Visual categories: mildly abnormal `10` (25.6%), moderately abnormal `22` (56.4%), severely abnormal `7` (18%).

## The Dissociation

Spontaneous EEG in MCS was highly variable and differed markedly from controls — posterior delta PSDn higher (`p < .0005`), alpha PSDn lower (`p < .00001`), and the delta/alpha ratio separated all three visual categories (`H(2) = 25.66, p < .0001`).

`PCImax` behaved completely differently:

- It exceeded `PCI* = 0.31` in **every** MCS patient.
- It did **not** differ across EEG background categories (`H(2) = 0.42, p = .81`).
- It did **not** correlate with posterior delta (`rho = .11, p = .50`) or alpha PSDn (`rho = -.04, p = .81`).
- ROC showed `PCImax` outperformed every spectral measure for separating controls from MCS.

Two illustrative patients make the point: patient `#17` (mildly abnormal background, high alpha) had `PCImax = 0.34`; patient `#26` (severely abnormal background, dominant delta, lowest alpha) had `PCImax = 0.40`. Both above threshold, opposite spectral profiles.

Their mechanistic reading: focal or multifocal injury produces local slow waves that dominate the scalp EEG by amplitude and volume conduction, but are averaged out by repeated perturbation, which extracts the deterministic complexity of the remaining network.

## What PCI Does Not Do

State this whenever the card is cited — the paper is explicit:

- `PCImax` did **not** correlate with best total CRS-R (`rho = -.07, p = .65`).
- `PCImax` could **not** separate MCS+ from MCS− (`AUC = 52.2%`).

PCI is a **detection** measure for capacity for consciousness, not a graded severity or prognostic index. Spectral measures did no better on that discrimination (AUC `60.0-64.7%`), so this is a limit of the whole approach, not a defeat for PCI specifically.

## Acquisition Checklist (Reusable)

The discussion lists the conditions on which PCI's sensitivity depends. These transfer directly to any clinical TMS-EEG protocol:

1. **Accurate target selection distant from structural lesions**, ideally neuronavigated. Targets overlying or adjacent to lesions were deliberately skipped, because they are not expected to produce measurable EEG responses.
2. **Constant arousal monitoring** (eyes open); apply the CRS-R sensory arousal-facilitation protocol when arousal drops, interrupting the recording to do so.
3. **High-SNR TEPs** — peak-to-peak `> 10 µV` in the first `50 ms` at the channel nearest the target, after averaging 20 trials.
4. **`120-150` trials per site**, to extract the deterministic response from spontaneous variability — especially where high-amplitude slow waves dominate.

Two further choices worth copying: targets at superior frontal gyrus (BA6/BA8) and superior parietal lobule (BA7) placed **~1 cm lateral to midline specifically to avoid lateral scalp muscle**, and **rt-TEP used online** to adjust location, orientation, and intensity until the amplitude criterion was met. Masking was TAAC noise played continuously through in-ear earphones.

## Their TEP Preprocessing

Pulse artefact removed by replacing `-2` to `+5 ms` with a **mirrored copy of baseline `-2` to `-9 ms`**, followed by a 4 ms moving average — an alternative to interpolation worth knowing. Then high-pass `.01 Hz` (1st-order IIR), high-pass `.1 Hz` (3rd-order Butterworth), epoch `-800` to `+800 ms`, visual rejection of channels and trials, average reference, ICA for ocular and muscle components, low-pass `45 Hz`, cubic spline interpolation of bad channels. PCI then computed per Casali et al. 2013: downsample to `362.5 Hz`, cortical current density estimation, bootstrap statistics for significant activations, normalized algorithmic complexity.

## Limitations

Single measurement session; spontaneous EEG characterised by only a small subset of available measures; EEG reactivity systematically evaluated in only `11` patients; the technique requires dedicated expertise and is limited by contraindications to TMS, restricting diffusion in typical clinical settings.

**Competing interests are declared and non-trivial:** Massimini is co-founder and shareholder of Intrinsic Powers; Casarotto, Sarasso and Rosanova are advisors and shareholders; Russo is Chief Medical Officer of Manava Plus. Mention this if a user is weighing PCI for clinical adoption.

## Claims To Avoid

Do not use this paper to support a PCIst cutoff — it uses PCI-LZ. Do not present PCI as tracking severity or predicting outcome. Do not read "PCI above threshold in all MCS patients" as evidence PCI detects consciousness in *unresponsive* patients — this cohort was behaviourally minimally conscious by CRS-R.

## Questions This Source Helps Answer

Does PCI add anything over spontaneous EEG? Can a patient have a severely abnormal background EEG and still show high complexity? What acquisition conditions must be met for a clinical PCI to be valid? Does PCI track behavioural severity?

## Related Cards

`steps/pci.md`; `papers/comolatti-2019-pcist.md`; `repos/pcist.md`; `papers/casali-2012-consciousness-effective-connectivity.md`; `papers/massimini-2005-breakdown-effective-connectivity-sleep.md`; `steps/pulse-artifact-removal-or-interpolation.md`; `artifacts/auditory-somatosensory-confounds.md`.
