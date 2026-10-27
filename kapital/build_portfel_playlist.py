# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_portfel_auto.py from kapital/portfel/.

    python3 kapital/build_portfel_playlist.py

The daily automatic portfel build reaches the work machine through the admin-only
«Kapital — Portfel auto» playlist: one lesson per file, numbered in install order.
Only the NEW files are here — view.py and process.py are already on the server and do not change.
Edit the files in kapital/portfel/, run this script, then import with --republish.
Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'portfel'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_portfel_auto.py'

# (path inside kapital/portfel, where it goes on the server, language, what it is) — in install order.
FILES = [
    ('daily.py', 'portfel/daily.py', 'python',
     'The same steps as portfel_get + portfel_process, but without a user: query → raw → all + svod. Writes .tmp first, svod last.'),
    ('management/commands/build_portfel.py', 'portfel/management/commands/build_portfel.py', 'python',
     'The command: previous working day (Monday → Friday); already built → nothing; database not updated → fails, the next run tries again.'),
    ('server/portfel.service', '/etc/systemd/system/portfel.service', 'ini',
     'What the timer runs. Copy User= and Environment lines from gunicorn.service.'),
    ('server/portfel.timer', '/etc/systemd/system/portfel.timer', 'ini',
     'When: working days at 08, 09, 10, 12 and 14 Tashkent time. After 14:00 nobody tries again.'),
]

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — Portfel auto playlist (admin only): the portfel builds itself every working morning.

GENERATED from kapital/portfel/ by kapital/build_portfel_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_portfel_auto.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — Portfel auto', 'category': 'programming', 'staff_only': True,
            'description': 'The portfel for the previous working day is built by itself at 08, 09, 10, 12 and 14 — no Redis, no RabbitMQ, just a systemd timer and a Django command. One file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(order, name, summary, content):
    d = {'title': f'PFA-{order}. {name}', 'category': 'programming',
         'order': order, 'summary': summary, 'content': content}
    return 'TUTORIALS.append(' + repr(d) + ')\n'


def main():
    n = len(FILES) + 2
    out = [HEADER]

    tree = ('portfel/\n    daily.py            ← new\n    management/\n        __init__.py     ← empty\n'
            '        commands/\n            __init__.py ← empty\n            build_portfel.py\n')
    setup = (f'<p>Step 1 of {n}. Your <code>view.py</code> and <code>process.py</code> stay as they are. '
             'Add these new files to the portfel app. The two <code>__init__.py</code> files are empty — '
             'without them Django does not see the command.</p>\n'
             '<h3>Layout</h3>\n' + code(tree, 'plaintext') +
             '<p>The two systemd files (steps 4 and 5) do not go into the project: they go to '
             '<code>/etc/systemd/system/</code>.</p>\n'
             '<h3>How it behaves</h3>\n<ul>\n'
             '<li><b>08:00</b> — builds the previous working day (on Monday: Friday).</li>\n'
             '<li>The database returned 0 rows (not updated yet) → the run fails, nothing is saved, '
             '<b>09:00, 10:00, 12:00, 14:00</b> try again.</li>\n'
             '<li>After a success the later runs only print «already done».</li>\n'
             '<li>Still nothing at 14:00 → «last try for today — giving up». That day has no portfel.</li>\n'
             '<li>Raw file saved but processing failed → the next run only processes, no second query.</li>\n'
             '<li>Saturday and Sunday: no runs.</li>\n</ul>\n')
    out.append('\n' + lesson(1, 'Setup: what goes where', 'Do this first: the new files and how it behaves.', setup))

    for k, (path, dest, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text()
        intro = f'<p>Step {k} of {n}. Save as <code>{dest}</code>.</p>\n<h3>{pathlib.Path(path).name}</h3>\n'
        out.append('\n' + lesson(k, pathlib.Path(path).name, summary, intro + code(src, lang)))

    turn_on = (f'<p>Step {n} of {n}. First a test by hand, on a date you know has data:</p>\n' +
               code('cd /var/www/dashboard/dashboard && source ../delta/bin/activate\n'
                    'python manage.py build_portfel --date 2026-10-23\n', 'bash') +
               '<p>Then switch the timer on:</p>\n' +
               code('sudo systemctl daemon-reload\n'
                    'sudo systemctl enable --now portfel.timer\n'
                    'systemctl list-timers | grep portfel     # when the next try is\n'
                    'journalctl -u portfel -n 50              # what the tries printed\n'
                    'sudo systemctl start portfel.service     # one try right now\n', 'bash') +
               '<p>After changing either systemd file: <code>sudo systemctl daemon-reload</code> again. '
               'After <code>git pull</code> nothing else is needed — the next run uses the new code '
               '(no gunicorn restart for the timer).</p>\n'
               '<p>⚠️ «Not updated yet» means the query returned 0 rows. If the database can be '
               '<i>half</i> loaded at 08:00, that half day is saved and not retried — then it needs a '
               'better «is the load finished?» check.</p>\n')
    out.append('\n' + lesson(n, 'Turn it on', 'Test by hand, enable the timer, read its log.', turn_on))

    OUT.write_text(''.join(out))
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
