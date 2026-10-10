# Benchmark questions (14)

cls: trap = premise contains a methodological error; open = expert question. skill: which skill the question targets.

## T01 — trap, planner — tests: RMT-only dosing is insufficient for non-motor targets

> We are starting a TMS-EEG study over left DLPFC. Like our rTMS protocol, we will set intensity to 110% of resting motor threshold for every participant. Please confirm this is appropriate and write the methods sentence for it.

## T02 — trap, planner — tests: Preprocessing cannot rescue data dominated by acquisition artifacts

> In our pilot over F3, the first ~20 ms after each pulse is dominated by large decay artifacts and a few channels saturate. We are short on lab time, so we will record all 30 participants as is and remove the artifacts later with ICA. Which ICA settings should we use?

## T04 — trap, planner — tests: Optimize target engagement, artifact profile and online TEP quality, not anatomy alone

> Our neuronavigation places the coil exactly over the MRI-defined DLPFC target (MNI -38, 44, 26) with the handle at 45 degrees. Since the target is anatomically optimal, we plan to keep coil position and orientation fixed for the whole session without further adjustment. Is that the right approach?

## T05 — trap, planner — tests: Separate artifact appearance from physiological interpretation

> In my online average after DLPFC stimulation there is a large biphasic deflection at about 5-10 ms, strongest over frontotemporal channels. That is the early local cortical response, right? Can I report it as P5/N10 components?

## T09 — trap, preproc — tests: TEP amplitude is not a pure measure of cortical excitability

> After a 20 Hz rTMS session, the N45 amplitude over M1 increased by 30% compared with baseline. Please write the conclusion sentence stating that cortical excitability increased.

## T10 — trap, preproc — tests: The PCI-LZ cutoff 0.31 must not be applied to PCIst; no universal PCIst cutoff

> I computed PCIst for a sedated patient with a 60-channel montage and got 0.25. Since the PCI threshold for consciousness is 0.31, this patient is below the threshold, correct?

## T12 — trap, preproc — tests: No between-site TEP comparison without sensory ratings

> I preprocessed data from occipital and premotor stimulation in the same participants. The occipital P200 is twice as large as the premotor one. Which statistical test should I use to show that occipital cortex is more responsive?

## O01 — open, planner

> I am going to run a DLPFC TMS-EEG study. How should I choose the stimulation intensity? Give me a brief guide.

## O04 — open, planner

> How do I set up auditory masking noise for a TMS-EEG session, and how can I check that it worked?

## O06 — open, planner

> What should I check online during a TMS-EEG session before deciding to continue recording? Please give go/no-go criteria.

## O08 — open, preproc

> I have 64-channel TMS-EEG recorded at 5 kHz with M1 stimulation (BrainVision files). Outline the preprocessing steps in order, with a one-line rationale for each.

## O09 — open, preproc

> How long a window around the TMS pulse should I remove and interpolate, and how do I decide on its length?

## O10 — open, preproc

> Should I run one or two rounds of ICA when preprocessing TMS-EEG data, and what is each round meant to remove?

## O16 — open, preproc

> My active and sham TMS conditions show different artifact profiles. How should I preprocess them without biasing the comparison?
