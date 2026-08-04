"""Shared pieces for the staff print sheets.

Every printable handout on the site — the grammar and vocab banks, and the
Prime English / Prime Korean lesson bundles — is a standalone HTML page the
staff member turns into a PDF with Ctrl+P. There is no PDF library: the
`pe-*` / `pk-*` component kit is flexbox and CSS-grid, which the Python PDF
renderers do not support, and the browser already renders it perfectly.

Two things are shared and live here: the access gate (reading content on-site
is open, walking away with a distributable copy is not) and the query that
pulls a stretch of a playlist with all three legs of each lesson attached.
"""
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied


# One bundle may not exceed this many lessons. A full 100-lesson playlist is
# ~1.5 MB of HTML plus 2000 practice questions; browsers render it, but the
# print preview crawls and the resulting PDF is unusable as a handout. Staff
# who really want the whole thing can pass ?cap=0.
MAX_BUNDLE_LESSONS = 25

# Which parts of a lesson a bundle can carry, in printing order.
BUNDLE_PARTS = ('tutorial', 'practice', 'reading')


def require_staff(request):
    """Gate for the take-away formats (print sheets, spreadsheet exports).

    Reading on-site is open to everyone; walking away with a distributable
    copy is not. Anonymous visitors are sent to log in (they may simply not be
    signed in yet); a signed-in non-staff user gets a 403, because for them it
    is a permission answer, not a login prompt.

    Returns a response to return, or None when the user may proceed.
    """
    if not request.user.is_authenticated:
        return redirect_to_login(request.get_full_path())
    if not request.user.is_staff:
        raise PermissionDenied
    return None


def qs_with(request, **overrides):
    """Current query string with some params replaced — the href for one toggle.

    Built here rather than in the template because Django templates cannot
    manipulate a QueryDict; a value of None drops the param.
    """
    params = request.GET.copy()
    for key, value in overrides.items():
        if value is None:
            params.pop(key, None)
        else:
            params[key] = value
    encoded = params.urlencode()
    return f'?{encoded}' if encoded else '?'


def print_options(request):
    """Read the toggles every print sheet understands off the querystring.

    `answers`  1 (default) = teacher copy: correct answers marked, explanations
               and quiz keys shown. 0 = pupil copy.
    `gloss`    1 = print each cn-word's translation inline, since a reader
               holding paper cannot tap it. 0 (default) = highlights only.
    `parts`    subset of BUNDLE_PARTS; bundles only. Accepted both as one
               comma-separated value (?parts=tutorial,practice) and as
               repeated keys, which is what a plain checkbox form submits —
               so the picker needs no JavaScript.
    """
    raw = ','.join(request.GET.getlist('parts'))
    parts = [p for p in BUNDLE_PARTS if p in raw.split(',')]
    return {
        'answers': request.GET.get('answers', '1') != '0',
        'gloss':   request.GET.get('gloss') == '1',
        'parts':   parts or list(BUNDLE_PARTS),
    }


def bar_context(request, back_url, show_gloss=False):
    """Everything templates/printing/_bar.html renders, plus the flags the
    part templates read (`answers`, `gloss`).

    `show_gloss` is False for sheets with no cn-word vocabulary to gloss —
    the toggle would do nothing there, so it is not offered.
    """
    options = print_options(request)
    return {
        'answers':         options['answers'],
        'gloss':           options['gloss'],
        'show_gloss':      show_gloss,
        'back_url':        back_url,
        'url_answers_on':  qs_with(request, answers=None),
        'url_answers_off': qs_with(request, answers=0),
        'url_gloss_on':    qs_with(request, gloss=1),
        'url_gloss_off':   qs_with(request, gloss=None),
        'options':         options,
    }


def lesson_range(request, total):
    """Clamp the ?from=/?to= range against a playlist of `total` lessons.

    Defaults to the first ten. Returns (start, end) as 1-based, inclusive
    positions in the playlist.
    """
    def as_int(name, fallback):
        try:
            return int(request.GET.get(name, fallback))
        except (TypeError, ValueError):
            return fallback

    start = max(1, min(as_int('from', 1), total or 1))
    end   = max(start, min(as_int('to', start + 9), total or 1))
    if request.GET.get('cap') != '0':
        end = min(end, start + MAX_BUNDLE_LESSONS - 1)
    return start, end


def lesson_rows(playlist, start, end):
    """The lessons at positions `start`..`end` of a playlist, three legs attached.

    One row per lesson: the tutorial, the practices linked to it and the Corner
    readings linked to it (`Tutorial.practices` / `Tutorial.stories`). Everything
    a bundle prints is prefetched here, so a ten-lesson booklet costs a handful
    of queries rather than several hundred.
    """
    items = (playlist.items
             .select_related('tutorial')
             .prefetch_related(
                 'tutorial__practices__questions__choices',
                 'tutorial__stories__collection',
                 'tutorial__stories__words',
                 'tutorial__stories__grammar',
                 'tutorial__stories__questions',
             )
             .order_by('order', 'id'))

    rows = []
    for position, item in enumerate(items, start=1):
        if position < start:
            continue
        if position > end:
            break
        tutorial = item.tutorial
        if not tutorial.is_published:
            continue
        rows.append({
            'n':         position,
            'tutorial':  tutorial,
            'practices': [p for p in tutorial.practices.all() if p.is_published],
            'stories':   [s for s in tutorial.stories.all() if s.is_published],
        })
    return rows
