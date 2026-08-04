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

---

## References

<sub>

Sources distilled into the bundle's cards. Listed alphabetically; entries shared by both skills appear once. Card contents are summaries and methodological extractions, not reproductions — consult the primary sources before acting on any recommendation.

</sub>

<sub>
<b>Literature</b><br><br>
Adank P, Kennedy-Higgins D, Maegherman G, Hannah R, Nuttall H E (2018). Effects of coil orientation on motor evoked potentials from orbicularis oris. <i>Frontiers in Neuroscience</i> 12:683. <a href="https://doi.org/10.3389/fnins.2018.00683">10.3389/fnins.2018.00683</a><br>
Atluri S, Frehlich M, Mei Y, Garcia Dominguez L, Rogasch N C, Wong W, Daskalakis Z J, Farzan F (2016). TMSEEG: a MATLAB-based graphical user interface for processing electrophysiological signals during transcranial magnetic stimulation. <i>Frontiers in Neural Circuits</i> 10:78. <a href="https://doi.org/10.3389/fncir.2016.00078">10.3389/fncir.2016.00078</a><br>
Atti I, Belardinelli P, Ilmoniemi R J, Metsomaa J (2024). Measuring the accuracy of ICA-based artifact removal from TMS-evoked potentials. <i>Brain Stimulation</i> 17(1):10–18. <a href="https://doi.org/10.1016/j.brs.2023.12.001">10.1016/j.brs.2023.12.001</a><br>
Balderston N L, Roberts C, Beydler E M, Deng Z-D, Radman T, Luber B, Lisanby S H, Ernst M, Grillon C (2020). A generalized workflow for conducting electric field-optimized, fMRI-guided, transcranial magnetic stimulation. <i>Nature Protocols</i> 15(11):3595–3614. <a href="https://doi.org/10.1038/s41596-020-0387-4">10.1038/s41596-020-0387-4</a><br>
Beck M M, Grandjean J, Hartwigsen G, Tomasevic L, Siebner H R (2024). Transcranial magnetic stimulation of primary motor cortex elicits an immediate transcranial evoked potential. <i>Brain Stimulation</i> 17(3):610–612. <a href="https://doi.org/10.1016/j.brs.2024.06.008">10.1016/j.brs.2024.06.008</a><br>
Belardinelli P, Biabani M, Blumberger D M, Bortoletto M, Casarotto S, David O, et al. (2019). Reproducibility in TMS-EEG studies: a call for data sharing, standard procedures and effective experimental control. <i>Brain Stimulation</i> 12(3):787–790. <a href="https://doi.org/10.1016/j.brs.2019.01.010">10.1016/j.brs.2019.01.010</a><br>
Biabani M, Fornito A, Mutanen T P, Morrow J, Rogasch N C (2019). Characterizing and minimizing the contribution of sensory inputs to TMS-evoked potentials. <i>Brain Stimulation</i> 12(6):1537–1552. <a href="https://doi.org/10.1016/j.brs.2019.07.009">10.1016/j.brs.2019.07.009</a><br>
Casali A G, Rosanova M, Massimini M, et al. (2012). Recovery of cortical effective connectivity and recovery of consciousness in vegetative patients. <i>Brain</i> 135(4):1308–1320. <a href="https://doi.org/10.1093/brain/awr340">10.1093/brain/awr340</a><br>
Casarotto S, Fecchio M, Rosanova M, Varone G, D'Ambrosio S, Sarasso S, Russo S, Comanducci A, Ilmoniemi R J, Massimini M (2022). The rt-TEP tool: real-time visualization of TMS-evoked potentials to maximize cortical activation and minimize artifacts. <i>Journal of Neuroscience Methods</i> 370:109486. <a href="https://doi.org/10.1016/j.jneumeth.2021.109486">10.1016/j.jneumeth.2021.109486</a><br>
Cline C C, Lucas M V, Sun Y, Menezes M, Etkin A (2021). Advanced artifact removal for automated TMS-EEG data processing. <i>10th International IEEE/EMBS Conference on Neural Engineering (NER)</i>:1039–1042. <a href="https://doi.org/10.1109/NER49283.2021.9441147">10.1109/NER49283.2021.9441147</a><br>
Gogulski J, Cline C C, Ross J M, Truong J, Sarkar M, Parmigiani S, Keller C J (2024). Mapping cortical excitability in the human dorsolateral prefrontal cortex. <i>Clinical Neurophysiology</i> 164:138–148. <a href="https://doi.org/10.1016/j.clinph.2024.05.008">10.1016/j.clinph.2024.05.008</a><br>
Gogulski J, Cline C C, Ross J M, et al. (2024). Reliability of the TMS-evoked potential in dorsolateral prefrontal cortex. <i>Cerebral Cortex</i> 34(4):bhae130. <a href="https://doi.org/10.1093/cercor/bhae130">10.1093/cercor/bhae130</a><br>
Gogulski J (2025). TMS-evoked potentials in the dlPFC: methodological considerations, reliability and sensory confounds. <i>Brain Stimulation</i> 18(1). <a href="https://doi.org/10.1016/j.brs.2024.12.184">10.1016/j.brs.2024.12.184</a><br>
Gomez-Tames J, Hamasaka A, Laakso I, Hirata A, Ugawa Y (2018). Atlas of optimal coil orientation and position for TMS: a computational study. <i>Brain Stimulation</i> 11(4):839–848. <a href="https://doi.org/10.1016/j.brs.2018.04.011">10.1016/j.brs.2018.04.011</a><br>
Gordon P C, Desideri D, Belardinelli P, Zrenner C, Ziemann U (2018). Comparison of cortical EEG responses to realistic sham versus real TMS of human motor cortex. <i>Brain Stimulation</i> 11(6):1322–1330. <a href="https://doi.org/10.1016/j.brs.2018.08.003">10.1016/j.brs.2018.08.003</a><br>
Gordon P C, Metsomaa J, Belardinelli P, Ziemann U (2026). Investigating the effects of TMS-related somatosensory inputs on TMS-evoked potentials provides evidence against significant interaction. <i>Scientific Reports</i>. <a href="https://doi.org/10.1038/s41598-026-37418-w">10.1038/s41598-026-37418-w</a><br>
Grasin S, Loginov S, Masliukova A, Smirnov A (2019). Realistic sham TMS. <i>Brain Stimulation</i> 12(2):e119. <a href="https://doi.org/10.1016/j.brs.2018.12.353">10.1016/j.brs.2018.12.353</a><br>
Hernandez-Pavon J C, Veniero D, Bergmann T O, Belardinelli P, Bortoletto M, Casarotto S, Casula E, Farzan F, Fecchio M, Julkunen P, Kallioniemi E, Lioumis P, Metsomaa J, Miniussi C, Mutanen T P, Rocchi L, Rogasch N C, Shafi M M, Siebner H R, Thut G, Zrenner C, Ziemann U, Ilmoniemi R J (2023). TMS combined with EEG: recommendations and open issues for data collection and analysis. <i>Brain Stimulation</i> 16(2):567–593. <a href="https://doi.org/10.1016/j.brs.2023.02.009">10.1016/j.brs.2023.02.009</a><br>
Hill A T, Rogasch N C, Fitzgerald P B, Hoy K E (2016). TMS-EEG: a window into the neurophysiological effects of transcranial electrical stimulation in non-motor brain regions. <i>Neuroscience &amp; Biobehavioral Reviews</i> 64:175–184.<br>
Jamil A, et al. (2024). The effect of stimulation intensity, sampling frequency, and sample synchronization in TMS-EEG on the TMS pulse artifact amplitude and duration. <i>IEEE Transactions on Neural Systems and Rehabilitation Engineering</i>. <a href="https://doi.org/10.1109/TNSRE.2024.3429176">10.1109/TNSRE.2024.3429176</a><br>
Janssen A M, Oostendorp T F, Stegeman D F (2015). The coil orientation dependency of the electric field induced by TMS for M1 and other brain areas. <i>Journal of NeuroEngineering and Rehabilitation</i> 12:47. <a href="https://doi.org/10.1186/s12984-015-0036-2">10.1186/s12984-015-0036-2</a><br>
Kabir M M, Dhami P, et al. (2024). Influence of large-scale brain state dynamics on the evoked response to brain stimulation. <i>Journal of Neuroscience</i> 44. <a href="https://doi.org/10.1523/JNEUROSCI.0782-24.2024">10.1523/JNEUROSCI.0782-24.2024</a><br>
Lankinen K, Fadel F, Nummenmaa A, Ilmoniemi R J, Raij T (2026). The effect of EEG lead configuration on early TMS-EEG artifacts. <a href="https://doi.org/10.64898/2026.02.10.705170">10.64898/2026.02.10.705170</a><br>
Lioumis P, Kicic D, Savolainen P, Mäkelä J P, Kähkönen S (2009). Reproducibility of TMS-evoked EEG responses. <i>Human Brain Mapping</i> 30(4):1387–1396.<br>
Lioumis P, Rosanova M (2022). The role of neuronavigation in TMS-EEG studies: current applications and future perspectives. <i>Journal of Neuroscience Methods</i> 380:109677. <a href="https://doi.org/10.1016/j.jneumeth.2022.109677">10.1016/j.jneumeth.2022.109677</a><br>
Lomi E, Jafarov O, Iannuzzo A, Roine T, Granö I, Gogulski J, Aydogan D B, Laakso I, Rosanova M, Rossi S, Makris N, Ilmoniemi R J, Lioumis P (2026). Distinct cortical excitability and connectivity profiles within the human SMA complex. <a href="https://doi.org/10.64898/2026.01.30.702764">10.64898/2026.01.30.702764</a><br>
Mäki H, Ilmoniemi R J (2011). Projecting out muscle artifacts from TMS-evoked EEG. <i>NeuroImage</i> 54(4):2706–2710.<br>
Massimini M, Ferrarelli F, Huber R, Esser S K, Singh H, Tononi G (2005). Breakdown of cortical effective connectivity during sleep. <i>Science</i> 309(5744):2228–2232.<br>
Momi D, Wang Z, Griffiths J D (2023). TMS-EEG evoked responses are driven by recurrent large-scale network dynamics. <i>eLife</i> 12:e83232. <a href="https://doi.org/10.7554/eLife.83232">10.7554/eLife.83232</a><br>
Mutanen T P, Kukkonen M, Nieminen J O, Stenroos M, Sarvas J, Ilmoniemi R J (2016). Recovering TMS-evoked EEG responses masked by muscle artifacts. <i>NeuroImage</i> 139:157–166.<br>
Mutanen T P, Metsomaa J, Makkonen M, Varone G, Marzetti L, Ilmoniemi R J (2022). Source-based artifact-rejection techniques for TMS-EEG. <i>Journal of Neuroscience Methods</i> 382:109693. <a href="https://doi.org/10.1016/j.jneumeth.2022.109693">10.1016/j.jneumeth.2022.109693</a><br>
Nuyts M, et al. (2025). Rostro-caudal TMS mapping of immediate transcranial evoked potentials reveals a pericentral crescendo-decrescendo pattern. <a href="https://doi.org/10.1101/2025.02.14.638272">10.1101/2025.02.14.638272</a><br>
Richter L, Neumann G, Oung S, Schweikard A, Trillenberg P (2013). Optimal coil orientation for transcranial magnetic stimulation. <i>PLoS ONE</i> 8(4):e60358. <a href="https://doi.org/10.1371/journal.pone.0060358">10.1371/journal.pone.0060358</a><br>
Rogasch N C, Thomson R H, Farzan F, Fitzgibbon B M, Bailey N W, Hernandez-Pavon J C, Daskalakis Z J, Fitzgerald P B (2014). Removing artefacts from TMS-EEG recordings using independent component analysis: importance for assessing prefrontal and motor cortex network properties. <i>NeuroImage</i> 101:425–439.<br>
Rogasch N C, Sullivan C, Thomson R H, Rose N S, Bailey N W, Fitzgerald P B, Farzan F, Hernandez-Pavon J C (2016). Analysing concurrent transcranial magnetic stimulation and electroencephalographic data: a review and introduction to the open-source TESA toolbox. <i>NeuroImage</i> 147:934–951.<br>
Rogasch N C, et al. Designing and comparing cleaning pipelines for TMS-EEG data.<br>
Rosanova M, Casali A, Bellina V, Resta F, Mariotti M, Massimini M (2009). Natural frequencies of human corticothalamic circuits. <i>Journal of Neuroscience</i> 29(24):7679–7685.<br>
Stango A, Zazio A, Barchiesi G, Bonfiglio N S, Bortoletto M (2025). Impact of high-frequency sampling rate and stimulation intensity on early TMS artifacts: considerations for immediate TMS-EEG responses. <i>NeuroImage</i> 320:121526. <a href="https://doi.org/10.1016/j.neuroimage.2025.121526">10.1016/j.neuroimage.2025.121526</a><br>
Stefanou M-I, Desideri D, Belardinelli P, Zrenner C, Ziemann U (2019). Brain state-dependent brain stimulation with real-time electroencephalography-triggered transcranial magnetic stimulation. <i>Journal of Visualized Experiments</i> 150.<br>
Székely O, Holmes N P, Ashton J, Breuer F, Chen H-Y, Di Chiaro N V, Duport A, Frangou P, Gwynne L, Hassan U, Lowe C J, Mathias B, Peng N, Pepper J L, Phylactou P, Szymanska M A, Tamè L (2026). Development and validation of the transcranial magnetic stimulation reporting assessment tool (TMS-RAT). <i>Brain Stimulation</i> 19:103155. <a href="https://doi.org/10.1016/j.brs.2026.103155">10.1016/j.brs.2026.103155</a><br>
Wischnewski M, Shirinpour S, Alekseichuk I, Lapid M I, Nahas Z, Lim K O, Croarkin P E, Opitz A (2024). Real-time TMS-EEG for brain state-controlled research and precision treatment: a narrative review and guide. <i>Journal of Neural Engineering</i> 21(6). <a href="https://doi.org/10.1088/1741-2552/ad8a8e">10.1088/1741-2552/ad8a8e</a><br>
Wu W, Keller C J, Rogasch N C, Longwell P, Shpigel E, Rolle C E, Etkin A (2018). ARTIST: a fully automated artifact rejection algorithm for single-pulse TMS-EEG data. <i>Human Brain Mapping</i> 39(4):1607–1625. <a href="https://doi.org/10.1002/hbm.23938">10.1002/hbm.23938</a><br>
Methodological choices matter: a systematic comparison of TMS-EEG preprocessing pipelines.<br>
</sub>

<sub>
<b>Tools and software</b><br><br>
AARATEP Pipeline — <a href="https://github.com/chriscline/AARATEPPipeline">github.com/chriscline/AARATEPPipeline</a><br>
MNE-Python — <a href="https://mne.tools/">mne.tools</a> · <a href="https://github.com/mne-tools/mne-python">github.com/mne-tools/mne-python</a><br>
NaviNIBS — <a href="https://github.com/precisionneurolab/navinibs">github.com/precisionneurolab/navinibs</a><br>
Nexstim NBS / SmartFocus nTMS E-field navigation — <a href="https://www.nexstim.com/research/tms-eeg">nexstim.com</a><br>
PyTEP-SOUND-SSP-SIR — <a href="https://github.com/MarcioCamposJr/PyTEP-SOUND-SSP-SIR">github.com/MarcioCamposJr/PyTEP-SOUND-SSP-SIR</a><br>
PyTepFit — <a href="https://github.com/GriffithsLab/PyTepFit">github.com/GriffithsLab/PyTepFit</a><br>
rt-TEP tool — see Casarotto et al. (2022) above<br>
SimNIBS — <a href="https://simnibs.github.io/simnibs/build/html/index.html">simnibs.github.io</a> · <a href="https://github.com/simnibs/simnibs">github.com/simnibs/simnibs</a><br>
SlicerTMS — <a href="https://github.com/lorifranke/SlicerTMS">github.com/lorifranke/SlicerTMS</a><br>
TESA (TMS-EEG Signal Analyser) — <a href="https://github.com/nigelrogasch/TESA">github.com/nigelrogasch/TESA</a><br>
TMS-RAT (TMS Reporting Assessment Tool) — <a href="https://tms-rat.org">tms-rat.org</a> · <a href="https://github.com/TMSMultiLab/TMSMultiLab/wiki">github.com/TMSMultiLab/TMSMultiLab/wiki</a><br>
tmseegpy — <a href="https://github.com/LazyCyborg/tmseegpy">github.com/LazyCyborg/tmseegpy</a><br>
</sub>
