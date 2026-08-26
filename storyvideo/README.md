# storyvideo

Turns a Prime Math reading into a silent 1080x1920 animatic for Shorts / Reels /
Telegram. No audio track: the video is played back full-screen on the tablet and
narrated live over the top, with the front-camera PIP circle in the top-right.

    python -m storyvideo lint    pm04     three gates, no rendering
    python -m storyvideo sheet   pm04     contact sheet, one frame per scene
    python -m storyvideo preview pm04     scrubbable stage in Chrome
    python -m storyvideo render  pm04     mp4 + cue sheet + verification sheet
    python -m storyvideo draft   67       spec skeleton from the Corner story

Run from this directory. Outputs land in `out/` (gitignored).

## How it works

A story is a **spec** (`stories/pm04.py`): a list of Scenes built from the beat
vocabulary in `scenes.py`. It is never new drawing code -- if a story needs a
visual that does not exist yet, it goes into `primitives.py` and every later
story gets it too.

`build.py` writes all the scenes into one stage HTML. Nothing in that page
animates on its own: **`anim.js` `seek(t)` is a pure function of time** that
walks the DOM and writes inline styles. That is the whole design:

* frames are reproducible from `t` alone, so `render.py` can point several
  Chromes at different slices of the timeline with no coordination;
* the same function drives the scrub slider in `preview`;
* there is no global-animation clock to get out of step with (the previous
  renderer drove CSS animations off `document.getAnimations()`, and any
  scene-relative offset silently rendered blank).

## The four story shapes

A spec is built from the beat vocabulary in `scenes.py`, and which beats it uses
depends on the shape of the source reading. The shelf's policy lives in
`corner/management/commands/toc_prime_math_readings.txt`; the video side of it:

| Shape | Beats | Example |
|---|---|---|
| Tutilgan xato | `claim` → `fill/walk` → `consequence` → `correct` | pm04, pm67, pm25 |
| Teskari natija | two `versus`, or two halves with a `beat` between | pm92, pm08 |
| Tanlov | `versus` with a verdict | pm92 |
| Kashfiyot | `board`/`count_in` → `climb` → `check` | pm12 |

Never three of the same in a row — the reason is in the toc header.

Every video ends `rule` → `ask` → `outro`. The `ask` scene is the reading's own
`Story.open_question`: a transfer question with no answer key, and the last thing
on screen because nothing that follows it could be a reply.

## The rules that matter

**Every quantity is countable.** A counter does not animate alongside the things
it counts -- it *counts* them, by reading back the opacity `seek()` just wrote.
The number on screen therefore cannot disagree with the picture. `lint` verifies
this against the live DOM at nine moments per scene.

**Nothing under the PIP.** The rect x=680..1080, y=40..440 is his face circle.
Top-aligned scenes start below it and park their counters in the free top-left
corner. `lint` fails on any overlap, and on anything clipped by the frame or set
below 34px.

**Every sum is computed twice.** `lint` re-evaluates every expression a scene puts
on screen, including the `a ÷ b = q, qoldiq r` form and Uzbek thousands spacing
(`52 × 25 000 = 1 300 000`). A wrong answer key is the worst thing this pipeline
could ship, so an unparseable expression is reported as unchecked rather than
assumed correct.

**Display type sizes itself.** `.hero`/`.ttl`/`.ask` and every `expr` shrink to fit
(`_FIT` and `expr_size` in primitives.py); headings wrap to 2-3 lines rather than
shrinking to nothing. Content width is 880px, not the 940px the padding allows,
because a `pop` entrance overshoots past scale 1 and the camera push multiplies it.

**The cue sheet is not a script.** `out/<slug>_sahna.html` gives the clock, a
thumbnail and the point to hit -- never a sentence to read aloud.

## Notes

* ~9 fps per Chrome at 1080x1920 on this machine; `--workers 3` renders 90s in
  about five minutes. Do not run other renders or probes at the same time --
  contention drops it to 2 fps and looks like a hang.
* This Mac has ffmpeg but **no ffprobe**; `render.duration_of()` parses the last
  `time=` out of `ffmpeg -i FILE -f null -`.
* Fonts are vendored in `assets/fonts/` so a render never depends on the network.
* `reference/` holds the hand-written prototype this grew out of, and the sample
  video that set the visual direction.
* The PIP circle is **one knob**: `--pip-x/y/w/h` in stage.css and `PIP` in lint.py
  (cx 880, cy 240, r 200). It is currently a 400px circle, which is a conservative
  guess — if his real face circle is smaller, shrink both and every scene gets
  room back. `--safe-top` exists only because of it.
* Django never imports this package and it is not in `INSTALLED_APPS`, so it adds
  nothing to the deployed site. `out/` is gitignored.
