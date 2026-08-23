"""One homework, four kinds of thing inside it.

A homework used to be a practice and nothing else, so every screen could just
read `homework.practice`. Now it can hold a tutorial, a Corner reading and an
exam-prep lesson as well, and four screens — the master's classroom list, the
pupil's inbox, the assignment detail, the profile card — need the same four
questions answered about each piece: what is it called, where does it live,
what icon does it wear, and has this pupil finished it?

Answering them in one place is what keeps those screens honest with each
other. Adding a fifth library means adding one block to `homework_items` and
one line to `_DONE` — nothing else changes.
"""
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


LABELS = {
    'practice':    _('Practice'),
    'tutorial':    _('Lesson'),
    'story':       _('Reading'),
    'exam_lesson': _('Exam prep'),
}

ICONS = {
    'practice':    'bi-journal-check',
    'tutorial':    'bi-journal-text',
    'story':       'bi-stars',
    'exam_lesson': 'bi-journal-bookmark',
}


def _row(kind, obj, url, title, subtitle=''):
    return {
        'kind': kind, 'obj': obj, 'url': url, 'title': title,
        'subtitle': subtitle, 'label': LABELS[kind], 'icon': ICONS[kind],
    }


def story_url(story):
    return reverse('corner_story', args=[
        story.collection.subject.slug, story.collection.slug, story.slug])


def exam_lesson_url(lesson):
    return reverse('examprep_lesson', args=[
        lesson.track.slug, lesson.skill, lesson.slug])


def homework_items(homework):
    """Every piece of a homework, in the order a pupil should meet them:
    read the lesson, then the reading, then sit the practice."""
    rows = []
    for t in homework.tutorials.all():
        rows.append(_row('tutorial', t, reverse('tutorial_detail', args=[t.pk]),
                         t.title, t.get_category_display()))
    for l in homework.exam_lessons.select_related('track').all():
        rows.append(_row('exam_lesson', l, exam_lesson_url(l), l.title,
                         f'{l.track.name} · {l.get_skill_display()}'))
    for s in homework.stories.select_related('collection__subject').all():
        rows.append(_row('story', s, story_url(s), s.title, s.collection.title))
    for p in homework.practices.select_related('subject').all():
        rows.append(_row('practice', p, reverse('practice_detail', args=[p.pk]),
                         p.title, p.subject.name if p.subject_id else ''))
    return rows


# ── Has this pupil finished it? ────────────────────────────────────────────
# Each reader takes (obj, user, panda) and answers yes or no. Practice is the
# odd one out: it hangs off the Panda (attempts are scored), the other three
# hang off the User (progress rows are flat completions).

def _practice_done(obj, user, panda):
    return bool(panda) and obj.attempts.filter(panda=panda, status='completed').exists()


def _tutorial_done(obj, user, panda):
    return obj.progress.filter(user=user).exists()


def _story_done(obj, user, panda):
    return obj.progress.filter(user=user).exists()


def _exam_lesson_done(obj, user, panda):
    return obj.progress.filter(user=user).exists()


_DONE = {
    'practice':    _practice_done,
    'tutorial':    _tutorial_done,
    'story':       _story_done,
    'exam_lesson': _exam_lesson_done,
}


def mark_done(rows, panda):
    """Add a `done` flag to each row for this pupil, in place."""
    user = getattr(getattr(panda, 'profile', None), 'user', None)
    for row in rows:
        row['done'] = bool(user) and _DONE[row['kind']](row['obj'], user, panda)
    return rows


def refresh_for(panda, only_containing=None):
    """Re-check every pending homework this pupil holds.

    Called after a pupil finishes anything — a practice, a tutorial, a reading,
    an exam-prep lesson. `only_containing` narrows the sweep to the homeworks
    that actually contain the thing just finished, which is the common case and
    keeps the hook cheap; without it every pending assignment is re-checked.
    """
    from .models import HomeworkAssignment
    qs = HomeworkAssignment.objects.filter(panda=panda).exclude(status='graded')
    if only_containing is not None:
        qs = qs.filter(only_containing)
    for assignment in qs.select_related('homework').distinct():
        assignment.refresh()


def tick_off(user, kind, obj):
    """A pupil just finished something — re-check the homeworks holding it.

    Called from the four "finish" views. Cheap (one narrowed queryset) and
    idempotent, so it is safe to call on a repeat finish as well as the first.
    """
    from django.db.models import Q

    panda = getattr(getattr(user, 'profile', None), 'panda', None)
    if panda is None or kind not in _DONE:
        return
    field = {'practice': 'practices', 'tutorial': 'tutorials',
             'story': 'stories', 'exam_lesson': 'exam_lessons'}[kind]
    refresh_for(panda, Q(**{f'homework__{field}': obj}))
