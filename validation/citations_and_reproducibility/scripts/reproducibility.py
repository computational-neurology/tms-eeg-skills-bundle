"""Exploratory: consistency of the 3 repeats per question within each condition (post-hoc, not pre-registered)."""
import itertools, re
import numpy as np, pandas as pd
from scipy import stats
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

log = pd.read_csv("runs_log.csv", dtype=str, keep_default_na=False)
log["text"] = [open(f"runs/{r}.md").read() for r in log.run_id]
log["cond"] = log.arm.map({"A": "skill", "B": "default"})
cites = pd.read_csv("analysis_extra/citations_instances.csv")

# Key elements: quantitative parameters and named methods/tools/concepts (fixed list, defined before looking at per-condition results)
UNIT = r"(?:µV|uV|μV|ms|kHz|Hz|kΩ|kOhm|%\s*(?:RMT|MSO|rMT)|%|trials?|V/m|mm|dB)"
NUM = re.compile(rf"(?<![\w.])(\d+(?:[.,]\d+)?(?:\s*[–-]\s*\d+(?:[.,]\d+)?)?)\s*{UNIT}", re.I)
TERMS = ["ICA", "FastICA", "SSP-SIR", "SOUND", "TESA", "EEGLAB", "MNE", "FieldTrip", "SimNIBS", "neuronavigation", "e-field", "rt-TEP", "TAAC",
         "masking", "foam", "sham", "GMFA", "LMFP", "PCI", "PCIst", "interpolat", "downsampl", "baseline", "average reference", "cluster-based",
         "permutation", "go/no-go", "impedance", "decay", "muscle artifact", "pulse artifact", "N100", "P200", "N45", "P30", "N15", "P60",
         "RMT", "MSO", "scalp-to-cortex", "coil orientation", "real-time", "sensory rating", "auditory", "somatosensory", "SICI", "MEP"]
def elements(t):
    nums = {re.sub(r"trials$", "trial", re.sub(r"\s+", "", m.group(0)).lower().replace("μ", "µ").replace("uv", "µv").replace("–", "-").replace("—", "-").replace(",", "."))
            for m in NUM.finditer(t)}
    terms = {k.lower() for k in TERMS if re.search(re.escape(k), t, re.I)}
    return nums, terms

vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True, min_df=2).fit(log.text)
X = vec.transform(log.text)
log["i"] = range(len(log))

def jacc(a, b): return len(a & b) / len(a | b) if (a | b) else np.nan
rows = []
for (pid, cond), g in log.groupby(["prompt_id", "cond"]):
    idx = list(g.i); E = [elements(t) for t in g.text]
    C = [set(zip(cites[cites.run_id == r].key, cites[cites.run_id == r].year)) for r in g.run_id]
    pairs = list(itertools.combinations(range(len(idx)), 2))
    w = [len(t.split()) for t in g.text]
    rows.append(dict(prompt_id=pid, condition=cond,
        tfidf_cosine=np.mean([cosine_similarity(X[idx[a]], X[idx[b]])[0, 0] for a, b in pairs]),
        params_jaccard=np.nanmean([jacc(E[a][0], E[b][0]) for a, b in pairs]),
        terms_jaccard=np.nanmean([jacc(E[a][1], E[b][1]) for a, b in pairs]),
        citations_jaccard=np.nanmean([jacc(C[a], C[b]) for a, b in pairs]) if any(C) else np.nan,
        length_cv=np.std(w, ddof=1) / np.mean(w),
        n_params_mean=np.mean([len(e[0]) for e in E]), n_terms_mean=np.mean([len(e[1]) for e in E])))
r = pd.DataFrame(rows)
# Cross-condition baseline: similarity between skill and default answers to the same question
cross = []
for pid, g in log.groupby("prompt_id"):
    a = list(g[g.cond == "skill"].i); b = list(g[g.cond == "default"].i)
    cross.append(cosine_similarity(X[a], X[b]).mean())
r.to_csv("analysis_extra/reproducibility_per_question.csv", index=False)
cls = pd.read_csv("data/prompts.csv").set_index("prompt_id").cls
out = []
for m in ["tfidf_cosine", "params_jaccard", "terms_jaccard", "citations_jaccard", "length_cv", "n_params_mean", "n_terms_mean"]:
    p = r.pivot(index="prompt_id", columns="condition", values=m).dropna()
    t = stats.wilcoxon(p.skill, p.default) if len(p) > 5 and (p.skill != p.default).any() else None
    out.append(dict(measure=m, n_questions=len(p), skill_median=p.skill.median(), default_median=p.default.median(),
                    skill_higher=int((p.skill > p.default).sum()), wilcoxon_p=t.pvalue if t else np.nan))
s = pd.DataFrame(out); s.to_csv("analysis_extra/reproducibility_summary.csv", index=False)
print(s.round(3).to_string(index=False))
print(f"\ncross-condition TF-IDF cosine (skill vs default, same question): median {np.median(cross):.3f}")
print("\nby class (median):"); print(r.assign(cls=r.prompt_id.map(cls)).groupby(["cls", "condition"])[["tfidf_cosine", "params_jaccard", "terms_jaccard"]].median().round(3))
