"""What a master may put in a homework — narrowed to the classroom's subject.

A master who teaches English should not have to scroll past 170 maths
tutorials and 64 Russian ones to find the lesson they just taught. Every
picker on the homework form runs through here, and every one of them asks the
same question: which canonical study subjects does this room teach?

The canonical subjects and their mappings onto each app's own taxonomy already
exist in `prime.subjects` — the same registry that filters the pupil-facing
libraries. Reusing it means "English" means the same thing on the homework
form as it does on the Corner shelf, and adding a subject stays a one-file job.

The registry's own visibility rule is kept: a value that *no* canonical subject
claims stays visible. A physics master with a "Fizika" practice bank must still
find it, and the price of that is a handful of unclaimed rows in the list —
much cheaper than an empty picker.
"""
from django.db.models import Q

from prime import subjects as registry


def classroom_slugs(classroom):
    """Canonical subject slugs this room teaches, or None meaning 'everything'.

    The room's own subject wins. A room that never set one falls back to what
    its master says they teach, matched loosely against the registry, and a
    master whose subjects match nothing gets the unfiltered list.
    """
    if classroom is not None and classroom.subject:
        return [classroom.subject]

    master = getattr(classroom, 'master', None)
    if master is None:
        return None
    stated = ' '.join(master.subject_names).lower()
    if not stated.strip():
        return None
    slugs = []
    for subject in registry.SUBJECTS:
        names = {subject['slug'], str(subject['name']).lower()}
        names |= {v.lower() for v in subject['practice_names']}
        if any(name in stated for name in names):
            slugs.append(subject['slug'])
    return slugs or None


def _visible_q(slugs, key, field, values_of):
    """A Q that keeps rows a chosen subject claims, plus rows nobody claims."""
    allowed = registry.allowed_values(slugs, key)
    mapped = registry.mapped_values(key)
    unclaimed = {v for v in values_of() if v not in mapped}
    keep = allowed | unclaimed
    return Q(**{f'{field}__in': keep})


# ── The four pickers ───────────────────────────────────────────────────────

def practice_queryset(classroom, master):
    """Own published practices plus everyone's shared ones, this room's subject."""
    from practice.models import Practice, Subject

    qs = (Practice.objects
          .filter(Q(master=master, is_published=True)
                  | Q(is_available_for_all=True, is_published=True))
          .select_related('subject', 'master'))
    slugs = classroom_slugs(classroom)
    if not slugs:
        return qs.order_by('subject__name', 'id')

    allowed = registry.allowed_values(slugs, 'practice_names')
    mapped = registry.mapped_values('practice_names')
    keep = [s.pk for s in Subject.objects.all()
            if s.name.strip().lower() in allowed or s.name.strip().lower() not in mapped]
    # A practice with no subject at all is claimed by nobody, so it stays.
    return qs.filter(Q(subject__in=keep) | Q(subject__isnull=True)).order_by('subject__name', 'id')


def tutorial_queryset(classroom):
    from tutorial.models import Tutorial, CATEGORY_CHOICES

    # Ordered by id, not title. A course is written in lesson order and that
    # is the order a master looks for it in; sorting the titles as text puts
    # PK-100 between PK-1 and PK-11 and scatters the whole course.
    qs = Tutorial.objects.filter(is_published=True)
    slugs = classroom_slugs(classroom)
    if not slugs:
        return qs.order_by('category', 'id')
    return qs.filter(_visible_q(
        slugs, 'tutorial_categories', 'category',
        lambda: [c for c, _label in CATEGORY_CHOICES],
    )).order_by('category', 'id')


def story_queryset(classroom):
    from corner.models import Story, Subject

    qs = (Story.objects
          .filter(is_published=True, collection__is_published=True,
                  collection__subject__is_published=True)
          .select_related('collection__subject'))
    slugs = classroom_slugs(classroom)
    if not slugs:
        return qs.order_by('collection__title', 'order')
    return qs.filter(_visible_q(
        slugs, 'corner_subjects', 'collection__subject__slug',
        lambda: Subject.objects.values_list('slug', flat=True),
    )).order_by('collection__title', 'order')


def exam_lesson_queryset(classroom):
    from examprep.models import Lesson, ExamTrack

    qs = (Lesson.objects
          .filter(is_published=True, track__is_published=True)
          .select_related('track'))
    slugs = classroom_slugs(classroom)
    if not slugs:
        return qs.order_by('track__name', 'skill', 'order')
    return qs.filter(_visible_q(
        slugs, 'examprep_tracks', 'track__slug',
        lambda: ExamTrack.objects.values_list('slug', flat=True),
    )).order_by('track__name', 'skill', 'order')


# ── The "one tutorial, three legs" rule ────────────────────────────────────

def expand_tutorials(tutorials):
    """The practices and readings that belong to these tutorials.

    Every Prime lesson is written as three legs — the tutorial teaches the
    pattern, the practice drills it, the reading shows it living in a text —
    and they are already linked on the Tutorial itself. So a master who picks
    "PE-24" almost always means all three, and the homework form offers to
    pull the other two in rather than making them hunt for the matching titles.
    """
    practices, stories = [], []
    for tutorial in tutorials:
        practices.extend(tutorial.practices.filter(is_published=True))
        stories.extend(tutorial.stories.filter(
            is_published=True, collection__is_published=True))
    return practices, stories
