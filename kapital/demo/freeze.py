"""Freeze the demo into plain files, so Powerty can serve it without running it.

    cd kapital/demo
    python make_fake_svod.py datasets/portfel/svod --months 6
    python freeze.py ../../prime/demo_dashboard \
        --static-dir ../../static/demo_dashboard --static-url /static/demo_dashboard/

Renders every page with Django's test client (one pass per month: the calendar
POST stores the date in the session, exactly as a visitor would), rewrites the
links between pages to relative ones, and copies the static files next to them:

    index.html                 home ("Финансовая Панель")
    calendar.html              the month picker
    internal.html              "only in the internal version"
    <date>/total.html, all.html, kk.html, rk.html, mk.html, portfel.xlsx
    static/...                 styles.css, dashboard.css, scripts.js, plotly.min.js
                               (or --static-dir/--static-url: let the host's WhiteNoise
                               serve them compressed and cached — plotly is 4.8 MB)
"""
import argparse
import os
import re
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
os.environ['DJANGO_SETTINGS_MODULE'] = 'demo_site.settings'
os.environ['DJANGO_ALLOWED_HOSTS'] = 'testserver'
os.environ['DJANGO_DEBUG'] = '0'

import django  # noqa: E402

django.setup()
from django.test import Client  # noqa: E402

DEPTS = ['total', 'all', 'kk', 'rk', 'mk']
ABOUT_ME = '/about/me/'


def rewrite(html, depth, month, static_url=None):
    """Absolute demo links → relative file links. depth = 0 at the root, 1 in a month folder."""
    up = '../' * depth

    def href(m):
        attr, url = m.group(1), m.group(2)
        r = re.fullmatch(r'/portfel/result/(\w+)/', url)
        if r:
            return f'{attr}="{up}{month}/{r.group(1)}.html"'
        if url == '/':
            return f'{attr}="{up}index.html"'
        if url == '/portfel/':
            return f'{attr}="{up}calendar.html"'
        if url == '/portfel/download/':
            return f'{attr}="{up}{month}/portfel.xlsx"'
        if url.startswith(('/internal/', '/members/')):
            return f'{attr}="{up}internal.html"'
        if url.startswith('/static/'):
            rest = url[len('/static/'):]
            return f'{attr}="{static_url}{rest}"' if static_url else f'{attr}="{up}static/{rest}"'
        return m.group(0)

    html = re.sub(r'\b(href|src)="(/[^"]*)"', href, html)
    # a way back to the author's page, inside the yellow banner
    html = html.replace(
        '<em>Demo on synthetic data — every number is invented.</em>',
        '<em>Demo on synthetic data — every number is invented.</em> '
        f'· <a href="{ABOUT_ME}" class="alert-link">← Usmanjon Abduraimov</a>', 1)
    return html


def calendar_page(html, months):
    """The date form cannot POST to static files: offer the frozen months as buttons."""
    buttons = '\n'.join(
        f'<a class="btn btn-outline-primary m-1" href="{m}/total.html">{m}</a>'
        for m in reversed(months))
    block = ('<div class="text-center">'
             '<p class="text-muted mb-3">В демо доступны отчёты на 1-е число месяца:</p>'
             f'{buttons}</div>')
    new, n = re.subn(r'<form action="" method="post".*?</form>', block, html, count=1, flags=re.S)
    assert n == 1, 'calendar form not found'
    return new


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('out')
    ap.add_argument('--static-dir', help='copy css/js here instead of OUT/static')
    ap.add_argument('--static-url', help='the URL that --static-dir is served at')
    a = ap.parse_args()
    assert bool(a.static_dir) == bool(a.static_url), 'give both --static-dir and --static-url'
    out = Path(a.out).resolve()
    static_out = Path(a.static_dir).resolve() if a.static_dir else out / 'static'
    su = a.static_url
    svod = HERE / 'datasets' / 'portfel' / 'svod'
    months = sorted(p.stem.replace('svod_', '') for p in svod.glob('svod_*.parquet'))
    assert months, f'no svod files in {svod} — run make_fake_svod.py first'
    latest = months[-1]

    for d in {out, static_out}:
        if d.exists():
            shutil.rmtree(d)
    out.mkdir(parents=True)
    c = Client()

    def get(url):
        r = c.get(url)
        assert r.status_code == 200, (url, r.status_code)
        return r

    for month in months:
        r = c.post('/portfel/', {'selected_date': month})
        assert r.status_code == 302, (month, r.status_code)
        (out / month).mkdir()
        for dept in DEPTS:
            html = get(f'/portfel/result/{dept}/').content.decode()
            (out / month / f'{dept}.html').write_text(rewrite(html, 1, month, su), encoding='utf-8')
        (out / month / 'portfel.xlsx').write_bytes(get('/portfel/download/').content)
        print(f'{month}: {len(DEPTS)} pages + xlsx')

    # root pages point at the newest month (the session now holds it, too)
    c.post('/portfel/', {'selected_date': latest})
    (out / 'index.html').write_text(rewrite(get('/').content.decode(), 0, latest, su), encoding='utf-8')
    (out / 'internal.html').write_text(
        rewrite(get('/internal/risk-result/').content.decode(), 0, latest, su), encoding='utf-8')
    cal = calendar_page(get('/portfel/').content.decode(), months)
    (out / 'calendar.html').write_text(rewrite(cal, 0, latest, su), encoding='utf-8')

    for sub in ('css', 'js'):
        shutil.copytree(HERE / 'static' / sub, static_out / sub)

    # every relative link must land on a file we wrote
    missing = set()
    for page in out.rglob('*.html'):
        for link in re.findall(r'(?:href|src)="([^"#:]+)"', page.read_text(encoding='utf-8')):
            if su and link.startswith(su):
                target = static_out / link[len(su):]
            elif link.startswith('/'):
                continue
            else:
                target = (page.parent / link).resolve()
            if not target.exists():
                missing.add((page.relative_to(out).as_posix(), link))
    for m in sorted(missing):
        print('BROKEN LINK', *m)
    size = sum(p.stat().st_size for d in {out, static_out} for p in d.rglob('*') if p.is_file())
    print(f'wrote {out} · {size / 1e6:.1f} MB · broken links: {len(missing)}')
    sys.exit(1 if missing else 0)


if __name__ == '__main__':
    main()
