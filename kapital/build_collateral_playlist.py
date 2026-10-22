# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_collateral.py from kapital/collateral/.

    python3 kapital/build_collateral_playlist.py

The collateral drill-down (Django app `collateral`) reaches the work machine through the
admin-only «Kapital — Collateral» playlist: one lesson per file, numbered in install order.
Edit the files in kapital/collateral/, run this script, then import with --republish.
Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'collateral'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_collateral.py'

# (path inside the app, language, what it is) — in install order.
FILES = [
    ('apps.py', 'python', 'App config.'),
    ('urls.py', 'python', 'Five pages: the drill-down, one deal, Excel, the parquet file, parameters + SQL.'),
    ('forms.py', 'python', 'The date form (and the «load again from the database» tick).'),
    ('queries.py', 'python', 'All the SQL. The three old scripts (avto / nedvijimost / others) as three parameter dicts and ONE skeleton. Change the import line, the three table names and ON_DATE.'),
    ('process.py', 'python', 'Oracle → parquet in datasets/collateral/ → clean pandas table → cards, KPIs, data checks. All the settings (buckets, codes, cards) are at the top.'),
    ('views.py', 'python', 'The views: each reads the address, asks process.py, renders a template.'),
    ('templates/collateral/style.html', 'html', 'The look (Kapitalbank colours), shared by all pages.'),
    ('templates/collateral/card.html', 'html', 'One breakdown card: rows are links that add a filter.'),
    ('templates/collateral/page.html', 'html', 'The main page: date form, header with breadcrumbs, KPIs, the three tiles, the cards, data checks, the deals list.'),
    ('templates/collateral/deal.html', 'html', 'One collateral deal with every filled field.'),
    ('templates/collateral/params.html', 'html', 'Every parameter name in the database on a date + the finished SQL to copy.'),
]
EMPTY = ['__init__.py']

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — Collateral playlist (admin only): the bank's collateral as a drill-down, one file per lesson.

GENERATED from kapital/collateral/ by kapital/build_collateral_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_collateral.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — Collateral', 'category': 'programming', 'staff_only': True,
            'description': 'Collateral of the bank on a date: cars, property, others (equipment, deposits, insurance ...), drill-down with no JavaScript, saved as parquet. One file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(order, name, summary, content):
    d = {'title': f'COL-{order}. {name}', 'category': 'programming',
         'order': order, 'summary': summary, 'content': content}
    return 'TUTORIALS.append(' + repr(d) + ')\n'


def main():
    n = len(FILES) + 1
    out = [HEADER]

    tree = 'collateral/\n' + ''.join(f'    {p}\n' for p in EMPTY + [f for f, _, _ in FILES])
    setup = (f'<p>Step 1 of {n}. Create the app folder with this layout. <code>__init__.py</code> '
             'is empty. Add <code>"collateral"</code> to <code>INSTALLED_APPS</code> and include '
             'its urls. There are no models, so no migrations.</p>\n'
             '<p>Needs <code>oracledb</code>, <code>pandas</code>, <code>pyarrow</code> (parquet) and '
             '<code>openpyxl</code> (Excel). The folder <code>BASE_DIR/datasets/collateral/</code> is '
             'created by itself on the first download.</p>\n'
             '<p>In <code>queries.py</code> change three things: the line '
             '<code>from main.oracle import get_oracle_connection</code>, the three table names '
             '(<code>DEAL_TABLE</code>, <code>PARAM_TABLE</code>, <code>PARENT_TABLE</code>) and, if your '
             'tables have no <code>date_from</code>, the <code>ON_DATE</code> line. Then open '
             '<code>/collateral/params/</code>: it lists every parameter in the database, so you can find '
             'the address field and add it to <code>PROPERTY</code>.</p>\n'
             '<p>Sidebar link in base.html: <code>{% url \'collateral\' %}</code>, icon '
             '<code>fa-solid fa-shield-halved</code>.</p>\n'
             '<h3>Layout</h3>\n' + code(tree, 'plaintext') +
             '<h3>urls.py of the project</h3>\n' +
             code('path("collateral/", include("collateral.urls")),\n', 'python'))
    out.append('\n' + lesson(1, 'Setup: folders, INSTALLED_APPS, urls',
                             'Do this first: the app layout and settings.', setup))

    for k, (path, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text()
        intro = f'<p>Step {k} of {n}. Save as <code>collateral/{path}</code>.</p>\n<h3>{path}</h3>\n'
        out.append('\n' + lesson(k, path, summary, intro + code(src, lang)))

    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
