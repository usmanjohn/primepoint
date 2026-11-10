# -*- coding: utf-8 -*-
"""Small helpers shared by the batch-2 «Mantiq jumbogʻi» specs (stagekit)."""
from spec import Scene
import stagekit as K

S = K.say


def scene(name, st, msg="", hold=0.8, hud=""):
    return Scene(round(st.end + hold, 2), st.html(msg=msg, hud=hud), cam="hold", name=name)


def bottle_grid(at=0.0, step=0.05, anim="rise", top=1000):
    """1000 bottles, 40 x 25, one row per element so they can arrive row by row."""
    rows = []
    one = ('<g transform="translate({x},0)"><rect x="5" y="0" width="6" height="5" fill="#7a5230"/>'
           '<rect x="1" y="5" width="14" height="21" rx="4" fill="#9b59b6" stroke="#5f3d73" '
           'stroke-width="1.5"/></g>')
    svg = ('<svg viewBox="0 0 900 26" width="900" height="26">'
           + "".join(one.format(x=4 + c * 22.4) for c in range(40)) + '</svg>')
    for r in range(25):
        tm = (f'data-at="{at + r * step:.3f}" data-dur="0.3" data-anim="{anim}"'
              if anim != "none" else 'data-at="0.000" data-dur="0.01" data-anim="none"')
        rows.append(f'<div class="sk-row" style="top:{top + r * 30}px" {tm}>{svg}</div>')
    return "".join(rows)
