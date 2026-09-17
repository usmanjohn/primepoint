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
| **«Bir maqol, ikki til»** | 속담 + its Uzbek twin | Korean (and any language with proverbs) | ko16-ko18 |

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
