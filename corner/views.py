from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.db.models import F, Count, Q
from django.urls import reverse
from django.utils.translation import gettext as _
from django.views.decorators.http import require_POST

from examprep.models import WritingDrill
from .models import (Subject, Collection, Story, StoryProgress,
                     WritingTemplate, STORY_POINTS)
from prime.subjects import get_study_subjects, value_visible
from prime.printing import require_staff, bar_context


def _can_edit(user, story):
    """Staff, or the story's own author, may edit on-page."""
    if not user.is_authenticated:
        return False
    return user.is_staff or (story.author_id and story.author_id == user.id)


def _published_filter(user):
    """Staff see drafts too; everyone else only published items."""
    return {} if user.is_staff else {'is_published': True}


def _finished_ids(user, collection):
    """IDs of stories in this collection the user has finished."""
    if not user.is_authenticated:
        return set()
    return set(StoryProgress.objects
               .filter(user=user, story__collection=collection)
               .values_list('story_id', flat=True))


def corner_home(request):
    """Subject shelves as cards, plus a hero link to writing templates."""
    subjects = (
        Subject.objects
        .filter(is_published=True)
        .annotate(
            story_count=Count('collections__stories',
                              filter=Q(collections__is_published=True,
                                       collections__stories__is_published=True),
                              distinct=True),
            template_count=Count('writing_templates',
                                 filter=Q(writing_templates__is_published=True),
                                 distinct=True),
        )
    )
    # Study-subject preference: applies unless the visitor asked for ?all=1
    personalized = False
    slugs = get_study_subjects(request)
    if slugs and not request.GET.get('all'):
        subjects = [s for s in subjects
                    if value_visible(s.slug, slugs, 'corner_subjects')]
        personalized = True
    template_total = WritingTemplate.objects.filter(is_published=True).count()
    return render(request, 'corner/home.html', {
        'subjects': subjects,
        'template_total': template_total,
        'personalized': personalized,
    })


def corner_subject(request, subject_slug):
    """One subject: its story collections and writing templates."""
    pub = _published_filter(request.user)
    subject = get_object_or_404(Subject, slug=subject_slug, **pub)

    collections = list(
        subject.collections.filter(**pub)
        .annotate(story_count=Count('stories', filter=Q(stories__is_published=True)))
    )
    if request.user.is_authenticated:
        finished = set(StoryProgress.objects
                       .filter(user=request.user, story__collection__subject=subject)
                       .values_list('story__collection_id', 'story_id'))
        for c in collections:
            done = sum(1 for cid, _sid in finished if cid == c.id)
            c.finished_count = done
            c.percent = round(done / c.story_count * 100) if c.story_count else 0

    templates = subject.writing_templates.filter(**pub)
    return render(request, 'corner/subject_detail.html', {
        'subject': subject,
        'collections': collections,
        'templates': templates,
    })


def corner_collection(request, subject_slug, collection_slug):
    """One collection: its stories in reading order with finished checkmarks."""
    pub = _published_filter(request.user)
    collection = get_object_or_404(
        Collection.objects.select_related('subject'),
        subject__slug=subject_slug, slug=collection_slug, **pub,
    )
    stories = list(collection.stories.filter(**pub))
    finished_ids = _finished_ids(request.user, collection)
    for s in stories:
        s.is_finished = s.id in finished_ids
    percent = round(len(finished_ids) / len(stories) * 100) if stories else 0

    return render(request, 'corner/collection_detail.html', {
        'subject': collection.subject,
        'collection': collection,
        'stories': stories,
        'finished_count': len(finished_ids),
        'percent': percent,
    })


def corner_story(request, subject_slug, collection_slug, slug):
    """The reader: paper page, highlighted vocab, flashcards, finish button."""
    pub = _published_filter(request.user)
    story = get_object_or_404(
        Story.objects.select_related('collection__subject'),
        collection__subject__slug=subject_slug,
        collection__slug=collection_slug, slug=slug, **pub,
    )
    collection = story.collection

    siblings = list(collection.stories.filter(**pub))
    index = siblings.index(story)
    prev_story = siblings[index - 1] if index > 0 else None
    next_story = siblings[index + 1] if index < len(siblings) - 1 else None

    finished_ids = _finished_ids(request.user, collection)
    percent = round(len(finished_ids) / len(siblings) * 100) if siblings else 0

    Story.objects.filter(pk=story.pk).update(views=F('views') + 1)

    return render(request, 'corner/story_detail.html', {
        'subject': collection.subject,
        'collection': collection,
        'story': story,
        'words': list(story.words.all()),
        'grammar': list(story.grammar.all()),
        'questions': list(story.questions.all()),
        'current_no': index + 1,
        'total_no': len(siblings),
        'prev_story': prev_story,
        'next_story': next_story,
        'is_finished': story.id in finished_ids,
        'percent': percent,
        'story_points': STORY_POINTS,
        'can_edit': _can_edit(request.user, story),
    })


def corner_story_print(request, subject_slug, collection_slug, slug):
    """One reading as a print sheet — text, vocabulary table, grammar, quiz.

    Staff only (see prime.printing): the reader is open to everyone, a
    distributable copy of it is not.
    """
    denied = require_staff(request)
    if denied:
        return denied
    story = get_object_or_404(
        Story.objects.select_related('collection__subject'),
        collection__subject__slug=subject_slug,
        collection__slug=collection_slug, slug=slug,
    )
    back_url = reverse('corner_story', args=[subject_slug, collection_slug, slug])
    context = bar_context(request, back_url, show_gloss=True)
    context.update({'story': story, 'sheet_title': story.title})
    return render(request, 'printing/single.html', context)


@login_required
@require_POST
def corner_story_finish(request, subject_slug, collection_slug, slug):
    """Mark a story finished; award points to the panda once."""
    story = get_object_or_404(
        Story.objects.select_related('collection__subject'),
        collection__subject__slug=subject_slug,
        collection__slug=collection_slug, slug=slug,
        **_published_filter(request.user),
    )
    progress, created = StoryProgress.objects.get_or_create(
        user=request.user, story=story,
        defaults={'points_awarded': STORY_POINTS},
    )
    if created:
        try:
            request.user.profile.panda.recalc_rating()
            messages.success(request, _('Story finished! +%(points)d points') % {'points': STORY_POINTS})
        except Exception:
            messages.success(request, _('Story finished!'))
    else:
        messages.info(request, _('You already finished this story.'))
    return redirect('corner_story', subject_slug=subject_slug,
                    collection_slug=collection_slug, slug=slug)


@login_required
def corner_story_edit(request, subject_slug, collection_slug, slug):
    """Raw-HTML editor for a story (author/staff only) — preserves cn-word spans."""
    story = get_object_or_404(
        Story.objects.select_related('collection__subject'),
        collection__subject__slug=subject_slug,
        collection__slug=collection_slug, slug=slug,
    )
    if not _can_edit(request.user, story):
        raise PermissionDenied

    if request.method == 'POST':
        story.title = (request.POST.get('title') or story.title).strip()
        story.summary = (request.POST.get('summary') or '')[:300]
        story.is_published = bool(request.POST.get('is_published'))
        try:
            story.order = int(request.POST.get('order', story.order))
        except (TypeError, ValueError):
            pass
        body = (request.POST.get('body') or '').strip()
        if body:
            story.body = body
        story.save()
        messages.success(request, 'Saqlandi / Saved.')
        return redirect('corner_story', subject_slug=subject_slug,
                        collection_slug=collection_slug, slug=story.slug)

    return render(request, 'corner/story_edit.html', {
        'subject': story.collection.subject,
        'collection': story.collection,
        'story': story,
    })


def corner_writing_list(request):
    """Gone — writing drills moved to examprep in July 2026 (Corner is the
    reading library now). Permanent redirect so the old sitemap URLs and any
    bookmarks still land somewhere useful."""
    return redirect('examprep_home', permanent=True)


def corner_writing_detail(request, pk):
    """Send an old drill URL to the same drill under its exam track."""
    drill = WritingDrill.objects.filter(pk=pk).select_related('track').first()
    if drill is None:
        return redirect('examprep_home', permanent=True)
    return redirect('examprep_drill', track_slug=drill.track.slug,
                    pk=drill.pk, permanent=True)


def corner_templates(request):
    """All writing templates as a card grid grouped by subject."""
    pub = _published_filter(request.user)
    templates = (WritingTemplate.objects.filter(**pub)
                 .select_related('subject')
                 .order_by('subject__order', 'subject__name', 'order', 'title'))
    return render(request, 'corner/template_list.html', {'templates': templates})


def corner_template_detail(request, pk):
    template = get_object_or_404(
        WritingTemplate.objects.select_related('subject'),
        pk=pk, **_published_filter(request.user),
    )
    return render(request, 'corner/template_detail.html', {'template': template})


def corner_template_download(request, pk):
    """Count the download, then send the visitor to the file URL."""
    template = get_object_or_404(
        WritingTemplate, pk=pk, **_published_filter(request.user),
    )
    WritingTemplate.objects.filter(pk=pk).update(downloads=F('downloads') + 1)
    return redirect(template.file.url)
