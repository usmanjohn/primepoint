from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from masters.models import Master


def register(request):
    if request.method == 'POST':
        u_form = UserRegistrationForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=user.profile)
            p_form.save()
            messages.success(request, f'Account created for {u_form.cleaned_data["username"]}!')
            return redirect('login')
    else:
        u_form = UserRegistrationForm()
        p_form = ProfileUpdateForm()
    return render(request, 'people/register.html', {'u_form': u_form, 'p_form': p_form})


def _profile_context(viewed_user, is_own_profile):
    from homework.models import Homework, HomeworkAssignment
    people = viewed_user.profile
    master = getattr(people, 'master', None)
    panda = getattr(people, 'panda', None)
    practices = master.practices.filter(is_published=True).order_by('-created_at')[:5] if master else []
    recent_attempts = panda.attempts.filter(status='completed').order_by('-completed_at')[:5] if panda else []
    all_masters = Master.objects.order_by('name') if panda else []

    # Homework for profile display (own profile only — private data)
    panda_hw_pending = panda_hw_done = master_hw = None
    if is_own_profile:
        if panda:
            assignments = (
                panda.homework_assignments
                .select_related('homework__master', 'homework__practice', 'attempt')
                .order_by('homework__due_date')
            )
            panda_hw_pending = assignments.filter(status='pending')[:5]
            panda_hw_done = assignments.filter(status__in=['submitted', 'graded'])[:5]
        if master:
            master_hw = (
                master.homeworks
                .prefetch_related('assignments')
                .order_by('-created_at')[:5]
            )

    return {
        'people': people,
        'viewed_user': viewed_user,
        'master': master,
        'panda': panda,
        'practices': practices,
        'recent_attempts': recent_attempts,
        'is_own_profile': is_own_profile,
        'all_masters': all_masters,
        'panda_hw_pending': panda_hw_pending,
        'panda_hw_done': panda_hw_done,
        'master_hw': master_hw,
    }


@login_required
def profile(request):
    return render(request, 'people/profile.html', _profile_context(request.user, True))


@login_required
def user_profile(request, username):
    viewed_user = get_object_or_404(User, username=username)
    is_own = request.user.is_authenticated and request.user == viewed_user
    return render(request, 'people/profile.html', _profile_context(viewed_user, is_own))


@login_required
def profile_update(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'people/update_profile.html', {'p_form': p_form})


@login_required
def update_panda_masters(request):
    panda = getattr(request.user.profile, 'panda', None)
    if not panda or request.method != 'POST':
        return redirect('profile')
    selected_ids = request.POST.getlist('masters')
    panda.masters.set(Master.objects.filter(pk__in=selected_ids))
    messages.success(request, 'Your masters have been updated.')
    return redirect('profile')
