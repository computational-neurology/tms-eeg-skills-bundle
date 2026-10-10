"""Simple block scheme of the validation design."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

SKILL, DEFAULT = "#2a78d6", "#eb6834"
INK, INK2, LINE, SURFACE, BOX = "#0b0b0b", "#52514e", "#8a8984", "#fcfcfb", "#f1f0ec"
plt.rcParams.update({"font.family": ["Arial", "DejaVu Sans"], "svg.fonttype": "none", "figure.facecolor": SURFACE, "savefig.facecolor": SURFACE})

fig, ax = plt.subplots(figsize=(9, 7.2))
ax.set_xlim(0, 100); ax.set_ylim(0, 100); ax.axis("off")

def box(x, y, w, h, title, sub="", fc=BOX, ec=LINE, tc=INK, sc=INK2, dashed=False, bold=True):
    ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0,rounding_size=1.6", fc=fc, ec=ec, lw=1.6,
                                linestyle=(0, (4, 3)) if dashed else "solid", zorder=2))
    ax.text(x, y + (2.2 if sub else 0), title, ha="center", va="center", fontsize=10.5, color=tc, fontweight="bold" if bold else None, zorder=3)
    if sub: ax.text(x, y - 3.0, sub, ha="center", va="center", fontsize=8.6, color=sc, zorder=3, linespacing=1.3)

def arrow(x1, y1, x2, y2):
    ax.add_patch(FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>", mutation_scale=12, lw=1.4, color=LINE, zorder=1,
                                 shrinkA=0, shrinkB=0))

# 1 questions
box(50, 92, 46, 10, "14 TMS-EEG methods questions", "7 trap (false premise) · 7 open · frozen rubric")
# 2 arms
box(28, 73, 36, 11, "Skill", "Claude Opus 5.5 + TMS-EEG skills bundle\n3 repeats per question", fc=SKILL, ec=SKILL, tc=SURFACE, sc=SURFACE)
box(72, 73, 36, 11, "Default", "Claude Opus 5.5 alone\n3 repeats per question", fc=DEFAULT, ec=DEFAULT, tc=SURFACE, sc=SURFACE)
arrow(40, 87, 30, 78.5); arrow(60, 87, 70, 78.5)
# 3 answers + audit
box(50, 54, 52, 10, "84 answers (42 + 42)", "transcript audit: no web / MCP; skill files only in skill arm")
arrow(30, 67.5, 42, 59); arrow(70, 67.5, 58, 59)
# 4 outcomes
outs = [(13, "Expert\nblinding guesses", "24 answers, 2 raters"), (37, "Reproducibility", "agreement across\nthe 3 repeats"),
        (63, "Citation\naccuracy", "Crossref-verified"), (87, "Cost & length", "tokens, words,\ntime per answer")]
for x, t, s in outs:
    box(x, 30, 21, 15, t, s, bold=True)
    arrow(50, 49, x, 37.6)
box(50, 12, 46, 9, "Next: LLM-judge rubric score", "pre-registered primary outcome · pending", dashed=True, fc=SURFACE)
ax.text(1, 99.5, "Validation design", fontsize=13, color=INK, fontweight="bold", va="top")
for ext in ("png", "svg"): fig.savefig(f"validation_support/fig_validation_scheme.{ext}", dpi=300, bbox_inches="tight")
print("ok")
