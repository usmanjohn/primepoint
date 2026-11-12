# -*- coding: utf-8 -*-
"""Regenerate tutorial/management/commands/_tutorials_code_branchmap.py from kapital/branchmap/.

    python3 kapital/build_branchmap_playlist.py

The branch map (Django app `branchmap`) reaches the work machine through the admin-only
«Kapital — Branch map» playlist: one lesson per file, numbered in install order.
Edit the files in kapital/branchmap/, run this script, then import with --republish.
Never edit the generated file by hand.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
APP = ROOT / 'kapital' / 'branchmap'
OUT = ROOT / 'tutorial' / 'management' / 'commands' / '_tutorials_code_branchmap.py'

# (path inside the app, language, what it is) — in install order.
FILES = [
    ('apps.py', 'python', 'App config.'),
    ('urls.py', 'python', 'One page: the map.'),
    ('geo.py', 'python', 'Everything about the map: reads the two data files, projects lon/lat to x/y, finds each office\'s region, places the labels (inside the region, or beside it with a leader line), counts per region.'),
    ('views.py', 'python', 'The view: builds the map once per worker and hands it to the template.'),
    ('templates/branchmap/page.html', 'html', 'The page: KPIs, the SVG map with its shadow, the Tashkent inset, the table by region. No JavaScript.'),
    ('data/offices.json', 'json', 'The 90 offices from kapitalbank.uz «Отделения» (2026-11-10): name, address, city, lat, lon. No ATMs.'),
    ('data/regions.geojson', 'json', 'The 14 regions (geoBoundaries / OpenStreetMap, ODbL 1.0), simplified. One long line: copy all of it.'),
]
EMPTY = ['__init__.py']

HEADER = '''# -*- coding: utf-8 -*-
"""Kapital — Branch map playlist (admin only): Kapitalbank's offices on the map of Uzbekistan, one file per lesson.

GENERATED from kapital/branchmap/ by kapital/build_branchmap_playlist.py — edit the files, then regenerate; do not edit by hand.

Import:
    python manage.py import_tutorials tutorial/management/commands/_tutorials_code_branchmap.py --author=prime
"""

PLAYLIST = {'title': 'Kapital — Branch map', 'category': 'programming', 'staff_only': True,
            'description': 'The 90 Kapitalbank offices (филиалы, ЦБУ, ОБУ, мини-банки) on a map of Uzbekistan drawn as SVG in Python: no JavaScript, no map tiles, works on a closed network. The base for portfolio maps. One file per lesson in install order. Admin only.'}

TUTORIALS = []
'''


def code(src, lang):
    return f'<pre><code class="language-{lang}">' + html.escape(src, quote=False) + '</code></pre>\n'


def lesson(order, name, summary, content):
    d = {'title': f'BM-{order}. {name}', 'category': 'programming',
         'order': order, 'summary': summary, 'content': content}
    return 'TUTORIALS.append(' + repr(d) + ')\n'


def main():
    n = len(FILES) + 1
    out = [HEADER]

    tree = 'branchmap/\n' + ''.join(f'    {p}\n' for p in EMPTY + [f for f, _, _ in FILES])
    setup = (f'<p>Step 1 of {n}. Create the app folder with this layout. <code>__init__.py</code> '
             'is empty. Add <code>"branchmap"</code> to <code>INSTALLED_APPS</code> and include its urls. '
             'There are no models, so no migrations. No new packages either: only Python and Django.</p>\n'
             '<p>The map needs no internet: the regions and the offices are two files in '
             '<code>branchmap/data/</code>, and the page is plain SVG.</p>\n'
             '<p>Sidebar link in base.html: <code>{% url \'branchmap\' %}</code>, icon '
             '<code>fa-solid fa-map-location-dot</code>.</p>\n'
             '<h3>Layout</h3>\n' + code(tree, 'plaintext') +
             '<h3>urls.py of the project</h3>\n' +
             code('path("branch-map/", include("branchmap.urls")),\n', 'python') +
             '<h3>Later: the portfolio on the map</h3>\n'
             '<p>Every office already knows its region (<code>geo.offices()</code> → '
             '<code>region</code> = UZ-AN, UZ-TK …, the same codes as the old map\'s UZAN). '
             'A portfolio by region or by МФО can be joined to that.</p>\n')
    out.append('\n' + lesson(1, 'Setup: folders, INSTALLED_APPS, urls',
                             'Do this first: the app layout and settings.', setup))

    for k, (path, lang, summary) in enumerate(FILES, start=2):
        src = (APP / path).read_text(encoding='utf-8')
        intro = f'<p>Step {k} of {n}. Save as <code>branchmap/{path}</code>.</p>\n<h3>{path}</h3>\n'
        out.append('\n' + lesson(k, path, summary, intro + code(src, lang)))

    OUT.write_text(''.join(out), encoding='utf-8')
    print('wrote', OUT.relative_to(ROOT), f'({n} numbered lessons)')


if __name__ == '__main__':
    main()
