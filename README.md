<p align="center">
  <img src="logo.png" alt="TMS-EEG Skills Bundle mascot shaped like a figure-eight TMS coil" width="260">
</p>

<h1 align="center">TMS-EEG Skills Bundle</h1>

<p align="center">
  <strong>Evidence-aware guidance from experiment design to preprocessing.</strong><br>
  A methodological bundle of separately callable TMS-EEG agent skills.
</p>

## Included Skills

| Skill | Role |
|---|---|
| `tms-eeg-experiment-planner` | Designs TMS-EEG studies before acquisition: target, coil orientation, intensity, trial count, sensory controls, rt-TEP monitoring, acquisition QC, neuronavigation, E-field simulation, SlicerTMS/NaviNIBS, and i-TEP practice. |
| `tms-eeg-preprocessing-consultant` | Plans, explains, and codes preprocessing/TEP analysis workflows after acquisition: artifact handling, MNE/Python, MATLAB/TESA, TEPs, GMFA/LMFP, i-TEPs, SOUND/SSP-SIR, ARTIST/AARATEP, and PyTepFit-oriented reasoning. |

## Runtime Design

- Keep each sub-skill narrow enough to route reliably.
- Use the experiment planner before data collection.
- Use the preprocessing consultant after data collection or when writing preprocessing scripts.
- Share methodological concepts through parallel card formats: routing cards, method cards, artifact cards, repository cards, paper cards, and templates/recipes.
- All cards include references to the relevant primary or methodological literature.

## Validation and Contributions

Community validation and contributions are welcome. If you identify an error, an unsupported claim, a missing reference, or an opportunity to improve a workflow, please open an issue or submit a pull request. Contributions from researchers and practitioners with direct TMS-EEG experience are especially encouraged.

## Disclaimer

AI assistance should be treated as assistance: it is not intended to replace expert review, direct dataset inspection, or engagement with the primary literature.

## License

This project is licensed under the MIT License.
