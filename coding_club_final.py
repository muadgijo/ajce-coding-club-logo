# AJCE Coding Club — CLI terminal aesthetic

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

DPI = 240
fig, ax = plt.subplots(figsize=(10, 13), dpi=DPI)

BG     = '#0D0D0D'
PURPLE = '#8B5CF6'
WHITE  = '#FFFFFF'
DARK   = '#0F0F22'
DIM    = '#C084FC'
SOFT   = '#E9D5FF'

fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)
ax.set_xlim(-1.15, 1.15)
ax.set_ylim(-1.65, 1.15)
ax.set_aspect('equal')
ax.axis('off')

S = 0.88

# ── Frame ──
ax.add_patch(FancyBboxPatch(
    (-S, -S), 2*S, 2*S,
    boxstyle="round,pad=0.04",
    facecolor=DARK, edgecolor=PURPLE,
    linewidth=4.0, zorder=2
))

# ── Inset ring ──
ax.add_patch(FancyBboxPatch(
    (-S+0.06, -S+0.06), 2*(S-0.06), 2*(S-0.06),
    boxstyle="round,pad=0.03",
    fill=False, edgecolor=PURPLE,
    linewidth=0.8, alpha=0.22, zorder=3
))

# ── Corner ticks ──
tick_len   = 0.15
tick_inset = 0.06
corners    = [(-S, -S), (-S, S), (S, -S), (S, S)]
directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

for (cx, cy), (dx, dy) in zip(corners, directions):
    kw = dict(color=PURPLE, linewidth=2.0, alpha=0.50,
              solid_capstyle='butt', zorder=4)
    ax.plot([cx + tick_inset*dx, cx + (tick_inset + tick_len)*dx],
            [cy + tick_inset*dy, cy + tick_inset*dy], **kw)
    ax.plot([cx + tick_inset*dx, cx + tick_inset*dx],
            [cy + tick_inset*dy, cy + (tick_inset + tick_len)*dy], **kw)

# ── >_ symbol ──
arm_len  = 0.285
angle    = np.radians(27)
cur_gap  = 0.060
cur_w    = 0.36
cur_h    = 0.072
center_y = 0.07
line_w   = 13.0

tip_x  = -(cur_gap + cur_w - arm_len * np.cos(angle)) / 2
base_x = tip_x - arm_len * np.cos(angle)
base_y = arm_len * np.sin(angle)

ax.plot([tip_x, base_x], [center_y, center_y + base_y],
        color=PURPLE, linewidth=line_w,
        solid_capstyle='round', solid_joinstyle='round', zorder=5)
ax.plot([tip_x, base_x], [center_y, center_y - base_y],
        color=PURPLE, linewidth=line_w,
        solid_capstyle='round', solid_joinstyle='round', zorder=5)

cursor_x   = tip_x + cur_gap
cursor_bot = center_y - base_y - 0.028
ax.add_patch(Rectangle(
    (cursor_x, cursor_bot), cur_w, cur_h,
    facecolor=PURPLE, edgecolor='none', zorder=5
))


# ── Type stack ──

GLOW_OFFSET = 0.005
GLOW_ALPHA  = 0.22

# "CODING CLUB" — same size 32, sitting close below the frame
for gdx, gdy in [(-GLOW_OFFSET,  GLOW_OFFSET),
                 ( GLOW_OFFSET, -GLOW_OFFSET),
                 (-GLOW_OFFSET, -GLOW_OFFSET),
                 ( GLOW_OFFSET,  GLOW_OFFSET)]:
    ax.text(0 + gdx, -1.03 + gdy,
            'CODING CLUB',
            ha='center', va='center',
            fontsize=32, fontweight=700,
            color=PURPLE, fontfamily='DejaVu Sans',
            alpha=GLOW_ALPHA, zorder=5)

ax.text(0, -1.03,
        'CODING CLUB',
        ha='center', va='center',
        fontsize=32, fontweight=700,
        color=SOFT, fontfamily='DejaVu Sans',
        zorder=6)


# Rule pulled up to -1.13 — tighter gap after the title
ax.plot([-0.45, 0.45], [-1.13, -1.13],
        color=PURPLE, linewidth=0.5, alpha=0.30, zorder=6)


# "A  J  C  E" — bumped to 15, y=-1.21 — close to rule, punchy
ax.text(0, -1.21,
        'A  J  C  E',
        ha='center', va='center',
        fontsize=15, fontweight=700,
        color=DIM, fontfamily='DejaVu Sans',
        alpha=0.90, zorder=6)


# Tagline — 12pt, alpha 0.85, mono — loud enough to land
ax.text(0, -1.33,
        '{ code responsibly }',
        ha='center', va='center',
        fontsize=12, fontweight=400,
        color=DIM, fontfamily='DejaVu Sans Mono',
        alpha=0.85, zorder=6)


# ── Export ──
out = 'coding_club_final.png'
plt.savefig(out, dpi=DPI, bbox_inches='tight',
            facecolor=BG, edgecolor='none')
plt.close()
print(f"Saved → {out}")