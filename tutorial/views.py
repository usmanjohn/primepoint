from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import F, Count, Q

from .models import Tutorial, TutorialReaction, CATEGORY_CHOICES
from .forms import TutorialForm


def _can_create(user):
    if not user.is_authenticated:
        return False
    if user.is_staff:
        return True
    try:
        return hasattr(user.profile, 'master')
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

    return render(request, 'tutorial/tutorial_detail.html', {
        'tutorial':      tutorial,
        'related':       related,
        'can_edit':      can_edit,
        'like_count':    like_count,
        'dislike_count': dislike_count,
        'user_reaction': user_reaction,
    })


@login_required
def tutorial_react(request, pk):
    if request.method != 'POST':
        return redirect('tutorial_detail', pk=pk)

    tutorial = get_object_or_404(Tutorial, pk=pk, is_published=True)
    reaction_type = request.POST.get('reaction')

    if reaction_type not in ('like', 'dislike'):
        return redirect('tutorial_detail', pk=pk)

    existing = TutorialReaction.objects.filter(user=request.user, tutorial=tutorial).first()
    if existing:
        if existing.reaction == reaction_type:
            existing.delete()          # toggle off
        else:
            existing.reaction = reaction_type
            existing.save()            # switch side
    else:
        TutorialReaction.objects.create(
            user=request.user, tutorial=tutorial, reaction=reaction_type
        )

    return redirect('tutorial_detail', pk=pk)


@login_required
def tutorial_create(request):
    if not _can_create(request.user):
        raise PermissionDenied

    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            tut = form.save(commit=False)
            tut.author = request.user
            tut.save()
            messages.success(request, 'Tutorial published successfully!')
            return redirect('tutorial_detail', pk=tut.pk)
    else:
        form = TutorialForm()

    return render(request, 'tutorial/tutorial_form.html', {'form': form})


@login_required
def tutorial_edit(request, pk):
    tutorial = get_object_or_404(Tutorial, pk=pk)
    if not (request.user == tutorial.author or request.user.is_staff):
        raise PermissionDenied

    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES, instance=tutorial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tutorial updated.')
            return redirect('tutorial_detail', pk=tutorial.pk)
    else:
        form = TutorialForm(instance=tutorial)

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
