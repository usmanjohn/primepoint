# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_vintage.py from kapital/vintage/.

    python3 kapital/build_vintage_playlist.py

The vintage analysis (Django app `vintage`) reaches the work machine through the admin-only
«Kapital — Vintage» playlist: one lesson per file, numbered in install order.
Edit the files in kapital/vintage/, run this script, then import with --republish.
Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'vintage'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_vintage.py'

# (path inside the app, language, what it is) — in install order.
FILES = [
    ('apps.py', 'python', 'App config.'),
    ('urls.py', 'python', 'The pages: the analysis, «Пересчитать», Excel, the business plan.'),
    ('process.py', 'python', 'Everything: settings at the top (your column names, NPL ≥ 3, 90+), the build (polars), the triangles, the projection, the insights, the plan, Excel.'),
    ('fake.py', 'python', 'Fake data in the bank\'s shape (a bad 2024 and a bad December are planted), to see the pages before the real file is there.'),
    ('management/commands/build_vintage.py', 'python', 'The command that does the heavy work in its own process: python manage.py build_vintage (--fake for fake data).'),
    ('views.py', 'python', 'The views: the page, the button that starts the command, Excel, the plan form.'),
    ('templates/vintage/style.html', 'html', 'The look (Kapitalbank colours), shared by both pages.'),
    ('templates/vintage/page.html', 'html', 'The analysis: insights, curves, the triangle, transitions, early signal, issue month, «how to read».'),
    ('templates/vintage/plan.html', 'html', 'The business plan: expected new 90+ / NPL per month, and the second route (transitions).'),
]
EMPTY = ['__init__.py', 'management/__init__.py', 'management/commands/__init__.py']

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — Vintage playlist (admin only): vintage analysis of the loan portfolio, one file per lesson.

GENERATED from kapital/vintage/ by kapital/build_vintage_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_vintage.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — Vintage', 'category': 'programming', 'staff_only': True,
            'description': 'Vintage analysis: loans grouped by issue month, followed month by month — overdue 30+/60+/90+ and NPL (category ≥ 3), the triangle, curves, transitions, an early signal and a 12-month business plan. One file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(order, name, summary, content):
    d = {'title': f'VIN-{order}. {name}', 'category': 'programming',
         'order': order, 'summary': summary, 'content': content}
    return 'TUTORIALS.append(' + repr(d) + ')\n'


def main():
    n = len(FILES) + 1
    out = [HEADER]
    tree = 'vintage/\n' + ''.join(f'    {p}\n' for p in EMPTY + [f for f, _, _ in FILES])
    setup = (f'<p>Step 1 of {n}. Create the app folder with this layout. The three <code>__init__.py</code> '
             'files are empty. Add <code>"vintage"</code> to <code>INSTALLED_APPS</code> and include its urls. '
             'There are no models, so no migrations.</p>\n'
             '<p>Needs <code>polars</code>, <code>numpy</code> and <code>openpyxl</code> (Excel). '
             'Put your parquet file(s) into <code>BASE_DIR/datasets/vintage/input/</code> — every <code>*.parquet</code> '
             'there is read. Columns: <code>date</code> (1st of the month = the previous month), <code>anketa</code>, '
             '<code>issue_date</code>, <code>maks_dni</code>, <code>npl_category</code>, <code>portfel_amount</code>. '
             'If yours are named differently, change the right-hand side of <code>COLUMNS</code> at the top of '
             '<code>process.py</code>.</p>\n'
             '<p>Then press «Пересчитать» on <code>/vintage/</code> (it runs the command in its own process, the page '
             'refreshes itself), or run it by hand:</p>\n' +
             code('python manage.py build_vintage          # your files\n'
                  'python manage.py build_vintage --fake   # fake data first, only if the folder is empty\n', 'bash') +
             '<p>Try <code>--fake</code> first to see every page; then delete <code>fake.parquet</code> and put the real file in.</p>\n'
             '<p>Sidebar link in base.html: <code>{% url \'vintage\' %}</code>, icon <code>fa-solid fa-layer-group</code>.</p>\n'
             '<h3>Layout</h3>\n' + code(tree, 'plaintext') +
             '<h3>urls.py of the project</h3>\n' +
             code('path("vintage/", include("vintage.urls")),\n', 'python'))
    out.append('\n' + lesson(1, 'Setup: folders, INSTALLED_APPS, urls, the data',
                             'Do this first: the app layout, settings and where the data goes.', setup))
    for k, (path, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text()
        intro = f'<p>Step {k} of {n}. Save as <code>vintage/{path}</code>.</p>\n<h3>{path}</h3>\n'
        out.append('\n' + lesson(k, path, summary, intro + code(src, lang)))
    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
