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
| **«Bitta soʻz»** | `word_family` + `build` | ko, pe, pj, pr, SAT roots | ko01 · ko10 · ko20 · ko24 · ko28 |
| **«Bir maqol, ikki til»** | 속담 + its Uzbek twin | Korean (and any language with proverbs) | ko16-ko19 · ko23 · ko27 |

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

### «Bir maqol, ikki til» — the proverb series (2026-09-16)

The one thing an Uzbek-language Korean channel can say that an English-language
one cannot: **a Korean proverb and an Uzbek proverb are very often the same
proverb with a different animal in it.** 호랑이도 제 말 하면 온다 is «boʻrini
yoʻqlasang, qulogʻi koʻrinar», word for word, with a tiger where the wolf is.

So the beat that carries it is `order` — three cells wide, the Korean row, the
literal row, the Uzbek row — and the turn is the moment the Uzbek line lands
underneath and matches. Nobody is wrong in these films; the arc is

    vaziyat → gʻalati tasvir → tekislash → egizak → qoida

**Each one must also teach something about the LANGUAGE, not only the wisdom**,
or it is a caption with a voice over it. ko17 is the model: 말 is «soʻz» and
«ot» written identically, so the proverb looks like a sentence about horses
until you know the homograph. ko18's is arithmetic — 10 × 365 against
200 × 3 — which is 티끌 모아 태산 doing work instead of being admired.

⛔ **Never present the two animals as translations of each other.** They are
not; the proverbs are twins and the animals are not. What they share is the
job — the most feared animal in the listener's own hills — and saying exactly
that is the film.

### The TOPIK films (ko13-ko15, 2026-09-16)

Exam tips are «Tutilgan xato» like everything else, and the band rotates the
KIND of mistake so three exam films do not feel like one film three times:

- **ko13 — a register** (쓰기 54 written in 해요체). Lost with good Korean.
- **ko14 — a clock** (읽기 50 savol / 70 daqiqa). Lost with perfect Korean.
- **ko15 — a mechanical slip** (the answer sheet one row out). Lost with
  answers you actually had, and nothing to do with Korean at all.

⚠️ **Every number comes from the site's own TOPIK strategy lesson**
(`examprep`, TOPIK → strategy, order 1), never from memory: 300 ball, 100 per
boʻlim, 50 savol / 70 daqiqa, 2 ball a question, 120/150/190/230 for 3-6급,
and 쓰기 = 10 + 10 + 30 + 50. The arithmetic goes on screen so `lint`
recomputes it, and the film cannot then disagree with the lesson it points at.

⛔ **Never state what a test centre supplies, what a guess is worth, or how
many words a level needs.** Those change, differ by centre, or were never
published — and a film cannot be re-recorded when they do. Describe the
process and point at the lesson.

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

### 4.2 The 한국어 badge — the subject, INSIDE the crop  (2026-09-23)

His ask was «make the start great so I can upload without editing the cover», plus
«maybe add 한국 as well». Both point at the same hole, and it had been there since §2:

> the corner chip labels the subject — and §4 rule 3 deliberately puts it **outside**
> y 420…1500. So the one frame a profile grid actually shows is the one frame with no
> subject label on it.

A viewer scrolling Reels therefore has to read the Hangul in the picture to know what
language this is. On ko22's cover that is «노력 노력» with a red bar through it: perfect
as a hook, useless as a label, and unreadable to exactly the beginner the channel wants.

So `cover(ko="한국어")` puts a filled accent pill on the kicker row, in the subject's own
script. **This is §1's rule, not an exception to it** — *brand the format, LABEL the
subject, never brand the subject.* The paper does not move, the accent does not move, and
the pill never becomes the promise: the promise is still the strange or wrong thing.

- **Filled, not outlined.** It has to survive being shrunk to a 120px grid cell.
- **On the kicker row**, so the stack does not grow and the essentials stay inside
  y 420…1500. ko19 measured at y 610…1250 with it.
- **한국어, not 한국.** The channel teaches the language, not the country, and 한국어 is
  what a learner sees on their own textbook.
- Optional, and off by default (`ko=None`), so every earlier film renders unchanged.
- It is a **picture-only** change: the narration is untouched, so it can be added to a
  film that is already recorded. Verified on all ten of ko19-ko28 by recomputing their
  scripts and diffing against the ones already handed over — no change.

The obvious extension when another language register starts: `日本語`, `Русский`, and so
on, one pill per subject, same rule.

**The fourth lint gate** checks `t=0`: ≥3 drawn elements and a ≥120px element. A film that
does not open on a `cover` is **warned, not failed** — those 22 are a to-do list, not a
blocker.

### 4.1 The endcard says WHERE — «Havola profilda» + `powerty.uz`  (2026-09-16)

The cover is the way in; this is the way out, and until today the films had no way out at
all. **A Reel is not clickable.** Every film ended on a `practice` card naming a lesson
and an `outro` naming the channel, and a viewer who wanted the lesson had to want it
enough to go looking. So, at his request, the address is now part of the furniture:

| card | carries | why that half |
|---|---|---|
| `practice` | the gold pill **`powerty.uz`** (`.cta__l`) | the name to remember, beside the lesson it belongs to |
| `outro` | **«Havola profilda»** then **`powerty.uz`** | the instruction — where the clickable thing actually is |

Both are **defaults** (`practice(link="powerty.uz")`, `outro(link=…, site=…)`), so a film
written later carries them without anyone remembering to; pass `None` to drop either. The
split is deliberate — one card says the name, the other says where to click, and neither
nags twice.

The narration of the last spoken block ends «Havola profilda.» in ko13-ko18. That line is
the only place the voice sells anything, and it costs three words.

⚠️ This is the **channel** layer of §1, which the table says never moves. It moved once,
on purpose, for a reason no design change can substitute for: the account exists to send
people to the site. Do not take it as licence to move the rest.

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

### 6.1 ✅ That list was built, 2026-09-22

Three of the four, and they cost about eighty lines between them:

| piece | where | what it does |
|---|---|---|
| `shock` · `laugh` · `cross` | `people.MOUTHS` + `people.face()` | the three moods the cast could not do. `sad` is disappointment, not shock, and nothing in the set laughed |
| `people.head()` → `P.reaction()` | `consequence(..., close=True)` | the same drawing cropped to the head. A standing figure at 340px spends nine tenths of its height on a shirt, so the expression — the only thing that beat exists for — is about 40px of face |
| `shake` · `stamp` | `anim.js` ANIM | the mistake wobbles in, the correction lands from above and stops dead. `correct(..., shake=True)` |
| `build()` → `W.compound()` | `scenes.py` / `wordkit.py` | 학(ilm) + 생(hayot) → 학생, tiles landing one at a time. `spell` does this for jamo; this does it for roots, which is what the vocabulary films were asserting rather than showing |

All of them are OFF by default — a new mood is a new string, a new entrance is a new key,
`close=` and `shake=` default False — so every film written before that date renders
byte-for-byte as it did. That was **verified, not assumed**: all 41 stages were built from
`git archive HEAD` and from the working tree and diffed (identical), and the same was done
for all 41 narration scripts after the `korean.py` change (also identical). Repeat that
diff before the next shared-kit change; it takes thirty seconds and it is stronger evidence
than a lint pass, because it proves the INPUT to lint did not move.

⚠️ **Two things the first contact sheet caught, and neither is visible in code:**
- the long-hair fringe dips to y=44, so at 430px it sits **on the eyes** and the brows
  disappear into it — Nodira opa's angry close-up came out a dark blob with a mouth.
  `head()` lifts it to y=34, the close-up only; the standing figure is untouched, because
  at 170px that low fringe is what makes the hair read as long.
- a laugh drawn as an open OVAL reads as a **shout**. What reads as laughing is a flat top
  with a deep round bottom (`LAUGH_MOUTH`) plus arc eyes — and the arcs must sit at y 45-52,
  or the fringe paints over them too.
- `.jamo__out` is a fixed 214px **square**, because `spell` builds exactly one syllable.
  A compound never does: 학생 at 168px is 336px wide and spilled straight out of the gold
  tile. `compound()` always emits a pill sized to its own length.

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

### 7.1 ⚠️ The speech-rate check — why `check` alone was not enough

`check` used to score each block's **span**, and a span includes the pauses inside it. So
a block carrying several `|` breaks can lose a whole clause and still span about the right
length. That is exactly what ko07 did on its first take (2026-09-15):

- span ratio **0.71x** — inside nobody's alarm, and `check` printed *"split ishonchli"*;
- but its 181 characters were spoken in **5.89s of actual speech** = 30.7 ch/s, against
  **21.6 ch/s** everywhere else in the same recording — **1.42x**;
- ~54 characters were never spoken, and the block was the `versus` scene carrying the
  film's whole argument. Rendering it would have put the 계세요 half of the contrast on
  screen in silence.

**The conservation test still applies and still works:** a misplaced boundary MOVES time,
so a squashed segment sits next to a stretched one. Missing text is absorbed by nobody —
ko07's neighbours were 1.17x and 0.94x. But the span ratio was not extreme enough to
trigger on, which is why the speech rate is now measured too.

`cmd_check` subtracts each segment's internal silences and flags any block reading
**>1.25x the median rate**. Validated before trusting it: across 25 blocks of the three
known-good takes (ko04, ko05, ko06) the spread is **0.89–1.05x**, so the margin to 1.25 is
wide and it does not cry wolf. It also settled an old question — ko06's block 5, which
`check` once flagged as a suspicious boundary at 1.39x span, reads at **0.98x** speech
rate, so that really was a false positive from inner-break density.

**The fix for a flagged block is to RESTRUCTURE it, not to re-record it unchanged**
(ko02 dropped the same sentence on two separate takes): remove the inner `||`, shorten it,
and make sure every remaining `|` has real text on both sides. Move what you cut into the
picture — ko07's literal glosses went to the `versus` card, which already printed them.

⚠️ **`check` assumes the script and the audio correspond.** It compares a script file to an
mp3; if the take was made from an older version of the script the report is meaningless.
After editing a spec, regenerate the script AND re-record.

### 7.1.0 ⛔ `check` now detects a SCRIPT/AUDIO MISMATCH by itself

§7.2.1 said `check` assumes the script and the audio correspond. It no longer
just assumes it — it tests it, because the assumption failed in practice on
2026-09-15 and cost a round trip: mo25 and mo31 were **shortened after** being
recorded, and `check` dutifully reported three blocks as "OVOZDA MATN YOQ" when
the takes were simply the older, longer script.

**The reasoning is exact: the engine can only DROP text, never add it.** So a
block whose audio holds more speech than the script accounts for cannot be an
engine fault.

The discriminating statistic is the **spread** of the speech rates (max/min),
which is scale-free — an absolute floor fails because several mismatched blocks
drag the median down with them, and mo25's slowest landed at exactly 0.75x and
slipped past a 0.75 threshold. Measured over 13 takes:

| | rate spread |
|---|---|
| 11 matched takes | 1.07 – **1.37** |
| the two edited after recording | **2.29**, **2.92** |

Threshold **1.7**, and the whole report stops there rather than printing
conclusions drawn from mismatched inputs. Validated both ways: flags both
mismatches, zero false positives across all 11 matched takes.

### 7.1.4 ⚠️ A SLOW BLOCK IS NEVER DROPPED TEXT — read the FAST ones

2026-09-23, ko24. `check` fired **SCRIPT VA OVOZ MOS EMAS** (spread 1.81x) and
named blocks 2, 6 and 9 — all of them *sekin* — concluding «bu yozuv boshqa
(uzunroq) script versiyasidan olingan». That conclusion was wrong, and the
message points at the wrong blocks, so it is worth knowing why.

§7.1.0's reasoning is exact and still holds: **the engine can only DROP text,
never add it.** But run that the other way round and it says something the
report does not: *dropping makes a block **FAST**.* A slow block therefore
cannot be missing words — whatever it is, it is not the fault the gate exists
to catch. So when the gate fires, compute the per-block speech rates yourself
and read the top of the list, not the bottom:

    #   ch   span    sil  speech   ch/s    rel
    4   62   4.23   2.01    2.22   27.9   1.33   build(사회)
    5   78   5.95   3.47    2.49   31.4   1.50   build(회사)   <-- the real fault

31.4 ch/s against a 21 ch/s median is **ko07's signature almost exactly**
(30.7 vs 21.6, §7.1). Two blocks were losing text, and they were the two
`build` scenes — the 사회 ↔ 회사 swap, which is the entire film. The gate never
mentioned either of them.

The fix was §7.1.2's, and it worked: remove the inner break, cut what the
picture already prints («Oʻsha ikkita boʻgʻin» — both tiles are on screen).
Block 5 went 78 → 56 characters and came back at **1.05x**.

### 7.1.5 A short block carries fixed pause overhead — shortening makes it WORSE

The same re-take left one outlier: a 31-character block at **0.68x**, whose
whole content was `Ildiz — 회, maʼnosi: yigʻilish`. 1.58s of its 3.90s span was
silence, most of it around the emphasised `회`. It had already been shortened
from 39 characters, and shortening moved it the WRONG way — 0.82x → 0.68x.

That is the tell, and it is diagnostic: missing text makes a block faster, so a
block that gets *slower* per character as you remove characters is paying a
fixed cost (the pauses an `<emphasis>` and the punctuation buy) spread over
fewer characters. **Do not "fix" it by shortening again.** Either leave it — a
slow block only makes `retime` hold the scene a little longer, which is
harmless — or merge it into its neighbour.

⚠️ This does NOT license relaxing the gate's floor: §7.1.3 measured 265 blocks
of matched takes and found no bucket's minimum below 0.88x, so 0.68x is a real
outlier and deserved the look it got. The rule is to *diagnose* it, not to
ignore it. **Excluding that one block ko24's spread was 1.35x**, inside the
1.07–1.37 band of every matched take in the project — which is the number that
settled it.

### 7.1.2 ⭐ KEEP A NARRATION BLOCK UNDER 120 CHARACTERS

The single most useful measurement in this pipeline so far. The engine silently
drops part of a block, and **length is the predictor** — measured over 105 blocks
across 13 recordings (2026-09-15):

| block length (converted) | blocks | dropped |
|---|---|---|
| **0 – 120 chars** | 59 | **0** |
| 120 – 160 | 27 | 1 (3.7%) |
| 160 – 200 | 17 | 1 (5.9%) |
| 200 + | 2 | 1 (50%) |

By sentence count: **1–2 sentences never failed in 45 blocks**; 5 sentences failed
11% of the time. ko07 is the case study — 181 chars dropped a clause, 143 dropped
another, 110 finally worked. Three takes for one film.

`cli.py script` now **warns before recording**, per block, with the risk figure.
That is the whole value: every earlier version of this problem cost a re-record,
and the user had said plainly that the manual churn was defeating the purpose.

**The fix is always the same, and it improves the film: cut what the PICTURE
already says.** mo25's `solve` ladder prints every number the voice was reciting;
mo31's `versus` card prints both sets of dimensions; its 71% card already reads
«Bu — √2 ning teskarisi». Removing those took both scripts down by a quarter
(1472→1081, 1704→1140) and lost nothing.

⚠️ **When a film has to be re-recorded, shorten EVERY risky block in it, not just
the one that failed.** A 6% block left in place brings him back a third time.

**Confirmed prospectively.** mo25 was re-recorded from the shortened script (every block
under 130 characters) and came back with speech rates of **0.97–1.06x** — a spread of
1.09x, the tightest of any take in the project, against 1.07–1.37 for matched takes
generally. Nothing dropped. That is the rule predicting a result before the fact, not
explaining one after it.

### 7.1.1 When the boundaries are FORCED, a span flag cannot be a mis-cut

`check` reports two things and they can disagree. The **span** ratio catches a
misplaced boundary (time moves between neighbours); the **speech rate** catches
missing text. A span flag with a clean speech rate is usually neither — it is the
per-character model mispredicting how much internal silence a block holds.

There is an arithmetic test for it, and I worked it out by hand twice (ko06
block 5, ko11 blocks 3-4) before putting it in the tool: **if there are exactly
n-1 silences at scene-break length and every other pause is clearly shorter, the
solver had no choice**, so a misplaced boundary is impossible. `check` now says
so:

    SHUBHALI CHEGARA - 3-blok 0.68x, qoshnilari ['0.97', '1.39'].
    ⓘ  Lekin chegaralar MAJBURIY: 8 ta sahna-sukut, 8 ta chegara kerak,
       qolgan eng uzun pauza 2.10s.
    Demak chegara notoʻgʻri boʻlishi MUMKIN EMAS.

So the decision rule is: **speech rate clean + boundaries forced → render.**
A short one-sentence block (ko11's block 3, 49 characters) will read low on span
forever and there is nothing to fix.

### 7.1.3 ⚠️ Before believing a mismatch, check the take is the RIGHT FILM

2026-09-16: six films were recorded in one sitting and two of the mp3s reached
`tts_audios/` under the wrong numbers (there was a `ko_19.mp3` and no `ko_15`).
`check` reported **SCRIPT VA OVOZ MOS EMAS** on ko16 and ko17 — correctly, and
about something entirely different from what it says in the message.

I spent twenty minutes on the wrong hypothesis (that the gate mis-scores very
short blocks) and got as far as shortening two narrations that were never
broken. **The measurement that killed that theory is worth keeping**: across
265 blocks of the matched takes, block length does not predict speech rate —
0-40 chars average 1.06x, and no bucket's minimum falls below 0.88x. So the
gate's 0.75x floor is not a short-block artefact, and it must not be relaxed.

The 30-second version of what took twenty minutes is a **cross-table**: score
every film against every recording. The scene-break count (`blocks - 1`) alone
eliminates most pairs, and the rate spread settles the rest — a correct pairing
sits at 1.1x and a wrong one at 2.5x+, so the diagonal lights up and nothing
else does:

               ko_13   ko_14   ko_15   ko_16   ko_17   ko_18
       ko13    1.13x   2.57x       ·       ·       ·       ·
       ko14    1.65x   1.17x       ·       ·       ·       ·
       ko15        ·       ·   1.17x       ·       ·   4.14x
       ko16        ·       ·       ·   1.14x   2.74x       ·

**So when `check` says the script and audio disagree, ask "is this even the
right film?" before asking "what changed in the script?"** Especially in a
batch: the failure is one `cp` away and looks exactly like a content fault.

⚠️ A related thing that bit here: a recording's **pace varies between takes**
(ko13 ran ~26 ch/s, ko14 ~20 ch/s from the same settings). The gate normalises
per take so this never affects correctness, but two films in the same posted
band will feel different. Worth a listen before posting a band, not a re-record.

### 7.2 ⚙️ Foreign words and Roman numerals are the PIPELINE's job, not yours

⚠️ **2026-09-15, and this was a fair complaint: "it is becoming more manual stuff
when our purpose is automation."** He was hand-editing the same things in every
paste — `prime` → `praym`, `examprep` → `ekzamprep`, `XVIII` → `oʻn sakkiz`. That is
the same class of bug as sending the engine a digit, and `speech.py`'s own docstring
already states the principle: *the engine's mistakes are nearly all OUR mistakes.*

**`speech.SAY_AS`** now converts the known foreign words on the way to the engine, and
Roman numerals become Uzbek words — with the **ordinal** before `asr`/`yil`, because the
18th century is «oʻn sakkizinchi asr», not «oʻn sakkiz asr»:

    XVIII asr oxirida      -> Oʻn sakkizinchi asr oxirida
    Prime Korean           -> Praym Korean
    Examprep lugʻati       -> Ekzamprep lugʻati
    MCMXLVIII yil          -> Ming toʻqqiz yuz qirq sakkizinchi yil
    IELTS imtihoni         -> Ayelts imtihoni

**When a new foreign word appears, add it to `SAY_AS` — never fix it by hand in the
script file**, or the next regeneration silently undoes the fix and he records the wrong
thing again.

The SPEC and the SCREEN keep the real name (`practice("Prime Korean · PK-9")`); only the
voice gets the respelling. Same bridge as `korean.py`, one alphabet over.

**`cli.py script` now prints a pronunciation review** — a short, high-signal list of every
token where risk actually lives (letters outside the Uzbek alphabet, ALL-CAPS acronyms,
and capitalised words that are not sentence-initial), plus a **hard failure** on any Roman
numeral that survived. His instruction behind it is the right one and worth keeping in
mind on every line: **"always try to not read but HEAR how it will be delivered."** I
cannot hear, so the substitute is to review the short list rather than skim the whole
script — the risk hides in the skim.

Still unresolved, surfaced by the review and left alone because he has never objected to
them: **`Powerty`** (an Uzbek voice has no `w`) and **`Korean`** in "Praym Korean". Ask
before changing either; both are his brand.

### 7.2.2 ⚠️ Cyrillic look-alikes, and why the eye cannot catch them

mo31's narration shipped **`kichrayди`** — д and и typed on a Cyrillic keyboard.
Latin-Uzbek prose with two Cyrillic letters in the middle of a word looks
completely ordinary at a glance, and the capitalisation review cannot see it
because the letters are lowercase. `cli.py script` now **hard-fails** on any
Cyrillic in the narration.

The same scan found a pre-existing one in the pipeline: `speech.py`'s suffix list
read `dan|gacha|dagi|daги|...` — `daги` is `dagi` typed on a Cyrillic keyboard,
and since `dagi` was already in the list that alternative had never matched
anything. Removed.

**Worth re-running after any hand-edit of a spec:** scan `say` and `html` for
`[Ѐ-ӿ]`. Two of the project's own files had it.

### 7.2.1 ⚠️ A recorded film's script file is a RECORD, not a live artifact

A dry regression on 2026-09-15 (compute what every script *would* be now, write nothing)
showed the already-recorded films would change — and **that is correct and must be left
alone**:

- ko01-ko06 would gain `Praym` / `Ekzamprep`;
- mo01 would gain `yigirmanchi` (the `uz_ordinal` vowel fix, made after it was recorded);
- pm04/pm08/pm25 would gain the widened breaks (`0.7s`→`0.45s`, `1.5s`→`2.5s`, changed
  2026-08-29).

Those files match the audio that exists. **Do not regenerate a recorded film's script to
"tidy" it** — `cli.py check` compares script to audio and assumes they correspond, so a
tidied script silently makes every future report on that film meaningless. Regenerate only
when re-recording.

The regression itself is worth repeating after any `speech.py` change: it is the only way
to see whether a new rule mangles text it was not aimed at. This run confirmed **no Roman
numeral false positives** — the `[IVXLCDM]{2,}` pattern touched nothing it should not.

### 7.3 Say "Praym", write "Prime"

An Uzbek voice mispronounces **"Prime"**. His own fix, adopted 2026-09-15: the narration
says **`Praym Korean`**, the on-screen `practice()` card keeps the real product name
**`Prime Korean`**. Same principle as the Korean romanisation — a bridge for the voice, the
real thing for the eye. Applied to ko07-ko09; ko04-ko06 were already recorded and were
left alone.

### 7.4 ElevenLabs — `cli.py eleven`, audio tags and fun words  (2026-10-08)

The narration is now recorded by the pipeline: `python3 cli.py eleven <slug>` voices each
block with `eleven_v4` (the only model that speaks Uzbek) and joins them with exact 2.5 s
scene breaks, so the split is always forced. `--only N` re-takes one block.

- **Audio tags work and are not read aloud** — `[laughs]`, `[gasps]`, `[excited]` in a
  `narrate(...)` line pass straight through `speech.for_tts`. Verified by transcribing the
  blocks with ElevenLabs STT (`scribe_v1`, `language_code=uz`): every word present, no tag
  spoken. One tag per block, at the reaction.
- **His ask (2026-10-08): make it fun** — Uzbek pet-names to the viewer («oshqovoqchalar»,
  «toʻnkalar — kechirasiz, aqllilar!») in the `ask` line, and Korean exclamations
  (아이고, 대박, 헐) written in Hangul so `korean.py` spells them for the voice. One or two per
  film, never in the rule. ⛔ Not 아 씨 — it is a mild curse, whatever it sounds like.
- **`check` was calibrated on edge-tts**, whose pace is flat. v4 varies more: a block with a
  tag or an exclamation reads SLOW (fires «MOS EMAS», ko41 1.73x) and a plain sentence can
  read 1.2x fast (ko36). §7.1.4 still decides — slow is never missing text — and for a fast
  flag, **transcribe the block with `cli.py hear <slug> <n>` instead of loosening the gate.**
- ⚙️ **Two Pythons.** The Django venv's Playwright driver is broken (`coreBundle` exports
  nothing) and Anaconda's has no `edge_tts`. So: `lint` / `sheet` / `voice` with
  `/Applications/anaconda3/bin/python3`; `kowords` / `eleven` / `check` with the venv.

## 8. Inventory

| register | slugs | state |
|---|---|---|
| Prime Math lessons | pm04 · pm07 · pm08 · pm12 · pm25 · pm55 · pm67 · pm79 · pm84 · pm90 · pm91 · pm92 · pm93 · pm94 · pm97 · pm99 | voiced · **uploaded** |
| Matematika olami | mo01 · mo03 · mo04 | voiced · **uploaded** |
| Matematika olami (new) | mo10 (Gauss) · mo27 (diagramma) | **scripts out, awaiting voice** |
| Koreya olami | ko01 · ko02 · ko03 | voiced · **uploaded** (ko02 = Sejong, the one that got traction) |
| Tutilgan xato (Korean) | ko04 · ko05 · ko06 | voiced · ko05 + ko06 **not yet uploaded** |
| Tutilgan xato (Korean) | ko07 · ko08 · ko09 | **scripts out, awaiting voice** |
| Tutilgan xato (Korean) | ko10 · ko11 · ko12 | voiced |
| TOPIK (Tutilgan xato) | ko13 (쓰기 54) · ko14 (읽기 soati) · ko15 (답안지) | voiced · rendered 2026-09-16 |
| Bir maqol, ikki til | ko16 (호랑이) · ko17 (말) · ko18 (티끌) | voiced · rendered 2026-09-16 |
| Bir maqol, ikki til | ko19 (등잔 밑) · ko23 (백문이 불여일견) · ko27 (고생 끝에 樂) | voiced · rendered 2026-09-23 |
| Bitta soʻz | ko20 (생) · ko24 (회 — 사회↔회사) · ko28 (인 — 人 vs 因) | voiced · rendered 2026-09-23 (ko24 re-recorded once, §7.1.4) |
| Tutilgan xato (grammatika) | ko21 (은/는 va 이/가) · ko25 (고 싶어하다) | voiced · rendered 2026-09-23 |
| TOPIK (Tutilgan xato) | ko22 (읽기 lugʻat metodi) · ko26 (쓰기 53) | voiced · rendered 2026-09-23 |
| Grammatika · Bir maqol · TOPIK · Matn | ko29 – ko34 | voiced · rendered 2026-09-30 |
| ElevenLabs (first) | ko35 (관용 표현) · ko36 (불 不) · ko37 (낮말은 새가) | voiced (eleven_v4) · rendered 2026-10-08 |
| ElevenLabs · week of 2026-10-08 | ko38 (아/어서 vs (으)니까) · ko39 (학 學) · ko40 (배보다 배꼽) · ko41 (대박) | voiced (eleven_v4) · rendered 2026-10-08 |

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
- [ ] the endcard carries the address (default since 2026-09-16 — see §4.1)
- [ ] cover shows the wrong/strange thing, promise ≤4 words, strike only on the wrong part
- [ ] `python3 korean.py` → 26/26 (language films)
- [ ] every target-language word re-derived and **read by eye** (see §5 and the palatalisation
      note in `STYLE_GUIDE_KOREAN_VIDEO.md`)
- [ ] `cli.py lint` → PASS (four gates)
- [ ] `cli.py sheet --per-scene` → **every frame looked at**, not one
- [ ] `cli.py script --one --ssml` → no digit, no Hangul, no hanja/jamo, <2000 chars
- [ ] `cli.py kowords` → clips fetched, each ≤2.1s
- [ ] `cli.py check --audio` → "split ishonchli" **AND every block's speech rate
      within ~1.1x of the median** (see §7.1 — the span ratio alone missed ko07)
- [ ] `cli.py voice` → then pull frames from the finished mp4 and look at them
- [ ] ⚠️ before touching the SHARED kit (`stage.css`, `primitives.py`), **lint the whole
      catalogue** — `min-width:0` fixed ko08 and broke mo01
