"""
Generate the committed one-tap PDF of each workbook's worksheet. DEV-ONLY.

    python manage.py gen_worksheet_pdfs              # every published workbook
    python manage.py gen_worksheet_pdfs --only PK-9 PK-10
    python manage.py gen_worksheet_pdfs --stale      # only those whose PDF is missing or stale

Renders /workbook/<pk>/worksheet/?bare=1 in-process, points its /static/ links
at the files on disk, prints it with headless Chrome (the same command the
hand-out kit's paper gate uses), and writes static/workbook/pdf/<code>.pdf
plus the workbook's data hash into manifest.json. The site only offers a PDF
whose manifest hash matches the imported data — see workbook/pdfs.py — so
after any `import_workbook --republish`, run this again and commit the files.
"""
import re
import subprocess
import tempfile
from pathlib import Path

from django.contrib.auth.models import AnonymousUser
from django.contrib.staticfiles import finders
from django.core.management.base import BaseCommand, CommandError
from django.test import RequestFactory
from django.utils import translation

from workbook import pdfs
from workbook.models import Workbook
from workbook.views import worksheet

CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
STATIC_LINK = re.compile(r'(href|src)="/static/([^"?#]+)[^"]*"')


def _local_static(html):
    def swap(m):
        found = finders.find(m.group(2))
        return f'{m.group(1)}="{Path(found).as_uri()}"' if found else m.group(0)
    return STATIC_LINK.sub(swap, html)


def _page_count(path):
    data = Path(path).read_bytes()
    return len(re.findall(rb'/Type\s*/Page(?!s)', data))


class Command(BaseCommand):
    help = 'Generate committed worksheet PDFs with headless Chrome (dev-only).'

    def add_arguments(self, parser):
        parser.add_argument('--only', nargs='*', help="Lesson codes, e.g. PK-9 PK-10.")
        parser.add_argument('--stale', action='store_true', help='Only missing or stale PDFs.')
        parser.add_argument('--chrome', default=CHROME)

    def handle(self, *args, **opts):
        if not Path(opts['chrome']).exists():
            raise CommandError(f"Chrome not found at {opts['chrome']} — pass --chrome.")
        workbooks = list(Workbook.objects.filter(is_published=True).select_related('tutorial'))
        if opts['only']:
            wanted = {c.upper() for c in opts['only']}
            workbooks = [w for w in workbooks if w.code.upper() in wanted]
        if opts['stale']:
            workbooks = [w for w in workbooks if pdfs.pdf_url(w) is None]
        if not workbooks:
            self.stdout.write('Nothing to do.')
            return

        manifest = dict(pdfs.read_manifest())
        pdfs.PDF_DIR.mkdir(parents=True, exist_ok=True)
        factory = RequestFactory()
        translation.activate('uz')
        with tempfile.TemporaryDirectory() as tmp:
            for wb in workbooks:
                request = factory.get(f'/workbook/{wb.pk}/worksheet/', {'bare': '1'})
                request.user = AnonymousUser()
                request.LANGUAGE_CODE = 'uz'
                html = worksheet(request, wb.pk).content.decode('utf-8')
                page = Path(tmp) / f'{wb.code}.html'
                page.write_text(_local_static(html), encoding='utf-8')
                out = pdfs.PDF_DIR / pdfs.filename(wb.code)
                subprocess.run([
                    opts['chrome'], '--headless', '--disable-gpu', '--no-pdf-header-footer',
                    '--allow-file-access-from-files', '--virtual-time-budget=8000',
                    f'--print-to-pdf={out}', page.as_uri(),
                ], check=True, capture_output=True, timeout=120)
                manifest[wb.code] = wb.data_hash
                self.stdout.write(self.style.SUCCESS(
                    f'  {wb.code}: {out.name} — {_page_count(out)} page(s), '
                    f'{out.stat().st_size // 1024} KB'))
        pdfs.write_manifest(manifest)
        self.stdout.write('Manifest updated. Commit static/workbook/pdf/.')
