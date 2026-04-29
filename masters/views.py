from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.db.models import Count, Avg
from django.utils import timezone

from .models import Master
from .forms import MasterForm
from practice.models import PracticeAttempt
from homework.models import PandaGroup, Homework
from tutorial.models import Tutorial


@login_required
def master_list(request):
    masters = Master.objects.all().annotate(
        practice_count=Count('practices', distinct=True),
        student_count_live=Count('pandas', distinct=True),
    ).order_by('-created_at')
    return render(request, 'masters/master_list.html', {'masters': masters})


@login_required
def master_detail(request, master_id):
    master = get_object_or_404(Master, id=master_id)
    is_owner = (request.user == master.profile.user)

    practice_qs = master.practices if is_owner else master.practices.filter(is_published=True)
    practices = practice_qs.annotate(
        question_count=Count('questions', distinct=True),
        attempt_count=Count('attempts', distinct=True),
        avg_score=Avg('attempts__score'),
    )

    attempts_qs = PracticeAttempt.objects.filter(practice__master=master)
    avg_student_score = attempts_qs.aggregate(avg=Avg('score'))['avg'] or 0
    total_attempts = attempts_qs.count()
    total_questions = sum(p.question_count for p in practices)

    days_active = (timezone.now() - master.created_at).days
    experience_years = days_active // 365
    experience_months = (days_active % 365) // 30

    students = master.pandas.select_related('profile__user').order_by('-rating')[:8]

    groups = []
    homeworks = []
    if is_owner:
        groups = master.panda_groups.annotate(
            member_count_ann=Count('members')
        ).order_by('name')
        homeworks = (
            master.homeworks
            .select_related('practice')
            .prefetch_related('assignments')
            .order_by('-created_at')
        )

    tutorials = (
        Tutorial.objects
        .filter(author=master.profile.user, is_published=True)
        .order_by('-created_at')[:6]
    )

    return render(request, 'masters/master_detail.html', {
        'master': master,
        'is_owner': is_owner,
        'practices': practices,
        'avg_student_score': avg_student_score,
        'total_attempts': total_attempts,
        'total_questions': total_questions,
        'experience_years': experience_years,
        'experience_months': experience_months,
        'students': students,
        'groups': groups,
        'homeworks': homeworks,
        'tutorials': tutorials,
    })


@login_required
def master_create(request):
    if hasattr(request.user.profile, 'master'):
        messages.info(request, "You already have a Master profile.")
        return redirect('masters-home')

    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            master = form.save(commit=False)
            master.profile = request.user.profile
            master.save()
            messages.success(request, "Your Master application has been submitted. You'll gain full access once an admin approves it.")
            return redirect('masters-home')
    else:
        form = MasterForm()
    return render(request, 'masters/master_form.html', {'form': form})


@login_required
def master_update(request, pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = MasterForm(request.POST, instance=master)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect('masters-detail', master_id=master.pk)
    else:
        form = MasterForm(instance=master)
    return render(request, 'masters/master_form.html', {'form': form, 'master': master})


@login_required
def master_delete(request, pk):
    master = get_object_or_404(Master, pk=pk)
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        master.delete()
        messages.success(request, "Master profile deleted.")
        return redirect('masters-home')
    return render(request, 'masters/master_confirm_delete.html', {'master': master})


@login_required
def certificate_generator(request):
    is_master = hasattr(request.user, 'profile') and hasattr(request.user.profile, 'master')
    if not request.user.is_staff and not (is_master and request.user.profile.master.is_approved):
        raise PermissionDenied

    master = None
    students = []
    if is_master:
        master = request.user.profile.master
        students = (
            master.pandas
            .select_related('profile__user')
            .order_by('profile__user__first_name', 'profile__user__username')
        )

    return render(request, 'masters/certificate.html', {
        'master':   master,
        'students': students,
        'today':    timezone.now().date(),
    })
