# Tokens and answer length per response

Source: the audited transcript of each of the 84 runs (usage summed per API call, de-duplicated by message id) and the word count of each answer file.

Columns in `tokens_words_per_run.csv`:
- `words`: words in the final answer
- `output`: generated tokens (answer, tool calls and any reasoning)
- `fresh_input`: input processed for the first time (uncached + cache writes)
- `cache_read`: context re-read from cache on later turns (billed at a reduced rate)
- `total_processed`: sum of all of the above
- `api_calls`: model turns, i.e. calls to the model; each tool use (reading a file, writing the answer) ends one turn and starts another
- `seconds_to_answer_written`, `seconds_total`: wall-clock time from the start of the run to writing the answer / to the last event
- `files_read`: skill files opened

`tokens_words_summary.csv` compares the two conditions paired by question (14 questions, mean of 3 repeats each; Wilcoxon signed-rank test).

Medians per question, skill vs default:
| measure | skill | default | ratio |
|---|---|---|---|
| words | 1,368 | 1,081 | 1.21 |
| output tokens | 6,015 | 3,900 | 1.51 |
| fresh input tokens | 49,371 | 25,556 | 1.84 |
| total processed tokens | 453,935 | 111,417 | 4.15 |
| model turns | 7 | 2 | 3.5 |
| time per response (s) | 88 | 64 | 1.44 |

Token, length and turn differences: p ≤ 0.001. Time: p = 0.011 (skill slower for 10/14 questions).

Timing caveat: runs were executed in parallel batches (a median of 18 other runs active at the same time), so the absolute seconds include queueing and rate-limit delays. Duration correlates with concurrency (rho 0.35); compare the conditions relative to each other, not as absolute latency.

Figure: `figures/fig_words_per_response.png`: words per response for each question (mean of 3 repeats and single repeats). Skill answers are longer for 13 of 14 questions; O01 (DLPFC intensity) is the exception, where the skill answers are shorter.
