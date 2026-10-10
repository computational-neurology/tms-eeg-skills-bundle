# Reproducibility: examples

Parameters "in all 3 repeats" were extracted automatically from the answers and checked in context. Full answers: `../03_answers/answers_by_question.md`.

**O01: choosing stimulation intensity for DLPFC (open question).** All three skill answers gave the same operational procedure:
- use RMT only as a starting reference (two runs gave 90-120% RMT), then titrate at the target with short online averages of 10-30 trials;
- aim for an early local response of about 8-10 µV peak-to-peak in the 8-50 ms window;
- treat deflections beyond about 4 ms over frontotemporal channels as muscle artifact that caps the intensity.

The three default answers shared no parameter. Each proposed a different dosing rule: 110% RMT, 120-130% RMT, 90-100% RMT, %MSO-per-mm distance corrections or 70-120 V/m e-field targets. A user asking twice would get two different protocols.

**O04: setting up auditory masking (open question).** All three skill answers described the same click-based masking procedure:
- record the click at 96 kHz about 25 cm from the coil, deliver pulses at a jittered 2000-2300 ms interval, and raise the noise until the click is undetectable on 10 consecutive pulses;
- titrate under real rather than sham TMS, because real stimulation needed about 6 dB more masking (84.1 vs 78.3 dB);
- click-derived noise masked at a lower level than white noise, roughly 83-84 vs 87 dB.

The default answers agreed only on generic values (the click exceeds 100 dB; keep the noise at or below about 90 dB). Their titration steps and verification criteria differed between runs.

**O10: one or two rounds of ICA (open question).** All three skill answers cited the same evidence and window:
- a pulse-removal window of about -2 to 10-12 ms;
- residual TMS-evoked muscle in the 5-15 ms window after a two-pass FastICA pipeline in about 62% of participants after prefrontal, 35% after premotor and 0% after parietal stimulation (Biabani et al. 2024).

The default answers shared only a generic 1-100 Hz band-pass.

**T10: applying the 0.31 PCI cutoff to PCIst (trap question).** All three skill answers gave the same checks before trusting a low PCIst:
- an early local TEP above 10 µV peak-to-peak within 50 ms after about 20 trials;
- the benchmark preprocessing (0.1-45 Hz band-pass, downsampling to 725 Hz).

The default answers agreed only on "a clear early response within about 50 ms"; one mentioned a ≥120 V/m field criterion, the others did not.

**Where the skill did not increase consistency.** In T01 (110% RMT for DLPFC) and T12 (comparing TEPs between sites), default answers were as consistent as, or slightly more consistent than, skill answers. In T01 the shared numbers largely come from the question itself (110% RMT) or from standard textbook values (50 µV MEP criterion).

**Caveat.** Several of the repeated skill values are figures from specific papers carried by the skill cards (e.g. 62% / 35% / 0%, 84.1 vs 78.3 dB). Consistency here means the answers are anchored to the same sources; whether the recommendations are correct is assessed separately (LLM-judge analysis, pending).
