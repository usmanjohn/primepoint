# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_converter.py from kapital/converter/.

    python3 kapital/build_converter_playlist.py

The PDF converter (Django app `converter`) reaches the work machine through the admin-only
«Kapital — PDF converter» playlist: one lesson per file, numbered in install order.
Edit the files in kapital/converter/, run this script, then import with --republish.
Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'converter'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_converter.py'

# (path inside the app, language, what it is) — in install order.
FILES = [
    ('apps.py', 'python', 'App config.'),
    ('urls.py', 'python', 'URL names converter and converter-run.'),
    ('pdftools.py', 'python', 'The tools: merge, pages (pick/reorder/delete), split to ZIP, rotate, PDF to Word, PDF to Excel. Bytes in, bytes out, nothing saved.'),
    ('views.py', 'python', 'The page and run(): checks the upload, calls the tool, returns the file as a download or shows the error in the tool card.'),
    ('templates/converter/page.html', 'html', 'One card per tool, each its own form. Bootstrap, no JavaScript. Russian UI.'),
]
EMPTY = ['__init__.py']

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — PDF converter playlist (admin only): merge, split, reorder, rotate, PDF to Word/Excel; one file per lesson.

GENERATED from kapital/converter/ by kapital/build_converter_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_converter.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — PDF converter', 'category': 'programming', 'staff_only': True,
            'description': 'PDF tools for colleagues without access to online converters. One file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


RENAMED = {}


def lesson(order, name, summary, content):
    d = {'title': f'PDF-{order}. {name}', 'category': 'programming',
         'order': order, 'summary': summary, 'content': content}
    if name in RENAMED:
        d['renamed_from'] = RENAMED[name]
    return 'TUTORIALS.append(' + repr(d) + ')\n'


def main():
    n = len(FILES) + 1
    out = [HEADER]

    tree = 'converter/\n' + ''.join(f'    {p}\n' for p in EMPTY + [f for f, _, _ in FILES])
    setup = (f'<p>Step 1 of {n}. Create the app folder with this layout. <code>__init__.py</code> is empty. '
             'Add <code>"converter"</code> to <code>INSTALLED_APPS</code> and include its urls. No models, no migrations: '
             'files are processed in memory and sent straight back, nothing is saved.</p>\n'
             '<p>Packages (one per tool; a tool whose package is missing switches itself off, the rest keep working):</p>\n'
             + code('pip install pypdf          # merge, pages, split, rotate\n'
                    'pip install pdfplumber     # PDF -> Excel (openpyxl is already there)\n'
                    'pip install pdf2docx       # PDF -> Word (pulls in PyMuPDF, numpy, opencv-python-headless)\n'
                    'sudo systemctl restart gunicorn\n', 'plaintext') +
             '<p>Add a sidebar link to <code>{% url \'converter\' %}</code> in base.html. If nginx limits uploads, '
             'raise <code>client_max_body_size 50M;</code>.</p>\n'
             '<h3>Layout</h3>\n' + code(tree, 'plaintext') +
             '<h3>urls.py of the project</h3>\n' +
             code('path("converter/", include("converter.urls")),\n', 'python'))
    out.append('\n' + lesson(1, 'Setup: folders, packages, urls',
                             'Do this first: the app layout, pip packages, settings and urls.', setup))

    for k, (path, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text()
        intro = f'<p>Step {k} of {n}. Save as <code>converter/{path}</code>.</p>\n<h3>{path}</h3>\n'
        out.append('\n' + lesson(k, path, summary, intro + code(src, lang)))

    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
