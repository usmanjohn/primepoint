# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_dynamic_report.py from kapital/dynamic_report/.

    python3 kapital/build_dynamic_report_playlist.py

The bank's dynamic portfolio report (Django app `dynamic_report`) reaches the work machine
through the admin-only «Kapital — Dynamic report» playlist: one lesson per file, numbered in the
order to install them. Edit the files in kapital/dynamic_report/, run this script, then import
with --republish. Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'dynamic_report'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_dynamic_report.py'

# (path inside the app, language, what it is) — in install order. Empty __init__.py files are
# listed in lesson 1 instead of getting a lesson each.
FILES = [
    ('models.py', 'python', 'The ReportRun job record: parameters, fingerprint, status, result path.'),
    ('admin.py', 'python', 'Admin registration for ReportRun.'),
    ('apps.py', 'python', 'App config.'),
    ('urls.py', 'python', 'URL names report-page, report-start, report-status, report-view, report-download.'),
    ('views.py', 'python', 'Form page, start (launches the job process), status polling, view/download. Reuses a finished report for identical requests and follows a running one instead of starting it twice.'),
    ('process.py', 'python', 'The engine: reads datasets/dynamics/yearly/*.parquet, builds the panel and marts, renders all 29 charts into one HTML report.'),
    ('templates/dynamic_report/page.html', 'html', 'The report page: form, presets, live status, history table. Russian UI, scoped under .drp.'),
    ('management/commands/build_report.py', 'python', 'Builds one report: started by the page with --run-id, or by hand from the command line.'),
    ('jobs.py', 'python', 'Last so the earlier lesson numbers stay put; install it with views.py. Runs each report as its own process (manage.py build_report --run-id N), one at a time server-wide (file lock), and marks a row failed when its process died (out of memory, restart).'),
]
EMPTY = ['__init__.py', 'management/__init__.py', 'management/commands/__init__.py', 'migrations/__init__.py']

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — Dynamic report playlist (admin only): the bank's loan-portfolio report app, one file per lesson.

GENERATED from kapital/dynamic_report/ by kapital/build_dynamic_report_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_dynamic_report.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — Dynamic report', 'category': 'programming', 'staff_only': True,
            'description': 'The dynamic loan-portfolio report app, one file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(order, name, summary, content):
    return 'TUTORIALS.append(' + repr({'title': f'DR-{order}. {name}', 'category': 'programming',
                                       'order': order, 'summary': summary, 'content': content}) + ')\n'


def main():
    n = len(FILES) + 1
    out = [HEADER]

    tree = 'dynamic_report/\n' + ''.join(f'    {p}\n' for p in EMPTY + [f for f, _, _ in FILES])
    setup = (f'<p>Step 1 of {n}. Create the app folder with this layout. The four <code>__init__.py</code> '
             'files are empty. Then add <code>"dynamic_report"</code> to <code>INSTALLED_APPS</code>, '
             'include its urls, and run the migrations.</p>\n'
             '<p>Data: <code>BASE_DIR / "datasets" / "dynamics" / "yearly"</code> '
             '(<code>history_2023.parquet</code>… then <code>history_10.2026.parquet</code>…). '
             'Reports are written to <code>datasets/dynamics/report</code>.</p>\n'
             '<h3>Layout</h3>\n' + code(tree, 'plaintext') +
             '<h3>urls.py of the project · then the shell</h3>\n' +
             code('path("dynamic_report/", include("dynamic_report.urls")),\n\n'
                  'python manage.py makemigrations dynamic_report\npython manage.py migrate\n', 'python'))
    out.append('\n' + lesson(1, 'Setup: folders, INSTALLED_APPS, migrate',
                             'Do this first: the app layout, settings and migrations.', setup))

    for k, (path, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text()
        intro = f'<p>Step {k} of {n}. Save as <code>dynamic_report/{path}</code>.</p>\n<h3>{path}</h3>\n'
        out.append('\n' + lesson(k, path, summary, intro + code(src, lang)))

    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
