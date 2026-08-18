"""How long a page was actually open — the honest half of "mark as finished".

`tutorial_finish` and `corner_story_finish` used to be bare buttons: land on the
page, click, collect the points. That was a hole in every number the platform
reports (rating, the progress page, analytics), and Prime Journey made it worse
by hanging a real game reward on it — a sealed gate opened for one click.

So a finish is now refused unless the page was open for a plausible fraction of
the time it takes to read. The clock lives in the session, is started by the
detail view, and needs no JavaScript.

**Be honest about what this is.** It raises the cost of faking a read from one
second to a minute or so; it does not prove anyone read anything, and it never
will. It is a speed bump. The only real proof of study on this platform is a
*scored* one — which is why Prime Journey pays its strength for a passed
practice and not for a click. See `_journey_credit_study` in games/views.py.
"""
import time

from django.utils.html import strip_tags

SESSION_KEY = 'reading_clock'

# A finish must arrive at least this long after the page was opened. Scaled to
# the length of the text, then clamped so a one-paragraph story is not a chore
# and a nine-minute lesson is not a formality.
SECONDS_PER_MINUTE_OF_TEXT = 12
MIN_SECONDS = 20
MAX_SECONDS = 100

# Opens older than this are forgotten: "I opened it last week" is not a read.
OPEN_TTL = 6 * 60 * 60

# Session housekeeping — a pupil who browses all day should not carry an
# unbounded dict around in their session.
MAX_TRACKED = 60


def _key(kind, pk):
    return f'{kind}:{pk}'


def _clean(clock, now):
    return {k: t for k, t in clock.items() if now - t < OPEN_TTL}


def mark_opened(request, kind, pk):
    """Start the clock for this page, if it is not already running.

    The *earliest* open in the window wins, so leaving to look at the practice
    and coming back does not reset a genuine reader's progress.
    """
    if not request.user.is_authenticated:
        return
    now = int(time.time())
    clock = _clean(request.session.get(SESSION_KEY) or {}, now)
    clock.setdefault(_key(kind, pk), now)
    if len(clock) > MAX_TRACKED:
        for stale in sorted(clock, key=clock.get)[:len(clock) - MAX_TRACKED]:
            del clock[stale]
    request.session[SESSION_KEY] = clock
    request.session.modified = True


def seconds_open(request, kind, pk):
    """How long this page has been open, or None if the clock never started."""
    now = int(time.time())
    clock = _clean(request.session.get(SESSION_KEY) or {}, now)
    opened = clock.get(_key(kind, pk))
    return None if opened is None else max(0, now - opened)


def required_seconds(html):
    """The shortest visit that counts as a read of this text."""
    words = len(strip_tags(str(html or '')).split())
    minutes = max(1, round(words / 200))
    return max(MIN_SECONDS, min(MAX_SECONDS, minutes * SECONDS_PER_MINUTE_OF_TEXT))


def too_soon(request, kind, pk, html):
    """Seconds still to wait before a finish is believable — 0 when it is.

    A missing clock counts as "never opened the page", which is the case this
    exists to catch, so it asks for the full time.
    """
    needed = required_seconds(html)
    open_for = seconds_open(request, kind, pk)
    if open_for is None:
        return needed
    return max(0, needed - open_for)
