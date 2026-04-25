from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.db.models import Count, Avg
from django.utils import timezone

from .models import Master
from .forms import MasterForm
from practice.models import PracticeAttempt


def master_list(request):
    masters = Master.objects.all().annotate(
        practice_count=Count('practices', distinct=True),
        student_count_live=Count('pandas', distinct=True),
    ).order_by('-created_at')
    return render(request, 'masters/master_list.html', {'masters': masters})


def master_detail(request, master_id):
    master = get_object_or_404(Master, id=master_id)

    practices = master.practices.filter(is_published=True).annotate(
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

    return render(request, 'masters/master_detail.html', {
        'master': master,
        'practices': practices,
        'avg_student_score': avg_student_score,
        'total_attempts': total_attempts,
        'total_questions': total_questions,
        'experience_years': experience_years,
        'experience_months': experience_months,
        'students': students,
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
            messages.success(request, "Master profile created! You can now create practices.")
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
