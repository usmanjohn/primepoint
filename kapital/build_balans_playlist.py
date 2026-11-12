# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_balans.py from kapital/balans/.

    python3 kapital/build_balans_playlist.py

The analytic balance sheet (Django app `balans`) reaches the work machine through the admin-only
«Kapital — Balans» playlist: one lesson per file, numbered in install order.
Edit the files in kapital/balans/, run this script, then import with --republish.
Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'balans'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_balans.py'

# (path inside the app, language, what it is) — in install order.
FILES = [
    ('functions.py', 'python',
     'ALL the maths and every rule you may want to change: what is excluded (161, 175 / 222, 23416), '
     'which accounts form each group, the official contra-account list, the ratios.'),
    ('views.py', 'python', 'The three pages: choose a date, load it from Oracle, show the report.'),
    ('urls.py', 'python', 'The same three addresses as before.'),
    ('forms.py', 'python', 'The date field — now opens on the last working day.'),
    ('templates/balans/home.html', 'html', 'Choose a date.'),
    ('templates/balans/result.html', 'html',
     'The report: the balance check, structure bars, assets / liabilities / equity, ratios, '
     'how the profit is made, currencies, largest accounts, how it is calculated.'),
]

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — Balans playlist (admin only): the analytic balance sheet, one file per lesson.

GENERATED from kapital/balans/ by kapital/build_balans_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_balans.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — Balans', 'category': 'programming', 'staff_only': True,
            'description': 'The analytic balance sheet: assets without 161/175, liabilities without 222/23416, a check that the balance adds up, structure, ratios, how the profit is made. Replaces the files of the app that already runs. One file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(order, name, summary, content):
    d = {'title': f'BAL-{order}. {name}', 'category': 'programming',
         'order': order, 'summary': summary, 'content': content}
    return 'TUTORIALS.append(' + repr(d) + ')\n'


def main():
    n = len(FILES) + 1
    out = [HEADER]
    setup = (f'<p>Step 1 of {n}. The app <code>balans</code> already runs on the server, so this is a '
             '<strong>replacement</strong>: overwrite the files below one by one. Nothing else changes — '
             '<code>queries.py</code> (your SQL) stays as it is, the addresses and the saved parquet files too. '
             'No migrations.</p>\n'
             '<p>The templates go to <code>balans/templates/balans/</code>, the same place as '
             '<code>home.html</code> and <code>result.html</code> now. <code>functions.py</code> no longer has '
             '<code>categorize_account</code>; <code>views.py</code> uses <code>build_report</code> instead.</p>\n'
             '<p>Files already saved keep working: <code>balans_get</code> added the profit of the year to 31206 '
             'before, and still does. One fix there: the profit is now added to <strong>one</strong> 31206 row — '
             'before, a 31206 row in two currencies got the profit twice.</p>\n'
             '<p>To change a rule later, open <code>functions.py</code>: the top half is plain lists '
             '(<code>EXCLUDE</code>, <code>PAIRS</code>, <code>ASSET_GROUPS</code> …). The page reloads them, '
             'no other file needs to know.</p>\n'
             '<h3>Layout</h3>\n' +
             code('balans/\n    functions.py\n    views.py\n    urls.py\n    forms.py\n    queries.py      (yours, unchanged)\n'
                  '    templates/balans/home.html\n    templates/balans/result.html\n', 'plaintext'))
    out.append('\n' + lesson(1, 'Setup: what to replace',
                             'Do this first: which files change and which stay.', setup))
    for k, (path, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text()
        intro = f'<p>Step {k} of {n}. Save as <code>balans/{path}</code> (replace the old one).</p>\n<h3>{path}</h3>\n'
        out.append('\n' + lesson(k, path, summary, intro + code(src, lang)))
    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
