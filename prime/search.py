"""Platform-wide search.

Search used to cover masters, practices and discussions only, which made the
rest of the platform — tutorials, exam prep, the Corner library, exams, games —
invisible to anyone who typed into the top bar. This module queries every
public content type and returns them as uniform groups so the results template
renders one loop instead of a hand-written block per source.

A group is::

    {'key', 'label', 'icon', 'items': [{'title', 'meta', 'url'}], 'count'}

`count` is the true number of matches; `items` is capped at PER_GROUP so one
noisy source can't bury the others.
"""
from django.db.models import Q
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

PER_GROUP = 6


def _group(key, label, icon, items, count):
    return {'key': key, 'label': label, 'icon': icon, 'items': items, 'count': count}


def _join(*parts):
    """Meta line from whichever parts are non-empty."""
    return ' · '.join(str(p) for p in parts if p)


def _tutorials(q):
    from tutorial.models import Tutorial

    qs = Tutorial.objects.filter(is_published=True).filter(
        Q(title__icontains=q) | Q(summary__icontains=q)
    ).order_by('-created_at')
    items = [{
        'title': t.title,
        'meta': _join(t.get_category_display(), t.summary),
        'url': reverse('tutorial_detail', args=[t.pk]),
    } for t in qs[:PER_GROUP]]
    return _group('tutorials', _('Tutorials'), 'bi-journal-text', items, qs.count())


def _practices(q):
    from practice.models import Practice

    qs = Practice.objects.filter(is_published=True).filter(
        Q(title__icontains=q) | Q(description__icontains=q)
    ).select_related('master').order_by('-created_at')
    items = [{
        'title': p.title,
        'meta': _join(p.level and p.level.capitalize(), p.subject,
                      _('Free') if p.is_free else None),
        'url': reverse('practice_detail', args=[p.pk]),
    } for p in qs[:PER_GROUP]]
    return _group('practices', _('Practice Sets'), 'bi-book-half', items, qs.count())


def _examprep(q):
    from examprep.models import Lesson

    qs = Lesson.objects.filter(
        is_published=True, track__is_published=True
    ).filter(
        Q(title__icontains=q) | Q(summary__icontains=q)
    ).select_related('track').order_by('track__name', 'order')
    items = [{
        'title': l.title,
        'meta': _join(l.track.name, l.get_skill_display()),
        'url': reverse('examprep_lesson', kwargs={
            'track_slug': l.track.slug, 'skill': l.skill, 'slug': l.slug,
        }),
    } for l in qs[:PER_GROUP]]
    return _group('examprep', _('Exam Prep'), 'bi-journal-bookmark', items, qs.count())


def _exams(q):
    from exam.models import Exam

    qs = Exam.objects.filter(is_published=True).filter(
        title__icontains=q
    ).order_by('-created_at')
    items = [{
        'title': e.title,
        'meta': _join(e.get_language_display() if e.language else None),
        'url': reverse('exam_detail', args=[e.pk]),
    } for e in qs[:PER_GROUP]]
    return _group('exams', _('Exams'), 'bi-journal-check', items, qs.count())


def _stories(q):
    from corner.models import Story

    qs = Story.objects.filter(
        is_published=True,
        collection__is_published=True,
        collection__subject__is_published=True,
    ).filter(
        Q(title__icontains=q) | Q(summary__icontains=q)
    ).select_related('collection__subject').order_by('collection__title', 'order')
    items = [{
        'title': s.title,
        'meta': _join(s.collection.title, s.summary),
        'url': reverse('corner_story', kwargs={
            'subject_slug': s.collection.subject.slug,
            'collection_slug': s.collection.slug,
            'slug': s.slug,
        }),
    } for s in qs[:PER_GROUP]]
    return _group('stories', _('Corner Stories'), 'bi-stars', items, qs.count())


def _writing(q):
    from examprep.models import WritingDrill

    qs = WritingDrill.objects.filter(is_published=True).select_related('track').filter(
        Q(title__icontains=q) | Q(summary__icontains=q) | Q(prompt__icontains=q)
    ).order_by('qtype', 'order')
    items = [{
        'title': w.title,
        'meta': _join(w.get_qtype_display() if w.qtype else None, w.summary),
        'url': reverse('examprep_drill', kwargs={'track_slug': w.track.slug, 'pk': w.pk}),
    } for w in qs[:PER_GROUP]]
    return _group('writing', _('Writing Drills'), 'bi-pencil-square', items, qs.count())


def _games(q):
    from games.catalog import search_games

    matches = search_games(q)
    items = [{
        'title': g['name'],
        'meta': _join(g['tag'], g['description']),
        'url': reverse(g['url']),
    } for g in matches[:PER_GROUP]]
    return _group('games', _('Games'), 'bi-controller', items, len(matches))


def _masters(q):
    from masters.models import Master

    qs = Master.objects.filter(
        Q(name__icontains=q) | Q(subject__icontains=q) |
        Q(description__icontains=q) | Q(category__icontains=q)
    ).order_by('name')
    items = [{
        'title': m.name,
        'meta': _join(m.subject, m.category),
        'url': reverse('masters-detail', args=[m.pk]),
    } for m in qs[:PER_GROUP]]
    return _group('masters', _('Masters'), 'bi-person-workspace', items, qs.count())


def _pandas(q):
    from panda.models import Panda

    # Profile carries only `first_name`; the surname lives on the User row.
    qs = Panda.objects.filter(
        Q(profile__user__username__icontains=q) |
        Q(profile__user__first_name__icontains=q) |
        Q(profile__user__last_name__icontains=q) |
        Q(profile__first_name__icontains=q)
    ).select_related('profile__user').order_by('-rating')
    items = [{
        'title': p.profile.user.get_full_name() or p.profile.user.username,
        'meta': _join(f'@{p.profile.user.username}', _('%(n)s points') % {'n': p.rating}),
        'url': reverse('user_profile', args=[p.profile.user.username]),
    } for p in qs[:PER_GROUP]]
    return _group('pandas', _('Pandas'), 'bi-mortarboard-fill', items, qs.count())


def _threads(q):
    from discussion.models import Thread

    qs = Thread.objects.filter(
        Q(title__icontains=q) | Q(body__icontains=q)
    ).select_related('category', 'author').order_by('-created_at')
    items = [{
        'title': t.title,
        'meta': _join(t.category.name if t.category_id else None, t.author.username),
        'url': reverse('thread_detail', args=[t.pk]),
    } for t in qs[:PER_GROUP]]
    return _group('threads', _('Discussions'), 'bi-chat-square-dots-fill', items, qs.count())


def _classrooms(q):
    from classroom.models import Classroom

    qs = Classroom.objects.filter(is_active=True).filter(
        Q(name__icontains=q) | Q(description__icontains=q)
    ).select_related('master').order_by('name')
    items = [{
        'title': c.name,
        'meta': _join(c.master.name if c.master_id else None, c.description),
        'url': reverse('classroom:detail', args=[c.pk]),
    } for c in qs[:PER_GROUP]]
    return _group('classrooms', _('Classrooms'), 'bi-easel-fill', items, qs.count())


# Learning material first — that is what people type into a search box — then
# people, then community spaces.
SOURCES = [
    _tutorials, _practices, _examprep, _exams, _stories, _writing,
    _games, _masters, _pandas, _threads, _classrooms,
]


def search_platform(query):
    """Search every public content type. Returns (non-empty groups, total)."""
    if not query:
        return [], 0

    groups = [g for g in (source(query) for source in SOURCES) if g['count']]
    return groups, sum(g['count'] for g in groups)
