# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_history.py from kapital/history/.

    python3 kapital/build_history_playlist.py

The history page (Django app `history`: downloads, cleanup, admin file manager) reaches the
work machine through the admin-only «Kapital — History» playlist: one lesson per file,
numbered in install order. Edit the files in kapital/history/, run this script, then import
with --republish. Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'history'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_history.py'

# (path inside the app, language, what it is) — in install order.
FILES = [
    ('views.py', 'python', 'Downloads, the fixed cleanup (selected deletes ONLY the ticked files; auto runs only on its own button) and the admin page with every file in datasets/.'),
    ('urls.py', 'python', 'Route names: history, download-file, export-model-to-excel, cleanup-portfels, datasets-files.'),
    ('templates/history/_file_card.html', 'html', 'One column of files with download buttons and admin checkboxes; used four times by home.html.'),
    ('templates/history/home.html', 'html', 'The history page: four file columns, admin cleanup panel, link to the file manager. Russian UI.'),
    ('templates/history/datasets.html', 'html', 'Admin only: every file in datasets/ grouped by folder with size and date; tick and delete. Russian UI.'),
]

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — History playlist (admin only): report downloads, disk cleanup, datasets file manager; one file per lesson.

GENERATED from kapital/history/ by kapital/build_history_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_history.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — History', 'category': 'programming', 'staff_only': True,
            'description': 'The history page: downloads, the fixed «delete selected», auto-cleanup and an admin page for every file in datasets/. One file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(order, name, summary, content):
    d = {'title': f'HIS-{order}. {name}', 'category': 'programming',
         'order': order, 'summary': summary, 'content': content}
    return 'TUTORIALS.append(' + repr(d) + ')\n'


def main():
    n = len(FILES) + 1
    out = [HEADER]

    tree = 'history/\n' + ''.join(f'    {p}\n' for p, _, _ in FILES)
    setup = (f'<p>Step 1 of {n}. The <code>history</code> app already exists at work: replace its files with the '
             'ones in the next lessons. No models, no migrations, no new packages.</p>\n'
             '<h3>What was wrong</h3>\n'
             '<p>«Удалить выбранные» also ran the auto-cleanup (the view never read which button was pressed), and '
             'the checkbox sent only the file name, so a same-named file in another folder was deleted too. Now the '
             'checkbox sends <code>folder/file</code> and each button does only its own job.</p>\n'
             '<h3>Layout</h3>\n' + code(tree, 'plaintext') +
             '<p>If your templates live in the project-level <code>templates/history/</code> folder, put the three '
             '<code>.html</code> files there instead.</p>\n'
             '<h3>urls.py of the project</h3>\n'
             '<p>Either include the app urls, or keep your own routes and make sure the names match '
             '(<code>history</code> is where cleanup returns; <code>datasets-files</code> is new):</p>\n' +
             code('path("history/", include("history.urls")),\n', 'python') +
             code('sudo systemctl restart gunicorn\n', 'plaintext'))
    out.append('\n' + lesson(1, 'Setup: what changed, layout, urls',
                             'Do this first: what was fixed, the file layout and the url names.', setup))

    for k, (path, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text()
        intro = f'<p>Step {k} of {n}. Save as <code>history/{path}</code>.</p>\n<h3>{path}</h3>\n'
        out.append('\n' + lesson(k, path, summary, intro + code(src, lang)))

    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
