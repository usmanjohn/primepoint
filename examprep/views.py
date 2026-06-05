from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F, Count, Q
from django.http import Http404

from .models import ExamTrack, Lesson, SKILL_CHOICES, SKILL_ICONS


def _published_filter(user):
    """Staff see drafts too; everyone else only published items."""
    return {} if user.is_staff else {'is_published': True}


def examprep_home(request):
    """List published exam tracks as cards."""
    tracks = (
        ExamTrack.objects
        .filter(is_published=True)
        .annotate(lesson_count=Count('lessons', filter=Q(lessons__is_published=True)))
    )
    return render(request, 'examprep/home.html', {'tracks': tracks})


def track_detail(request, track_slug):
    """One track; its skills (Reading, Writing, ...) shown as a playlist menu."""
    pub = _published_filter(request.user)
    track = get_object_or_404(ExamTrack, slug=track_slug, **pub)

    lessons = list(track.lessons.filter(**pub))

    # Group by skill, preserving SKILL_CHOICES order; link each to its first lesson.
    groups = []
    for value, label in SKILL_CHOICES:
        skill_lessons = [l for l in lessons if l.skill == value]
        if skill_lessons:
            groups.append({
                'value':   value,
                'label':   label,
                'icon':    SKILL_ICONS.get(value, 'bi-journal-text'),
                'count':   len(skill_lessons),
                'first':   skill_lessons[0],
            })

    return render(request, 'examprep/track_detail.html', {
        'track':  track,
        'groups': groups,
    })


def skill_redirect(request, track_slug, skill):
    """Jump straight to the first lesson of a skill within a track."""
    pub = _published_filter(request.user)
    track = get_object_or_404(ExamTrack, slug=track_slug, **pub)
    first = track.lessons.filter(skill=skill, **pub).first()
    if not first:
        raise Http404('No lessons in this section yet.')
    return redirect('examprep_lesson', track_slug=track.slug, skill=skill, slug=first.slug)


def lesson_detail(request, track_slug, skill, slug):
    """A lesson 'player': its blocks, plus prev/next + a jump list for the skill."""
    pub = _published_filter(request.user)
    lesson = get_object_or_404(
        Lesson.objects.select_related('track'),
        track__slug=track_slug, skill=skill, slug=slug, **pub,
    )

    # Ordered siblings in the same track + skill drive the playlist navigation.
    siblings = list(lesson.track.lessons.filter(skill=skill, **pub))
    index = siblings.index(lesson)
    prev_lesson = siblings[index - 1] if index > 0 else None
    next_lesson = siblings[index + 1] if index < len(siblings) - 1 else None

    blocks = list(lesson.blocks.prefetch_related('choices').all())
    has_question = any(b.choices.exists() for b in blocks)

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
    })
