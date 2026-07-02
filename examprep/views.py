from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import F, Count, Q, Max
from django.http import Http404

from .models import ExamTrack, Lesson, LessonBlock, SKILL_CHOICES, SKILL_ICONS


def _can_edit(user, lesson):
    """Staff, or the lesson's own author, may edit on-page."""
    if not user.is_authenticated:
        return False
    return user.is_staff or (lesson.author_id and lesson.author_id == user.id)


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
