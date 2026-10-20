# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_client_portfolio.py from kapital/client_portfolio/.

    python3 kapital/build_client_portfolio_playlist.py

The client portfolio page (Django app `client_portfolio`) reaches the work machine through the
admin-only «Kapital — Client portfolio» playlist: one lesson per file, numbered in install order.
Edit the files in kapital/client_portfolio/, run this script, then import with --republish.
Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'client_portfolio'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_client_portfolio.py'

# (path inside the app, language, what it is) — in install order.
FILES = [
    ('apps.py', 'python', 'App config.'),
    ('urls.py', 'python', 'URL names client-portfolio and client-portfolio-excel.'),
    ('queries.py', 'python', 'All the SQL: client name, accounts, live deals, account↔deal links, 6-month turnover. Change the get_oracle_connection import line to your path.'),
    ('accounts.py', 'python', 'The CBU chart of accounts as Python dicts: first 5 digits → loan / interest / deposit / off-balance, with status and a Russian label.'),
    ('logic.py', 'python', 'All the calculations: loans by product, deals, credit lines (RNK), deposits, off-balance, turnover, KPIs.'),
    ('excel.py', 'python', 'The same portfolio as an .xlsx file, one sheet per section (openpyxl).'),
    ('views.py', 'python', 'The page (GET form → portfolio) and the Excel download.'),
    ('templates/client_portfolio/page.html', 'html', 'The page: form, header, KPIs, loans, deals, RNK, deposits, off-balance, turnover, all accounts. Bootstrap, no JS except the print button.'),
]
EMPTY = ['__init__.py']

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — Client portfolio playlist (admin only): one client's portfolio on a date, one file per lesson.

GENERATED from kapital/client_portfolio/ by kapital/build_client_portfolio_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_client_portfolio.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — Client portfolio', 'category': 'programming', 'staff_only': True,
            'description': 'Client portfolio by contragent and date: loans, deals, credit lines, deposits, off-balance, turnover. One file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(order, name, summary, content):
    return 'TUTORIALS.append(' + repr({'title': f'CP-{order}. {name}', 'category': 'programming',
                                       'order': order, 'summary': summary, 'content': content}) + ')\n'


def main():
    n = len(FILES) + 1
    out = [HEADER]

    tree = 'client_portfolio/\n' + ''.join(f'    {p}\n' for p in EMPTY + [f for f, _, _ in FILES])
    setup = (f'<p>Step 1 of {n}. Create the app folder with this layout. <code>__init__.py</code> '
             'is empty. Add <code>"client_portfolio"</code> to <code>INSTALLED_APPS</code> and include '
             'its urls. There are no models, so no migrations.</p>\n'
             '<p>Needs <code>oracledb</code> and <code>openpyxl</code> (both already in the project). '
             'In <code>queries.py</code> change the line <code>from main.oracle import get_oracle_connection</code> '
             'to where your function lives. Add a sidebar link to <code>{% url \'client-portfolio\' %}</code> in base.html.</p>\n'
             '<h3>Layout</h3>\n' + code(tree, 'plaintext') +
             '<h3>urls.py of the project</h3>\n' +
             code('path("client_portfolio/", include("client_portfolio.urls")),\n', 'python'))
    out.append('\n' + lesson(1, 'Setup: folders, INSTALLED_APPS, urls',
                             'Do this first: the app layout and settings.', setup))

    for k, (path, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text()
        intro = f'<p>Step {k} of {n}. Save as <code>client_portfolio/{path}</code>.</p>\n<h3>{path}</h3>\n'
        out.append('\n' + lesson(k, path, summary, intro + code(src, lang)))

    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
