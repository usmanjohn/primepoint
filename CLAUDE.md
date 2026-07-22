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
  Corner writing drills, or anything else added via a `python manage.py import_*`
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

## Creating Corner stories (bulk)
`corner` is the resource library at `/corner/` (`Subject` → `Collection` → `Story`, plus
`WritingTemplate` files uploaded via admin). Story vocabulary is marked inline as
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

## Creating Corner writing drills (bulk) — TOPIK 쓰기 53 etc.
`corner`'s `WritingPractice` is the interactive exam-writing trainer at `/corner/writing/`
(exam question + HTML/SVG chart → fill-in scaffold with `wp-blank` gaps → model answer
reveal → auto flashcards from `cn-word` spans). When the user asks (e.g. "make the next
5 TOPIK 53 writing drills"):
1. Read `corner/management/commands/STYLE_GUIDE_WRITING.md` (how to write — chart markup,
   blank/expression conventions; section 8 holds the user's own tips once they share them).
2. Read the question type's toc, e.g. `corner/management/commands/toc_topik_writing_53.txt`
   (header gives SUBJECT, QTYPE, AUTHOR; body is the ordered drill list).
3. Find where to continue: query the DB for the highest existing `order`, e.g.
   `WritingPractice.objects.filter(qtype='53').order_by('-order').first()`.
4. Write the next batch into `corner/management/commands/_writing_<exam><qtype>_<range>.py`
   as `SUBJECT = {...}` + `PRACTICES = [...]` (Korean exam text, Uzbek translations/tips).
5. Import: `python manage.py import_writing <that file> --author=<AUTHOR from toc>`
   (add `--republish` to overwrite existing ones — it rebuilds each drill's word list).
6. Give the `railway run python manage.py import_writing ...` command for production
   (see Deployment section) — automatically, every time.
Question types 51/52/54: add a new `toc_topik_writing_<qtype>.txt`; same workflow.
