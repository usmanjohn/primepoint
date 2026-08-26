# -*- coding: utf-8 -*-
"""Sahna varaqasi — the sheet he rehearses from before recording.

Deliberately NOT a script. Reading prepared lines aloud was tried twice and
rejected; what works is talking freely over something already moving. So each
row gives the clock, a thumbnail of what is on screen and a talking POINT --
the fact to hit, not the sentence to say.

One self-contained HTML file (thumbnails inlined as data URIs) so it opens on
the tablet next to the video.
"""

import base64
import html
import pathlib

CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Mulish',system-ui,sans-serif;background:#f2ede4;color:#1a1410;
     padding:36px 22px 70px;line-height:1.5}
.wrap{max-width:780px;margin:0 auto}
h1{font-family:'Playfair Display',Georgia,serif;font-size:34px;line-height:1.15}
.sub{color:#8d8175;font-size:15px;margin:6px 0 4px}
.tot{color:#c9923a;font-weight:800;font-size:15px;margin-bottom:26px}
.hint{background:#fffdf7;border:2px solid #f0d9b5;border-radius:14px;
      padding:14px 18px;font-size:14px;color:#4a3f35;margin-bottom:30px}
.row{display:flex;gap:16px;background:#fff;border-radius:16px;padding:14px;
     margin-bottom:14px;box-shadow:0 3px 12px rgba(26,20,16,.07)}
.row img{width:92px;border-radius:9px;flex:0 0 auto;background:#faf7f2;
         border:1px solid #e8e0d4}
.meta{flex:1;min-width:0}
.t{font-family:'Playfair Display',Georgia,serif;font-weight:800;font-size:21px;
   color:#c9923a}
.n{font-size:12px;color:#8d8175;text-transform:uppercase;letter-spacing:.07em;
   margin:2px 0 7px}
.say{font-size:16px;color:#1a1410}
.beat{background:#f7f3ec;border-left:5px solid #b84444}
.beat .say{color:#b84444;font-weight:700}
@media print{body{background:#fff}.row{break-inside:avoid;box-shadow:none;
  border:1px solid #e8e0d4}}
"""


def _clock(t):
    return f"{int(t) // 60}:{int(t) % 60:02d}"


def build(video, thumbs=None, out=None):
    """thumbs: {scene_index: path to a png} -- inlined so the file travels alone."""
    rows = []
    for i, (a, b, sc) in enumerate(video.bounds()):
        img = ""
        p = (thumbs or {}).get(i)
        if p and pathlib.Path(p).exists():
            b64 = base64.b64encode(pathlib.Path(p).read_bytes()).decode()
            img = f'<img src="data:image/png;base64,{b64}" alt="">'
        cls = "row beat" if sc.name == "beat" else "row"
        rows.append(
            f'<div class="{cls}">{img}<div class="meta">'
            f'<div class="t">{_clock(a)} – {_clock(b)}</div>'
            f'<div class="n">{html.escape(sc.name)} · {sc.dur:.1f}s</div>'
            f'<div class="say">{html.escape(sc.note)}</div>'
            f'</div></div>')

    page = f"""<!doctype html><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(video.title)} — sahna varaqasi</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;800&family=Mulish:wght@400;700;800&display=swap" rel="stylesheet">
<style>{CSS}</style>
<div class="wrap">
<h1>{html.escape(video.title)}</h1>
<div class="sub">{html.escape(video.lesson)} · {html.escape(video.story)}</div>
<div class="tot">{video.duration:.0f} soniya · {len(video.scenes)} sahna</div>
<div class="hint"><b>Bu matn emas — tayanch.</b> Har sahnada nimani aytish
kerakligi yozilgan, qanday aytish sizga havola. Videoni bir marta koʻrib
chiqing, keyin yozib oling.<br><br>
<b>Qizil sahna</b> — jim turadigan joy: tomoshabin oʻzi hisoblasin.</div>
{"".join(rows)}
</div>"""
    out = pathlib.Path(out or pathlib.Path(__file__).parent / "out" /
                       f"{video.slug}_sahna.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out
