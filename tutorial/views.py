from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import F, Count, Q
from django.http import JsonResponse, Http404
from django.urls import reverse

from django.utils.translation import gettext as _
from django.views.decorators.http import require_POST

from prime import reading
from .models import (Tutorial, TutorialReaction, TutorialPlaylist, PlaylistTutorial,
                     TutorialProgress, TUTORIAL_POINTS, CATEGORY_CHOICES)
from .forms import TutorialForm, TutorialPlaylistForm
from prime.subjects import get_study_subjects, allowed_values, mapped_values
from prime.printing import (require_staff, bar_context, qs_with,
                            lesson_range, lesson_rows, answer_key, glossary)
from prime import books as book_registry


def _save_playlist_assignment(tutorial, form):
    playlist = form.cleaned_data.get('playlist')
    order    = form.cleaned_data.get('playlist_order') or 0
    PlaylistTutorial.objects.filter(tutorial=tutorial).delete()
    if playlist:
        PlaylistTutorial.objects.create(tutorial=tutorial, playlist=playlist, order=order)


def _can_create(user):
    if not user.is_authenticated:
        return False
    if user.is_staff:
        return True
    try:
        return hasattr(user.profile, 'master') and user.profile.master.is_approved
    except Exception:
        return False


def tutorial_list(request):
    qs = (
        Tutorial.objects
        .filter(is_published=True)
        .select_related('author')
        .annotate(like_count=Count('reactions', filter=Q(reactions__reaction='like')))
        .order_by('-created_at')
    )

    category = request.GET.get('category', '')
    if category:
        qs = qs.filter(category=category)

    # Study-subject preference: applies only without an explicit filter or ?all=1
    personalized = False
    slugs = get_study_subjects(request)
    if slugs and not category and not request.GET.get('all'):
        chosen = allowed_values(slugs, 'tutorial_categories')
        unmapped = {c for c, _ in CATEGORY_CHOICES} - mapped_values('tutorial_categories')
        qs = qs.filter(category__in=chosen | unmapped)
        personalized = True

    paginator = Paginator(qs, 12)
    tutorials  = paginator.get_page(request.GET.get('page'))

    return render(request, 'tutorial/tutorial_list.html', {
        'tutorials':       tutorials,
        'active_category': category,
        'categories':      CATEGORY_CHOICES,
        'can_create':      _can_create(request.user),
        'total_count':     Tutorial.objects.filter(is_published=True).count(),
        'personalized':    personalized,
    })


def tutorial_detail(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk, is_published=True)
    Tutorial.objects.filter(pk=pk).update(views=F('views') + 1)
    reading.mark_opened(request, 'tutorial', pk)

    related = Tutorial.objects.filter(
        category=tutorial.category, is_published=True
    ).exclude(pk=pk).order_by('-created_at')[:4]

    can_edit = request.user.is_authenticated and (
        request.user == tutorial.author or request.user.is_staff
    )

    like_count    = tutorial.reactions.filter(reaction='like').count()
    dislike_count = tutorial.reactions.filter(reaction='dislike').count()
    user_reaction = None
    is_finished   = False
    if request.user.is_authenticated:
        r = tutorial.reactions.filter(user=request.user).first()
        user_reaction = r.reaction if r else None
        is_finished = TutorialProgress.objects.filter(
            user=request.user, tutorial=tutorial).exists()

    # Playlist navigation context
    playlist_context = None
    pl_item = PlaylistTutorial.objects.filter(tutorial=tutorial).select_related('playlist').order_by('playlist__created_at').first()
    if pl_item and pl_item.playlist.is_published:
        siblings = list(pl_item.playlist.items.select_related('tutorial'))
        idx = next((i for i, s in enumerate(siblings) if s.tutorial_id == tutorial.pk), None)
        if idx is not None:
            playlist_context = {
                'playlist': pl_item.playlist,
                'position': idx + 1,
                'total':    len(siblings),
                'prev':     siblings[idx - 1].tutorial if idx > 0 else None,
                'next':     siblings[idx + 1].tutorial if idx < len(siblings) - 1 else None,
            }

    return render(request, 'tutorial/tutorial_detail.html', {
        'tutorial':         tutorial,
        'related':          related,
        'can_edit':         can_edit,
        'like_count':       like_count,
        'dislike_count':    dislike_count,
        'user_reaction':    user_reaction,
        'is_finished':      is_finished,
        'tutorial_points':  TUTORIAL_POINTS,
        'linked_practices': tutorial.practices.filter(is_published=True),
        'linked_stories':   tutorial.stories.filter(is_published=True)
                                            .select_related('collection'),
        'playlist_context': playlist_context,
    })


@login_required
def tutorial_react(request, pk):
    if request.method != 'POST':
        return redirect('tutorial_detail', pk=pk)

    tutorial = get_object_or_404(Tutorial, pk=pk, is_published=True)
    reaction_type = request.POST.get('reaction')

    if reaction_type not in ('like', 'dislike'):
        return redirect('tutorial_detail', pk=pk)

    user_reaction = None
    existing = TutorialReaction.objects.filter(user=request.user, tutorial=tutorial).first()
    if existing:
        if existing.reaction == reaction_type:
            existing.delete()
        else:
            existing.reaction = reaction_type
            existing.save()
            user_reaction = reaction_type
    else:
        TutorialReaction.objects.create(user=request.user, tutorial=tutorial, reaction=reaction_type)
        user_reaction = reaction_type

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'like_count': tutorial.reactions.filter(reaction='like').count(),
            'dislike_count': tutorial.reactions.filter(reaction='dislike').count(),
            'user_reaction': user_reaction,
        })

    return redirect('tutorial_detail', pk=pk)


@login_required
def tutorial_create(request):
    if not _can_create(request.user):
        raise PermissionDenied

    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES, user=request.user)
        if form.is_valid():
            tut = form.save(commit=False)
            tut.author = request.user
            tut.save()
            form.save_m2m()
            _save_playlist_assignment(tut, form)
            messages.success(request, 'Tutorial published successfully!')
            return redirect('tutorial_detail', pk=tut.pk)
    else:
        form = TutorialForm(user=request.user)

    return render(request, 'tutorial/tutorial_form.html', {'form': form})


@login_required
def tutorial_edit(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    if not (request.user == tutorial.author or request.user.is_staff):
        raise PermissionDenied

    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES, instance=tutorial, user=request.user)
        if form.is_valid():
            form.save()
            _save_playlist_assignment(tutorial, form)
            messages.success(request, 'Tutorial updated.')
            return redirect('tutorial_detail', pk=tutorial.pk)
    else:
        form = TutorialForm(instance=tutorial, user=request.user)

    return render(request, 'tutorial/tutorial_form.html', {
        'form': form, 'tutorial': tutorial,
    })


@login_required
def tutorial_delete(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    if not (request.user == tutorial.author or request.user.is_staff):
        raise PermissionDenied

    if request.method == 'POST':
        tutorial.delete()
        messages.success(request, 'Tutorial deleted.')
        return redirect('tutorial_list')

    return render(request, 'tutorial/tutorial_confirm_delete.html', {
        'tutorial': tutorial,
    })


# ── Playlist views ────────────────────────────────────────────────────────────

def playlist_list(request):
    qs = (
        TutorialPlaylist.objects
        .filter(is_published=True)
        .select_related('author')
        .annotate(tutorial_count=Count('items'))
        .order_by('-created_at')
    )
    category = request.GET.get('category', '')
    if category:
        qs = qs.filter(category=category)

    paginator = Paginator(qs, 12)
    playlists = paginator.get_page(request.GET.get('page'))

    return render(request, 'tutorial/playlist_list.html', {
        'playlists':       playlists,
        'active_category': category,
        'categories':      CATEGORY_CHOICES,
        'can_create':      _can_create(request.user),
        'total_count':     TutorialPlaylist.objects.filter(is_published=True).count(),
    })


def playlist_detail(request, pk):
    playlist = get_object_or_404(TutorialPlaylist, pk=pk, is_published=True)
    items    = playlist.items.select_related('tutorial').filter(tutorial__is_published=True)
    can_edit = request.user.is_authenticated and (
        request.user == playlist.author or request.user.is_staff
    )
    # Quick-pick ranges for the staff print card: 1-10, 11-20, … Built here
    # because a Django template cannot count in tens.
    total = len(items)
    print_ranges = [{'start': s, 'end': min(s + 9, total)}
                    for s in range(1, total + 1, 10)]
    # Courses that are a printable series (prime/books.py) also offer the
    # bound-book link; everything else just gets the handout above it.
    book = book_registry.book_for(playlist)
    return render(request, 'tutorial/playlist_detail.html', {
        'playlist':      playlist,
        'items':         items,
        'can_edit':      can_edit,
        'print_ranges':  print_ranges,
        'total_items':   total,
        # Volume bounds are positions in the whole playlist, unpublished
        # lessons included — the same count playlist_book clamps against.
        'book_volumes':  book_registry.volumes(book, playlist.items.count()) if book else [],
    })


def tutorial_print(request, pk):
    """One tutorial as a print sheet. Staff only — see prime.printing."""
    denied = require_staff(request)
    if denied:
        return denied
    tutorial = get_object_or_404(Tutorial, pk=pk)
    context = bar_context(request, reverse('tutorial_detail', args=[pk]))
    context.update({'tutorial': tutorial, 'sheet_title': tutorial.title})
    return render(request, 'printing/single.html', context)


def playlist_print(request, pk):
    """A range of a playlist as one booklet — cover, contents, then each
    lesson with its practice and its reading. Staff only.

    ?from= / ?to=  1-based positions in the playlist (default the first ten,
                   capped at MAX_BUNDLE_LESSONS unless ?cap=0)
    ?parts=        subset of tutorial,practice,reading
    ?answers=0     pupil copy
    ?gloss=1       print cn-word translations inline
    """
    denied = require_staff(request)
    if denied:
        return denied
    playlist = get_object_or_404(TutorialPlaylist, pk=pk)

    total        = playlist.items.count()
    start, end   = lesson_range(request, total)
    context      = bar_context(request, reverse('playlist_detail', args=[pk]),
                                      show_gloss=True)
    parts        = context['options']['parts']
    context.update({
        'playlist':      playlist,
        'lessons':       lesson_rows(playlist, start, end),
        'start':         start,
        'end':           end,
        'total':         total,
        'show_tutorial': 'tutorial' in parts,
        'show_practice': 'practice' in parts,
        'show_reading':  'reading' in parts,
    })
    return render(request, 'printing/bundle.html', context)


def playlist_book(request, pk):
    """A volume of a playlist as a bound book — covers, front matter, lessons,
    answer key, glossary. Staff only.

    The older `playlist_print` gives the same lessons as a stapled handout;
    this gives them as a printed volume, which is why it needs Paged.js: page
    numbers, running heads, a contents list that knows what page a lesson is
    on and blank versos so chapters open on the right are all CSS Paged Media
    features Chrome does not implement on its own.

    ?vol=2      which volume (from prime/books.py); ignored if ?from=/?to= given
    ?from=/?to= a custom range, same semantics as playlist_print
    ?key=inline answers beside the questions instead of in the key at the back
    ?answers=0  pupil copy (drops the key and the explanations entirely)
    ?gloss=1    print cn-word translations inline in the readings too
    ?paged=0    skip Paged.js: no page numbers, no running heads and no
                contents page numbers, but it renders instantly. Everything
                else — the A5 geometry, the covers, the front matter, the
                chapter breaks, the answer key, the glossary — is plain CSS
                and does not depend on it.
    """
    denied = require_staff(request)
    if denied:
        return denied
    playlist = get_object_or_404(TutorialPlaylist, pk=pk)
    book     = book_registry.book_for(playlist)
    if not book:
        raise Http404('This playlist is not a printable book series.')

    total = playlist.items.count()
    try:
        vol = book_registry.volume(book, total, int(request.GET.get('vol', 1)))
    except (TypeError, ValueError):
        vol = book_registry.volume(book, total, 1)

    # An explicit range wins over the volume, so a teacher can bind lessons
    # 7-12 for one pupil without the registry knowing about it.
    if 'from' in request.GET or 'to' in request.GET:
        start, end = lesson_range(request, total)
        vol = dict(vol or {}, start=start, end=end, custom=True)
    if not vol:
        raise Http404('This playlist has no lessons to bind.')

    rows       = lesson_rows(playlist, vol['start'], vol['end'])
    context    = bar_context(request, reverse('playlist_detail', args=[pk]),
                             show_gloss=True)
    key_at_back = request.GET.get('key') != 'inline'
    recto       = request.GET.get('recto') != '0'
    book_url    = reverse('playlist_book', args=[pk])
    context.update({
        # The book's own toggles. `vol` clears from/to so the volume picker
        # escapes a custom range rather than being overruled by it.
        'url_key_back':   qs_with(request, key=None),
        'url_key_inline': qs_with(request, key='inline'),
        'url_recto_on':   qs_with(request, recto=None),
        'url_recto_off':  qs_with(request, recto=0),
        'vol_urls': [
            dict(v, url=book_url + qs_with(request, vol=v['n'], **{'from': None, 'to': None}))
            for v in book_registry.volumes(book, total)
        ],
        'recto': recto,
    })
    context.update({
        'playlist':    playlist,
        'book':        book,
        'vol':         vol,
        'lessons':     rows,
        'total':       total,
        'key_at_back': key_at_back,
        'answer_key':  answer_key(rows) if context['answers'] and key_at_back else [],
        'glossary':    glossary(rows),
        'paged':       request.GET.get('paged') != '0',
        'brand':       book_registry.BRAND,
        'site':        book_registry.SITE,
        'slogan':      book_registry.SLOGAN,
        'rights':      book_registry.RIGHTS,
    })
    return render(request, 'printing/book.html', context)


@login_required
def playlist_create(request):
    if not _can_create(request.user):
        raise PermissionDenied

    if request.method == 'POST':
        form = TutorialPlaylistForm(request.POST, request.FILES)
        if form.is_valid():
            pl = form.save(commit=False)
            pl.author = request.user
            pl.save()
            messages.success(request, 'Playlist created!')
            return redirect('playlist_detail', pk=pl.pk)
    else:
        form = TutorialPlaylistForm()

    return render(request, 'tutorial/playlist_form.html', {'form': form})


@login_required
def playlist_edit(request, pk):
    playlist = get_object_or_404(TutorialPlaylist, pk=pk)
    if not (request.user == playlist.author or request.user.is_staff):
        raise PermissionDenied

    if request.method == 'POST':
        form = TutorialPlaylistForm(request.POST, request.FILES, instance=playlist)
        if form.is_valid():
            form.save()
            messages.success(request, 'Playlist updated.')
            return redirect('playlist_detail', pk=playlist.pk)
    else:
        form = TutorialPlaylistForm(instance=playlist)

    return render(request, 'tutorial/playlist_form.html', {
        'form': form, 'playlist': playlist,
    })


@login_required
def playlist_delete(request, pk):
    playlist = get_object_or_404(TutorialPlaylist, pk=pk)
    if not (request.user == playlist.author or request.user.is_staff):
        raise PermissionDenied

    if request.method == 'POST':
        playlist.delete()
        messages.success(request, 'Playlist deleted.')
        return redirect('playlist_list')

    return render(request, 'tutorial/playlist_confirm_delete.html', {
        'playlist': playlist,
    })


@login_required
@require_POST
def tutorial_finish(request, pk):
    """Mark a tutorial read; award points to the panda once."""
    tutorial = get_object_or_404(Tutorial, pk=pk, is_published=True)

    # "Mark as finished" used to be worth 4 points for one click. It now has to
    # arrive after the page has been open long enough to have been read — see
    # prime/reading.py for what this does and does not prove.
    wait = reading.too_soon(request, 'tutorial', pk, tutorial.content)
    if wait:
        messages.warning(
            request,
            _('Not so fast — stay with the lesson a little longer (about '
              '%(secs)d more seconds) and then mark it finished.')
            % {'secs': wait})
        return redirect('tutorial_detail', pk=pk)

    progress, created = TutorialProgress.objects.get_or_create(
        user=request.user, tutorial=tutorial,
        defaults={'points_awarded': TUTORIAL_POINTS},
    )
    if created:
        try:
            request.user.profile.panda.recalc_rating()
            messages.success(request, _('Tutorial finished! +%(points)d points')
                             % {'points': TUTORIAL_POINTS})
        except Exception:
            messages.success(request, _('Tutorial finished!'))
    else:
        messages.info(request, _('You already finished this tutorial.'))

    # A tutorial can be one leg of a homework now — tick it off there too.
    from homework.items import tick_off
    tick_off(request.user, 'tutorial', tutorial)
    return redirect('tutorial_detail', pk=pk)
