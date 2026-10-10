"""Figures for the exploratory reproducibility and length results (paired dumbbell per question)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

SKILL, DEFAULT = "#2a78d6", "#eb6834"          # validated categorical slots 1-2 (light)
INK, INK2, GRID, SURFACE = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"
plt.rcParams.update({"font.family": ["Arial", "DejaVu Sans"], "svg.fonttype": "none", "font.size": 9, "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2,
                     "ytick.color": INK, "axes.facecolor": SURFACE, "figure.facecolor": SURFACE, "savefig.facecolor": SURFACE})
prompts = pd.read_csv("data/prompts.csv").set_index("prompt_id")

def label(pid):
    return f"{pid} ({prompts.loc[pid, 'cls']})"

def dumbbell(ax, wide, title, xlabel, order, xlim=None, fmt="{:.2f}"):
    y = range(len(order))
    for i, pid in enumerate(order):
        a, b = wide.loc[pid, "default"], wide.loc[pid, "skill"]
        ax.plot([a, b], [i, i], color=GRID if a == b else "#b9b8b2", lw=2, zorder=1, solid_capstyle="round")
    ax.scatter(wide.loc[order, "default"], y, s=55, color=DEFAULT, edgecolor=SURFACE, linewidth=1.5, zorder=3, label="Default (no skill)")
    ax.scatter(wide.loc[order, "skill"], y, s=55, color=SKILL, edgecolor=SURFACE, linewidth=1.5, zorder=3, label="Skill")
    ax.set_yticks(list(y), [label(p) for p in order])
    ax.set_title(title, loc="left", fontsize=10, color=INK, pad=8)
    ax.set_xlabel(xlabel, color=INK2)
    ax.grid(axis="x", color=GRID, lw=0.8); ax.set_axisbelow(True)
    for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
    ax.tick_params(axis="y", length=0)
    if xlim: ax.set_xlim(*xlim)
    med_d, med_s = wide["default"].median(), wide["skill"].median()
    ax.text(1.0, -0.13, f"median: default {fmt.format(med_d)} · skill {fmt.format(med_s)}", transform=ax.transAxes, ha="right", va="top", fontsize=8, color=INK2)

# Figure 1: reproducibility
r = pd.read_csv("analysis_extra/reproducibility_per_question.csv")
wide = {m: r.pivot(index="prompt_id", columns="condition", values=m) for m in ["params_jaccard", "terms_jaccard", "tfidf_cosine"]}
order = (wide["params_jaccard"]["skill"] - wide["params_jaccard"]["default"]).sort_values().index.tolist()
fig, axes = plt.subplots(1, 3, figsize=(11, 4.8), sharey=True)
dumbbell(axes[0], wide["params_jaccard"], "Same numerical parameters\nacross the 3 repeats", "Jaccard overlap (0-1)", order, (0, 1.05))
dumbbell(axes[1], wide["terms_jaccard"], "Same methods / tools named\nacross the 3 repeats", "Jaccard overlap (0-1)", order, (0, 1.05))
dumbbell(axes[2], wide["tfidf_cosine"], "Overall text similarity\nbetween the 3 repeats", "TF-IDF cosine (0-1)", order, (0, 1.05))
h, l = axes[0].get_legend_handles_labels()
fig.legend(h[::-1], l[::-1], loc="upper center", ncol=2, frameon=False, bbox_to_anchor=(0.5, 1.0))
fig.suptitle("Consistency of answers across repeats, per question (14 questions, Claude Opus 5.5)", x=0.01, ha="left", y=1.06, fontsize=11, color=INK)
fig.tight_layout(); fig.savefig("analysis_extra/fig_reproducibility.png", dpi=300, bbox_inches="tight"); fig.savefig("analysis_extra/fig_reproducibility.svg", bbox_inches="tight")

# Figure 2: words per response
t = pd.read_csv("results/tokens_words_per_run.csv")
w = t.groupby(["prompt_id", "condition"]).words.mean().unstack()
order2 = (w["skill"] - w["default"]).sort_values().index.tolist()
fig, ax = plt.subplots(figsize=(6.2, 4.8))
for cond, col, off in (("default", DEFAULT, -0.12), ("skill", SKILL, 0.12)):
    pts = t[t.condition == cond]
    ax.scatter(pts.words, [order2.index(p) + off for p in pts.prompt_id], s=12, color=col, alpha=0.35, linewidth=0, zorder=2)
dumbbell(ax, w, "Words per response, per question\n(large dots = mean of 3 repeats; small dots = single repeats)", "Words in the answer", order2, fmt="{:.0f}")
ax.legend(loc="lower right", frameon=False)
fig.tight_layout(); fig.savefig("analysis_extra/fig_words_per_response.png", dpi=300, bbox_inches="tight"); fig.savefig("analysis_extra/fig_words_per_response.svg", bbox_inches="tight")
print("ok")
