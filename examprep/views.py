import re

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import F, Count, Q, Max
from django.http import Http404

from .models import ExamTrack, Topic, Lesson, LessonBlock, SKILL_CHOICES, SKILL_ICONS


def _can_edit(user, lesson):
    """Staff, or the lesson's own author, may edit on-page."""
    if not user.is_authenticated:
        return False
    return user.is_staff or (lesson.author_id and lesson.author_id == user.id)


def _published_filter(user):
    """Staff see drafts too; everyone else only published items."""
    return {} if user.is_staff else {'is_published': True}


def examprep_home(request):
    """List published exam tracks as cards, each with its skill chips."""
    tracks = list(
        ExamTrack.objects
        .filter(is_published=True)
        .annotate(lesson_count=Count('lessons', filter=Q(lessons__is_published=True)))
    )
    skill_labels = dict(SKILL_CHOICES)
    for track in tracks:
        skills = (track.lessons.filter(is_published=True)
                  .values_list('skill', flat=True).distinct())
        track.skill_chips = [
            {'value': value, 'label': skill_labels[value],
             'icon': SKILL_ICONS.get(value, 'bi-journal-text')}
            for value, _ in SKILL_CHOICES if value in skills
        ]
    return render(request, 'examprep/home.html', {'tracks': tracks})


def track_detail(request, track_slug):
    """One track; its skills (Reading, Writing, ...) shown as cards."""
    pub = _published_filter(request.user)
    track = get_object_or_404(ExamTrack, slug=track_slug, **pub)

    lessons = list(track.lessons.filter(**pub))
    topics = list(track.topics.filter(**pub))

    # Group by skill, preserving SKILL_CHOICES order.
    groups = []
    for value, label in SKILL_CHOICES:
        skill_lessons = [l for l in lessons if l.skill == value]
        if skill_lessons:
            groups.append({
                'value':       value,
                'label':       label,
                'icon':        SKILL_ICONS.get(value, 'bi-journal-text'),
                'count':       len(skill_lessons),
                'topic_count': sum(1 for t in topics if t.skill == value),
            })

    return render(request, 'examprep/track_detail.html', {
        'track':  track,
        'groups': groups,
    })


def skill_detail(request, track_slug, skill):
    """One skill inside a track: its question-type topics as cards, each card
    listing that topic's lessons. Lessons without a topic form a final group."""
    skill_label = dict(SKILL_CHOICES).get(skill)
    if skill_label is None:
        raise Http404('Unknown section.')

    pub = _published_filter(request.user)
    track = get_object_or_404(ExamTrack, slug=track_slug, **pub)

    lessons = list(track.lessons.filter(skill=skill, **pub))
    if not lessons:
        raise Http404('No lessons in this section yet.')

    groups = []
    for topic in track.topics.filter(skill=skill, **pub):
        topic_lessons = [l for l in lessons if l.topic_id == topic.id]
        if topic_lessons:
            groups.append({'topic': topic, 'lessons': topic_lessons})

    grouped_ids = {l.id for g in groups for l in g['lessons']}
    loose_lessons = [l for l in lessons if l.id not in grouped_ids]

    return render(request, 'examprep/skill_detail.html', {
        'track':         track,
        'skill':         skill,
        'skill_label':   skill_label,
        'skill_icon':    SKILL_ICONS.get(skill, 'bi-journal-text'),
        'groups':        groups,
        'loose_lessons': loose_lessons,
        'lesson_count':  len(lessons),
    })


def lesson_detail(request, track_slug, skill, slug):
    """A lesson 'player': its blocks, plus prev/next + a jump list for the skill."""
    pub = _published_filter(request.user)
    lesson = get_object_or_404(
        Lesson.objects.select_related('track', 'topic'),
        track__slug=track_slug, skill=skill, slug=slug, **pub,
    )

    # Ordered siblings drive the playlist: lessons of the same topic when the
    # lesson belongs to one, otherwise the skill's remaining ungrouped lessons.
    siblings_qs = lesson.track.lessons.filter(skill=skill, **pub)
    if lesson.topic_id:
        siblings_qs = siblings_qs.filter(topic_id=lesson.topic_id)
    else:
        siblings_qs = siblings_qs.filter(topic__isnull=True)
    siblings = list(siblings_qs)
    index = siblings.index(lesson)
    prev_lesson = siblings[index - 1] if index > 0 else None
    next_lesson = siblings[index + 1] if index < len(siblings) - 1 else None

    blocks = list(lesson.blocks.prefetch_related('choices').all())
    has_question = any(b.choices.exists() for b in blocks)

    # Older lessons open with an <h2> repeating the lesson title, which stacks
    # a third copy under the breadcrumb and page <h1>. Hide that one heading at
    # render time (display only — nothing is saved).
    if blocks and blocks[0].rich_text:
        m = re.match(r'\s*<h2[^>]*>(.*?)</h2>', blocks[0].rich_text, re.S | re.I)
        if m:
            heading = re.sub(r'<[^>]+>', '', m.group(1))
            norm = lambda s: re.sub(r'\s+', ' ', s).strip().casefold()
            if norm(heading) == norm(lesson.title):
                blocks[0].rich_text = blocks[0].rich_text[m.end():]

    submitted = request.method == 'POST'
    if submitted:
        # Stateless check: mark each choice and the block result, no DB writes.
        for block in blocks:
            choices = list(block.choices.all())
            if not choices:
                continue
            raw = request.POST.get(f'mcq_{block.id}')
            selected_id = int(raw) if (raw and raw.isdigit()) else None
            correct = next((c for c in choices if c.is_correct), None)
            block.selected_id = selected_id
            block.is_correct = bool(correct and selected_id == correct.id)
            block.answered = selected_id is not None
            for choice in choices:
                choice.was_selected = (choice.id == selected_id)
    else:
        # Count a view only on plain reads, not on answer submissions.
        Lesson.objects.filter(pk=lesson.pk).update(views=F('views') + 1)

    skill_label = dict(SKILL_CHOICES).get(skill, skill)
    return render(request, 'examprep/lesson_detail.html', {
        'lesson':       lesson,
        'topic':        lesson.topic,
        'skill':        skill,
        'skill_label':  skill_label,
        'skill_icon':   SKILL_ICONS.get(skill, 'bi-journal-text'),
        'blocks':       blocks,
        'siblings':     siblings,
        'current_no':   index + 1,
        'total_no':     len(siblings),
        'prev_lesson':  prev_lesson,
        'next_lesson':  next_lesson,
        'has_question': has_question,
        'submitted':    submitted,
        'can_edit':     _can_edit(request.user, lesson),
    })


@login_required
def lesson_edit(request, track_slug, skill, slug):
    """On-page editor for a lesson and its content blocks (author/staff only)."""
    lesson = get_object_or_404(
        Lesson.objects.select_related('track'),
        track__slug=track_slug, skill=skill, slug=slug,
    )
    if not _can_edit(request.user, lesson):
        raise PermissionDenied

    blocks = list(lesson.blocks.all())

    if request.method == 'POST':
        lesson.title = (request.POST.get('title') or lesson.title).strip()
        lesson.summary = (request.POST.get('summary') or '')[:300]
        lesson.is_published = bool(request.POST.get('is_published'))
        try:
            lesson.order = int(request.POST.get('order', lesson.order))
        except (TypeError, ValueError):
            pass
        lesson.save()

        for b in blocks:
            if request.POST.get(f'delete_{b.id}'):
                b.delete()
                continue
            b.rich_text = (request.POST.get(f'rich_text_{b.id}') or '') or None
            b.explanation = (request.POST.get(f'explanation_{b.id}') or '') or None
            b.caption = (request.POST.get(f'caption_{b.id}') or '')[:300]
            try:
                b.order = int(request.POST.get(f'order_{b.id}', b.order))
            except (TypeError, ValueError):
                pass
            b.save()

        new_html = (request.POST.get('new_rich_text') or '').strip()
        if new_html:
            nxt = (lesson.blocks.aggregate(m=Max('order'))['m'] or 0) + 1
            LessonBlock.objects.create(lesson=lesson, order=nxt, rich_text=new_html)

        messages.success(request, 'Saqlandi / Saved.')
        return redirect('examprep_lesson', track_slug=lesson.track.slug,
                        skill=skill, slug=lesson.slug)

    return render(request, 'examprep/lesson_edit.html', {
        'lesson': lesson,
        'skill':  skill,
        'blocks': blocks,
    })
