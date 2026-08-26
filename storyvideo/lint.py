# -*- coding: utf-8 -*-
"""Three gates a video must pass before it is worth rendering.

1. LAYOUT   -- nothing clipped by the frame, nothing hidden under the PIP circle,
               no type too small to read on a phone.
2. COUNT    -- every quantity a scene claims is both dealt out as n discrete
               objects and tracked by a counter. "Countable on screen" is the
               format's one hard promise.
3. ARITHMETIC -- every sum a scene puts on screen is recomputed here. CLAUDE.md
               requires every number in this course to be computed twice, and a
               wrong answer key is the worst thing this pipeline could ship.
"""

import re
import pathlib

FRAME_W, FRAME_H = 1080, 1920
PIP = (880, 240, 200)               # cx, cy, r -- his face circle
MIN_FONT = 34
MAX_DUR = 180


# ───────────────────────────────────────────────── arithmetic gate ──
def _norm(e):
    """Uzbek maths notation -> something Python can evaluate."""
    e = (e.replace("\u00d7", "*").replace("\u00b7", "*").replace("\u00f7", "/")
          .replace("\u2212", "-").replace("\u2013", "-")
          .replace("\u00a0", " ").replace("\u2009", " ").replace("\u202f", " "))
    # Uzbek writes thousands with a space: 25 000, 1 300 000. Join those digits
    # or the sum is silently skipped instead of being checked -- and a silent
    # skip on a price is exactly how a wrong answer would reach a pupil.
    prev = None
    while prev != e:
        prev = e
        e = re.sub(r"(?<=\d) (?=\d)", "", e)
    # Uzbek decimal comma: 0,4 -> 0.4. Only between digits, so the separator in
    # "= 6, qoldiq 1" is left alone.
    e = re.sub(r"(?<=\d),(?=\d)", ".", e)
    return e


def _value(side):
    """Evaluate one side of an equation, or None if it states no number."""
    side = side.split(":")[-1]                    # drop a label: "narxi: 52*25000"
    s = re.sub(r"[^\d+\-*/(). ]", " ", side)
    s = re.sub(r"\s+", " ", s).strip()
    if not s or not re.search(r"\d", s):
        return None                               # words only; asserts nothing
    if " " in s and not re.search(r"[+\-*/()]", s):
        s = s.split()[0]                          # "56 m" -> "56"
    try:
        return eval(s, {"__builtins__": {}}, {})
    except Exception:
        return None


def check_expression(raw):
    """Return (ok, detail). Anything that asserts nothing is skipped."""
    e = _norm(raw).strip()

    # "a / b = q, qoldiq r" -- division with a remainder, the shape this course
    # leans on hardest, and the one the PM-4 story turns on.
    m = re.match(r"^\s*(\d+)\s*/\s*(\d+)\s*=\s*(\d+)\s*[,(]?\s*qoldiq\s*(\d+)\)?\s*$",
                 e, re.I)
    if m:
        a, b, q, r = (int(x) for x in m.groups())
        if b == 0:
            return False, f"{raw}: division by zero"
        if q * b + r != a:
            return False, f"{raw}: {q}*{b}+{r} = {q*b+r}, not {a}"
        if r >= b:
            return False, f"{raw}: remainder {r} is not smaller than divisor {b}"
        if a // b != q:
            return False, f"{raw}: {a}//{b} = {a//b}, not {q}"
        return True, f"{raw} \u2713"

    if "=" not in e:
        return True, None                         # states a sum, asserts no result

    sides = [x.strip() for x in e.split("=") if x.strip()]
    if len(sides) < 2:
        return True, None
    vals = [_value(x) for x in sides]
    if any(v is None for v in vals):
        return True, None
    if len({round(v, 9) for v in vals}) != 1:
        return False, f"{raw}: sides differ -> {vals}"
    return True, f"{raw} \u2713"


def check_arithmetic(video):
    bad, checked = [], 0
    for _, _, sc in video.bounds():
        for claim in sc.claims:
            ok, detail = check_expression(claim)
            if detail:
                checked += 1
            if not ok:
                bad.append(f"[{sc.name}] {detail}")
    return bad, checked


COUNT_JS = r"""
(() => {
  const out = [];
  const vis = el => { const st = getComputedStyle(el);
    return st.visibility !== 'hidden' && parseFloat(st.opacity) > 0.5; };
  document.querySelectorAll('.scene').forEach(scene => {
    if (scene.style.display === 'none') return;
    scene.querySelectorAll('.counter[data-counts]').forEach(c => {
      if (!vis(c)) return;
      const want = parseInt(c.textContent, 10);
      const got = [...scene.querySelectorAll(c.dataset.counts)].filter(vis).length;
      if (want !== got)
        out.push({scene: scene.dataset.name, sel: c.dataset.counts,
                  says: want, shows: got});
    });
    scene.querySelectorAll('.counter[data-sum-of]').forEach(c => {
      if (!vis(c)) return;
      const want = parseFloat(c.textContent);
      let got = 0;
      scene.querySelectorAll(c.dataset.sumOf).forEach(o => {
        if (vis(o)) got += parseFloat(o.dataset.val || 0); });
      if (Math.abs(want - got) > 0.011)
        out.push({scene: scene.dataset.name, sel: c.dataset.sumOf + ' (sum)',
                  says: want, shows: got});
    });
  });
  return out;
})()
"""


def check_countable(stage, video, samples=9):
    """The format's one hard promise: the number on screen equals the number of
    things on screen. Checked against the live DOM, not by eye."""
    from playwright.sync_api import sync_playwright
    import render

    times = []
    for a, b, sc in video.bounds():
        if not sc.counts:
            continue
        times += [a + (b - a) * (k + 1) / (samples + 1) for k in range(samples)]

    bad, seen = [], set()
    if not times:
        return bad
    with sync_playwright() as pw:
        br, pg = render._page(pw, pathlib.Path(stage).resolve().as_uri())
        for t in times:
            pg.evaluate(f"seek({t})")
            for r in pg.evaluate(COUNT_JS):
                key = (r["scene"], r["sel"], r["says"], r["shows"])
                if key in seen:
                    continue
                seen.add(key)
                bad.append(f'[{r["scene"]}] counter says {r["says"]} '
                           f'but {r["shows"]} {r["sel"]} are on screen')
        br.close()
    return bad


# ───────────────────────────────────────────────────── count gate ──
def check_counts(video):
    """A scene that declares n must render n things and count them."""
    bad = []
    for _, _, sc in video.bounds():
        for n in sc.counts:
            if n <= 1:
                continue
            if f'data-to="{n}"' not in sc.html:
                bad.append(f"[{sc.name}] shows {n} but no counter ticks to {n}")
    return bad


# ──────────────────────────────────────────────────── layout gate ──
PROBE_JS = r"""
(() => {
  const PIP = %s, MINF = %d, W = %d, H = %d;
  const out = [];
  document.querySelectorAll('.scene').forEach(scene => {
    if (scene.style.display === 'none') return;
    const name = scene.dataset.name;
    scene.querySelectorAll('*').forEach(el => {
      if (el.classList.contains('pipguide')) return;
      // Report whole drawings, not the rects and paths inside them: a figure
      // that strays under the PIP is one finding, not thirty.
      const svg = el.closest('svg');
      if (svg && svg !== el) {
        // Inside a drawing, only <text> is worth checking, and it is checked
        // against the drawing's own scale.
        if (el.tagName.toLowerCase() !== 'text') return;
        const r2 = el.getBoundingClientRect();
        if (r2.height > 1 && r2.height < 26)
          out.push({scene: name, kind: 'tiny-type', el: 'svg text',
                    size: Math.round(r2.height),
                    text: (el.textContent || '').trim().slice(0, 30)});
        return;
      }
      const st = getComputedStyle(el);
      if (st.visibility === 'hidden' || parseFloat(st.opacity) < 0.06) return;
      const r = el.getBoundingClientRect();
      if (r.width < 2 || r.height < 2) return;
      const cls = (el.getAttribute('class') || '').split(' ')[0];
      const tag = el.tagName.toLowerCase() + (cls ? '.' + cls : '');
      // Only leaf-ish elements: a wrapper overflowing is its child's fault.
      // An <svg> is one drawing, so it counts as a leaf even though it has
      // children -- otherwise a figure straying under the PIP is never reported.
      const hasBoxKid = el.tagName.toLowerCase() !== 'svg' &&
        [...el.children].some(c => c.getBoundingClientRect().width > 2);
      if (r.x < -1 || r.y < -1 || r.right > W + 1 || r.bottom > H + 1)
        out.push({scene: name, kind: 'overflow', el: tag,
                  box: [Math.round(r.x), Math.round(r.y), Math.round(r.right), Math.round(r.bottom)]});
      const nx = Math.max(r.x, Math.min(PIP[0], r.right));
      const ny = Math.max(r.y, Math.min(PIP[1], r.bottom));
      const hitsPip = Math.hypot(nx - PIP[0], ny - PIP[1]) < PIP[2];
      if (!hasBoxKid && hitsPip)
        out.push({scene: name, kind: 'under-pip', el: tag,
                  box: [Math.round(r.x), Math.round(r.y), Math.round(r.right), Math.round(r.bottom)]});
      const txt = (el.textContent || '').trim();
      if (txt && !hasBoxKid && el.tagName.toLowerCase() !== 'svg' &&
          parseFloat(st.fontSize) < MINF)
        out.push({scene: name, kind: 'tiny-type', el: tag,
                  size: Math.round(parseFloat(st.fontSize)), text: txt.slice(0, 30)});
    });
  });
  return out;
})()
""" % (list(PIP), MIN_FONT, FRAME_W, FRAME_H)


def check_layout(stage, video, per_scene=3):
    """Probe each scene at a few moments, once everything has settled."""
    from playwright.sync_api import sync_playwright
    import render

    times = []
    for a, b, sc in video.bounds():
        for k in range(per_scene):
            times.append(a + sc.dur * (0.45 + 0.5 * k / max(per_scene - 1, 1)))
    times = [min(t, video.duration - 0.01) for t in times]

    seen, rows = set(), []
    with sync_playwright() as pw:
        b_, pg = render._page(pw, pathlib.Path(stage).resolve().as_uri())
        for t in times:
            pg.evaluate(f"seek({t})")
            for r in pg.evaluate(PROBE_JS):
                key = (r["scene"], r["kind"], r["el"], str(r.get("box") or r.get("size")))
                if key in seen:
                    continue
                seen.add(key)
                rows.append(r)
        b_.close()
    return rows


# ───────────────────────────────────────────────────────── report ──
def run(video, stage, layout=True):
    print(f"lint {video.slug} — {video.duration:.1f}s, {len(video.scenes)} scenes")
    fails = 0

    bad, n = check_arithmetic(video)
    print(f"  arithmetic: {n} expression(s) recomputed", end="")
    print(" — OK" if not bad else "")
    for b in bad:
        print(f"    FAIL {b}")
    fails += len(bad)

    bad = check_counts(video)
    if layout:
        bad += check_countable(stage, video)
    print(f"  counts: {sum(len(s.counts) for _,_,s in video.bounds())} quantity claim(s)", end="")
    print(" — OK" if not bad else "")
    for b in bad[:12]:
        print(f"    FAIL {b}")
    if len(bad) > 12:
        print(f"    ... and {len(bad) - 12} more")
    fails += len(bad)

    if video.duration > MAX_DUR:
        print(f"    FAIL duration {video.duration:.0f}s > {MAX_DUR}s")
        fails += 1

    if layout:
        rows = check_layout(stage, video)
        by = {}
        for r in rows:
            by.setdefault(r["kind"], []).append(r)
        print(f"  layout: {len(rows)} finding(s)" + (" — OK" if not rows else ""))
        for kind, rs in sorted(by.items()):
            groups = {}
            for r in rs:
                groups.setdefault((r["scene"], r["el"]), []).append(r)
            for (scene, el), g in groups.items():
                if "box" in g[0]:
                    xs = [b for r in g for b in (r["box"][0], r["box"][2])]
                    ys = [b for r in g for b in (r["box"][1], r["box"][3])]
                    extra = f"x {min(xs)}..{max(xs)}  y {min(ys)}..{max(ys)}"
                else:
                    extra = f'{g[0]["size"]}px "{g[0]["text"]}"'
                n = f" x{len(g)}" if len(g) > 1 else ""
                print(f'    {kind:<10} [{scene}] {el}{n}  {extra}')
        fails += len(rows)

    print(f"  => {'PASS' if fails == 0 else str(fails) + ' problem(s)'}")
    return fails
