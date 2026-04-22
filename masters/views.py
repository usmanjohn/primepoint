from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Master
from .forms import MasterForm
from django.contrib import messages

def master_list(request):
    masters = Master.objects.all().order_by('-created_at')
    return render(request, 'masters/master_home.html', {'masters': masters})

def master_detail(request, master_id):
    master = get_object_or_404(Master, id=master_id)
    return render(request, 'masters/master_detail.html', {'master': master})

@login_required
def master_create(request):
    user = request.user
    if user.profile.master is not None:
        message = "You already have a Master profile. Please edit your existing profile instead."
        messages.error(request, message)
        return redirect('masters-home')  # or some error page
    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('masters-home')
    else:
        form = MasterForm()
    return render(request, 'masters/master_form.html', {'form': form})

@login_required
def master_update(request, pk):
    master = get_object_or_404(Master, pk=pk)
    
    # UserPassesTestMixin logic
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = MasterForm(request.POST, instance=master)
        if form.is_valid():
            form.save()
            return redirect('masters-home')
    else:
        form = MasterForm(instance=master)
    return render(request, 'masters/master_form.html', {'form': form})

@login_required
def master_delete(request, pk):
    master = get_object_or_404(Master, pk=pk)
    
    # UserPassesTestMixin logic
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        master.delete()
        return redirect('masters-home')
    return render(request, 'masters/master_confirm_delete.html', {'master': master})
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Master
from .forms import MasterForm

def master_list(request):
    masters = Master.objects.all().order_by('-created_at')
    return render(request, 'masters/master_list.html', {'masters': masters})

def master_detail(request, master_id):
    master = get_object_or_404(Master, id=master_id)
    return render(request, 'masters/master_detail.html', {'master': master})

@login_required
def master_create(request):
    if request.method == 'POST':
        form = MasterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('masters-home')
    else:
        form = MasterForm()
    return render(request, 'masters/master_form.html', {'form': form})

@login_required
def master_update(request, pk):
    master = get_object_or_404(Master, pk=pk)
    
    # UserPassesTestMixin logic
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = MasterForm(request.POST, instance=master)
        if form.is_valid():
            form.save()
            return redirect('masters-home')
    else:
        form = MasterForm(instance=master)
    return render(request, 'masters/master_form.html', {'form': form})

@login_required
def master_delete(request, pk):
    master = get_object_or_404(Master, pk=pk)
    
    # UserPassesTestMixin logic
    if request.user != master.profile.user:
        raise PermissionDenied

    if request.method == 'POST':
        master.delete()
        return redirect('masters-home')
    return render(request, 'masters/master_confirm_delete.html', {'master': master})
