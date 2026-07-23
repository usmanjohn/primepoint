"""Canonical study subjects and their mappings onto each app's own taxonomy.

The user's preference is stored as a comma-separated list of slugs
(on Profile.study_subjects for logged-in users, in the session for guests):
    ''      -> never chosen (show the welcome picker)
    'all'   -> explicitly chose everything (no filtering)
    'a,b'   -> filter to those subjects
Content that maps to no canonical subject at all is always visible.
"""
from django.utils.translation import gettext_lazy as _

SESSION_KEY = 'study_subjects'

SUBJECTS = [
    {
        'slug': 'english', 'name': _('English'),
        'icon': 'bi-translate', 'color': '#38bdf8',
        'tutorial_categories': ['english'],
        'examprep_tracks': ['ielts'],
        'corner_subjects': ['english'],
        'practice_names': ['english'],
        'exam_languages': ['english'],
    },
    {
        'slug': 'korean', 'name': _('Korean'),
        'icon': 'bi-flag', 'color': '#f87171',
        'tutorial_categories': ['korean'],
        'examprep_tracks': ['topik'],
        'corner_subjects': ['korean'],
        'practice_names': ['korean', '한국어'],
        'exam_languages': ['korean'],
    },
    {
        'slug': 'math', 'name': _('Math'),
        'icon': 'bi-calculator', 'color': '#f59e0b',
        'tutorial_categories': ['math'],
        'examprep_tracks': [],
        'corner_subjects': [],
        'practice_names': ['math', 'mathematics', 'sat math'],
        'exam_languages': [],
    },
    {
        'slug': 'russian', 'name': _('Russian'),
        'icon': 'bi-globe-americas', 'color': '#a78bfa',
        'tutorial_categories': ['russian'],
        'examprep_tracks': [],
        'corner_subjects': ['russian'],
        'practice_names': ['russian'],
        'exam_languages': [],
    },
]

SUBJECT_MAP = {s['slug']: s for s in SUBJECTS}
SUBJECT_SLUGS = list(SUBJECT_MAP)


def parse_subjects(raw):
    """Raw stored string -> list of chosen slugs, or None meaning 'no filtering'."""
    if not raw or raw == 'all':
        return None
    slugs = [s for s in raw.split(',') if s in SUBJECT_MAP]
    if not slugs or len(slugs) >= len(SUBJECTS):
        return None
    return slugs


def get_raw(request):
    if request.user.is_authenticated:
        try:
            return request.user.profile.study_subjects
        except Exception:
            return ''
    return request.session.get(SESSION_KEY, '')


def get_study_subjects(request):
    """Chosen slugs for this visitor, or None meaning 'show everything'."""
    return parse_subjects(get_raw(request))


def has_chosen_subjects(request):
    """True once the visitor has made any choice (including 'Everything')."""
    return bool(get_raw(request))


def mapped_values(key):
    """Every value of `key` claimed by any canonical subject."""
    return {v for s in SUBJECTS for v in s[key]}


def allowed_values(slugs, key):
    """Values of `key` belonging to the chosen subjects."""
    return {v for slug in slugs for v in SUBJECT_MAP[slug][key]}


def value_visible(value, slugs, key, normalize=False):
    """A value is visible if a chosen subject claims it, or nobody claims it."""
    if normalize:
        value = (value or '').strip().lower()
    return value in allowed_values(slugs, key) or value not in mapped_values(key)
