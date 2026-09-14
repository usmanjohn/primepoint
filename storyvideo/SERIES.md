# SERIES.md — what the videos ARE, and how they are made

`README.md` is the renderer. `STYLE_GUIDE_KOREAN_VIDEO.md` is how to write a language
film. **This file is the layer above both: the series, the covers, the branding and the
posting policy** — the decisions that are not visible in any single spec and were
therefore the easiest to lose between sessions.

Written 2026-09-14, at the user's request, after a session where these rules were agreed
verbally and would have been forgotten.

---

## 1. The one idea

Eight subjects have to live on one Instagram account. **The viewer's intersection is not
the topic — it is the format and the cast.** So:

> **Brand the format. LABEL the subject. Never brand the subject.**

Three layers, and only the middle one moves:

| layer | what | changes? |
|---|---|---|
| paper, Playfair/Mulish, counter, `beat`, `ask`, `outro`, the cast | the channel | **never** |
| `--accent` + the corner chip | the subject | per video |
| the opening ritual and the cover layout | the series | per series |

⛔ **Never give a subject its own BACKGROUND.** The warm paper (`--paper #faf7f2`) is the
one thing no other educational account has, and it is the only reason a grid of eight
subjects still reads as one channel. Change the accent; keep the paper.

## 2. `Video(subject=...)` — the subject registry

One word in the spec sets the accent colour (`stage.css`, **SUBJECT ACCENT**) and the
bottom-left chip. `spec.SUBJECTS` holds the glyph and the Uzbek name.

| subject | accent | glyph |
|---|---|---|
| `math` | gold `#c9923a` | `÷` |
| `english` | teal `#2e7d7a` | `ə` |
| `korean` | blue `#3b6ea5` | `한` |
| `japanese` | indigo `#3d4a7d` | `日` |
| `russian` | violet `#7a5aa0` | `Ж` |
| `sat` | graphite `#24405e` | `SAT` |
| `logic` | olive `#5f7d3a` | `⚖` |
| `story` | wood `#c08a52` | `✦` |

The glyph is taken from the subject's **own material**, never a flag emoji. Hues are
separated so the bands are distinguishable at 120px, which is the profile-grid size.

`subject=""` gives neither accent nor chip, so every film written before 2026-09-11
renders exactly as it did. **Those still need re-covering — see §8.**

The chip is emitted **once, outside every scene**, and is `position: fixed`. A chip inside
a scene rides the camera and at the 1.075 end of a `push` is pushed clean off the bottom
of the frame (27 lint findings on ko04, which is how this was found). It is channel
furniture, not part of the drawing.

## 3. The series

Not one series per subject — **one series per SHAPE**, cutting across subjects. A viewer
learns the ritual and recognises it in 0.3s.

| series | beats | subjects | shipped |
|---|---|---|---|
| **«Tutilgan xato»** | `says → consequence → correct` | every subject | ko04-ko09 |
| **«Nega shunday?»** | `fact/era/portrait` + mechanism | the `olami` shelves | mo01, mo03, mo04, mo10, mo27 |
| **«Sanab koʻring»** | `count_in → beat → check` | maths, logic | the pm films |
| **«Bitta soʻz»** | `word_family` | ko, pe, pj, pr, SAT roots | ko01 |

«Tutilgan xato» should be the majority: a wrong answer on screen is the least scrollable
thing in short video, and it is subject-agnostic.

**Rotate the SHAPE inside a band of three.** ko07-09 deliberately run
Uzbek-collision → social-cost → language-internal so three films do not feel like one
film three times:

- **Uzbek collision** — one Uzbek word, two target-language forms (ko05 `-da`, ko07 «xayr»).
  The mistake is the pupil's own language working correctly, and saying so is the film.
- **Social cost** — nothing ungrammatical happens; the damage is what the listener hears
  (ko04 speech level, ko08 안/못).
- **Language-internal** — a mechanism nothing in Uzbek prepares them for (ko06 two number
  systems, ko09 the ㅂ-irregular).

### Which shelf feeds a maths film

⚠️ **The format that actually got traction on Instagram was the ORIGIN STORY** (ko02,
Sejong — from **Koreya olami**, bound to no lesson), not a lesson film. Its maths twin is
**Matematika olami** (`toc_matematika_olami.txt`), and 10 of its 15 stories are still
unfilmed. Prefer that shelf for new maths videos. Strong unused candidates: Fales +
piramida (6), asalarilar va olti burchak (15), Fibonachchi (17), lyuk qopqogʻi (23),
shtrix-kod (25), A4 qogʻoz (31).

## 4. The cover contract — `cover()`

**Frame 0 IS the thumbnail.** Reels, Shorts and Telegram all reach for it. `hook` cannot
do this job: it pops every line in from `scale(0.3)` at `t=0.0`, so its frame 0 is bare
paper — which is true of all 22 films written before the beat existed.

Everything in `cover()` is drawn at `t=0` with `anim="none"`. Three rules, and they are
the format, not decoration:

1. **It shows the WRONG thing, struck through, or the STRANGE thing — never the topic's
   name.** «Koreys tili darsi» is unclickable; 고마워 with a red bar through it cannot be
   scrolled past. A discovery film uses `strike=False` and shows the strange thing
   (mo10 shows the answer `5 050`, because the secret is the method).
2. **The promise is at most four words**, in the subject accent, on a slab.
3. **Both sit inside y 420…1500** — the centre square a profile grid crops to. The chip
   deliberately sits outside it.

⚠️ **The red bar must cross ONLY the wrong part.** ko06's promise is «Yarmi xato» and the
first version struck the whole phrase — the picture contradicted its own words. Pass
`strike=False` and wrap only the wrong fragment in `<span class="strike">` (ko05, ko06,
ko09 all do this).

The cover carries the film's **first narration line**, so nothing is spent on a silent
title card.

**The fourth lint gate** checks `t=0`: ≥3 drawn elements and a ≥120px element. A film that
does not open on a `cover` is **warned, not failed** — those 22 are a to-do list, not a
blocker.

## 5. Echo policy (language films)

Two `echo` beats per film, placed apart so two silent scenes never sit together.

- ⚠️ **≤ ~6 syllables.** `koaudio.track` puts the second utterance **2.1s** after the
  first, so a longer clip overlaps itself. Measure with `koaudio._load(txt)` before
  committing — every clip shipped so far is 0.70–1.48s.
- ⛔ **Never echo a non-word.** ko09 says the wrong form 춥어요 in the *narration* (so the
  pupil hears the mistake) but echoes only real words. A Korean voice reading an invented
  conjugation is a defect, not a lesson.
- An early echo of a form that is *wrong for the situation* is fine, but change the head:
  ko04 and ko07 use `head="Serialda shunday eshitiladi"` — recognition, not production.
- Adding an echo is **free for an already-recorded film**: `script_one` skips scenes with
  no `say`, so a silent scene leaves the pasted text byte-identical. Verified by diffing
  ko04/ko05 after adding one. Only the `None` in `narrate(...)` has to be added.

## 6. ⛔ Reaction images, memes and GIFs — the decision

The user asked (2026-09-14) about dropping viral reaction GIFs into the films for
attention. **Answer: no to imported viral clips, yes to reactions we already own.**

**Why not:**
- `people.py` already has his cast with moods, and `consequence()` **is** the reaction
  beat. His own character reacting, on his paper, in his colours, beats a stranger's meme
  face — which is someone else's brand dropped into the middle of his.
- The paper look is the asset that makes the grid cohere. A viral GIF imports a different
  visual language and the grid stops reading as one channel.
- Rights: reusing viral clips in monetisable content is a real risk on Reels (muted audio,
  restricted reach) and he would never know which post it hit.

**And a hard technical reason for GIFs specifically:** `seek(t)` is a pure function of
time, which is what lets three workers render different slices in parallel. **A GIF
animates on its own clock** — at the same `t` three workers capture three different GIF
frames and the output flickers at every worker boundary. A GIF would have to be
decomposed into frames with ffmpeg and indexed by `t` (~30 lines). Static images have no
such problem and obey `data-at` like anything else.

**If he supplies images anyway:** static PNG, transparent background, his own or licensed.
Place them at the turn, **inside an existing scene, never as a new scene** — that way
adding them later never changes the narration line count and never invalidates a
recording.

**What to build instead, for the same goal:** more moods on the cast (shock/anger/laugh in
`people.py`), a `reaction()` element that pops a big face at the turn, a stinger cue at
the mistake moment, and a faster camera on the turn.

## 7. Sound

**`--sfx-gain` default is 1.5** (raised from 1.0 on 2026-09-14 at his request — the cues
were too quiet under the voice on the finished Reels). Measured on ko04, not guessed:

| gain | sfx peak | mix peak | limiter | sfx/voice RMS |
|---|---|---|---|---|
| 1.0 | 0.390 | 0.982 | 0.988 | 0.41 |
| **1.5** | 0.584 | 1.042 | 0.931 | **0.62** |
| 2.2 | 0.857 | 1.157 | 0.838 | 0.91 |

The limiter's 7% comes off the **whole** mix, so nothing gets quieter relative to anything
else. Past ~1.8 the cues stop being punctuation and start competing with the narration.
The table is repeated in `sfx.py` so nobody re-guesses it.

## 8. Inventory

| register | slugs | state |
|---|---|---|
| Prime Math lessons | pm04 · pm07 · pm08 · pm12 · pm25 · pm55 · pm67 · pm79 · pm84 · pm90 · pm91 · pm92 · pm93 · pm94 · pm97 · pm99 | voiced · **uploaded** |
| Matematika olami | mo01 · mo03 · mo04 | voiced · **uploaded** |
| Matematika olami (new) | mo10 (Gauss) · mo27 (diagramma) | **scripts out, awaiting voice** |
| Koreya olami | ko01 · ko02 · ko03 | voiced · **uploaded** (ko02 = Sejong, the one that got traction) |
| Tutilgan xato (Korean) | ko04 · ko05 · ko06 | voiced · ko05 + ko06 **not yet uploaded** |
| Tutilgan xato (Korean) | ko07 · ko08 · ko09 | **scripts out, awaiting voice** |

**No film from before 2026-09-11 has a cover** (blank frame 0). Re-covering them is
mechanical — add `cover()` and `subject=`, no re-recording, because the cover carries the
existing first narration line.

## 9. Posting policy (Instagram)

Decided 2026-09-14 after ko02 outperformed the maths films. He asked whether to switch to
Korean-only; the answer was **no — concentrate, do not switch**:

- **Korean-led, roughly 4 of 5 posts.** One data point cannot justify writing off the
  whole maths shelf, and a monoculture account has a ceiling. He is building a school.
- **Post in three-post bands of one subject**, so the grid reads as clean colour bands
  instead of confetti.
- ⚠️ **The confound worth remembering:** ko02 is an *origin story*, not a Korean lesson.
  "Korean won" and "origin stories won" are indistinguishable from one result — which is
  why mo10 and mo27 come from the same shelf shape. That IS the experiment.
- **Reels distribution is per video**, to that video's own interest graph. A maths post
  does not reduce the reach of the next Korean post. What mixing costs is **follower
  conversion**, not reach — so the lever is the bio, not the content mix. If the profile
  promises "koreys tili", a maths post is a broken promise; if it promises the format, it
  is on-promise.
- **Do not split off a second account yet** — he cannot feed two, and a starved account is
  worse than a mixed one. Revisit when Korean alone sustains three posts a week.
- **Measure follows-per-view and the reach of the NEXT Korean post**, not likes.
- Grid crop: the profile centre-crops the 9:16 cover, so essentials live in y 420…1500.
- Caption first line is the label: `한 Koreys tili · 07 — Tutilgan xato`.
- Highlights are the playlists Instagram refuses to give you: one per subject, in the
  accent colours.

## 10. Per-film checklist

- [ ] `Video(subject=...)` set, and the film opens on `cover()`
- [ ] cover shows the wrong/strange thing, promise ≤4 words, strike only on the wrong part
- [ ] `python3 korean.py` → 26/26 (language films)
- [ ] every target-language word re-derived and **read by eye** (see §5 and the palatalisation
      note in `STYLE_GUIDE_KOREAN_VIDEO.md`)
- [ ] `cli.py lint` → PASS (four gates)
- [ ] `cli.py sheet --per-scene` → **every frame looked at**, not one
- [ ] `cli.py script --one --ssml` → no digit, no Hangul, no hanja/jamo, <2000 chars
- [ ] `cli.py kowords` → clips fetched, each ≤2.1s
- [ ] `cli.py check --audio` → "split ishonchli"
- [ ] `cli.py voice` → then pull frames from the finished mp4 and look at them
- [ ] ⚠️ before touching the SHARED kit (`stage.css`, `primitives.py`), **lint the whole
      catalogue** — `min-width:0` fixed ko08 and broke mo01
