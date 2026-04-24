from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from .models import Homework, HomeworkAssignment, PandaGroup
from .forms import HomeworkForm, HomeworkAssignForm, PandaGroupForm


def _get_master(request):
    return getattr(request.user.profile, 'master', None)


def _get_panda(request):
    return getattr(request.user.profile, 'panda', None)


def _bulk_assign(homework, pandas_qs):
    """Create HomeworkAssignment for each panda not already assigned. Returns count created."""
    existing = set(homework.assignments.values_list('panda_id', flat=True))
    created = 0
    for panda in pandas_qs:
        if panda.pk not in existing:
            HomeworkAssignment.objects.create(homework=homework, panda=panda)
            created += 1
    return created


# ── Student views ────────────────────────────────────────────────────────────

@login_required
def my_homework(request):
    panda = _get_panda(request)
    master = _get_master(request)

    if not panda and not master:
        messages.info(request, "You don't have a student or master profile yet.")
        return redirect('index')

    pending = submitted = None
    if panda:
        assignments = (
            panda.homework_assignments
            .select_related('homework__master', 'homework__practice', 'attempt')
            .order_by('homework__due_date', '-homework__created_at')
        )
        pending = assignments.filter(status='pending')
        submitted = assignments.filter(status__in=['submitted', 'graded'])

    master_homeworks = None
    groups = None
    if master:
        master_homeworks = master.homeworks.prefetch_related('assignments').order_by('-created_at')[:5]
        groups = master.panda_groups.prefetch_related('members')

    return render(request, 'homework/my_homework.html', {
        'pending': pending,
        'submitted': submitted,
        'master': master,
        'master_homeworks': master_homeworks,
        'groups': groups,
    })


# ── Master homework views ─────────────────────────────────────────────────────

@login_required
def manage_homework(request):
    master = _get_master(request)
    if not master:
        raise PermissionDenied

    homeworks = master.homeworks.prefetch_related('assignments')
    return render(request, 'homework/manage_homework.html', {
        'homeworks': homeworks,
        'groups': master.panda_groups.all(),
    })


@login_required
def create_homework(request):
    master = _get_master(request)
    if not master:
        raise PermissionDenied

    hw_form = HomeworkForm(master=master)
    assign_form = HomeworkAssignForm(master=master)

    if request.method == 'POST':
        hw_form = HomeworkForm(master=master, data=request.POST)
        assign_form = HomeworkAssignForm(master=master, data=request.POST)

        if hw_form.is_valid() and assign_form.is_valid():
            homework = hw_form.save(commit=False)
            homework.master = master
            homework.save()

            count = _bulk_assign(homework, assign_form.get_all_pandas())
            messages.success(request, f"'{homework.title}' created and assigned to {count} student(s).")
            return redirect('homework_detail', pk=homework.pk)

    return render(request, 'homework/homework_form.html', {
        'hw_form': hw_form,
        'assign_form': assign_form,
    })


@login_required
def homework_detail(request, pk):
    master = _get_master(request)
    if not master:
        raise PermissionDenied

    homework = get_object_or_404(Homework, pk=pk, master=master)
    assignments = homework.assignments.select_related('panda__profile__user', 'attempt')
    return render(request, 'homework/homework_detail.html', {
        'homework': homework,
        'assignments': assignments,
    })


@login_required
def assign_homework(request, pk):
    """Reuse an existing homework — assign it to more pandas/groups."""
    master = _get_master(request)
    if not master:
        raise PermissionDenied

    homework = get_object_or_404(Homework, pk=pk, master=master)

    if request.method == 'POST':
        form = HomeworkAssignForm(master=master, data=request.POST)
        if form.is_valid():
            count = _bulk_assign(homework, form.get_all_pandas())
            if count:
                messages.success(request, f"Assigned to {count} new student(s).")
            else:
                messages.info(request, "All selected students already have this homework.")
            return redirect('homework_detail', pk=homework.pk)
    else:
        form = HomeworkAssignForm(master=master)

    already_assigned = set(homework.assignments.values_list('panda_id', flat=True))
    return render(request, 'homework/assign_homework.html', {
        'form': form,
        'homework': homework,
        'already_assigned': already_assigned,
    })


@login_required
def edit_homework(request, pk):
    master = _get_master(request)
    if not master:
        raise PermissionDenied

    homework = get_object_or_404(Homework, pk=pk, master=master)

    if request.method == 'POST':
        form = HomeworkForm(master=master, data=request.POST, instance=homework)
        if form.is_valid():
            form.save()
            messages.success(request, "Homework updated.")
            return redirect('homework_detail', pk=homework.pk)
    else:
        form = HomeworkForm(master=master, instance=homework)

    return render(request, 'homework/homework_form.html', {
        'hw_form': form,
        'homework': homework,
    })


@login_required
def delete_homework(request, pk):
    master = _get_master(request)
    if not master:
        raise PermissionDenied

    homework = get_object_or_404(Homework, pk=pk, master=master)

    if request.method == 'POST':
        homework.delete()
        messages.success(request, "Homework deleted.")
        return redirect('manage_homework')

    return render(request, 'homework/homework_confirm_delete.html', {'homework': homework})


# ── Group views ───────────────────────────────────────────────────────────────

@login_required
def manage_groups(request):
    master = _get_master(request)
    if not master:
        raise PermissionDenied

    groups = master.panda_groups.prefetch_related('members__profile__user')
    return render(request, 'homework/manage_groups.html', {'groups': groups})


@login_required
def create_group(request):
    master = _get_master(request)
    if not master:
        raise PermissionDenied

    if request.method == 'POST':
        form = PandaGroupForm(master=master, data=request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.master = master
            group.save()
            form.save_m2m()
            messages.success(request, f"Group '{group.name}' created with {group.member_count} student(s).")
            return redirect('manage_groups')
    else:
        form = PandaGroupForm(master=master)

    return render(request, 'homework/group_form.html', {'form': form})


@login_required
def edit_group(request, gpk):
    master = _get_master(request)
    if not master:
        raise PermissionDenied

    group = get_object_or_404(PandaGroup, pk=gpk, master=master)

    if request.method == 'POST':
        form = PandaGroupForm(master=master, data=request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, "Group updated.")
            return redirect('manage_groups')
    else:
        form = PandaGroupForm(master=master, instance=group)

    return render(request, 'homework/group_form.html', {'form': form, 'group': group})


@login_required
def delete_group(request, gpk):
    master = _get_master(request)
    if not master:
        raise PermissionDenied

    group = get_object_or_404(PandaGroup, pk=gpk, master=master)

    if request.method == 'POST':
        group.delete()
        messages.success(request, "Group deleted.")
        return redirect('manage_groups')

    return render(request, 'homework/group_confirm_delete.html', {'group': group})
