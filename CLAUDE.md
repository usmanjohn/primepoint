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
- Deployed on railways through github repo.

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
Other subjects: add a new `toc_<subject>.txt` with its own PREFIX/CATEGORY; same workflow.
