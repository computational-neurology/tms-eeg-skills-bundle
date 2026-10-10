# Citation accuracy and reproducibility across repeats (exploratory)

Both analyses were added after the data were collected; they are not pre-registered. Data: the 84 answers (14 questions x 2 conditions x 3 repeats, Claude Opus 5.5).

## 1. Citation accuracy

Method:
- Every author-year citation was extracted from the answers: in-text, e.g. "(Rossi et al., 2021)", and reference-list entries with title/journal (`citations_instances.csv`, 199 instances).
- Existence: each unique first-author + year was checked against Crossref.
- Detail accuracy: each reference-list entry that gives a title was checked for title, author, year and journal.
- Every automated miss was re-checked by targeted Crossref/DOI lookup (`*_adjudicated.csv`, evidence column).

| | skill | default |
|---|---|---|
| answers containing citations | 15 / 42 | 26 / 42 |
| citations per answer (mean) | 0.9 | 3.8 |
| unique papers cited | 13 | 35 |
| citations whose first-author + year exists | 38 / 38 | 161 / 161 |
| reference-list entries with title | 0 | 45 |
| ...of which with an error | — | 3 (6.7%) |

The three errors, all in default answers:
- Mutanen 2013 cited with the title and journal of Mutanen 2016 (wrong year / conflated papers).
- Rogasch 2017 with an invented title.
- Stokes 2005 with a paraphrased title and hedged year/journal ("2005/2007", "J Neurophysiol / Brain Stimulation").

Fabricated papers: none in either condition. All 42 unique cited author-year pairs exist; Gordon 2026 = Sci Rep, DOI 10.1038/s41598-026-37418-w.

Limitations:
- The check verifies that a cited paper exists, not that it supports the claim attached to it.
- In-text citations without titles can only be checked at author-year level.

## 2. Reproducibility across the 3 repeats

For each question and condition, the three repeats were compared pairwise (`reproducibility_per_question.csv`); the conditions were then compared paired by question (n = 14, Wilcoxon signed-rank).

| measure (median per question) | skill | default | skill higher | p |
|---|---|---|---|---|
| text similarity (TF-IDF cosine) | 0.46 | 0.40 | 13/14 | <0.001 |
| overlap of numerical parameters (Jaccard) | 0.48 | 0.26 | 12/14 | 0.001 |
| overlap of named methods/tools/concepts (Jaccard) | 0.73 | 0.67 | 11/14 | 0.013 |
| variability of answer length (CV) | 0.07 | 0.11 | 4/14 | 0.017 |
| numerical parameters per answer | 9.7 | 8.2 | 7/14 | 0.80 |

Skill answers to the same question agree more with each other, most clearly in the concrete numbers they recommend. They do not contain more numbers: the gain is consistency, not volume. Similarity between skill and default answers to the same question is lower (0.27), so the two conditions give different content.

Example (O01, DLPFC intensity):
- Skill: all three repeats give the same parameters (8-10 µV, 8-50 ms window, 10-30 trials, artifact >4 ms).
- Default: the three repeats share none, and propose 110% RMT, 120-130% RMT, 90-100% RMT, %MSO-per-mm corrections and 70-120 V/m in different runs.

Limitations:
- Text similarity partly reflects shared wording taken from the same skill files; parameter overlap is the more meaningful measure.
- Parameter and term extraction use fixed regular expressions and a fixed term list (`scripts/reproducibility.py`).
- Consistency is not correctness: whether the repeated recommendations are right is assessed by the LLM-judge analysis (pending).

See also: `reproducibility_table.md` (summary table), `figures/fig_reproducibility.png`, and `EXAMPLES.md` (worked examples: O01 DLPFC intensity, O04 masking, O10 ICA, T10 PCIst, and questions without a gain).
