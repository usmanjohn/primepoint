# Django Project: [Prime Point]

## Project Structure
- Custom apps (`prime`, `people`, `analytics`, `masters`, `practice`, `panda`, `homework`, `discussion`, `tutorial`) are located in the root directory.
- `templates/`: Global templates folder.
- `static/css/style.css`: Primary location for custom styles.

## Coding Standards
- Use Function-Based Views (FBVs).
- Templates must use Bootstrap CSS classes [if applicable].
- Avoid Javascript where applicable
- Make the pages mobile friendly
- Make the project support PWA
- Always in two languages: English (main) and uzbek.
## Common Commands
- Run Server: `python manage.py runserver`
- Migrations: `python manage.py makemigrations && python manage.py migrate`

## Deployment
- Deployed on railways through github repo. Railway's own deploy step (`railway.toml`
  startCommand) only runs `migrate` + a couple of `attach_exam_audio` calls — it does
  **NOT** run any bulk-content import command. Pushing to GitHub alone never gets new
  tutorials/lessons/stories/drills into the live DB.
- **Whenever a bulk-content task finishes (tutorials, examprep lessons, Corner stories,
  examprep writing drills, or anything else added via a `python manage.py import_*`
  management command) — ALWAYS give the matching `railway run python manage.py ...`
  command(s) at the end, without being asked.** The user runs these himself after he
  pushes to GitHub. Use `--author=powerty` (the production admin — local dev uses
  `prime` instead, see each toc file's AUTHOR header). One line per file imported, in
  the order the files must be applied (e.g. story data file(s) before an audio-attach
  step, since the collection/lesson must exist first). Example shape:
  ```
  railway run python manage.py import_corner corner/management/commands/_stories_<x>.py --author=powerty
  railway run python manage.py import_corner_audio corner/management/commands/audio/<slug> --collection="<title>"
  ```
  Swap in `import_tutorials` / `import_examprep` / `import_writing` / etc. as appropriate
  for whichever app the task touched.

## Creating Tutorials (bulk) — the generic, older workflow
⚠️ Every course that exists today has its **own** section below (Prime English, Korean,
Russian, Math, SAT). Use this generic workflow only for a **brand-new subject** that has no
section yet. In particular, "make the next 5 SAT tutorials" now means **Prime SAT Math** —
see that section; `STYLE_GUIDE.md` and `toc_sat_math.txt` are superseded for SAT.
When the user asks for a subject with no section of its own:
1. Read `tutorial/management/commands/STYLE_GUIDE.md` (how to write — the generic guide).
2. Read the subject's table of contents (its header gives PREFIX, CATEGORY, AUTHOR; the
   body is the ordered topic list).
3. Find where to continue: query the DB for the highest existing number, e.g.
   `Tutorial.objects.filter(title__startswith='SAT-')`.
4. Write the next batch into `tutorial/management/commands/_tutorials_<subject>_<range>.py`
   as a `TUTORIALS = [...]` list (titles like `SAT-7: ...`, math as HTML never LaTeX).
5. Import: `python manage.py import_tutorials <that file> --author=<AUTHOR from toc>`
   (add `--republish` to overwrite existing ones).
6. Give the `railway run python manage.py import_tutorials ...` command for production
   (see Deployment section) — automatically, every time.
Other subjects: add a new `toc_<subject>.txt` with its own PREFIX/CATEGORY; same workflow.

## Creating Prime English tutorials (bulk) — English grammar
**Prime English** is the 100-lesson English-grammar course in `tutorial`, held together by a
`TutorialPlaylist` called "Prime English" (so lessons get Prev/Next and a progress bar).
Titles are `PE-1: …` It has its **own** style guide and its own CSS component kit — do NOT
write these like the SAT tutorials. When the user asks (e.g. "make the next 5 Prime English
tutorials"):
1. Read `tutorial/management/commands/STYLE_GUIDE_PRIME_ENGLISH.md` (how to write + the full
   `pe-*` component reference; section 6 holds the user's own tips once they share them).
2. Read `tutorial/management/commands/toc_prime_english.txt` (header gives PREFIX, CATEGORY,
   AUTHOR, PLAYLIST; body is the ordered 100-lesson list with `[done]` markers).
3. Find where to continue: `Tutorial.objects.filter(title__startswith='PE-')`.
4. Write the next batch into `tutorial/management/commands/_tutorials_prime_english_<range>.py`
   as `PLAYLIST = {...}` + `TUTORIALS = [...]` (copy the `PLAYLIST` dict unchanged from the
   previous batch file; each lesson carries `"order": <lesson number>`).
5. Import: `python manage.py import_tutorials <that file> --author=prime` (add `--republish`
   to overwrite). The importer **creates the playlist itself** from the `PLAYLIST` dict, so
   production needs no manual admin step.
6. Mark the range `[done]` in the toc, then give the `railway run python manage.py
   import_tutorials ...` command for production — automatically, every time.
The lessons' visual kit (`pe-formula` pattern strips, `pe-ex` colour-coded examples,
`pe-timeline`, `pe-uz` callouts, `pe-reveal` tap-to-see answers…) lives in the
**PRIME ENGLISH** section at the bottom of `static/css/style.css`. It is pure CSS — never add
JavaScript to a lesson, and never invent a `pe-*` class without adding it to that section and
to the style guide first.

### Prime English readings (the third leg) — "Prime English Readings" in `corner`
Like Prime Korean, **every PE lesson gets a Corner reading with audio**: the tutorial teaches
the pattern, the practice drills it, the reading shows it living in a text. Collection
"Prime English Readings" (subject **English**, `order` 6) — story `order` = the lesson number,
so PE-24's reading is order 24. When the user asks (e.g. "make the next 5 Prime English
readings"), batches of 5 matching the tutorial files:
1. Read `corner/management/commands/STYLE_GUIDE_CORNER.md` **plus the overrides in
   `corner/management/commands/toc_prime_english_readings.txt`** (that header holds the whole
   policy: language split, the cumulative rule, the PE-1…PE-8 narrative-frame exception, the
   length curve, the written-register switch at PE-83, vocab/question counts).
2. Find where to continue:
   `Story.objects.filter(collection__title='Prime English Readings').order_by('-order').first()`
3. Write `corner/management/commands/_stories_prime_english_<range>.py` as `SUBJECT = {...}` +
   `COLLECTION = {...}` + `STORIES = [...]` (copy SUBJECT/COLLECTION unchanged from the
   previous batch — `import_corner` overwrites the shelf's fields).
   **Language policy is the mirror of Prime Korean**: story text, titles and questions in
   **English**; `summary`, `cn-word data-tr` glosses, `grammar` meanings and question
   `explanation`s in **Uzbek**. Bold the focus pattern with `<strong>` where it appears
   (house style of the English collections) and never put a `cn-word` inside a `<strong>`.
4. Import, generate audio, attach it, then link the readings to the lessons:
   ```
   python manage.py import_corner corner/management/commands/_stories_prime_english_<range>.py --author=prime
   python manage.py gen_corner_audio --collection="Prime English Readings"     # en-US-JennyNeural
   python manage.py import_corner_audio corner/management/commands/audio/prime-english-readings --collection="Prime English Readings"
   ```
   then add `"stories": ["<reading title>"],` to each lesson in
   `_tutorials_prime_english_<range>.py` (right before `"content"`) and re-run
   `import_tutorials <that file> --author=prime --republish` so the Reading card appears next
   to the Practice card. The story must exist first.
5. Mark the range `[done]` in the readings toc, then give the four
   `railway run python manage.py ...` commands **in that order** (import_corner →
   import_corner_audio → import_tutorials --republish) — automatically, every time.

## Creating Prime Korean tutorials (bulk) — koreys tili grammatikasi
**Prime Korean** is the 100-lesson Korean course in `tutorial`, held together by a
`TutorialPlaylist` called "Prime Korean". Titles are `PK-1: …`. It mirrors Prime English's
machinery but **inverts the language policy**: Prime English teaches *in* English, Prime
Korean teaches **in Uzbek** (the pupil can't read Hangul in lesson 1) — Korean is only the
material. **No English anywhere**, same as `examprep` TOPIK. When the user asks (e.g. "make
the next 5 Prime Korean tutorials"):
1. Read `tutorial/management/commands/STYLE_GUIDE_PRIME_KOREAN.md`.
2. Read `tutorial/management/commands/toc_prime_korean.txt` (header gives PREFIX, CATEGORY,
   AUTHOR, PLAYLIST; body is the ordered 100-lesson list with `[done]`/`[next]` markers).
3. Find where to continue: `Tutorial.objects.filter(title__startswith='PK-')`.
4. Write into `tutorial/management/commands/_tutorials_prime_korean_<range>.py` as
   `PLAYLIST = {...}` + `TUTORIALS = [...]` (copy `PLAYLIST` unchanged from the previous
   batch; each lesson carries `"order": <lesson number>`, category `korean`).
5. Import: `python manage.py import_tutorials <that file> --author=prime` (`--republish`
   to overwrite). The importer creates the playlist itself.
6. Mark the range `[done]` in the toc, then give the `railway run python manage.py
   import_tutorials ...` command — automatically, every time.
**Each Prime Korean lesson has THREE legs, written together in batches of 3 lessons:**
1. the **tutorial** (`tutorial`, PK-n) — teaches the pattern;
2. the **practice** (`practice`, 20 questions; shorter and reading-drill style for the
   Hangul lessons PK-1…PK-8) — drills it;
3. the **reading** (`corner`, collection "Prime Korean Readings", `order` = lesson number)
   — shows it living in a text, with `cn-word` tappable vocab, a `grammar` block naming
   the focus pattern, 2-3 comprehension questions and generated audio.
So a batch = 3 tutorials + 3 practices + 3 readings + 3 mp3s, all finished together.
Writing the three side by side keeps the test and the text drilling that lesson's own
examples. Guides: `practice/management/commands/STYLE_GUIDE_PK_PRACTICE.md` and
`corner/management/commands/toc_prime_korean_readings.txt` (readings start at PK-9 —
the Hangul lessons have no grammar to embed; readings are **cumulative**: earlier patterns
free, later ones forbidden).
`Tutorial.stories` (M2M to `corner.Story`) links a lesson to its reading, mirroring
`Tutorial.practices`; `import_tutorials` accepts a `"stories": [...]` key of titles/ids and
`tutorial_detail.html` renders a **Reading** card beside the Practice one. Import order per
batch: tutorials → practices → readings → audio → re-run `import_tutorials --republish`
so the `stories` links resolve (the story must exist first).
The visual kit **reuses the whole `pe-*` component set** and adds Korean-only pieces
(`pk-hangul` alphabet cards, `pk-block` syllable diagram, `pk-batchim` 받침 fork,
`pk-conj` conjugation ladder, `pk-level` speech-level ladder, `pk-say` pronunciation arrow)
in the **PRIME KOREAN** section at the bottom of `static/css/style.css`. Pure CSS — never add
JavaScript, and never invent a `pk-*` class without adding it to that section and the style
guide first.
Prime Korean is **not** exam prep: `examprep` TOPIK = question types and strategy, the
grammar/vocab banks = lookup tables, `corner` = reading. Prime Korean = the language itself,
from zero, in order.

## Creating Prime Russian tutorials (bulk) — rus tili grammatikasi
**Prime Russian** is the 100-lesson Russian course in `tutorial`, held together by a
`TutorialPlaylist` called "Prime Russian". Titles are `PR-1: …`, category `russian`. It is the
third course built on the same machinery as Prime English and Prime Korean, and — like
Prime Korean — it **teaches in Uzbek**; Russian is only the material. **No English anywhere.**
Its two differences from Prime Korean are worth remembering:
- the alphabet block is **5 lessons, not 8** (an Uzbek pupil already reads Cyrillic — PR-1
  sorts out what they know and warns them about the seven false friends В Н Р С У Х Ы);
- **Uzbek has cases too**, so every падеж is taught beside its Uzbek kelishik
  (*kitob**ni*** → *кни́г**у***). That mapping is the course's biggest teaching lever.
When the user asks (e.g. "make the next 3 Prime Russian tutorials"):
1. Read `tutorial/management/commands/STYLE_GUIDE_PRIME_RUSSIAN.md`.
2. Read `tutorial/management/commands/toc_prime_russian.txt` (header gives PREFIX, CATEGORY,
   AUTHOR, PLAYLIST; body is the ordered 100-lesson list with `[done]`/`[next]` markers).
3. Find where to continue: `Tutorial.objects.filter(title__startswith='PR-')`.
4. Write into `tutorial/management/commands/_tutorials_prime_russian_<range>.py` as
   `PLAYLIST = {...}` + `TUTORIALS = [...]` (copy `PLAYLIST` unchanged from the previous
   batch; each lesson carries `"order": <lesson number>`, category `russian`).
5. Import: `python manage.py import_tutorials <file> --author=prime` (`--republish` to
   overwrite). The importer creates the playlist itself.
6. Mark the range `[done]` in the toc, then give the `railway run python manage.py
   import_tutorials ...` command — automatically, every time.
**Each Prime Russian lesson from PR-6 has THREE legs, written together in batches of 3:**
1. the **tutorial** (`tutorial`, PR-n) — teaches the pattern;
2. the **practice** (`practice`, 20 questions; 12 for the alphabet lessons PR-1…PR-5) —
   drills it, subject `Russian`, guide `practice/management/commands/STYLE_GUIDE_PR_PRACTICE.md`;
3. the **reading** (`corner`, collection "Prime Russian Readings", `order` = lesson number)
   — shows it living in a text, with `cn-word` tappable vocab, a `grammar` block and 2-3
   comprehension questions. Guide: the overrides in
   `corner/management/commands/toc_prime_russian_readings.txt`.
So a batch = 3 tutorials + 3 practices + 3 readings. Import order per batch: tutorials →
practices → readings → re-run `import_tutorials --republish` so the `stories` links resolve
(the story must exist first).
**⛔ NO AUDIO on Prime Russian Readings** (user's decision 2026-08-09, after hearing the
first three): edge-tts' Russian voices "read very strange". Never run `gen_corner_audio` /
`import_corner_audio` for this collection and never offer it. Korean and English keep theirs.
A useful side effect: readings no longer need to be strictly-alternating one-speaker-per-`<p>`
dialogues, so mix narration and dialogue freely and use as many characters as the story wants.
**Two rules the user set for the readings (2026-08-08), written into that toc's header:**
**CLARITY** — name characters and keep using the name, chronological order only, one thing
per sentence, a time/place word whenever the scene moves; if the text cannot be summarised
in one Uzbek sentence, rewrite it. **VERSATILITY** — rotate the genre (letter, diary, folk
tale, news item, recipe, review, interview, popular science, biography…) and never run three
of the same shape in a row; retelling real material is encouraged, and facts must be true.
The visual kit **reuses the whole `pe-*` component set** and adds Russian-only pieces
(`pr-cyr` alphabet cards with the same/false-friend/new families, `pr-gender` three-way род
fork, `pr-case` падеж table, `pr-decl` ladder, `pr-aspect` НСВ/СВ pair, `pr-say`
pronunciation arrow, `pr-stress`/`pr-pair` for ударение) in the **PRIME RUSSIAN** section at
the bottom of `static/css/style.css`. Pure CSS — never add JavaScript, and never invent a
`pr-*` class without adding it to that section and the style guide first.
Prime Russian's practices are **not** the older `Часть NN: …` Russian drills (written in
Russian, attached to no lesson) — those stay as they are.

## Creating Prime Math tutorials (bulk) — maktab matematikasi, oʻzbek tilida
**Prime Math** is the 100-lesson school-maths course in `tutorial`, held together by a
`TutorialPlaylist` called "Prime Math". Titles are `PM-1: …`, category `math`. It is the
fourth course on the Prime machinery and the first that is **not a language**: it runs from
5-sinf arithmetic to a solid 9-sinf level (sonlar → kasr/foiz → algebra → funksiya va grafik
→ geometriya → statistika → matnli masalalar → mantiq), and it feeds the English-language
SAT Math tutorials (`SAT-…`) that already exist. Taught **in Uzbek**; the only English
allowed is the term equivalent in each lesson's `pe-gloss` key-words list (the SAT bridge).
When the user asks (e.g. "make the next 3 Prime Math lessons"):
1. Read `tutorial/management/commands/STYLE_GUIDE_PRIME_MATH.md`.
2. Read `tutorial/management/commands/toc_prime_math.txt` (header gives PREFIX, CATEGORY,
   AUTHOR, PLAYLIST; body is the ordered 100-lesson list with `[done]`/`[next]` markers).
3. Find where to continue: `Tutorial.objects.filter(title__startswith='PM-')`.
4. Write into `tutorial/management/commands/_tutorials_prime_math_<range>.py` as
   `PLAYLIST = {...}` + `TUTORIALS = [...]` (copy `PLAYLIST` unchanged from the previous
   batch; each lesson carries `"order": <lesson number>`, category `math`).
5. Import: `python manage.py import_tutorials <file> --author=prime` (`--republish` to
   overwrite). The importer creates the playlist itself.
6. Mark the range `[done]` in the toc, then give the `railway run python manage.py
   import_tutorials ...` command — automatically, every time.
**Each Prime Math lesson has THREE legs, written together in batches of 3:**
1. the **tutorial** (`tutorial`, PM-n) — teaches the idea, with a `pm-solve` ladder whose
   right column says *why* each line happened, and **at least one worked matnli masala
   whatever the topic**;
2. the **practice** (`practice`, 20 questions, subject **`Matematika`**) — drills it;
   **questions 19–20 are always word problems.** Guide:
   `practice/management/commands/STYLE_GUIDE_PM_PRACTICE.md`, list: `toc_pm_practices.txt`.
   Always import with `--expect-questions=20`;
3. the **reading** (`corner`, collection "Prime Math Readings", `order` = lesson number) —
   the maths doing real work in a text. Guide: the overrides in
   `corner/management/commands/toc_prime_math_readings.txt`.
Import order per batch: tutorials → practices → readings → re-run `import_tutorials
--republish` so the `stories` links resolve (the story must exist first).
**Corner has a SECOND maths shelf: "Matematika olami"** (`toc_matematika_olami.txt`) —
standalone texts bound to no lesson: buyuk matematiklar (al-Xorazmiy, Beruniy, Ulugʻbek,
Gauss, Ramanujan), tabiatdagi matematika, kundalik hayotdagi matematika, jumboqlar. This is
the shelf pupils open for pleasure; write 2–3 alongside the lesson batches or on request.
Facts must be true.
**⛔ NO AUDIO on either maths shelf** — formulas, `x²` and `3/4` do not survive TTS. Never
run `gen_corner_audio` / `import_corner_audio` for them and never offer it.
**⚠️ THE ARITHMETIC GATE (the rule that matters most).** A wrong answer key is the worst bug
this course can ship. Every numeric answer in the tutorials, the practices and the readings
is computed twice — the second time by a throwaway script in the scratchpad
(`verify_pm_<range>.py`) that recomputes each answer and prints any mismatch. Run it, fix,
then import.
The visual kit **reuses the whole `pe-*` component set** and adds maths-only pieces
(`pm-solve` solving ladder, `pm-frac` fractions, `pm-root`, `pm-num` number line, `pm-col`
column arithmetic, `pm-fig` + inline SVG figures with `pm-ln`/`pm-fill`/`pm-lbl`, `pm-model`
bar model, `pm-word` phrase→symbol table, `pm-check`, `pm-est`, plus `pe-ex__math`) in the
**PRIME MATH** section at the bottom of `static/css/style.css`. Pure CSS — never add
JavaScript, and never invent a `pm-*` class without adding it to that section and the style
guide first. Maths is written as **HTML, never LaTeX** (`x<sup>2</sup>`, × ÷ √ ≤ ≥ π °,
decimals with a comma), and geometry figures are **inline SVG**, never uploaded images.
Prime Math is **not** the SAT course (`SAT-…`, English, exam-shaped) and not the Math
Championship game (auto-generated, no explanations). It is the school course itself, from
zero, in order.

## Creating Prime SAT Math lessons (bulk) — digital SAT, ikki tilda
**Prime SAT Math** is the 100-lesson digital-SAT maths course in `tutorial`, held together
by a `TutorialPlaylist` called "Prime SAT Math". Titles are `SAT-1: …`, category `math`.
It is the fifth course on the Prime machinery and the **only bilingual one**: the exam
speaks **English**, the teacher speaks **Uzbek**.
⚠️ **This is a REWRITE, not a new course.** `SAT-1 … SAT-100` already exist in the DB from
an older, thinner generation (English prose, two Uzbek asides, no playlist, no practice).
The new lessons carry **the same titles** and go in with `--republish`, overwriting them.
**Never reword a title** — the title is the importer's match key, and a changed one creates
a duplicate lesson instead of upgrading the old one.
When the user asks (e.g. "make the next 5 Prime SAT lessons"):
1. Read `tutorial/management/commands/STYLE_GUIDE_PRIME_SAT.md` (§0 is the language split,
   §0.1 the American number format, §0.2 the facts about the test, §7 the answer gate).
2. Read `tutorial/management/commands/toc_prime_sat_math.txt` (header gives PREFIX, CATEGORY,
   AUTHOR, PLAYLIST; body is the ordered 100-lesson list with `[done]`/`[next]` markers).
   The old `toc_sat_math.txt` is marked SUPERSEDED — do not write from it.
3. Find where to continue: `Tutorial.objects.filter(title__startswith='SAT-')` plus the
   toc's `[next]` markers (the DB alone lies here — all 100 titles already exist).
4. Write into `tutorial/management/commands/_tutorials_prime_sat_<range>.py` as
   `PLAYLIST = {...}` + `TUTORIALS = [...]` (copy `PLAYLIST` unchanged from the previous
   batch; each lesson carries `"order": <lesson number>`, category `math`).
5. Import with **`--republish`** (not optional — the old lesson is already there).
6. Mark the range `[done]` in both tocs, then give the two `railway run python manage.py …`
   commands — automatically, every time.
**Each Prime SAT lesson has THREE legs, written together in batches of 5:**
1. the **tutorial** (`tutorial`, SAT-n) — teaches the idea in Uzbek, with at least two
   `.ps-stem` exam questions in English and their traps named;
2. the **practice** (`practice`, 20 questions, subject **`Math`** — Telegram shows it as
   "Matematika (SAT)"; NOT `Matematika`, which is Prime Math's) — drills it. Guide:
   `practice/management/commands/STYLE_GUIDE_PS_PRACTICE.md`, list: `toc_ps_practices.txt`.
   Questions in English, explanations in Uzbek. Always `--expect-questions=20`.
3. the **reading** (`corner`, collection "Prime SAT Readings", `order` = lesson number)
   — the maths doing real work in an **English** text, with `cn-word` Uzbek glosses,
   an "Exam English" block and **audio**. Guide: the overrides in
   `corner/management/commands/toc_prime_sat_readings.txt`.
   ⛔ **No algebraic notation in a reading's body** — no x, no equations. Quantities are
   English ("a joining fee of $30 and $8 for each event"). Two reasons, both hard: it is
   the skill being trained (turning an English sentence into maths), and an equation does
   not survive TTS. Spell units out (millilitres, degrees) so the narrator reads them.
   ⚠️ **Always pass `--voice` explicitly.** This shelf sits under the *Matematika* subject,
   whose `gen_corner_audio` default voice is not English — an unattended run narrates an
   English text with a Korean voice. Alternate `en-US-JennyNeural` / `en-US-GuyNeural`.
Import order per batch: tutorials → practices → readings → audio → `import_tutorials
--republish` (so the `"stories": [...]` links resolve; the story must exist first).
```
python manage.py import_tutorials tutorial/management/commands/_tutorials_prime_sat_<range>.py --author=prime --republish
python manage.py import_practices practice/management/commands/_practice_ps_<range>.py --master=prime --expect-questions=20
python manage.py import_corner corner/management/commands/_stories_prime_sat_readings_<range>.py --author=prime
python manage.py gen_corner_audio --collection="Prime SAT Readings" --only <n> --voice en-US-JennyNeural
python manage.py import_corner_audio corner/management/commands/audio/prime-sat-readings --collection="Prime SAT Readings"
python manage.py import_tutorials tutorial/management/commands/_tutorials_prime_sat_<range>.py --author=prime --republish
```
**Corner has a SECOND SAT shelf: "SAT olami"** (`toc_sat_olami.txt`, subject Matematika,
order 4) — standalone Uzbek texts about the **exam itself**, bound to no lesson: how the
adaptive module works, how 1,600 is put together, Desmos, test day, why the test changed in
2024. This is the shelf a pupil opens to understand what they have signed up for. ⛔ **No
audio** (the prose is Uzbek, the English in it is single terms — same as Koreya olami), and
⛔ **never invent fees, test dates, centre names or university cut-offs**: describe the
process and send the reader to the official source. Write 2–3 alongside the lesson batches
or on request. Facts must be true.
**⚠️ THE ANSWER GATE** (inherited from Prime Math and extended). Every numeric answer in the
lessons and all 20 keys of every practice are computed twice, the second time by throwaway
scripts in the scratchpad (`verify_sat_<range>.py` for the practices, plus one for the
tutorials) that recompute each answer by a **different route** — brute force over
`Fraction`s, or a numeric fingerprint of the expression at three sample points — and print
any mismatch. They also check the key is among the choices, no two choices are equal, and
numeric choice lists are sorted. Then re-read each English stem and ask whether a careful
reader could defend a second answer: **ambiguity is a bug**. Run, fix, then import.
The visual kit **reuses the whole `pe-*` set and the whole `pm-*` maths set**, and adds the
`ps-*` pieces an exam course needs (`ps-stem` + `ps-ch` + `ps-sol` the exam question card,
`ps-tactic` the move, `ps-trap` the planted wrong answer, `ps-desmos` the keystrokes,
`ps-gridin` the answer box, `ps-phrase` exam English → what it asks, `ps-time` the pacing
chip) in the **PRIME SAT** section at the bottom of `static/css/style.css`. Pure CSS — never
add JavaScript, and never invent a `ps-*` class without adding it to that section and the
style guide first. Maths is **HTML, never LaTeX**; figures are inline SVG.
**⚠️ THE DOLLAR-SIGN TRAP (fixed 2026-09-04, do not reintroduce).** `tutorial_detail.html`
renders a lesson through the `render_math` filter, and MathJax is loaded on that page. Both
used to treat `$…$` as inline maths — so in a lesson full of prices, everything between two
amounts was read as a formula and **stripped of its markup**: paragraphs merged and the rest
of the page collapsed into one grey block (it hit SAT-3, SAT-5, SAT-10 and eight older
lessons). The fix is in place — `render_math` now refuses a region that crosses a block
boundary, runs past 200 characters or opens mid-markup, and `inlineMath` no longer lists
`['$','$']` — with regression tests in `tutorial/tests.py`. Write prices normally (`$12`);
never "fix" this by escaping them, and if real LaTeX is ever needed use `\( … \)`.

**Numbers use the SAT's own convention — `3.5` and `1,200`, decimal point and comma
thousands** — the exact opposite of Prime Math's `3,5`. A pupil who types a comma into a
grid-in loses the mark, so the habit is broken inside the course.
Prime SAT is **not** Prime Math (Uzbek school maths, from zero) and not the Math
Championship. It is the exam itself: its sentences, its traps and its clock.

## Creating Logic Arena puzzles (bulk) — sealed-answer logic problems
**Logic Arena** (`logic` app, `/logic/`, uz "Mantiq maydoni") is the weekly logic-puzzle
section: nine coins and two weighings, the wolf/goat/cabbage, the twelve-coin problem. Its
one idea is that **you answer but you are not told whether you were right until the reveal
date** — a puzzle opens, everyone seals an answer, and a week later the solution and the
wall of solvers appear for everyone at once. Answering while sealed is worth full points;
solving an old one from the archive is worth half. Guests may read; only logged-in users
may answer. No JavaScript anywhere — the countdown is a server-rendered number and the
hint/solution are native `<details>`.
Puzzles are **bilingual in the data itself** (English + `*_uz` columns on the model), not
through gettext: the bodies are content, not interface. Figures are **inline SVG built by
`logic/figures.py`** — never an uploaded image.
When the user asks (e.g. "make the next 4 logic puzzles"):
1. Read `logic/management/commands/STYLE_GUIDE_LOGIC.md` (how to choose a puzzle, why the
   typed answer must be a short unguessable value, the figure kit; section 12 holds the
   user's own tips once they share them).
2. Read `logic/management/commands/toc_logic_puzzles.txt` (header gives AUTHOR, SCHEDULE;
   body is the ordered list with `[done]`/`[next]` markers and a candidate pool).
3. Find where to continue: `LogicPuzzle.objects.order_by('-number').first()`.
4. Write `logic/management/commands/_puzzles_logic_<range>.py` as `SCHEDULE = {...}`
   (copied unchanged from the previous file — one season, one schedule) + `PUZZLES = [...]`,
   **two puzzles per round**, one gentler and one harder.
5. Import: `python manage.py import_logic <file> --author=prime` (`--republish` to
   overwrite, `--draft` to import unpublished). The importer refuses a puzzle whose Uzbek
   title/body/solution is missing.
6. Mark the range `[done]` in the toc, then give the `railway run python manage.py
   import_logic ...` command — automatically, every time.
**⚠️ THE ANSWER GATE.** A wrong answer key is the worst bug this section can ship — the
pupil is told they were wrong a week after they were right, in public on the solvers wall.
Every answer is computed twice, the second time by a throwaway script in the scratchpad
(`verify_logic_<range>.py`) that derives each answer independently (brute force, BFS over
states, or an explicit formula) and prints any mismatch. Run it, fix, then import.
**Keep at least four rounds ahead of today** or the Arena runs out of live puzzles.
The visual kit is the `lg-*` section at the bottom of `static/css/style.css` (`lg-hero`,
`lg-card`, `lg-status`, `lg-rule` constraint box, `lg-ask` "what to type" box, `lg-fold`
hint/solution `<details>`, `lg-envelope` wax seal, `lg-steps` numbered solution ladder,
`lg-moral` the-trick line, `lg-fig` + `lg-ln`/`lg-fill`/`lg-lbl` for figures). Pure CSS —
never add JavaScript, and never invent an `lg-*` class without adding it to that section
and to the style guide first.
Logic Arena is **not** the Math Championship (auto-generated, instantly marked) and not a
practice test. It is one hard, beautiful problem a week with a real explanation attached.

## Creating examprep lessons (bulk) — TOPIK etc.
`examprep` holds detailed, by-skill exam prep (`ExamTrack` → skill → `Topic` (question-type
card, e.g. Reading → "Reklama va e'lonlar (광고)") → `Lesson` → ordered `LessonBlock`s with
rich text + optional inline MCQ). Use this — not `tutorial` — for TOPIK
reading/writing/listening prep. When the user asks (e.g. "make the next 5 TOPIK reading lessons"):
1. Read `examprep/management/commands/STYLE_GUIDE_TOPIK.md` (how to write — section 7 holds
   the user's own TOPIK tips once they share them; their tips override the generic advice).
2. Read the skill's table of contents, e.g. `examprep/management/commands/toc_topik_reading.txt`
   (header gives TRACK, SKILL, AUTHOR; body is the ordered lesson list).
3. Find where to continue: query the DB for the highest existing `order` in that track+skill, e.g.
   `Lesson.objects.filter(track__name='TOPIK', skill='reading').order_by('-order').first()`.
4. Write the next batch into `examprep/management/commands/_lessons_topik_<skill>_<range>.py`
   as a `TRACK = {...}` dict + `TOPIC = {...}` dict + `LESSONS = [...]` list (each lesson
   carries `"topic": TOPIC` and is a list of `blocks`; Korean as Hangul, with inline Uzbek
   per the style guide). The toc's `## TOPIC:` headers say which topic each lesson is in.
5. Import: `python manage.py import_examprep <that file> --author=<AUTHOR from toc>`
   (add `--republish` to overwrite existing ones — it rebuilds each lesson's blocks).
6. Give the `railway run python manage.py import_examprep ...` command for production
   (see Deployment section) — automatically, every time.
Other exams/skills: add a new `toc_<exam>_<skill>.txt` with its own TRACK/SKILL; same workflow.
Note: `exam` (the timed, scored test simulator) is separate — keep mock-test questions there.

## Creating grammar-bank entries (bulk) — TOPIK grammatika jadvali
`examprep`'s `GrammarPoint` is the grammar summary table at `/examprep/<track>/grammar/`
— a filterable, printable, downloadable (xlsx/csv) reference of every grammar pattern,
grouped either by grammatical type (`category`) or by MEANING (`function`), which is what
puts near-synonyms side by side. Each row expands to examples, nuance, common mistakes and
`GrammarSynonym` rows whose notes say how the similar patterns DIFFER; the importer
cross-links those into clickable pairs. This is a **reference**, not lessons — teaching a
pattern in depth still belongs in an `examprep` Lesson.
**Access:** reading the table is open to everyone, but the **print sheet and the
xlsx/csv download are staff-only** (`_require_staff` in `examprep/views.py`; the buttons
are hidden from non-staff). The print sheet is watermarked. Keep this split for any
similar take-away reference added later. When the user asks (e.g. "add the
TOPIK conjunctive adverbs to the grammar table"):
1. Read `examprep/management/commands/STYLE_GUIDE_GRAMMAR.md` (how to write — field
   meanings, the synonym rule, section 12 holds the user's own tips once they share them).
2. Read `examprep/management/commands/toc_topik_grammar.txt` (header gives TRACK, AUTHOR;
   body is the group list with each group's `order` decade and `[done]`/`[next]` status).
3. Find where to continue:
   `GrammarPoint.objects.filter(track__name='TOPIK').order_by('-order').first()`
4. Write `_grammar_topik_<group>.py` as `TRACK = {...}` + `POINTS = [...]` (Korean patterns
   and examples, Uzbek meanings/notes — no English).
5. Import: `python manage.py import_grammar <that file> --author=<AUTHOR from toc>`
   (add `--republish` to overwrite — it rebuilds examples + synonyms and re-resolves every
   cross-link across the whole track).
6. Give the `railway run python manage.py import_grammar ...` command for production
   (see Deployment section) — automatically, every time.
Another exam: add a `toc_<exam>_grammar.txt` with its own TRACK; same workflow.

**IELTS has its own grammar bank** at `/examprep/ielts/grammar/` (116 patterns, 11 groups —
tenses, modals/hedging, clauses, conditionals, passive, articles, prepositions, comparison,
verb patterns, cohesion, advanced). Same models and importer, different wording:
- write with `STYLE_GUIDE_GRAMMAR_IELTS.md` + `toc_ielts_grammar.txt` (NOT the TOPIK ones);
- patterns and examples in **English**, every explanation in **Uzbek**;
- `category` uses the `en_*` values (`en_tense`, `en_clause`…), never TOPIK's;
- `level` 1-6 renders as **Band 5 … Band 7.5+**, not TOPIK levels.
The per-track labels live in `examprep/banklabels.py` — that module decides which choice
values a track shows, what they are called, and the page wording (Band vs TOPIK, root
origin vs Hanja, "English" vs 한국어). **Adding a track means adding a block there, not
forking the models or templates.**

## Creating vocab-bank entries (bulk) — TOPIK lug'at
`examprep`'s `VocabEntry` is the vocabulary table at `/examprep/<track>/vocab/`, sibling of
the grammar bank (same access rules: open to read, **staff-only + watermarked** to print or
download). Its own idea is **root families** (`VocabRoot`) at
`/examprep/<track>/vocab/roots/` — most TOPIK II vocabulary is Sino-Korean, so 출(出) once
gives 출구·출근·출발·출석·제출·수출. Words carry `hanja` + `roots` (M2M), plus
`VocabExample`s and `VocabRelation`s (synonym / antonym / related, cross-linked on import).
When the user asks (e.g. "add the TOPIK adverbs to the vocab table"):
1. Read `examprep/management/commands/STYLE_GUIDE_VOCAB.md` (field meanings, the root rule,
   the "state the DIFFERENCE" rule for relations; section 12 holds the user's own tips).
2. Read `examprep/management/commands/toc_topik_vocab.txt` (header gives TRACK, AUTHOR and
   the **required import order**; body is the group list with `order` decades and status).
3. Find where to continue:
   `VocabEntry.objects.filter(track__name='TOPIK').order_by('-order').first()` and
   `VocabRoot.objects.filter(track__name='TOPIK').values_list('syllable', flat=True)`.
4. Write `_vocab_topik_<group>.py` as `TRACK = {...}` + optional `ROOTS = [...]` + `WORDS = [...]`
   (Korean words and examples, Uzbek meanings — no English).
5. Import: `python manage.py import_vocab <that file> --author=<AUTHOR from toc>`
   (add `--republish` to overwrite — it rebuilds examples, root links and relations).
   ⚠️ **Each root is defined in exactly one file, and files must be imported in the toc's
   order** — `import_vocab` errors out on a root it cannot find rather than silently
   dropping the word from its family. Never copy a root definition into a second file.
6. Give the `railway run python manage.py import_vocab ...` commands **in that same order**
   for production (see Deployment section) — automatically, every time.

**IELTS has its own vocab bank** at `/examprep/ielts/vocab/` (167 words, 31 root families,
7 groups). The root-family idea carries over from Hanja to **Latin/Greek roots**: `spect`
once gives inspect · spectator · perspective · prospect. Same models and importer:
- write with `STYLE_GUIDE_VOCAB_IELTS.md` + `toc_ielts_vocab.txt` (NOT the TOPIK ones),
  and follow that toc's import order — roots files 1-3 before the thematic files 4-7;
- words and examples in **English**, meanings and notes in **Uzbek**;
- `syllable` holds the root (`spect`, `re-`, `-ion`), `hanja` holds the **origin**
  (`specere (lat.) — qaramoq`) on roots and the **build** (`in- + spect`) on words;
- prefixes and suffixes count as roots on this track;
- `topic` adds `academic` and `data` (Task 1 trend language); `level` renders as a Band.
Each data file ends with a loop stamping its `order` decade onto `WORDS` — keep it, and
give a new file an unused decade.

## Creating Corner stories (bulk)
`corner` is the reading library at `/corner/` (`Subject` → `Collection` → `Story`, plus
`WritingTemplate` files uploaded via admin). Writing drills are **not** here — they live in
`examprep`; see the writing-drills section below. Story vocabulary is marked inline as
`<span class="cn-word" data-tr="uzbekcha tarjima">한국어</span>` — tappable highlights and
the end-of-story flashcards are auto-generated from those spans on save.
When the user asks (e.g. "make the next 5 Keimyung stories"):
1. Read `corner/management/commands/STYLE_GUIDE_CORNER.md` (how to write — section 6 holds
   the user's own tips once they share them; their tips override the generic advice).
2. Read the collection's table of contents, e.g. `corner/management/commands/toc_keimyung_korean.txt`
   (header gives SUBJECT, COLLECTION, AUTHOR; body is the ordered story list).
3. Find where to continue: query the DB for the highest existing `order` in that collection, e.g.
   `Story.objects.filter(collection__title='Keimyung Korean Readings').order_by('-order').first()`.
4. Write the next batch into `corner/management/commands/_stories_<collection>_<range>.py`
   as `SUBJECT = {...}` + `COLLECTION = {...}` dicts + a `STORIES = [...]` list
   (story text in the target language, translations/summaries in Uzbek per the style guide).
5. Import: `python manage.py import_corner <that file> --author=<AUTHOR from toc>`
   (add `--republish` to overwrite existing ones — it rebuilds each story's word list).
6. Give the `railway run python manage.py import_corner ...` command for production (and
   the matching `import_corner_audio` one if audio was generated too) — see Deployment
   section — automatically, every time.
Other collections: add a new `toc_<collection>.txt` with its own SUBJECT/COLLECTION; same workflow.

## Creating exam-prep writing drills (bulk) — TOPIK 쓰기 53 etc.
`examprep`'s `WritingDrill` is the interactive exam-writing trainer at
`/examprep/<track>/drills/` (exam question + HTML/SVG chart → fill-in scaffold with
`wp-blank` gaps → model answer reveal → auto flashcards from `cn-word` spans). It lives
under the exam track it belongs to — TOPIK drills at `/examprep/topik/drills/`, IELTS at
`/examprep/ielts/drills/`. (Moved out of `corner` in July 2026: Corner is the reading
library. Old `/corner/writing/...` URLs 301-redirect here.) When the user asks (e.g. "make
the next 5 TOPIK 53 writing drills"):
1. Read `examprep/management/commands/STYLE_GUIDE_WRITING.md` (how to write — chart markup,
   blank/expression conventions; section 8 holds the user's own tips once they share them).
2. Read the question type's toc, e.g. `examprep/management/commands/toc_topik_writing_53.txt`
   (header gives TRACK, QTYPE, AUTHOR; body is the ordered drill list).
3. Find where to continue: query the DB for the highest existing `order`, e.g.
   `WritingDrill.objects.filter(qtype='53').order_by('-order').first()`.
4. Write the next batch into `examprep/management/commands/_writing_<exam><qtype>_<range>.py`
   as `TRACK = {...}` + `PRACTICES = [...]` (Korean exam text, Uzbek translations/tips).
   `TRACK` is the ExamTrack (matched by name, e.g. "TOPIK") — not a Corner subject.
5. Import: `python manage.py import_writing <that file> --author=<AUTHOR from toc>`
   (add `--republish` to overwrite existing ones — it rebuilds each drill's word list).
6. Give the `railway run python manage.py import_writing ...` command for production
   (see Deployment section) — automatically, every time.
Question types 51/52/54: add a new `toc_topik_writing_<qtype>.txt`; same workflow.
Adding drills for another exam: add its `qtype` codes to `QTYPE_CHOICES` in
`examprep/models.py` (IELTS `t1`/`t2` are already there) and point `TRACK` at that exam.

## The Telegram channel (`telegrambot/`) — outbound-only bot
`telegrambot` posts site content to the Telegram channel **@powertyuz** through the bot
**@PowertyuzBot**. It is **outbound only**: no webhook, no public endpoint, nothing stored
about who reads the channel. Read `telegrambot/README.md` before touching it.
- **Daily 22:00 Tashkent (`0 17 * * *`, Railway cron is UTC)** — **one `PracticeQuestion`
  per subject** as native quiz polls (Ingliz tili, Koreys tili, Matematika, Rus tili,
  Matematika (SAT)), 3s apart. Never repeats (`TelegramPost`); the guard is per subject
  per day, so a re-run sends only what is missing.
- ⛔ **Never post from the local database.** `DATABASES` silently falls back to sqlite
  without `DATABASE_URL`, and posts built from dev rows carry dev ids in every link —
  this shipped once (2026-09-02). `api.refuse_local_database()` blocks it; use
  `--dry-run` to preview locally.
- **Weekly** — the Logic Arena puzzle when it opens and its answer when it reveals.
- The channel is **Uzbek only**; only the material (an English sentence, a Korean line) is not.
- Always `--dry-run` before sending: `python manage.py post_daily_quiz --dry-run`.
  `telegram_ping` checks the token; `telegram_daily` is what Railway cron runs.
- **`SITE_URL` must be set in Railway** — a cron command has no request to build links from,
  so if it is wrong every button in every post is dead.
- The cron is its **own Railway service** (`0 17 * * *`, `python manage.py telegram_daily`)
  and does **not** inherit the web service's variables — they must be set on it too.
- Railway's **private network is not up when a cron container starts**, so `telegram_daily`
  waits for the DB before working; otherwise it dies on `postgres.railway.internal`.
- ⛔ Never add user tracking / account linking to this bot without being asked: the user
  chose outbound-only deliberately (2026-09-02).

## Social accounts (`prime/social.py`)
Telegram `@Albetta` (contact) + channel `@powertyuz`, Instagram `@powerty.uz`, YouTube
`@powertyuz`, e-mail `powertyuz@gmail.com` live in **one** registry, `prime/social.py`,
exposed to every template by `prime.context_processors.social` and rendered by
`templates/includes/social_links.html` (`style="compact"` = icon row, default = full cards).
Change a handle there and the sidebar, About, Help and the schema.org `sameAs` block all
follow. Never hard-code a handle in a template.

## Making videos (`storyvideo/`) — Shorts/Reels animatics
`storyvideo/` is a plain Python package at the repo root (**not** a Django app, never
imported by Django, costs production nothing). It turns a Corner reading into a
1080x1920 animatic with TTS narration and a synthesised sound layer.
⚠️ Always `cd storyvideo && python3 cli.py …` — `python -m storyvideo` is broken.
- **`storyvideo/README.md`** — the renderer, the `seek(t)` contract, the three lint
  gates, the maths/history beat vocabulary.
- **`storyvideo/STYLE_GUIDE_KOREAN_VIDEO.md`** — read this before writing ANY language
  video (Korean now, English later): the full loop, the language beats, the three
  narration rules (never send Hangul; hanja and lone jamo are refused; digits become
  words), the native-Korean `echo` beat, and the two fault classes `cli.py check` tells
  apart. Its checklist is the definition of done.
- **`cli.py check <slug> --audio …` before EVERY render** — one second against six
  minutes. It has already caught two recordings that would have shipped broken.
Source shelves: "Prime Math Readings" + "Matematika olami" (maths),
**"Koreya olami"** (`toc_koreya_olami.txt`, Uzbek prose about Korean — the language is
the material, each word a `cn-word` span, ⛔ no audio). Those import through
`import_corner`, so they DO need a `railway run` line; the videos themselves do not.
