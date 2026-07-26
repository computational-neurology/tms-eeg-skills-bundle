<p align="center">
  <img src="logo.png" alt="TMS-EEG Skills Bundle mascot shaped like a figure-eight TMS coil" width="260">
</p>

<h1 align="center">TMS-EEG Skills Bundle</h1>

<p align="center">
  <strong>Evidence-aware guidance from experiment design to preprocessing.</strong><br>
  A methodological bundle of separately callable TMS-EEG agent skills.
</p>

## Installation and Use

The bundle can be used in several ways, depending on the agent environment and how that environment discovers skills.

1. **Claude.** Package each skill folder as a ZIP file and upload it through the Claude Skills interface. Where available, this can be done through `Settings > Skills`; alternatively, provide the ZIP in chat and ask Claude to install or create the skill.
2. **Claude Code.** Copy the skill folders directly into the local skills directory. Project-specific skills can be placed in `.claude/skills/`, while personal skills can be placed in `~/.claude/skills/`. Each skill folder includes a `SKILL.md` file and supporting `references/`, `recipes/`, and `templates/` folders.
3. **ChatGPT / Codex desktop app.** Manage skills through the desktop app by opening `Settings > Plugins` and selecting the Skills area or tab, where supported. The same skill folders can be uploaded or installed there, depending on workspace permissions and the available interface.
4. **Project-folder use.** For repository-based use, add the bundle directly to the project folder, for example under `.agents/skills/` for Codex or another documented location. If formal skill detection is not available, add instructions in `AGENTS.md`, `CLAUDE.md`, or the relevant project instruction file telling the agent to consult the appropriate `SKILL.md` first and load only the necessary cards, recipes, or templates.

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

AI assistance should be treated as support rather than a substitute for expert review, dataset inspection, or safety oversight during real experiments. The bundle includes constraints to reduce overreach: it does not imply that preprocessing can rescue data dominated by acquisition artifacts, or that TEP components can be interpreted definitively. Stimulation parameters, target locations, coil orientation, safety limits, and participant-specific constraints must always be verified against safety guidelines, local protocols, and expert supervision before implementation.

Several risks remain. AI models can produce fluent but incorrect statements, and recommendations should be checked against the cited primary literature and toolbox documentation. Performance may also vary across model versions, and the knowledge base may lag behind the literature or reflect gaps in the curated sources. For this reason, the card architecture is versioned and open to correction.

## License

This project is licensed under the MIT License.
