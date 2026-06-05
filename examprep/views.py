from django.shortcuts import render, get_object_or_404
from django.db.models import F, Count, Q

from .models import ExamTrack, Lesson, SKILL_CHOICES, SKILL_ICONS


def examprep_home(request):
    """List published exam tracks as cards."""
    tracks = (
        ExamTrack.objects
        .filter(is_published=True)
        .annotate(lesson_count=Count('lessons', filter=Q(lessons__is_published=True)))
    )
    return render(request, 'examprep/home.html', {
        'tracks': tracks,
    })


def track_detail(request, slug):
    """One track; its lessons grouped by skill."""
    staff = request.user.is_staff
    track = get_object_or_404(
        ExamTrack, slug=slug, **({} if staff else {'is_published': True})
    )

    lessons_qs = track.lessons.all()
    if not staff:
        lessons_qs = lessons_qs.filter(is_published=True)

    # Group lessons by skill, preserving the SKILL_CHOICES order.
    grouped = []
    for value, label in SKILL_CHOICES:
        skill_lessons = [l for l in lessons_qs if l.skill == value]
        if skill_lessons:
            grouped.append({
                'value':   value,
                'label':   label,
                'icon':    SKILL_ICONS.get(value, 'bi-journal-text'),
                'lessons': skill_lessons,
            })

    return render(request, 'examprep/track_detail.html', {
        'track':   track,
        'grouped': grouped,
        'total':   len(lessons_qs),
    })


def lesson_detail(request, track_slug, slug):
    """Render a lesson's blocks; check MCQ answers statelessly on POST."""
    staff = request.user.is_staff
    lesson = get_object_or_404(
        Lesson.objects.select_related('track'),
        track__slug=track_slug, slug=slug,
        **({} if staff else {'is_published': True}),
    )

    blocks = list(lesson.blocks.prefetch_related('choices').all())
    has_mcq = any(b.block_type == 'mcq' for b in blocks)

    submitted = request.method == 'POST'
    if submitted:
        # Stateless check: mark each choice and the block result, no DB writes.
        for block in blocks:
            if block.block_type != 'mcq':
                continue
            raw = request.POST.get(f'mcq_{block.id}')
            selected_id = int(raw) if (raw and raw.isdigit()) else None
            correct = next((c for c in block.choices.all() if c.is_correct), None)
            block.selected_id = selected_id
            block.is_correct = bool(correct and selected_id == correct.id)
            block.answered = selected_id is not None
            for choice in block.choices.all():
                choice.was_selected = (choice.id == selected_id)
    else:
        # Count a view only on plain reads, not on answer submissions.
        Lesson.objects.filter(pk=lesson.pk).update(views=F('views') + 1)

    return render(request, 'examprep/lesson_detail.html', {
        'lesson':    lesson,
        'blocks':    blocks,
        'has_mcq':   has_mcq,
        'submitted': submitted,
    })
