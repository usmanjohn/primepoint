"""
Print the founder's résumé to the committed PDF. DEV-ONLY.

    python manage.py gen_resume_pdf

Renders /about/me/resume/?bare=1 in-process, points its /static/ links at the
files on disk, prints it with headless Chrome (the same command the hand-out
kit and the workbook worksheets use) and writes prime/resume/<PDF_FILENAME>
plus manifest.json — the hash of the sources it was printed from. The download
view serves that file; `prime.tests.ResumeTests` fails while the hash is stale,
so after editing prime/resume.py, the template or resume.css: run this, commit.

⚠️ PAPER GATE: refuses anything but exactly two A4 pages.
"""
import json
import re
import subprocess
import tempfile
from pathlib import Path

from django.contrib.auth.models import AnonymousUser
from django.core.management.base import BaseCommand, CommandError
from django.test import RequestFactory
from django.utils import translation

from prime import resume as cv
from prime.views import cv_pdf_path, resume_print

# Same three helpers as workbook's gen_worksheet_pdfs — repeated, not imported,
# because importing that module drags in examprep.views (and openpyxl).
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
STATIC_LINK = re.compile(r'(href|src)="/static/([^"?#]+)[^"]*"')


def _local_static(html):
    from django.contrib.staticfiles import finders

    def swap(m):
        found = finders.find(m.group(2))
        return f'{m.group(1)}="{Path(found).as_uri()}"' if found else m.group(0)
    return STATIC_LINK.sub(swap, html)


def _page_count(path):
    return len(re.findall(rb'/Type\s*/Page(?!s)', Path(path).read_bytes()))

PAGES = 2


def source_hash():
    """What the PDF was printed from. Shared with the test that checks it."""
    import hashlib
    from django.conf import settings
    h = hashlib.sha256()
    for rel in ('prime/resume.py', 'prime/templates/prime/resume_print.html', 'static/css/resume.css'):
        h.update((settings.BASE_DIR / rel).read_bytes())
    return h.hexdigest()


def manifest_path():
    return cv_pdf_path().parent / 'manifest.json'


class Command(BaseCommand):
    help = 'Print the résumé to prime/resume/ with headless Chrome (dev-only).'

    def add_arguments(self, parser):
        parser.add_argument('--chrome', default=CHROME)

    def handle(self, *args, **opts):
        if not Path(opts['chrome']).exists():
            raise CommandError(f"Chrome not found at {opts['chrome']} — pass --chrome.")
        out = cv_pdf_path()
        out.parent.mkdir(parents=True, exist_ok=True)
        translation.activate('en')
        request = RequestFactory().get('/about/me/resume/', {'bare': '1'})
        request.user = AnonymousUser()
        request.LANGUAGE_CODE = 'en'
        html = resume_print(request).content.decode('utf-8')
        with tempfile.TemporaryDirectory() as tmp:
            page = Path(tmp) / 'resume.html'
            page.write_text(_local_static(html), encoding='utf-8')
            pdf = Path(tmp) / 'resume.pdf'
            subprocess.run([
                opts['chrome'], '--headless', '--disable-gpu', '--no-pdf-header-footer',
                '--allow-file-access-from-files', '--virtual-time-budget=8000',
                f'--print-to-pdf={pdf}', page.as_uri(),
            ], check=True, capture_output=True, timeout=120)
            pages = _page_count(pdf)
            if pages != PAGES:
                raise CommandError(f'The résumé printed to {pages} page(s), not {PAGES}. '
                                   'Trim the copy in prime/resume.py or the spacing in resume.css.')
            out.write_bytes(pdf.read_bytes())
        manifest_path().write_text(json.dumps({'source_hash': source_hash()}, indent=2) + '\n')
        self.stdout.write(self.style.SUCCESS(
            f'{out.relative_to(out.parents[2])}: {pages} pages, {out.stat().st_size // 1024} KB. '
            'Commit prime/resume/.'))
