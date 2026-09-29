"""Search-facing titles and descriptions — one registry, like every other
site-wide concern in this package.

Every lesson here is named for its place in a course: "PK-24: -고 싶다",
"TOPIK 광고 3: Xizmat va joy reklamalari", "SAT R&W 11: Read the Sentence".
That is the right name inside the course and the wrong one in a search result.
Nobody types "PK-24", so a page titled with it can match nothing and, on the
rare occasion it does surface, tells the reader nothing about what it holds.

So: move the topic to the front, where Google and a human scanning ten blue
links both read first, and say afterwards what kind of thing it is.

    PK-24: -고 싶다  ->  -고 싶다 — koreys tili grammatikasi | Powerty

Derived, never stored. 601 tutorials + 317 examprep lessons + 768 stories is
far too many to re-title by hand, the course code is a dependable prefix, and
a derived title cannot drift out of sync with the lesson it names. If a single
page ever deserves a hand-written title, add a nullable `seo_title` field and
let it win here — the rest keep working untouched.
"""
import re

from django.utils.html import strip_tags

BRAND = 'Powerty'

# Google shows roughly 600px of title, which is ~60 characters of Latin text.
# Past that the tail is cut, so the brand is dropped before the topic is.
TITLE_BUDGET = 65
DESCRIPTION_BUDGET = 160

_TUTORIAL_CODE = re.compile(r'^([A-Z]+)-(\d+)\s*:\s*')

# A course code is what sits before the FIRST colon, and only when it looks
# like a code rather than the opening clause of a sentence: short, numbered,
# a handful of words. Anchoring on the colon keeps "PJ-42: Imkoniyat 2 —
# potensial shakl" from losing "Imkoniyat 2" as well, which a greedier
# pattern matching on the dash happily did.
_CODE_MAX_CHARS = 24
_CODE_MAX_WORDS = 4

# Keyed on the title prefix rather than `category`, because `math` holds two
# very different courses: Prime Math (Uzbek school maths) and Prime SAT.
TUTORIAL_QUALIFIERS = {
    'PE': 'ingliz tili grammatikasi',
    'PK': 'koreys tili grammatikasi',
    'PR': 'rus tili grammatikasi',
    'PJ': 'yapon tili grammatikasi',
    'PM': 'matematika',
    'SAT': 'SAT Math',
}

# Fallback when a title carries no course code we know.
CATEGORY_QUALIFIERS = {
    'english': 'ingliz tili',
    'korean': 'koreys tili',
    'russian': 'rus tili',
    'japanese': 'yapon tili',
    'math': 'matematika',
}

EXAMPREP_SKILLS = {
    'reading': 'oʻqish',
    'listening': 'tinglash',
    'writing': 'yozish',
    'speaking': 'gapirish',
    'strategy': 'strategiya',
}

# The Corner subject as a searchable phrase. A story's own title is already
# natural language ("Samarqand gumbazidagi naqsh"); what it lacks is any hint
# that it is a graded reading text in a particular language.
CORNER_SUBJECTS = {
    'Korean': 'koreyscha oʻqish matni',
    'English': 'inglizcha oʻqish matni',
    'Russian': 'ruscha oʻqish matni',
    'Japanese': 'yaponcha oʻqish matni',
    'Matematika': 'matematika oʻqish matni',
}


def strip_course_code(title):
    """Drop a leading course code so the topic lands first.

    Only ever removes a prefix it recognises; a title that does not carry one
    comes back untouched rather than losing its first word.

    >>> strip_course_code('PK-24: -고 싶다')
    '-고 싶다'
    >>> strip_course_code('TOPIK 광고 3: Xizmat va joy reklamalari')
    'Xizmat va joy reklamalari'
    >>> strip_course_code("Bananas Don't Grow on Trees")
    "Bananas Don't Grow on Trees"
    """
    title = (title or '').strip()
    head, sep, tail = title.partition(':')
    if not sep or not tail.strip():
        return title
    if len(head) > _CODE_MAX_CHARS or len(head.split()) > _CODE_MAX_WORDS:
        return title
    if not any(ch.isdigit() for ch in head):
        return title
    return tail.strip()


def _already_says(topic, qualifier):
    """True when the topic already names the subject the qualifier would add.

    "Rus tili qayerdan kelgan" does not need "— rus tili grammatikasi" after
    it. Repeating the term reads like keyword stuffing to a person and is
    treated as such by Google, so the qualifier is dropped instead.

    Only the qualifier's leading subject word counts, matched whole: the rest
    ("tili", "grammatikasi") is common enough in these titles to fire on
    unrelated lessons.
    """
    head = (qualifier or '').split()[:1]
    if not head:
        return True
    return re.search(rf'(?<!\w){re.escape(head[0])}(?!\w)', topic, re.I) is not None


def compose(topic, qualifier=''):
    """topic — qualifier | Powerty, dropping the brand before anything else.

    The topic is never truncated: it holds the words someone might search for,
    and a half-word is worse than a missing brand. The qualifier is never
    truncated either — it is the part that says which subject this belongs to,
    which is exactly what a bare lesson title fails to say. Only the brand is
    negotiable, so a long title simply loses "| Powerty".

    Going past the ~65 characters Google *displays* is fine: it truncates the
    tail it shows, but indexes the whole thing, and the tail here is the least
    important part by construction.
    """
    topic = (topic or '').strip()
    if not topic:
        return BRAND
    if _already_says(topic, qualifier):
        full = topic
    else:
        # A second em dash in one title reads as a typo — "거늘, 기로서니 —
        # adabiy yon berish — koreys tili grammatikasi". Step down a level.
        separator = ' · ' if '—' in topic else ' — '
        full = f'{topic}{separator}{qualifier}'
    branded = f'{full} | {BRAND}'
    return branded if len(branded) <= TITLE_BUDGET else full


def tutorial_title(tutorial):
    match = _TUTORIAL_CODE.match(tutorial.title or '')
    qualifier = ''
    if match:
        qualifier = TUTORIAL_QUALIFIERS.get(match.group(1), '')
    if not qualifier:
        qualifier = CATEGORY_QUALIFIERS.get(
            getattr(tutorial, 'category', '') or '', '')
    return compose(strip_course_code(tutorial.title), qualifier)


def examprep_title(lesson):
    track = getattr(getattr(lesson, 'track', None), 'name', '') or ''
    skill = EXAMPREP_SKILLS.get(getattr(lesson, 'skill', '') or '', '')
    qualifier = ' '.join(part for part in (track, skill) if part)
    return compose(strip_course_code(lesson.title), qualifier)


def story_title(story):
    collection = getattr(story, 'collection', None)
    subject = getattr(getattr(collection, 'subject', None), 'name', '') or ''
    return compose(strip_course_code(story.title),
                   CORNER_SUBJECTS.get(subject, ''))


def practice_title(practice):
    subject = getattr(getattr(practice, 'subject', None), 'name', '') or ''
    return compose(strip_course_code(practice.title),
                   PRACTICE_SUBJECTS.get(subject, 'test'))


# Practice subjects are stored in the language of the material ('한국어',
# '日本語'), which is exactly what an Uzbek searcher will not type. 'Math' is
# the SAT bank and 'Matematika' the school one — the same split as the
# tutorials, kept apart here for the same reason.
PRACTICE_SUBJECTS = {
    'English': 'ingliz tili testi',
    'Matematika': 'matematika testi',
    'Math': 'SAT Math testi',
    '한국어': 'koreys tili testi',
    '日本語': 'yapon tili testi',
    'Russian': 'rus tili testi',
}


# Model label -> the function that titles it. A registry for the same reason
# `progress.SOURCES` is one: the next content type is an entry, not an edit.
TITLERS = {
    'tutorial.Tutorial': tutorial_title,
    'examprep.Lesson': examprep_title,
    'corner.Story': story_title,
    'practice.Practice': practice_title,
}


def title_for(obj):
    """The search-facing <title> for a content object, brand included."""
    if obj is None:
        return BRAND
    titler = TITLERS.get(getattr(getattr(obj, '_meta', None), 'label', ''))
    if titler is None:
        return compose(strip_course_code(getattr(obj, 'title', '') or ''))
    return titler(obj)


def strip_brand(title):
    """The title without its trailing brand, for og:title and headings."""
    suffix = f' | {BRAND}'
    return title[:-len(suffix)] if title.endswith(suffix) else title


def description(*candidates):
    """The first candidate with words in it, as plain text inside the budget.

    Cut at a word boundary: Google rewrites a description it finds unhelpful,
    and a sentence ending mid-word is the clearest signal that it should.
    """
    for candidate in candidates:
        text = re.sub(r'\s+', ' ', strip_tags(str(candidate or ''))).strip()
        if not text:
            continue
        if len(text) <= DESCRIPTION_BUDGET:
            return text
        clipped = text[:DESCRIPTION_BUDGET].rsplit(' ', 1)[0].rstrip(' ,;:—-')
        return f'{clipped}…'
    return ''
