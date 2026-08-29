# storyvideo

Turns a Prime Math reading into a 1080x1920 animatic for Shorts / Reels / Telegram,
with TTS narration and a synthesised sound layer under it.

    python3 cli.py lint    pm04     three gates, no rendering
    python3 cli.py sheet   pm04     contact sheet, one frame per scene
    python3 cli.py preview pm04     scrubbable stage in Chrome
    python3 cli.py render  pm04     silent mp4 + cue sheet
    python3 cli.py script  pm04 --one --ssml    the TTS text to paste
    python3 cli.py voice   pm04 --audio tts_audios/pm_4.mp3 \
                                --script tts_scripts/pm04_tts_recorded.txt
    python3 cli.py draft   67       spec skeleton from the Corner story

Run from **this** directory with `python3 cli.py` — `python -m storyvideo` from the
repo root does not work (`__main__.py` does a bare `from cli import main`).

## Where things live

| papka | nima | git |
|---|---|---|
| `stories/` | hikoya spetsifikatsiyalari + ovoz matni (`narrate`) | kuzatiladi |
| `tts_scripts/` | saytga qoʻyiladigan matn, va yozib olingan nusxasi | kuzatiladi |
| `tts_audios/` | yozib olingan ovozlar (`pm_4.mp3`) | ignore |
| `videos/` | tayyor `<slug>_voiced.mp4` | ignore |
| `out/` | ishchi fayllar — istalgan vaqtda oʻchirsa boʻladi | ignore |

Ovoz sozlamalari: **Speed +26%, Pitch +10%**, matn 2000 belgidan oshmasin.

## The pipeline, end to end

1. `script <slug> --one --ssml` → `tts_scripts/<slug>_tts_one.txt`
2. paste it into the TTS site, save the mp3 as `tts_audios/pm_<n>.mp3`
3. `voice <slug> --audio … --script …` — splits the recording on its long
   breaks, **cuts the picture to the voice**, mixes the cue layer under it and
   muxes → `videos/<slug>_voiced.mp4`. `--sfx-gain` tunes the sound level.

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

## Koreys videolar (`ko*`) — the third register

> **Toʻliq qoʻllanma: [`STYLE_GUIDE_KOREAN_VIDEO.md`](STYLE_GUIDE_KOREAN_VIDEO.md)** —
> sikl, beatlar, ovoz matnining uchta qoidasi, `check` ning ikki xil nosozligi,
> chizmadagi tuzoqlar va chiqarishdan oldingi roʻyxat. Yangi til videosi
> yozishdan oldin oʻshani oʻqing.

Added 2026-08-30. The bet was that the maths format never depended on maths: it
depended on the picture making an argument the viewer can check. A language has
its own countable structure, so the same machinery works with no new format —
`ko01` is a `count_in` scene where the countable things are words.

| file | what |
|---|---|
| `korean.py` | 한글 → Uzbek letters. The sibling of `speech.py` |
| `wordkit.py` | the language kit — `pron`, `family`, `jamo`, `mouth`, `cta` |
| `koaudio.py` | native Korean word clips (edge-tts), cached in `assets/ko_words/` |

New beats in `scenes.py`: `word` · `echo` · `word_family` · `spell` · `shape` ·
`practice`. The `pe-*`-style visual kit is the **KOREYS** section at the bottom
of `stage.css`.

### The two rules that are new

**Never send the engine Hangul.** It is the same rule as "never send it a
digit", and it works the same way: a spec writes the real word once, `speech.py`
calls `korean.romanise_all` on the way to the engine, and the picture keeps the
한글. `cli.py script` fails if any survives. **Hanja and lone jamo (ㄱ, 出) are
REFUSED, not converted** — a hanja has several readings and a bare consonant has
no vowel, so there is nothing to compute. On screen they are the point; in
narration, say the sound in Uzbek.

The transliteration is checked against 15 cases in `korean.py` — run
`python3 korean.py`. 감사합니다 → `kamsahamnida` is the reference case: it pins
down both word-initial ㄱ = k and 비음화 (ㅂ before ㄴ becomes m).

**A Korean word is spoken by a Korean voice, and only in a silent scene.** The
Uzbek narration fills nearly every second of a scene it owns, so a Korean word
mixed under it is mud, and there is no word-level alignment to find a hole with.
`scenes.echo` is a scene with `say=None`: `retime` gives it its settle time,
`mix` puts no narration in it, and `koaudio` lays the word there twice. Nothing
in `voice.split` had to change.

    python3 cli.py kowords ko01     fetch the clips (the only online step)
    python3 cli.py voice ko01 --audio … --script …   --ko-gain / --no-ko

### The source shelf

`corner` collection **"Koreya olami"** (Korean subject, order 5) — the twin of
Matematika olami: Uzbek prose about the language and the country, bound to no
lesson. Policy in `corner/management/commands/toc_koreya_olami.txt`. Its one
inversion: the prose is Uzbek and Korean is the *material*, each word a
`cn-word` span. ⛔ No audio on that shelf (the prose is Uzbek).

Pronunciations quoted in those texts are spelled the way `korean.py` spells
them, so the shelf, the video and the narration never disagree.
