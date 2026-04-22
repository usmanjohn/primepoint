from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
    people = viewed_user.profile
    master = getattr(people, 'master', None)
    panda = getattr(people, 'panda', None)
    practices = master.practices.filter(is_published=True).order_by('-created_at')[:5] if master else []
    recent_attempts = panda.attempts.filter(status='completed').order_by('-completed_at')[:5] if panda else []
    return {
        'people': people,
        'viewed_user': viewed_user,
        'master': master,
        'panda': panda,
        'practices': practices,
        'recent_attempts': recent_attempts,
        'is_own_profile': is_own_profile,
    }


@login_required
def profile(request):
    return render(request, 'people/profile.html', _profile_context(request.user, True))


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
