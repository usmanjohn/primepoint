"""What a master has contributed to the platform, and what it is worth.

The old `avg_rating` averaged the *pupils'* point totals, so a master who
taught strong students scored well without ever writing a line of content, and
a master with no students scored zero however much they built. It measured the
wrong thing, and it is now the student-review average instead.

This module answers the other question: **how much of Powerty did this person
build, and did anyone use it?** Two halves, both of which have to be non-zero
for a good score:

    made    published practices, tutorials, exam-prep lessons, readings,
            writing drills and logic puzzles — weighted by how much work one
            item of that kind actually is
    used    how many distinct pupils worked through that content, and how many
            times in total — content nobody opens is worth its authoring
            points and nothing more

Deliberately *not* counted: attempts by the master themselves, unpublished
drafts, and anything a pupil merely opened without finishing.

The breakdown is rendered on the master's own detail page, so every number here
has a label — a master should be able to see exactly where the score came from.
Adding a library means adding one entry to `CONTENT_SOURCES`; the score, the
breakdown table and the list page all pick it up.
"""
from django.db.models import Count
from django.utils.translation import gettext_lazy as _

# Points for authoring one published item. A practice or a tutorial is a
# day's work; a Corner story is an evening's.
CONTENT_POINTS = {
    'practices': 6,
    'tutorials': 6,
    'lessons': 6,
    'stories': 4,
    'drills': 4,
    'puzzles': 6,
}
QUESTION_POINTS = 0.3       # per authored practice question
LEARNER_POINTS = 3          # per distinct pupil who worked through their content
COMPLETION_POINTS = 0.4     # per finished item (a pupil may finish many)
STUDENT_POINTS = 5          # per enrolled pupil of their own


def _authored(master):
    """Every published thing this master made, per source.

    Practices hang off the Master row; everything else is authored by the
    underlying User, which is how the bulk importers write them.
    """
    from corner.models import Story
    from examprep.models import Lesson, WritingDrill
    from logic.models import LogicPuzzle
    from tutorial.models import Tutorial

    user = master.profile.user
    return {
        'practices': master.practices.filter(is_published=True),
        'tutorials': Tutorial.objects.filter(author=user, is_published=True),
        'lessons': Lesson.objects.filter(author=user, is_published=True,
                                         track__is_published=True),
        'stories': Story.objects.filter(author=user, is_published=True,
                                        collection__is_published=True),
        'drills': WritingDrill.objects.filter(author=user, is_published=True),
        'puzzles': LogicPuzzle.objects.filter(author=user, is_published=True),
    }


CONTENT_LABELS = {
    'practices': _('Practice tests'),
    'tutorials': _('Tutorials'),
    'lessons': _('Exam-prep lessons'),
    'stories': _('Readings'),
    'drills': _('Writing drills'),
    'puzzles': _('Logic puzzles'),
}


def _engagement(master, authored):
    """Who used that content: (distinct pupil user ids, total completions).

    Distinct pupils are counted across all six libraries at once — a pupil who
    read three of this master's tutorials and sat two of their practices is one
    pupil, not five.
    """
    from corner.models import StoryProgress
    from examprep.models import LessonProgress, WritingDrillProgress
    from practice.models import PracticeAttempt
    from tutorial.models import TutorialProgress

    author_id = master.profile.user_id
    learners, completions = set(), 0

    attempts = (PracticeAttempt.objects
                .filter(practice__in=authored['practices'], status='completed')
                .exclude(panda__profile__user_id=author_id)
                .values_list('panda__profile__user_id', flat=True))
    attempts = list(attempts)
    learners.update(attempts)
    completions += len(attempts)

    progress_sources = [
        (TutorialProgress, 'tutorial__in', authored['tutorials']),
        (LessonProgress, 'lesson__in', authored['lessons']),
        (StoryProgress, 'story__in', authored['stories']),
        (WritingDrillProgress, 'drill__in', authored['drills']),
    ]
    for model, lookup, queryset in progress_sources:
        ids = list(model.objects
                   .filter(**{lookup: queryset})
                   .exclude(user_id=author_id)
                   .values_list('user_id', flat=True))
        learners.update(ids)
        completions += len(ids)

    return learners, completions


def contribution_summary(master):
    """The full breakdown: rows for the table, plus the totals cached on Master.

    Returns ``{'rows': [...], 'score': int, 'content_count': int,
    'learner_count': int, 'completions': int}`` where each row is
    ``{'key', 'label', 'count', 'points'}``.
    """
    authored = _authored(master)
    rows, score, content_count = [], 0.0, 0

    for key, queryset in authored.items():
        count = queryset.count()
        if key == 'practices':
            # A twenty-question test is more work than a five-question one.
            questions = (queryset.aggregate(n=Count('questions'))['n'] or 0)
            points = count * CONTENT_POINTS[key] + questions * QUESTION_POINTS
        else:
            points = count * CONTENT_POINTS[key]
        content_count += count
        score += points
        rows.append({'key': key, 'label': CONTENT_LABELS[key],
                     'count': count, 'points': round(points)})

    learners, completions = _engagement(master, authored)
    reach_points = len(learners) * LEARNER_POINTS + completions * COMPLETION_POINTS
    score += reach_points
    rows.append({'key': 'learners', 'label': _('Pupils who used it'),
                 'count': len(learners), 'points': round(reach_points)})

    students = master.pandas.count()
    student_points = students * STUDENT_POINTS
    score += student_points
    rows.append({'key': 'students', 'label': _('Own students'),
                 'count': students, 'points': round(student_points)})

    return {
        'rows': rows,
        'score': int(round(score)),
        'content_count': content_count,
        'learner_count': len(learners),
        'completions': completions,
    }
