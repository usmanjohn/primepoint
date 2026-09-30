"""The one-tap PDF of each worksheet — committed files, never runtime work.

The worksheet page (`/workbook/<pk>/worksheet/`) is always current and can be
printed from any laptop. A phone cannot Ctrl+P comfortably, so each lesson
also has a real PDF file, generated dev-side by `gen_worksheet_pdfs`
(headless Chrome, the same way the hand-out kit is checked) and committed
under static/workbook/pdf/ like the Corner mp3s and the QR codes.

A PDF goes stale the moment its workbook is edited. So the manifest records
the hash of the data each PDF was made from, the importer stores the hash of
the data it imported, and the download link only appears while the two agree.
A stale PDF is never offered; the page falls back to "print this page".
"""
import hashlib
import json
from pathlib import Path

from django.conf import settings
from django.templatetags.static import static

PDF_DIR = Path(settings.BASE_DIR) / 'static' / 'workbook' / 'pdf'
MANIFEST = PDF_DIR / 'manifest.json'

_cache = {'mtime': None, 'data': {}}


def data_hash(entry):
    """Stable hash of one workbook's data dict, as written in its data file."""
    blob = json.dumps(entry, sort_keys=True, ensure_ascii=False, default=str)
    return hashlib.sha256(blob.encode('utf-8')).hexdigest()


def filename(code):
    """'PK-9' → 'pk-9.pdf'."""
    return f'{code.lower()}.pdf'


def read_manifest():
    try:
        mtime = MANIFEST.stat().st_mtime
    except OSError:
        return {}
    if _cache['mtime'] != mtime:
        try:
            _cache['data'] = json.loads(MANIFEST.read_text(encoding='utf-8'))
        except (OSError, ValueError):
            _cache['data'] = {}
        _cache['mtime'] = mtime
    return _cache['data']


def write_manifest(data):
    PDF_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False) + '\n',
                        encoding='utf-8')


def pdf_url(workbook):
    """The committed PDF's URL, or None when there is none or it is stale."""
    code = workbook.code
    if not workbook.data_hash or read_manifest().get(code) != workbook.data_hash:
        return None
    if not (PDF_DIR / filename(code)).exists():
        return None
    return static(f'workbook/pdf/{filename(code)}')
