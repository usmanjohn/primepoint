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

## Creating Tutorials (bulk)
When the user asks to create/continue tutorials (e.g. "make the next 5 SAT tutorials"):
1. Read `tutorial/management/commands/STYLE_GUIDE.md` (how to write — same for every subject).
2. Read the subject's table of contents, e.g. `tutorial/management/commands/toc_sat_math.txt`
   (its header gives PREFIX, CATEGORY, AUTHOR; the body is the ordered topic list).
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
