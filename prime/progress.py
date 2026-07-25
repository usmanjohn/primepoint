"""Learning activity: what a person has done, and what it is worth in points.

One registry, three readers: the student progress page, the master's view of
their students, and the staff analytics dashboard. Before this existed the
points logic lived inside `Panda.recalc_rating` and covered three libraries
while the platform had eight — 224 exam-prep lessons and 70 tutorials earned
nothing and showed up nowhere.

Each source answers three questions for one user:

    total   how many published items exist        (the denominator)
    done    how many this user has completed      (the numerator)
    points  what those completions are worth

`done` counts *distinct items*, never attempts, so re-taking a practice can
never inflate progress — though it can still earn points, which is deliberate:
progress measures coverage, points measure effort.

Adding a library means adding one entry to SOURCES. Nothing else changes: the
progress page, the master dashboard and analytics all pick it up.
"""
from django.db.models import Count, Sum
from django.utils.translation import gettext_lazy as _

# Points per completed item. Practice and exam attempts are scored, so their
# points are stored per attempt instead of being a flat rate.
from corner.models import STORY_POINTS, WRITING_POINTS  # noqa: F401 — re-exported
from examprep.models import LESSON_POINTS  # noqa: F401
from tutorial.models import TUTORIAL_POINTS  # noqa: F401

# A completed exam is the single biggest piece of work on the platform: three
# timed sections in one sitting. Scored 0-100 across sections, then weighted.
EXAM_BASE_POINTS = 10
EXAM_SCORE_POINTS = 20


def _published_counts():
    """Total published items per source. Cached per request by the callers."""
    from corner.models import Story, WritingPractice
    from examprep.models import Lesson
    from exam.models import Exam
    from practice.models import Practice
    from tutorial.models import Tutorial

    return {
        'practices': Practice.objects.filter(is_published=True).count(),
        'examprep': Lesson.objects.filter(
            is_published=True, track__is_published=True).count(),
        'tutorials': Tutorial.objects.filter(is_published=True).count(),
        'stories': Story.objects.filter(
            is_published=True,
            collection__is_published=True,
            collection__subject__is_published=True).count(),
        'writing': WritingPractice.objects.filter(is_published=True).count(),
        'exams': Exam.objects.filter(is_published=True).count(),
    }


def exam_points(attempt):
    """Points for one completed exam attempt.

    Sections a student never reached score None rather than 0, so an abandoned
    attempt that was later force-completed doesn't read as three zeros.
    """
    scores = [s for s in (attempt.listening_score, attempt.reading_score,
                          attempt.writing_score) if s is not None]
    if not scores:
        return EXAM_BASE_POINTS
    average = sum(scores) / len(scores)
    return round(EXAM_BASE_POINTS + (average / 100) * EXAM_SCORE_POINTS, 1)


# ── Per-source readers ─────────────────────────────────────────────────────
# Each takes a User and returns (done, points).

def _practices(user, panda):
    if not panda:
        return 0, 0
    agg = panda.attempts.filter(status='completed').aggregate(
        done=Count('practice', distinct=True), points=Sum('rating_points'))
    return agg['done'] or 0, agg['points'] or 0


def _examprep(user, panda):
    agg = user.examprep_progress.aggregate(
        done=Count('id'), points=Sum('points_awarded'))
    return agg['done'] or 0, agg['points'] or 0


def _tutorials(user, panda):
    agg = user.tutorial_progress.aggregate(
        done=Count('id'), points=Sum('points_awarded'))
    return agg['done'] or 0, agg['points'] or 0


def _stories(user, panda):
    agg = user.corner_progress.aggregate(
        done=Count('id'), points=Sum('points_awarded'))
    return agg['done'] or 0, agg['points'] or 0


def _writing(user, panda):
    agg = user.corner_writing_progress.aggregate(
        done=Count('id'), points=Sum('points_awarded'))
    return agg['done'] or 0, agg['points'] or 0


def _exams(user, panda):
    if not panda:
        return 0, 0
    attempts = panda.exam_attempts.filter(current_section='completed')
    done = attempts.values('exam').distinct().count()
    return done, round(sum(exam_points(a) for a in attempts), 1)


SOURCES = [
    {'key': 'practices', 'label': _('Practice Sets'), 'icon': 'bi-book-half',
     'url': 'practice_list', 'reader': _practices},
    {'key': 'examprep', 'label': _('Exam Prep'), 'icon': 'bi-journal-bookmark',
     'url': 'examprep_home', 'reader': _examprep},
    {'key': 'tutorials', 'label': _('Tutorials'), 'icon': 'bi-journal-text',
     'url': 'tutorial_list', 'reader': _tutorials},
    {'key': 'stories', 'label': _('Corner Stories'), 'icon': 'bi-stars',
     'url': 'corner_home', 'reader': _stories},
    {'key': 'writing', 'label': _('Writing Drills'), 'icon': 'bi-pencil-square',
     'url': 'corner_writing_list', 'reader': _writing},
    {'key': 'exams', 'label': _('Exams'), 'icon': 'bi-journal-check',
     'url': 'exam_list', 'reader': _exams},
]


def student_progress(user):
    """Per-library progress for one learner, plus totals.

    Returns rows even for libraries the student hasn't touched — seeing "0 / 224
    exam prep" is the point of a progress page.
    """
    panda = getattr(getattr(user, 'profile', None), 'panda', None)
    totals = _published_counts()

    rows = []
    for source in SOURCES:
        done, points = source['reader'](user, panda)
        total = totals[source['key']]
        rows.append({
            'key': source['key'],
            'label': source['label'],
            'icon': source['icon'],
            'url': source['url'],
            'done': done,
            'total': total,
            'points': round(points, 1),
            'percent': round(done / total * 100) if total else 0,
        })

    done_sum = sum(r['done'] for r in rows)
    total_sum = sum(r['total'] for r in rows)
    return {
        'rows': rows,
        'done': done_sum,
        'total': total_sum,
        'percent': round(done_sum / total_sum * 100) if total_sum else 0,
        'points': round(sum(r['points'] for r in rows), 1),
        'panda': panda,
    }


def total_points(user):
    """Every point this user has earned, across every source."""
    panda = getattr(getattr(user, 'profile', None), 'panda', None)
    return round(sum(s['reader'](user, panda)[1] for s in SOURCES), 1)


def master_progress(master):
    """A master's students with their progress, ordered by points."""
    students = []
    for panda in master.pandas.select_related('profile__user'):
        summary = student_progress(panda.profile.user)
        students.append({
            'panda': panda,
            'user': panda.profile.user,
            'done': summary['done'],
            'total': summary['total'],
            'percent': summary['percent'],
            'points': summary['points'],
            'rows': summary['rows'],
        })
    students.sort(key=lambda s: s['points'], reverse=True)

    count = len(students)
    return {
        'students': students,
        'count': count,
        'avg_percent': round(sum(s['percent'] for s in students) / count) if count else 0,
        'avg_points': round(sum(s['points'] for s in students) / count, 1) if count else 0,
        'active': sum(1 for s in students if s['done']),
    }


def platform_totals():
    """Library sizes and how much of each has actually been completed.

    Completion is counted across every learner, so `done` can exceed `total` —
    two students finishing the same story is two completions of one item.
    """
    from corner.models import StoryProgress, WritingPracticeProgress
    from examprep.models import LessonProgress
    from exam.models import ExamAttempt
    from practice.models import PracticeAttempt
    from tutorial.models import TutorialProgress

    totals = _published_counts()
    completions = {
        'practices': PracticeAttempt.objects.filter(status='completed').count(),
        'examprep': LessonProgress.objects.count(),
        'tutorials': TutorialProgress.objects.count(),
        'stories': StoryProgress.objects.count(),
        'writing': WritingPracticeProgress.objects.count(),
        'exams': ExamAttempt.objects.filter(current_section='completed').count(),
    }
    return [{
        'key': s['key'],
        'label': s['label'],
        'icon': s['icon'],
        'total': totals[s['key']],
        'completions': completions[s['key']],
    } for s in SOURCES]
