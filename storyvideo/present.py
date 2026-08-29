# -*- coding: utf-8 -*-
"""Presenter build — one self-contained page that WAITS for him.

The sync problem was never his timing, it was the contract: scene lengths were
authored and a human was asked to match them. Here each beat plays its animation,
settles, and then holds until he taps. He talks for as long as he likes. The take
is in sync by construction and needs no processing afterwards.

Everything is inlined (fonts as data URIs, CSS, the seek runtime) so the page can
be published once and opened on the tablet with no server and no network.

    python -m storyvideo present pm04 pm08 pm12 pm25 pm67 pm92
"""

import base64
import html as _html
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent


def _fonts_inline():
    """fonts.css with every woff2 swapped for a data: URI."""
    d = HERE / "assets" / "fonts"
    css = (d / "fonts.css").read_text()

    def sub(m):
        f = d / m.group(1)
        b64 = base64.b64encode(f.read_bytes()).decode()
        return f"url(data:font/woff2;base64,{b64})"

    return re.sub(r"url\(\./([^)]+\.woff2)\)", sub, css)


def _stage_css():
    css = (HERE / "stage.css").read_text()
    return css.replace('@import url("./assets/fonts/fonts.css");', _fonts_inline())


PRESENTER_CSS = """
/* ---- presenter chrome -------------------------------------------------
   The stage keeps its true 1080x1920 and is scaled to fit the screen. On a
   10:16 tablet that leaves paper-coloured bars at the sides, which vanish when
   he centre-crops the recording back to 9:16. */
html, body { width: 100%; height: 100%; overflow: hidden; background: var(--paper); }
body::after { content: none; }            /* grain belongs to the stage, not the page */

#wrap { position: fixed; inset: 0; background: var(--paper); }
#stage { position: absolute; left: 50%; top: 50%; width: 1080px; height: 1920px;
         transform-origin: 0 0; background: var(--paper); overflow: hidden; }
#stage::after { content: ''; position: absolute; inset: 0; pointer-events: none;
  z-index: 99; opacity: .5;
  background-image: radial-gradient(circle at 1px 1px, rgba(26,20,16,.05) 1px, transparent 0);
  background-size: 4px 4px; }

/* ---- index ---- */
#menu { position: fixed; inset: 0; overflow-y: auto; background: var(--paper);
        display: flex; flex-direction: column; align-items: center;
        padding: clamp(28px, 6vh, 72px) 20px 60px; z-index: 500; }
.mhead { width: min(560px, 100%); margin-bottom: clamp(20px, 4vh, 40px); }
.mhead h1 { font-family: var(--ff-head); font-weight: 900;
            font-size: clamp(30px, 6vw, 46px); color: var(--ink); line-height: 1.05;
            letter-spacing: -.015em; }
.mhead p { font-family: var(--ff-body); font-weight: 600;
           font-size: clamp(14px, 3.2vw, 17px); color: var(--ink-soft);
           margin-top: 10px; line-height: 1.5; max-width: 52ch; }
.mlist { width: min(560px, 100%); display: flex; flex-direction: column; gap: 10px; }
.row { display: flex; align-items: center; gap: 16px; width: 100%; text-align: left;
       background: #fff; border: 1px solid var(--paper-3); border-radius: 14px;
       padding: 16px 18px; cursor: pointer; font: inherit; color: inherit;
       transition: border-color .15s, transform .15s; }
.row:hover, .row:focus-visible { border-color: var(--gold); transform: translateY(-1px); }
.row:focus-visible { outline: 3px solid var(--gold); outline-offset: 2px; }
.row__n { font-family: var(--ff-head); font-weight: 900; font-size: 21px;
          color: var(--gold); min-width: 62px; font-variant-numeric: tabular-nums; }
.row__t { flex: 1; min-width: 0; }
.row__t b { display: block; font-family: var(--ff-body); font-weight: 800;
            font-size: 16px; color: var(--ink); line-height: 1.3; }
.row__t span { display: block; font-family: var(--ff-body); font-weight: 600;
               font-size: 13px; color: var(--ink-faint); margin-top: 3px;
               font-variant-numeric: tabular-nums; }
.row__go { font-family: var(--ff-body); font-weight: 800; font-size: 12px;
           letter-spacing: .1em; text-transform: uppercase; color: var(--gold); }
.mnote { width: min(560px, 100%); margin-top: 26px; padding: 16px 18px;
         background: var(--paper-2); border-radius: 14px;
         font-family: var(--ff-body); font-size: 14px; line-height: 1.6;
         color: var(--ink-soft); }
.mnote b { color: var(--ink); }
.mnote kbd { font-family: var(--ff-body); font-weight: 800; font-size: 12px;
             background: #fff; border: 1px solid var(--paper-3); border-radius: 6px;
             padding: 2px 7px; }

/* ---- rehearsal HUD (off while recording; press H) ---- */
#hud { position: fixed; left: 0; right: 0; bottom: 0; z-index: 600; display: none;
       background: rgba(26,20,16,.92); color: var(--paper); padding: 14px 20px;
       font-family: var(--ff-body); font-size: 16px; line-height: 1.45; }
body.hud #hud { display: block; }
#hud b { color: var(--gold); font-weight: 800; }
#hud i { font-style: normal; opacity: .65; }
@media (prefers-reduced-motion: reduce) { .row { transition: none; } }
"""

PRESENTER_JS = r"""
const $ = s => document.querySelector(s);
const stage = $('#stage'), wrap = $('#wrap'), menu = $('#menu'), hud = $('#hud');
let cur = null, idx = -1, t0 = 0, holding = false, raf = 0, lock = null;

function fit() {
  const k = Math.min(wrap.clientWidth / 1080, wrap.clientHeight / 1920);
  stage.style.transform = `translate(${-540 * k}px, ${-960 * k}px) scale(${k})`;
}
addEventListener('resize', fit);

async function keepAwake() {
  try { lock = await navigator.wakeLock.request('screen'); } catch (e) {}
}

function open(slug) {
  cur = VIDEOS[slug];
  stage.innerHTML = cur.html;
  document.body.dataset.resolved = '';
  resolve();
  // Where each beat has finished moving -- the point it should start waiting.
  // Scene durations were authored for narration, so their tail is dead air here.
  const scenes = [...stage.querySelectorAll('.scene')];
  cur.settle = cur.scenes.map((s, i) => {
    let m = s.start;
    scenes[i].querySelectorAll('[data-in]').forEach(e => {
      m = Math.max(m, parseFloat(e.dataset.in) + parseFloat(e.dataset.dur || 0.5));
    });
    return Math.min(s.end - 0.02, m + 0.35);
  });
  menu.style.display = 'none';
  fit(); keepAwake();
  if (wrap.requestFullscreen) wrap.requestFullscreen().catch(() => {});
  idx = -1; next();
}

function next() {
  idx++;
  if (idx >= cur.scenes.length) { idx = cur.scenes.length - 1; return; }
  t0 = performance.now(); holding = false; tick();
}

function back() { if (idx > 0) { idx--; t0 = performance.now(); holding = false; tick(); } }

function tick() {
  cancelAnimationFrame(raf);
  const s = cur.scenes[idx], settle = cur.settle[idx];
  const t = s.start + (performance.now() - t0) / 1000;
  let show = t;
  if (t >= settle) {
    // Hold -- but let the camera keep drifting so the frame is never dead.
    show = Math.min(s.end - 0.02, settle + (t - settle) * 0.12);
    holding = true;
  }
  seek(show);
  if (hud) hud.innerHTML = `<b>${idx + 1}/${cur.scenes.length}</b> ${s.name}` +
    (holding ? ' <i>— kutmoqda, bosing</i>' : '') + `<br>${s.note || ''}`;
  raf = requestAnimationFrame(tick);
}

function advance() {
  if (!cur) return;
  if (holding) next();
  // Not settled yet: skip straight to the end of this beat.
  else t0 = performance.now() - (cur.settle[idx] - cur.scenes[idx].start) * 1000;
}

function quit() {
  cancelAnimationFrame(raf); cur = null;
  if (document.fullscreenElement) document.exitFullscreen().catch(() => {});
  if (lock) { lock.release(); lock = null; }
  stage.innerHTML = ''; menu.style.display = '';
}

wrap.addEventListener('pointerdown', e => { if (cur) { e.preventDefault(); advance(); } });
addEventListener('keydown', e => {
  if (!cur) return;
  if ([' ', 'ArrowRight', 'ArrowDown', 'PageDown', 'Enter'].includes(e.key)) {
    e.preventDefault(); advance();
  } else if (['ArrowLeft', 'ArrowUp', 'PageUp'].includes(e.key)) {
    e.preventDefault(); back();
  } else if (e.key === 'Escape') quit();
  else if (e.key === 'h' || e.key === 'H') document.body.classList.toggle('hud');
});
document.querySelectorAll('.row').forEach(r =>
  r.addEventListener('click', () => open(r.dataset.slug)));
fit();
"""


def build(slugs, out=None):
    import build as B

    videos, rows = {}, []
    for slug in slugs:
        v = B.load_story(slug)
        parts = []
        for i, (a, b, sc) in enumerate(v.bounds()):
            cls = "scene" + (" scene--dark" if sc.dark else "") + (" scene--top" if sc.top else "")
            parts.append(
                f'<section class="{cls}" data-start="{a:.4f}" data-end="{b:.4f}" '
                f'data-cam="{sc.cam}" data-name="{_html.escape(sc.name)}">{sc.html}</section>')
        videos[slug] = {
            "title": v.title, "lesson": v.lesson, "duration": round(v.duration, 1),
            "html": "".join(parts),
            "scenes": [{"name": sc.name, "start": round(a, 4), "end": round(b, 4),
                        "note": sc.note} for a, b, sc in v.bounds()],
        }
        rows.append(
            f'<button class="row" data-slug="{slug}">'
            f'<span class="row__n">{_html.escape(v.lesson)}</span>'
            f'<span class="row__t"><b>{_html.escape(v.title)}</b>'
            f'<span>{len(v.scenes)} sahna · ~{v.duration:.0f} s video</span></span>'
            f'<span class="row__go">Boshlash</span></button>')

    page = f"""<meta charset="utf-8">
<title>Powerty Sahna</title>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<style>{_stage_css()}{PRESENTER_CSS}</style>

<div id="wrap"><div id="stage"></div></div>

<div id="menu">
  <div class="mhead">
    <h1>Sahna</h1>
    <p>Video sizni kutadi. Har sahna oʻz animatsiyasini oʻynaydi va toʻxtaydi —
       xohlagancha gapiring, keyin ekranni bosing. Shoshilish yoʻq.</p>
  </div>
  <div class="mlist">{"".join(rows)}</div>
  <div class="mnote">
    <b>Yozib olish:</b> videoni tanlang, ekranni toʻliq qiling, ekran yozuvini
    (PIP bilan) yoqing va gapiring. Keyingi sahnaga oʻtish uchun <b>istalgan
    joyni bosing</b>.<br><br>
    <kbd>bosish</kbd> keyingi · <kbd>←</kbd> orqaga · <kbd>H</kbd> matn (mashq uchun)
    · <kbd>Esc</kbd> roʻyxatga qaytish
  </div>
</div>

<div id="hud"></div>

<script>{(HERE / "anim.js").read_text()}</script>
<script>const VIDEOS = {json.dumps(videos, ensure_ascii=False)};</script>
<script>{PRESENTER_JS}</script>
"""
    out = pathlib.Path(out or HERE / "out" / "sahna.html")
    out.write_text(page, encoding="utf-8")
    return out
