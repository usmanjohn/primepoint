from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.db.models import Count

from .models import Master
from .forms import MasterForm


def master_list(request):
    masters = Master.objects.all().annotate(
        practice_count=Count('practices', distinct=True)
    ).order_by('-created_at')
    return render(request, 'masters/master_list.html', {'masters': masters})


def master_detail(request, master_id):
    master = get_object_or_404(Master, id=master_id)
    practices = master.practices.filter(is_published=True).annotate(
        question_count=Count('questions', distinct=True)
    )
    return render(request, 'masters/master_detail.html', {
        'master': master,
        'practices': practices,
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
