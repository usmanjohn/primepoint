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
