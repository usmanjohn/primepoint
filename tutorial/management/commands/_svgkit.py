# -*- coding: utf-8 -*-
"""Tiny SVG geometry helper for the Prime Math geometry block (Blok E, PM-57…74).

NOT a Django management command — the leading underscore keeps it out of
`manage.py help`. It is an AUTHORING tool: run it from a throwaway generator
script, paste the printed SVG into the lesson file, then let
verify_pm_<range>.py re-check the result.

Hand-computed arc endpoints are how PM-59 shipped a figure whose angle mark
stopped 14° short of the ray it was marking. Everything angular in Blok E is
generated here instead, then re-checked by verify_pm_<range>.py.

Screen coordinates: y grows DOWNWARD, so a "maths angle" of 30° points
up-and-right on the page.
"""
import math

# ---------------------------------------------------------------------


def pt(vertex, angle_deg, r):
    """Point at radius r from vertex, at a maths angle (CCW from east)."""
    vx, vy = vertex
    a = math.radians(angle_deg)
    return (vx + r * math.cos(a), vy - r * math.sin(a))


def f(v):
    """Format a coordinate: no trailing .0, at most one decimal."""
    r = round(v, 1)
    return str(int(r)) if r == int(r) else str(r)


def arc(vertex, a_from, a_to, r, cls="pm-ln"):
    """Angle mark from maths-angle a_from to a_to, drawn the short way round.

    Returns an SVG <path>. The endpoints are exactly on the two rays, at
    exactly radius r — which is the property verify checks.
    """
    span = (a_to - a_from) % 360
    if span > 180:                       # always mark the angle itself
        a_from, a_to = a_to, a_from
        span = 360 - span
    p0 = pt(vertex, a_from, r)
    p1 = pt(vertex, a_to, r)
    # CCW in maths space == counter-clockwise on screen == sweep-flag 0
    return (f'<path class="{cls}" d="M {f(p0[0])} {f(p0[1])} '
            f'A {f(r)} {f(r)} 0 0 0 {f(p1[0])} {f(p1[1])}" fill="none"/>')


def arc_label(vertex, a_from, a_to, r, text, cls="pm-lbl", dy=4.5, dx=None):
    """Label sitting in the middle of that angle, at radius r."""
    span = (a_to - a_from) % 360
    if span > 180:
        a_from, a_to = a_to, a_from
        span = 360 - span
    mid = a_from + span / 2
    x, y = pt(vertex, mid, r)
    w = len(text) * 3.6 if dx is None else dx     # rough half-width
    return (f'<text class="{cls}" x="{f(x - w)}" y="{f(y + dy)}">{text}</text>')


def ray_angle(vertex, through):
    """Maths angle of the ray vertex -> through."""
    vx, vy = vertex
    tx, ty = through
    return math.degrees(math.atan2(vy - ty, tx - vx)) % 360


def line_at_y(p0, p1, y):
    """x where the line p0-p1 has that y."""
    (x0, y0), (x1, y1) = p0, p1
    t = (y - y0) / (y1 - y0)
    return x0 + t * (x1 - x0)


def tick(p0, p1, n=1, size=6, gap=5, cls="pm-ln"):
    """n small cross-ticks at the midpoint of a segment (equal-sides marks)."""
    (x0, y0), (x1, y1) = p0, p1
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    dx, dy = x1 - x0, y1 - y0
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L          # along
    nx, ny = -uy, ux                 # normal
    out = []
    start = -(n - 1) / 2
    for i in range(n):
        off = (start + i) * gap
        cx, cy = mx + ux * off, my + uy * off
        out.append(
            f'<line class="{cls}" x1="{f(cx - nx * size)}" y1="{f(cy - ny * size)}"'
            f' x2="{f(cx + nx * size)}" y2="{f(cy + ny * size)}"/>')
    return "\n    ".join(out)


def right_angle_mark(vertex, a1, a2, s=13, cls="pm-ln"):
    """The little square that means 90 degrees."""
    p1 = pt(vertex, a1, s)
    p2 = pt(vertex, a2, s)
    corner = (p1[0] + p2[0] - vertex[0], p1[1] + p2[1] - vertex[1])
    return (f'<polyline class="{cls}" points="{f(p1[0])},{f(p1[1])} '
            f'{f(corner[0])},{f(corner[1])} {f(p2[0])},{f(p2[1])}" fill="none"/>')


def arrow(p_from, p_to, size=6, cls="pm-pt"):
    """Solid triangular arrowhead at p_to, pointing along p_from -> p_to."""
    (x0, y0), (x1, y1) = p_from, p_to
    ang = math.atan2(y1 - y0, x1 - x0)
    back = ang + math.pi
    a = (x1 + size * 2 * math.cos(back - 0.38),
         y1 + size * 2 * math.sin(back - 0.38))
    b = (x1 + size * 2 * math.cos(back + 0.38),
         y1 + size * 2 * math.sin(back + 0.38))
    return (f'<polygon class="{cls}" points="{f(x1)},{f(y1)} '
            f'{f(a[0])},{f(a[1])} {f(b[0])},{f(b[1])}"/>')
