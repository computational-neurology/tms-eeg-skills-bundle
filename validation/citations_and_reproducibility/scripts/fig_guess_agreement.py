"""Tile chart: true condition vs each rater's guess for the 24 blinded answers, grouped by rater agreement."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Patch
import pandas as pd

SKILL, DEFAULT = "#2a78d6", "#eb6834"
INK, INK2, GRID, SURFACE = "#0b0b0b", "#52514e", "#e6e5e1", "#fcfcfb"
plt.rcParams.update({"font.family": ["Arial", "DejaVu Sans"], "svg.fonttype": "none", "font.size": 9, "figure.facecolor": SURFACE, "savefig.facecolor": SURFACE})
D = "validation_support/04_human_blinding_guesses"
t = pd.read_csv(f"{D}/guesses_with_truth.csv")
t["agree"] = t.rater1_guess == t.rater2_guess
t = t.sort_values(["agree", "true_condition", "cls", "prompt_id", "blind_id"], ascending=[False, False, True, True, True]).reset_index(drop=True)

n_ag = int(t.agree.sum()); gap = 1.0
rows_y = [i if a else i + gap for i, a in enumerate(t.agree)]
fig, ax = plt.subplots(figsize=(6.4, 8.6))
cols = [("true_condition", "True\ncondition", None), ("rater1_guess", "Rater 1\nguess", "rater1_correct"), ("rater2_guess", "Rater 2\nguess", "rater2_correct")]
W, H = 0.92, 0.84
for j, (col, head, ok) in enumerate(cols):
    ax.text(j, -1.1, head, ha="center", va="bottom", fontsize=9.5, color=INK, fontweight="bold")
    for y, (_, r) in zip(rows_y, t.iterrows()):
        val = r[col]; fill = SKILL if val == "skill" else DEFAULT
        correct = True if ok is None else bool(r[ok])
        ax.add_patch(Rectangle((j - W / 2, y - H / 2), W, H, facecolor=fill if correct else SURFACE, edgecolor=fill, lw=2,
                               hatch=None if correct else "//", zorder=2))
        txt = val if ok is None else (f"{val}  ✓" if correct else f"{val}  ✗")
        ax.text(j, y, txt, ha="center", va="center", fontsize=8.5, color=SURFACE if correct else INK, zorder=3,
                bbox=None if correct else dict(boxstyle="round,pad=0.18", facecolor=SURFACE, edgecolor="none"))
for y, (_, r) in zip(rows_y, t.iterrows()):
    ax.text(-0.62, y, f"{r.blind_id} · {r.prompt_id} ({r.cls})", ha="right", va="center", fontsize=8.5, color=INK)
# group headers
ax.text(-2.05, -0.75 + 0.15, "", fontsize=1)
ax.annotate(f"Raters agreed: {n_ag}/24 answers, all correct", xy=(2.6, (n_ag - 1) / 2), xytext=(2.62, (n_ag - 1) / 2), ha="left", va="center", fontsize=9, color=INK)
ax.plot([2.55, 2.55], [-0.4, n_ag - 0.6], color=INK2, lw=1.2)
y0, y1 = n_ag + gap - 0.4, len(t) + gap - 0.6
ax.plot([2.55, 2.55], [y0, y1], color=INK2, lw=1.2)
ax.text(2.62, (y0 + y1) / 2, f"Raters disagreed: {len(t) - n_ag}/24\nrater 2 correct, rater 1 wrong\n(5 of 6 are trap questions)", ha="left", va="center", fontsize=9, color=INK)
ax.set_xlim(-2.3, 4.6); ax.set_ylim(len(t) + gap, -1.6); ax.axis("off")
ax.set_title("Blinded expert guesses: skill or default?\n24 answers, 2 raters (never both wrong)", loc="left", x=-0.02, fontsize=11, color=INK, pad=34)
legend = [Patch(facecolor=SKILL, edgecolor=SKILL, label="skill"), Patch(facecolor=DEFAULT, edgecolor=DEFAULT, label="default"),
          Patch(facecolor=SURFACE, edgecolor=INK2, hatch="//", label="wrong guess (✗)")]
ax.legend(handles=legend, loc="lower left", bbox_to_anchor=(0.0, -0.06), ncol=3, frameon=False, fontsize=8.5)
fig.tight_layout()
for ext in ("png", "svg"): fig.savefig(f"{D}/fig_guess_agreement.{ext}", dpi=300, bbox_inches="tight")
print("ok")
