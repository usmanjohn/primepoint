"""Homework, from the pupil's side.

Setting homework lives in the classroom now — a master assigns inside the room
they teach, which is what makes the pickers subject-aware and the roster the
right roster. What stays here is the other half: one inbox where a pupil sees
everything due from every classroom at once. A pupil in three rooms should not
have to open three pages to find out what is due tomorrow.

The old master-facing URLs are kept as redirects rather than deleted, because
they are bookmarked and linked from older pages.
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext as _

from .models import Homework, HomeworkAssignment


def _get_master(request):
    return getattr(request.user.profile, 'master', None)


def _get_panda(request):
    return getattr(request.user.profile, 'panda', None)


# ── The pupil's inbox ────────────────────────────────────────────────────────

@login_required
def my_homework(request):
    panda = _get_panda(request)
    master = _get_master(request)

    if not panda and not master:
        messages.info(request, _("You don't have a student or master profile yet."))
        return redirect('index')

    pending = submitted = None
    if panda:
        assignments = list(
            panda.homework_assignments
            .select_related('homework__master', 'homework__classroom')
            .prefetch_related('homework__practices', 'homework__tutorials',
                              'homework__stories', 'homework__exam_lessons')
            .order_by('homework__due_date', '-homework__created_at')
        )
        # Re-check before showing: a pupil who read the tutorial and sat the
        # practice ten minutes ago should find the row already ticked off.
        for assignment in assignments:
            assignment.refresh()
        pending = [a for a in assignments if a.status == 'pending']
        submitted = [a for a in assignments if a.status in ('submitted', 'graded')]

    classrooms = None
    if master:
        classrooms = (master.classrooms
                      .prefetch_related('homeworks')
                      .order_by('-created_at'))

    return render(request, 'homework/my_homework.html', {
        'pending': pending,
        'submitted': submitted,
        'master': master,
        'classrooms': classrooms,
    })


# ── Old master-facing routes, now inside the classroom ───────────────────────

def _to_classroom(request):
    messages.info(request, _('Homework is set inside a classroom now — open the '
                             'classroom you teach and use its Homework tab.'))
    return redirect('classroom:list')


@login_required
def manage_homework(request):
    return _to_classroom(request)


@login_required
def create_homework(request):
    return _to_classroom(request)


@login_required
def manage_groups(request):
    return _to_classroom(request)


@login_required
def homework_detail(request, pk):
    """Land on the right classroom's copy of this homework."""
    homework = get_object_or_404(Homework, pk=pk)
    if homework.classroom_id:
        return redirect('classroom:homework_detail',
                        classroom_pk=homework.classroom_id, hw_pk=homework.pk)
    return _to_classroom(request)
