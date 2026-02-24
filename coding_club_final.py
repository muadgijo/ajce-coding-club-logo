# AJCE Coding Club — CLI terminal aesthetic, cooler type treatment

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

DPI = 240
fig, ax = plt.subplots(figsize=(10, 12.2), dpi=DPI)

BG     = '#0D0D0D'
PURPLE = '#8B5CF6'
WHITE  = '#FFFFFF'
DARK   = '#0F0F22'
DIM    = '#C084FC'

fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-1.15, 1.15)
ax.set_ylim(-1.72, 1.15)
ax.set_aspect('equal')
ax.axis('off')

FONT = 'Liberation Mono'
S    = 0.88

# Frame
ax.add_patch(FancyBboxPatch(
    (-S, -S), 2*S, 2*S,
    boxstyle="round,pad=0.04",
    facecolor=DARK, edgecolor=PURPLE,
    linewidth=4.0, zorder=2
))

# Inset ring
ax.add_patch(FancyBboxPatch(
    (-S+0.06, -S+0.06), 2*(S-0.06), 2*(S-0.06),
    boxstyle="round,pad=0.03",
    fill=False, edgecolor=PURPLE,
    linewidth=0.8, alpha=0.22, zorder=3
))

# Corner ticks
T, I = 0.15, 0.06
for (cx, cy), (dx, dy) in zip(
    [(-S,-S),(-S,S),(S,-S),(S,S)],
    [(1,1),(1,-1),(-1,1),(-1,-1)]
):
    kw = dict(color=PURPLE, linewidth=2.0, alpha=0.50, solid_capstyle='butt', zorder=4)
    ax.plot([cx+I*dx, cx+(I+T)*dx], [cy+I*dy, cy+I*dy], **kw)
    ax.plot([cx+I*dx, cx+I*dx], [cy+I*dy, cy+(I+T)*dy], **kw)

# >_ symbol
ARM   = 0.285
THETA = np.radians(27)
GAP   = 0.060
CUR_W = 0.36
CUR_H = 0.072

TIP_X = -(GAP + CUR_W - ARM * np.cos(THETA)) / 2
ax_x  = TIP_X - ARM * np.cos(THETA)
ax_y  = ARM * np.sin(THETA)
CY    = 0.07

LW = 13.0
ax.plot([TIP_X, ax_x], [CY, CY + ax_y],
        color=PURPLE, linewidth=LW,
        solid_capstyle='round', solid_joinstyle='round', zorder=5)
ax.plot([TIP_X, ax_x], [CY, CY - ax_y],
        color=PURPLE, linewidth=LW,
        solid_capstyle='round', solid_joinstyle='round', zorder=5)

CUR_X   = TIP_X + GAP
CUR_BOT = CY - ax_y - 0.028
ax.add_patch(Rectangle(
    (CUR_X, CUR_BOT), CUR_W, CUR_H,
    facecolor=PURPLE, edgecolor='none', zorder=5
))

# — Type stack —

# CODING CLUB — dominant, primary
ax.text(0, -1.02,
        'CODING CLUB',
        ha='center', va='center',
        fontsize=24, fontweight='bold',
        color=WHITE, fontfamily='Liberation Sans', zorder=6)

# AJCE — secondary, clearly smaller, not competing
ax.text(0, -1.165,
        'AJCE',
        ha='center', va='center',
        fontsize=17, fontweight='semibold',
        color=WHITE, fontfamily='Liberation Sans', zorder=6)

# tagline — tertiary, normal weight, purple, slightly pulled back
ax.text(0, -1.315,
        '{ code responsibly }',
        ha='center', va='center',
        fontsize=9.5, fontweight='normal',
        color=DIM, fontfamily='Liberation Mono',
        alpha=0.80, zorder=6)

out = '/mnt/user-data/outputs/coding_club_final.png'
plt.savefig(out, dpi=DPI, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print(f"Saved → {out}")
