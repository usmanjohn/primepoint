# -*- coding: utf-8 -*-
"""storyvideo — build, check and render one story video.

    python -m storyvideo lint    pm04        three gates, no rendering
    python -m storyvideo sheet   pm04        contact sheet of every scene
    python -m storyvideo preview pm04        scrubbable stage in Chrome
    python -m storyvideo render  pm04        the mp4 + the cue sheet
    python -m storyvideo draft   4           spec skeleton from the Corner story

Run from the storyvideo/ directory (or as `python -m storyvideo` from the repo
root).
"""

import argparse
import pathlib
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import build            # noqa: E402
import cue              # noqa: E402
import lint as lintmod  # noqa: E402
import render as R      # noqa: E402

OUT = HERE / "out"


def _scene_times(v):
    """One settled frame per scene -- what a scene looks like once it has landed."""
    return [min(b - 0.35, a + s.dur * 0.86) for a, b, s in v.bounds()]


def cmd_lint(a):
    v = build.load_story(a.slug)
    stage = build.build(v)
    return 1 if lintmod.run(v, stage, layout=not a.fast) else 0


def cmd_sheet(a):
    v = build.load_story(a.slug)
    stage = build.build(v, guides=a.guides)
    d = OUT / f"{a.slug}_frames"
    times = _scene_times(v) if a.per_scene else [i * a.every for i in
                                                 range(int(v.duration // a.every) + 1)]
    frames = R.shoot(stage, times, d, guides=a.guides)
    out = R.contact_sheet(frames, OUT / f"{a.slug}_sheet.png",
                          cols=a.cols, tile_w=310)
    print(f"-> {out}  ({len(frames)} frames)")
    return 0


def cmd_preview(a):
    v = build.load_story(a.slug)
    stage = build.build(v, guides=True, tail=SCRUB)
    print(f"-> {stage}")
    subprocess.run(["open", "-a", "Google Chrome", str(stage)])
    return 0


def cmd_render(a):
    v = build.load_story(a.slug)
    stage = build.build(v)

    if not a.skip_lint:
        if lintmod.run(v, stage, layout=True):
            print("\nlint failed — fix it or pass --skip-lint")
            return 1
        print()

    out = R.render(v, stage, fps=a.fps, workers=a.workers)
    got = R.duration_of(out)
    print(f"-> {out}  {out.stat().st_size / 1e6:.1f} MB  "
          f"spec {v.duration:.2f}s / file {got:.2f}s")
    if got and abs(got - v.duration) > 0.3:
        print(f"   WARNING: encoded length is off by {abs(got - v.duration):.2f}s")

    # Cue sheet, with a thumbnail of each scene.
    d = OUT / f"{a.slug}_frames"
    frames = R.shoot(stage, _scene_times(v), d)
    sheet = cue.build(v, thumbs=dict(enumerate(frames)))
    print(f"-> {sheet}")

    vs = R.sheet_from_video(out, OUT / f"{a.slug}_check.png", every=max(1, int(v.duration // 30)))
    print(f"-> {vs}  (contact sheet taken from the encoded file)")
    return 0


def cmd_draft(a):
    import draft
    print(draft.draft(int(a.order)))
    return 0


SCRUB = """
const bar = document.createElement('input');
bar.type = 'range'; bar.min = 0; bar.max = VIDEO.duration; bar.step = 0.05; bar.value = 0;
bar.style.cssText = 'position:fixed;left:20px;right:20px;bottom:16px;z-index:999';
const tag = document.createElement('div');
tag.style.cssText = 'position:fixed;left:20px;bottom:52px;z-index:999;font:700 22px Mulish,sans-serif;background:#1a1410;color:#faf7f2;padding:6px 14px;border-radius:9px';
document.body.append(bar, tag);
function draw(){ const t = +bar.value; seek(t);
  const s = VIDEO.scenes.find(s => t >= s.start && t < s.end) || {name:'-'};
  tag.textContent = t.toFixed(2) + 's  ' + s.name; }
bar.addEventListener('input', draw);
addEventListener('keydown', e => {
  const d = e.shiftKey ? 1 : 1/30;
  if (e.key === 'ArrowRight') { bar.value = +bar.value + d; draw(); }
  if (e.key === 'ArrowLeft')  { bar.value = +bar.value - d; draw(); }
});
draw();
"""


def main():
    ap = argparse.ArgumentParser(prog="storyvideo")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("lint");    p.add_argument("slug"); p.set_defaults(fn=cmd_lint)
    p.add_argument("--fast", action="store_true", help="skip the browser layout pass")

    p = sub.add_parser("sheet");   p.add_argument("slug"); p.set_defaults(fn=cmd_sheet)
    p.add_argument("--every", type=float, default=4.0)
    p.add_argument("--cols", type=int, default=6)
    p.add_argument("--per-scene", action="store_true", default=True)
    p.add_argument("--guides", action="store_true")

    p = sub.add_parser("preview"); p.add_argument("slug"); p.set_defaults(fn=cmd_preview)

    p = sub.add_parser("render");  p.add_argument("slug"); p.set_defaults(fn=cmd_render)
    p.add_argument("--fps", type=int, default=30)
    p.add_argument("--workers", type=int, default=4)
    p.add_argument("--skip-lint", action="store_true")

    p = sub.add_parser("draft");   p.add_argument("order"); p.set_defaults(fn=cmd_draft)

    a = ap.parse_args()
    sys.exit(a.fn(a))


if __name__ == "__main__":
    main()
