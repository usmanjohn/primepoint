# -*- coding: utf-8 -*-
"""spec -> stage.html

The stage is one HTML file holding every scene of the video at once. Nothing in
it moves on its own: anim.js seek(t) decides what is visible and where. That is
what makes a frame a pure function of t, and therefore what lets six renderers
each jump into a different part of the timeline without talking to each other.
"""

import html as _html
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent

PAGE = """<!doctype html>
<meta charset="utf-8">
<title>{title}</title>
<link rel="stylesheet" href="{css}">
<body>
{scenes}
<div class="pipguide"></div>
<script src="{js}"></script>
<script>
window.VIDEO = {meta};
{tail}
</script>
"""


def load_story(slug):
    """Import storyvideo/stories/<slug>.py and hand back its VIDEO."""
    path = HERE / "stories" / f"{slug}.py"
    if not path.exists():
        sys.exit(f"no spec at {path}")
    sys.path.insert(0, str(HERE))
    spec = importlib.util.spec_from_file_location(f"storyvideo_story_{slug}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.VIDEO


def build(video, out=None, guides=False, tail=""):
    parts = []
    for i, (a, b, sc) in enumerate(video.bounds()):
        cls = "scene"
        if sc.dark:
            cls += " scene--dark"
        if sc.top:
            cls += " scene--top"
        parts.append(
            f'<section class="{cls}" data-start="{a:.4f}" data-end="{b:.4f}" '
            f'data-cam="{sc.cam}" data-name="{_html.escape(sc.name or f"s{i}")}">'
            f'{sc.html}</section>')

    meta = ("{" + f'"slug":"{video.slug}","duration":{video.duration:.4f},'
            f'"scenes":[' + ",".join(
                f'{{"name":"{_html.escape(sc.name)}","start":{a:.4f},"end":{b:.4f}}}'
                for a, b, sc in video.bounds()) + "]}")

    page = PAGE.format(
        title=_html.escape(video.title),
        css=(HERE / "stage.css").as_uri(),
        js=(HERE / "anim.js").as_uri(),
        scenes="\n".join(parts),
        meta=meta,
        tail=("document.body.classList.add('guides');\n" if guides else "") + tail,
    )
    out = pathlib.Path(out or HERE / "out" / f"{video.slug}.stage.html")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page, encoding="utf-8")
    return out
