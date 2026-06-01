from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import UserRegistrationForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from masters.models import Master
from .models import Notification

_RANK_THRESHOLDS = [
    (0, 'Novice', 50),
    (50, 'Scholar', 150),
    (150, 'Expert', 300),
    (300, 'Grandmaster', None),
]

def _next_rank_pts(rating):
    for low, name, cap in _RANK_THRESHOLDS:
        if cap and rating < cap:
            return cap
    return None

def _next_rank_name(rating):
    if rating < 50: return 'Scholar'
    if rating < 150: return 'Expert'
    if rating < 300: return 'Grandmaster'
    return None

def _rank_progress_pct(rating):
    """Percent through the current rank tier (0-100)."""
    tiers = [(0, 50), (50, 150), (150, 300), (300, 500)]
    for low, high in tiers:
        if rating < high:
            return min(100, round((rating - low) / (high - low) * 100))
    return 100


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
    from django.db.models import Avg, Count as _Count
    practices = master.practices.filter(is_published=True).order_by('-created_at')[:5] if master else []
    recent_attempts = (
        panda.attempts.filter(status='completed')
        .select_related('practice')
        .order_by('-completed_at')[:8]
    ) if panda else []
    all_masters = Master.objects.only('id', 'name').order_by('name') if panda else []

    # Rating stats for student profile
    rating_stats = None
    if panda:
        agg = panda.attempts.filter(status='completed').aggregate(
            total=_Count('id'),
            avg_score=Avg('score'),
        )
        rating_stats = {
            'total_tests': agg['total'] or 0,
            'avg_score': round(agg['avg_score'] or 0, 1),
            'next_rank_pts': _next_rank_pts(panda.rating),
            'next_rank_name': _next_rank_name(panda.rating),
            'rank_progress_pct': _rank_progress_pct(panda.rating),
        }

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

    from masters.models import Certificate
    certificates = Certificate.objects.filter(panda=panda, is_visible=True).select_related('master') if panda else []

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
        'rating_stats': rating_stats,
        'certificates': certificates,
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
    from masters.models import StudentEnrollment
    panda = getattr(request.user.profile, 'panda', None)
    if not panda or request.method != 'POST':
        return redirect('profile')
    selected_ids = set(int(i) for i in request.POST.getlist('masters'))
    current_ids = set(panda.masters.values_list('pk', flat=True))

    new_ids = selected_ids - current_ids
    removed_ids = current_ids - selected_ids

    panda.masters.set(Master.objects.filter(pk__in=selected_ids))

    for master_id in new_ids:
        StudentEnrollment.objects.get_or_create(
            master_id=master_id, panda=panda,
        )
    for master_id in removed_ids:
        StudentEnrollment.objects.filter(master_id=master_id, panda=panda).delete()

    messages.success(request, 'Your masters have been updated.')
    return redirect('profile')


@login_required
def notifications(request):
    notifs = Notification.objects.filter(user=request.user).select_related('user')[:60]
    Notification.objects.filter(user=request.user, is_read=False).update(is_read=True)
    return render(request, 'people/notifications.html', {'notifications': notifs})


@login_required
def mark_notification_read(request, pk):
    notif = get_object_or_404(Notification, pk=pk, user=request.user)
    notif.is_read = True
    notif.save(update_fields=['is_read'])
    if notif.url:
        return redirect(notif.url)
    return redirect('notifications')
