# Reproducibility across the 3 repeats (exploratory)

Each question's three repeats were compared with each other, separately per condition. The conditions were then compared per question (n = 14 questions, Wilcoxon signed-rank test). Claude Opus 5.5.

| Median per question | Skill | Default | Skill higher | p |
|---|---|---|---|---|
| Text similarity between repeats (TF-IDF cosine) | 0.46 | 0.40 | 13/14 | <0.001 |
| Same numerical parameters across repeats (Jaccard) | 0.48 | 0.26 | 12/14 | 0.001 |
| Same methods/tools named (Jaccard) | 0.73 | 0.67 | 11/14 | 0.013 |
| Variation in answer length (coefficient of variation) | 7% | 11% | 4/14 | 0.017 |
| Numerical parameters per answer | 9.7 | 8.2 | 7/14 | 0.80 |

Skill answers do not contain more numbers; they repeat the same ones across runs. Parameter overlap is the measure to quote, since text similarity is partly inflated by wording shared from the same skill files. Consistency is not correctness.

Figure: `figures/fig_reproducibility.png` (per-question values: `reproducibility_per_question.csv`). Examples: `EXAMPLES.md`.
