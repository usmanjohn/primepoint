"""Regenerate the QR codes printed on the hand-out materials.

    python manage.py gen_qr
    python manage.py gen_qr --scale 12

Dev-only helper, exactly like `gen_icons`: it needs `segno` (`pip install segno`,
not in requirements.txt) and the files it writes are committed to the repo, so
production never runs it and never imports it.

The codes are *static* — they point at fixed addresses — so baking them into
`static/images/qr/` beats drawing one per request: no dependency in production,
no CPU on a page that is printed a hundred times, and the same file can be
downloaded on its own by a print shop.

Three rules the files obey, all of them print rules:

* **Error correction H (30%).** Paper gets smudged, folded and photocopied;
  a business card lives in a pocket. H is the difference between a code that
  survives that and one that does not.
* **A real quiet zone, and it is white.** `border=4` modules, filled white
  rather than left transparent, because a scanner needs the light margin and a
  transparent SVG dropped on a dark card has none.
* **No logo in the middle.** It would look lovely and it is the single easiest
  way to ship a thousand unscannable cards. The panda sits *beside* the code
  on the card instead.

Each target gets both an `.svg` (what the pages embed — vector, so it stays
crisp at any print size) and a `.png` (what someone hands to a print shop).
"""
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

# What we point people at. Keyed by file name; keep the addresses in sync with
# `prime/social.py` and `SITE_URL` in settings.
#
# The site link carries the www: the apex powerty.uz has no HTTPS certificate,
# so a QR on https://powerty.uz/ would open a blank page on every phone that
# scanned it — and a printed card cannot be fixed afterwards.
TARGETS = {
    'powerty-site': 'https://www.powerty.uz/',
    'powerty-telegram': 'https://t.me/powertyuz',
}

OUT_DIR = 'images/qr'

# QR ink. Near-black rather than pure black so it matches the printed ink of
# the rest of the sheet; scanners read contrast, and #0f172a on white is 17:1.
DARK = '#0f172a'
LIGHT = '#ffffff'


class Command(BaseCommand):
    help = 'Regenerate the printed QR codes into static/images/qr/ (dev only).'

    def add_arguments(self, parser):
        parser.add_argument('--scale', type=int, default=12,
                            help='PNG module size in pixels (default 12).')

    def handle(self, *args, **opts):
        try:
            import segno
        except ImportError:
            raise CommandError(
                'segno is not installed. This is a dev-only authoring tool:\n'
                '    pip install segno\n'
                'Do not add it to requirements.txt — the generated files are '
                'committed and production only serves them.')

        out = Path(settings.BASE_DIR) / 'static' / OUT_DIR
        out.mkdir(parents=True, exist_ok=True)

        for name, url in TARGETS.items():
            qr = segno.make(url, error='h')
            svg_path = out / f'{name}.svg'
            png_path = out / f'{name}.png'

            qr.save(str(svg_path), kind='svg', scale=10, border=4,
                    dark=DARK, light=LIGHT, omitsize=True, xmldecl=False)
            qr.save(str(png_path), kind='png', scale=opts['scale'], border=4,
                    dark=DARK, light=LIGHT)

            self.stdout.write(self.style.SUCCESS(
                f'  {name}: {url}  →  version {qr.version}, '
                f'{svg_path.name} + {png_path.name}'))

        self.stdout.write(self.style.SUCCESS(
            f'\nDone — {len(TARGETS)} codes in static/{OUT_DIR}/. '
            'Scan them with a real phone before printing anything.'))
