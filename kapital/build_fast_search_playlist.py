# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_fast_search.py from kapital/fast_search/.

    python3 kapital/build_fast_search_playlist.py

Fast search (Django app `fast_search`) reaches the work machine through the admin-only
«Kapital — Fast search» playlist: one lesson per file, numbered in install order.
Edit the files in kapital/fast_search/, run this script, then import with --republish.
Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'fast_search'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_fast_search.py'

# (path inside the app, language, what it is) — in install order.
FILES = [
    ('apps.py', 'python', 'App config.'),
    ('urls.py', 'python', 'Two pages: the list of reports and one report.'),
    ('reports.py', 'python', 'The engine: reads the .sql files, finds the :parameters, makes the form, runs the query, shows the result. The usual parameters and their labels are in FIELDS at the top.'),
    ('process.py', 'python', 'Optional Python per report: a function with the same name as the .sql file.'),
    ('views.py', 'python', 'The views: the form (GET), the result, the Excel download.'),
    ('templates/fast_search/style.html', 'html', 'The look (Kapitalbank colours), shared by both pages.'),
    ('templates/fast_search/index.html', 'html', 'Every report as a card.'),
    ('templates/fast_search/report.html', 'html', 'One report: the form, the result table, Excel, the SQL.'),
    ('sql/client_deals.sql', 'sql', 'Example report: a client\'s deals on an archive date, branch optional.'),
    ('sql/deals_period.sql', 'sql', 'Example report: deals opened between two dates, with extra Python in process.py.'),
]
EMPTY = ['__init__.py']

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — Fast search playlist (admin only): one .sql file = one report with a form and Excel, one file per lesson.

GENERATED from kapital/fast_search/ by kapital/build_fast_search_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_fast_search.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — Fast search', 'category': 'programming', 'staff_only': True,
            'description': 'Put a .sql file in a folder and it becomes a page: the form is made from its :parameters, the result is shown and downloads as Excel. Nothing is saved. One file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(order, name, summary, content):
    d = {'title': f'FS-{order}. {name}', 'category': 'programming',
         'order': order, 'summary': summary, 'content': content}
    return 'TUTORIALS.append(' + repr(d) + ')\n'


def main():
    n = len(FILES) + 1
    out = [HEADER]

    tree = 'fast_search/\n' + ''.join(f'    {p}\n' for p in EMPTY + [f for f, _, _ in FILES])
    setup = (f'<p>Step 1 of {n}. Create the app folder with this layout. <code>__init__.py</code> '
             'is empty. Add <code>"fast_search"</code> to <code>INSTALLED_APPS</code> and include '
             'its urls. There are no models, so no migrations, and nothing is ever saved.</p>\n'
             '<p>Needs <code>oracledb</code>, <code>pandas</code> and <code>openpyxl</code> (Excel). '
             'In <code>reports.py</code> check the line '
             '<code>from main.oracle import get_oracle_connection</code>.</p>\n'
             '<h3>How to add a report</h3>\n'
             '<p>Put a <code>.sql</code> file in <code>fast_search/sql/</code>. The first comment line is '
             'the title, the next comment lines the description. Every <code>:parameter</code> in the SQL '
             'becomes a field of the form by itself; the ones you do not use are simply not there. '
             'An optional parameter: <code>(:siteid is null or d.siteid = :siteid)</code>. '
             'Russian column names: <code>as "Сумма"</code>. Extra Python: a function with the file\'s '
             'name in <code>process.py</code>.</p>\n'
             + code('-- Сделки клиента\n-- Все сделки контрагента на дату архива.\n'
                    'select d.id as "ID сделки", d.amounteq / 100 as "Сумма"\n'
                    'from   schema2.deal d\nwhere  d.contragentid = :contragentid\n'
                    '  and  trunc(d.arcdate) = :arcdate\n', 'sql') +
             '<p>Sidebar link in base.html: <code>{% url \'fast-search\' %}</code>, icon '
             '<code>fa-solid fa-magnifying-glass-chart</code>.</p>\n'
             '<h3>Layout</h3>\n' + code(tree, 'plaintext') +
             '<h3>urls.py of the project</h3>\n' +
             code('path("fast-search/", include("fast_search.urls")),\n', 'python'))
    out.append('\n' + lesson(1, 'Setup: folders, INSTALLED_APPS, urls, how to add a report',
                             'Do this first: the app layout, settings, and how a .sql file becomes a page.', setup))

    for k, (path, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text()
        intro = f'<p>Step {k} of {n}. Save as <code>fast_search/{path}</code>.</p>\n<h3>{path}</h3>\n'
        out.append('\n' + lesson(k, path, summary, intro + code(src, lang)))

    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
