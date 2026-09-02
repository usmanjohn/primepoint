"""Choosing what to post today.

The rotation is by calendar day, not by a stored counter, so a missed day or a
re-run never shifts the cycle: 2 September is always the same subject's day.
"""
import random

from practice.models import PracticeQuestion

from .content import ROTATION, quiz_fits
from .models import TelegramPost

# How many candidates to test before giving up on a subject. Only ~0.3% of the
# bank fails quiz_fits(), so this is generous.
MAX_TRIES = 40


def subject_for(date):
    """The subject whose turn it is on `date` → (db name, uzbek label, emoji)."""
    return ROTATION[date.toordinal() % len(ROTATION)]


def rotation_from(date):
    """Today's subject first, then the rest — the order to look for a question in."""
    start = date.toordinal() % len(ROTATION)
    return ROTATION[start:] + ROTATION[:start]


def subjects_posted_on(date):
    """Which subjects already had a question go out on `date`.

    Derived from the questions themselves rather than a column on TelegramPost,
    so the daily guard needs no extra field: a re-run posts nothing twice.
    """
    ids = (TelegramPost.objects
           .filter(kind=TelegramPost.QUIZ, posted_at__date=date)
           .values_list('object_id', flat=True))
    if not ids:
        return set()
    return set(PracticeQuestion.objects
               .filter(id__in=list(ids))
               .values_list('practice__subject__name', flat=True))


def used_question_ids():
    return set(TelegramPost.objects
               .filter(kind=TelegramPost.QUIZ)
               .values_list('object_id', flat=True))


def pick_question(date, subject_name=None):
    """An unposted, poll-shaped question for `date` → (question, subject name).

    Falls through to the next subject in the rotation when today's is exhausted,
    so the daily post keeps working even after a subject runs dry.
    """
    used = used_question_ids()
    if subject_name:
        wanted = [row for row in ROTATION if row[0] == subject_name] or [(subject_name, subject_name, '📚')]
    else:
        wanted = rotation_from(date)

    for name, _label, _emoji in wanted:
        candidates = list(
            PracticeQuestion.objects
            .filter(practice__is_published=True, practice__subject__name=name)
            .exclude(id__in=used)
            .values_list('id', flat=True)
        )
        if not candidates:
            continue
        random.Random(date.toordinal()).shuffle(candidates)
        for question_id in candidates[:MAX_TRIES]:
            question = (PracticeQuestion.objects
                        .select_related('practice', 'practice__subject')
                        .prefetch_related('choices')
                        .get(id=question_id))
            if quiz_fits(question):
                return question, name
    return None, None


def remaining_by_subject():
    """How many unposted questions each subject still has — for the status command."""
    used = used_question_ids()
    counts = {}
    for name, label, _emoji in ROTATION:
        counts[label] = (PracticeQuestion.objects
                         .filter(practice__is_published=True, practice__subject__name=name)
                         .exclude(id__in=used)
                         .count())
    return counts
