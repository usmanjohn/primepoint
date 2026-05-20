from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import F, Count, Q
from django.http import JsonResponse

from .models import Tutorial, TutorialReaction, TutorialPlaylist, PlaylistTutorial, CATEGORY_CHOICES
from .forms import TutorialForm, TutorialPlaylistForm


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

    paginator = Paginator(qs, 12)
    tutorials  = paginator.get_page(request.GET.get('page'))

    return render(request, 'tutorial/tutorial_list.html', {
        'tutorials':       tutorials,
        'active_category': category,
        'categories':      CATEGORY_CHOICES,
        'can_create':      _can_create(request.user),
        'total_count':     Tutorial.objects.filter(is_published=True).count(),
    })


def tutorial_detail(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk, is_published=True)
    Tutorial.objects.filter(pk=pk).update(views=F('views') + 1)

    related = Tutorial.objects.filter(
        category=tutorial.category, is_published=True
    ).exclude(pk=pk).order_by('-created_at')[:4]

    can_edit = request.user.is_authenticated and (
        request.user == tutorial.author or request.user.is_staff
    )

    like_count    = tutorial.reactions.filter(reaction='like').count()
    dislike_count = tutorial.reactions.filter(reaction='dislike').count()
    user_reaction = None
    if request.user.is_authenticated:
        r = tutorial.reactions.filter(user=request.user).first()
        user_reaction = r.reaction if r else None

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
        'linked_practices': tutorial.practices.filter(is_published=True),
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
    return render(request, 'tutorial/playlist_detail.html', {
        'playlist': playlist,
        'items':    items,
        'can_edit': can_edit,
    })


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
