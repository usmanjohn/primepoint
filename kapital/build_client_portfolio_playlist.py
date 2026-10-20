# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_client_portfolio.py from kapital/cprofile/.

    python3 kapital/build_client_portfolio_playlist.py

The client portfolio page (Django app `cprofile`) reaches the work machine through the
admin-only «Kapital — Client portfolio» playlist: one lesson per file, numbered in install order.
Edit the files in kapital/cprofile/, run this script, then import with --republish.
Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'cprofile'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_client_portfolio.py'

# (path inside the app, language, what it is) — in install order.
FILES = [
    ('apps.py', 'python', 'App config.'),
    ('urls.py', 'python', 'URL names client-portfolio and client-portfolio-excel.'),
    ('queries.py', 'python', 'All the SQL: client name, accounts, ACTIVE deals, account↔deal links, 6-month turnover, overdue history (dealfact). Change the get_oracle_connection import line to your path.'),
    ('accounts.py', 'python', 'The CBU chart of accounts as Python dicts: first 5 digits → loan / interest / deposit / off-balance, with status and a Russian label.'),
    ('logic.py', 'python', 'All the calculations: loans by product, active deals, credit lines (RNK), deposits, off-balance, turnover, overdue days per month, KPIs.'),
    ('excel.py', 'python', 'The same portfolio as an .xlsx file, one sheet per section (openpyxl).'),
    ('views.py', 'python', 'The page (GET form → portfolio) and the Excel download.'),
    ('templates/cprofile/page.html', 'html', 'The page: form, header, KPIs, loans, deals, RNK, deposits, off-balance, turnover, all accounts. Bootstrap, no JS except the print button.'),
]
EMPTY = ['__init__.py']

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — Client portfolio playlist (admin only): one client's portfolio on a date, one file per lesson.

GENERATED from kapital/cprofile/ by kapital/build_client_portfolio_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_client_portfolio.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — Client portfolio', 'category': 'programming', 'staff_only': True,
            'description': 'Client portfolio by contragent and date: loans, deals, credit lines, deposits, off-balance, turnover. One file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


# Lessons whose title changed: the importer matches on title, so it renames these in place.
RENAMED = {'templates/cprofile/page.html': ['CP-9. templates/client_portfolio/page.html']}


def lesson(order, name, summary, content):
    d = {'title': f'CP-{order}. {name}', 'category': 'programming',
         'order': order, 'summary': summary, 'content': content}
    if name in RENAMED:
        d['renamed_from'] = RENAMED[name]
    return 'TUTORIALS.append(' + repr(d) + ')\n'


def main():
    n = len(FILES) + 1
    out = [HEADER]

    tree = 'cprofile/\n' + ''.join(f'    {p}\n' for p in EMPTY + [f for f, _, _ in FILES])
    setup = (f'<p>Step 1 of {n}. Create the app folder with this layout. <code>__init__.py</code> '
             'is empty. Add <code>"cprofile"</code> to <code>INSTALLED_APPS</code> and include '
             'its urls. There are no models, so no migrations.</p>\n'
             '<p>Needs <code>oracledb</code> and <code>openpyxl</code> (both already in the project). '
             'In <code>queries.py</code> change the line <code>from main.oracle import get_oracle_connection</code> '
             'to where your function lives. Add a sidebar link to <code>{% url \'client-portfolio\' %}</code> in base.html.</p>\n'
             '<h3>Layout</h3>\n' + code(tree, 'plaintext') +
             '<h3>urls.py of the project</h3>\n' +
             code('path("cprofile/", include("cprofile.urls")),\n', 'python'))
    out.append('\n' + lesson(1, 'Setup: folders, INSTALLED_APPS, urls',
                             'Do this first: the app layout and settings.', setup))

    for k, (path, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text()
        intro = f'<p>Step {k} of {n}. Save as <code>cprofile/{path}</code>.</p>\n<h3>{path}</h3>\n'
        out.append('\n' + lesson(k, path, summary, intro + code(src, lang)))

    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
