"""The classroom is the teacher's whole workspace.

Everything a master does with a real class now happens here and nowhere else:
the lessons, the homework, the roster, the attendance register, the money, and
the shelf of notes and links. It used to be scattered — homework under
`/homework/`, pupils and payments under `/masters/<id>/my-students/` — which
meant a teacher running two classes had one undifferentiated pile of students
and no way to tell one class's homework from the other's. A classroom is the
unit a teacher actually thinks in, so it is the unit the software uses.

Three access rules run through every view below:
  `_require_master_owns`  — only the owning master may change anything;
  `_require_member`       — only the master and the enrolled pupils may look;
  and every roster/homework/payment queryset is scoped to *this* room, so a
  master with two classrooms can never assign or bill across the wall.
"""
import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.db.models import Q, F, Sum
from django.utils import timezone
from django.utils.translation import gettext as _

from .models import (
    Classroom, Lesson, LessonNote, ClassroomDiscussion, ClassroomReply,
    ClassroomResource,
)
from .forms import (
    ClassroomForm, ClassroomMembershipForm, LessonForm,
    LessonNoteForm, ClassroomDiscussionForm, ClassroomReplyForm,
    ClassroomResourceForm, HomeworkForm, HomeworkAssignForm, PandaGroupForm,
    PaymentForm, AttendanceForm, CertificateForm, AddStudentForm,
)
from . import content
from homework.models import Homework, HomeworkAssignment, PandaGroup
from masters.models import (
    StudentPayment, Attendance, Certificate, StudentEnrollment,
)
from panda.models import Panda


def _get_master(request):
    try:
        return request.user.profile.master
    except Exception:
        return None


def _require_master_owns(request, classroom):
    if not request.user.is_authenticated or classroom.master.profile.user != request.user:
        raise PermissionDenied


def _require_member(request, classroom):
    if not classroom.is_member(request.user):
        raise PermissionDenied


def _member_or_404(classroom, panda_pk):
    """A pupil, but only if they are in this room."""
    return get_object_or_404(classroom.get_all_pandas(), pk=panda_pk)


def _parse_date(raw, default=None):
    try:
        return datetime.date.fromisoformat(raw)
    except (TypeError, ValueError):
        return default or timezone.now().date()


# ── Classroom CRUD ─────────────────────────────────────────────────────────────

def classroom_list(request):
    all_classrooms = Classroom.objects.filter(is_active=True).select_related('master').order_by('-created_at')
    is_master = False
    enrolled_ids = set()

    if request.user.is_authenticated:
        master = _get_master(request)
        if master:
            is_master = True
            all_classrooms = Classroom.objects.filter(master=master).order_by('-created_at')
        else:
            try:
                panda = request.user.profile.panda
                enrolled_ids = set(
                    Classroom.objects.filter(
                        Q(groups__members=panda) | Q(individual_pandas=panda)
                    ).values_list('id', flat=True)
                )
            except Exception:
                pass

    return render(request, 'classroom/classroom_list.html', {
        'classrooms': all_classrooms,
        'is_master': is_master,
        'enrolled_ids': enrolled_ids,
    })


@login_required
def classroom_create(request):
    master = _get_master(request)
    if not master:
        raise PermissionDenied
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.master = master
            classroom.save()
            messages.success(request, _('Classroom created. Now add your students.'))
            return redirect('classroom:students', pk=classroom.pk)
    else:
        form = ClassroomForm()
    return render(request, 'classroom/classroom_form.html', {
        'form': form,
        'form_title': _('Create Classroom'),
        'form_subtitle': _('Set up a new private classroom for your students.'),
    })


def classroom_detail(request, pk):
    """The hub: lessons, what is due, the shelf, and — for a pupil — their own
    homework and payment standing in this room."""
    classroom = get_object_or_404(Classroom, pk=pk)
    if not classroom.is_member(request.user):
        return render(request, 'classroom/classroom_locked.html', {'classroom': classroom})

    is_master_user = classroom.is_master_user(request.user)
    panda = classroom.panda_for(request.user)

    lessons = classroom.lessons.all() if is_master_user else classroom.lessons.filter(is_published=True)
    resources = classroom.resources.all()[:6]

    homeworks = my_assignments = my_payments = None
    if is_master_user:
        homeworks = (classroom.homeworks
                     .prefetch_related('assignments')
                     .order_by('-created_at')[:5])
    elif panda:
        my_assignments = [
            a for a in HomeworkAssignment.objects
            .filter(panda=panda, homework__classroom=classroom)
            .select_related('homework')
            .order_by('homework__due_date', '-homework__created_at')
        ]
        my_payments = StudentPayment.objects.filter(
            classroom=classroom, panda=panda).order_by('-created_at')[:5]

    members = classroom.get_all_pandas().select_related('profile__user')[:12]
    return render(request, 'classroom/classroom_detail.html', {
        'classroom': classroom,
        'lessons': lessons,
        'is_master_user': is_master_user,
        'members': members,
        'resources': resources,
        'homeworks': homeworks,
        'my_assignments': my_assignments,
        'my_payments': my_payments,
        'tab': 'lessons',
    })


@login_required
def classroom_edit(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    _require_master_owns(request, classroom)
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            messages.success(request, _('Classroom updated.'))
            return redirect('classroom:detail', pk=classroom.pk)
    else:
        form = ClassroomForm(instance=classroom)
    return render(request, 'classroom/classroom_form.html', {
        'form': form,
        'classroom': classroom,
        'form_title': _('Edit Classroom'),
        'form_subtitle': _('Update classroom details.'),
    })


@login_required
def classroom_delete(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    _require_master_owns(request, classroom)
    if request.method == 'POST':
        classroom.delete()
        messages.success(request, _('Classroom deleted.'))
        return redirect('classroom:list')
    return render(request, 'classroom/classroom_confirm_delete.html', {
        'classroom': classroom,
        'object_name': classroom.name,
        'cancel_url': 'classroom:detail',
        'cancel_pk': classroom.pk,
    })


@login_required
def classroom_manage(request, pk):
    """Attach whole groups or individual pupils to the room."""
    classroom = get_object_or_404(Classroom, pk=pk)
    _require_master_owns(request, classroom)
    master = classroom.master
    if request.method == 'POST':
        form = ClassroomMembershipForm(master, request.POST)
        if form.is_valid():
            classroom.groups.set(form.cleaned_data['groups'])
            classroom.individual_pandas.set(form.cleaned_data['individual_pandas'])
            messages.success(request, _('Membership updated.'))
            return redirect('classroom:students', pk=classroom.pk)
    else:
        form = ClassroomMembershipForm(master, initial={
            'groups': classroom.groups.all(),
            'individual_pandas': classroom.individual_pandas.all(),
        })
    all_pandas = classroom.get_all_pandas().select_related('profile__user')
    return render(request, 'classroom/classroom_manage.html', {
        'classroom': classroom,
        'form': form,
        'all_pandas': all_pandas,
        'is_master_user': True,
        'tab': 'students',
    })


# ── Lesson CRUD ────────────────────────────────────────────────────────────────

@login_required
def lesson_create(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    master = classroom.master
    if request.method == 'POST':
        form = LessonForm(master, classroom, request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.classroom = classroom
            lesson.save()
            form.save_m2m()
            messages.success(request, _('Lesson created.'))
            return redirect('classroom:lesson_detail', classroom_pk=classroom.pk, lesson_pk=lesson.pk)
    else:
        next_order = classroom.lessons.count()
        form = LessonForm(master, classroom, initial={'order': next_order})
    return render(request, 'classroom/lesson_form.html', {
        'form': form,
        'classroom': classroom,
        'form_title': _('Add Lesson'),
        'is_master_user': True,
        'tab': 'lessons',
    })


@login_required
def lesson_detail(request, classroom_pk, lesson_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, classroom=classroom)
    is_master_user = classroom.is_master_user(request.user)
    if not is_master_user and not lesson.is_published:
        raise PermissionDenied
    return render(request, 'classroom/lesson_detail.html', {
        'classroom': classroom,
        'lesson': lesson,
        'notes': lesson.notes.all(),
        'practices': lesson.practices.all(),
        'homeworks': lesson.homeworks.all(),
        'tutorials': lesson.tutorials.prefetch_related('practices', 'stories'),
        'note_form': LessonNoteForm() if is_master_user else None,
        'is_master_user': is_master_user,
        'tab': 'lessons',
    })


@login_required
def lesson_edit(request, classroom_pk, lesson_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, classroom=classroom)
    master = classroom.master
    if request.method == 'POST':
        form = LessonForm(master, classroom, request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, _('Lesson updated.'))
            return redirect('classroom:lesson_detail', classroom_pk=classroom.pk, lesson_pk=lesson.pk)
    else:
        form = LessonForm(master, classroom, instance=lesson)
    return render(request, 'classroom/lesson_form.html', {
        'form': form,
        'classroom': classroom,
        'lesson': lesson,
        'form_title': _('Edit Lesson'),
        'is_master_user': True,
        'tab': 'lessons',
    })


@login_required
def lesson_delete(request, classroom_pk, lesson_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, classroom=classroom)
    if request.method == 'POST':
        lesson.delete()
        messages.success(request, _('Lesson deleted.'))
        return redirect('classroom:detail', pk=classroom.pk)
    return render(request, 'classroom/lesson_confirm_delete.html', {
        'classroom': classroom,
        'lesson': lesson,
    })


@login_required
def lesson_note_upload(request, classroom_pk, lesson_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, classroom=classroom)
    if request.method == 'POST':
        form = LessonNoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.lesson = lesson
            note.save()
            messages.success(request, _('Note uploaded.'))
        else:
            messages.error(request, _('Please select a valid file.'))
    return redirect('classroom:lesson_detail', classroom_pk=classroom.pk, lesson_pk=lesson.pk)


@login_required
def lesson_note_delete(request, classroom_pk, lesson_pk, note_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, classroom=classroom)
    note = get_object_or_404(LessonNote, pk=note_pk, lesson=lesson)
    if request.method == 'POST':
        note.delete()
        messages.success(request, _('Note deleted.'))
    return redirect('classroom:lesson_detail', classroom_pk=classroom.pk, lesson_pk=lesson.pk)


# ── Homework ───────────────────────────────────────────────────────────────────

def _assign(homework, pandas):
    """Give the homework to these pupils; returns how many were new."""
    existing = set(homework.assignments.values_list('panda_id', flat=True))
    created = 0
    for panda in pandas:
        if panda.pk not in existing:
            HomeworkAssignment.objects.create(homework=homework, panda=panda)
            created += 1
    return created


@login_required
def homework_list(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    is_master_user = classroom.is_master_user(request.user)
    panda = classroom.panda_for(request.user)

    homeworks = assignments = None
    if is_master_user:
        homeworks = (classroom.homeworks
                     .prefetch_related('assignments', 'practices', 'tutorials',
                                       'stories', 'exam_lessons')
                     .order_by('-created_at'))
    else:
        assignments = (HomeworkAssignment.objects
                       .filter(panda=panda, homework__classroom=classroom)
                       .select_related('homework')
                       .order_by('status', 'homework__due_date', '-homework__created_at'))

    return render(request, 'classroom/homework_list.html', {
        'classroom': classroom,
        'homeworks': homeworks,
        'assignments': assignments,
        'is_master_user': is_master_user,
        'tab': 'homework',
    })


@login_required
def homework_create(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)

    if request.method == 'POST':
        form = HomeworkForm(request.POST)
        assign_form = HomeworkAssignForm(classroom, request.POST)
        if form.is_valid() and assign_form.is_valid():
            homework = form.save(commit=False)
            homework.master = classroom.master
            homework.classroom = classroom
            homework.save()
            count = _assign(homework, assign_form.get_all_pandas())
            messages.success(
                request,
                _('"%(title)s" created for %(n)s student(s). Now add what they '
                  'have to do.') % {'title': homework.title, 'n': count})
            return redirect('classroom:homework_detail',
                            classroom_pk=classroom.pk, hw_pk=homework.pk)
    else:
        form = HomeworkForm()
        assign_form = HomeworkAssignForm(classroom)

    return render(request, 'classroom/homework_form.html', {
        'classroom': classroom,
        'form': form,
        'assign_form': assign_form,
        'is_master_user': True,
        'tab': 'homework',
    })


# The four libraries a homework can pull from, and how to search each one.
_PICKERS = {
    'tutorial':    (content.tutorial_queryset,    ['title__icontains', 'summary__icontains']),
    'practice':    (None,                          ['title__icontains', 'description__icontains']),
    'story':       (content.story_queryset,        ['title__icontains', 'summary__icontains']),
    'exam_lesson': (content.exam_lesson_queryset,  ['title__icontains', 'summary__icontains']),
}

_FIELD = {
    'tutorial': 'tutorials', 'practice': 'practices',
    'story': 'stories', 'exam_lesson': 'exam_lessons',
}


def _picker_queryset(kind, classroom):
    if kind == 'practice':
        return content.practice_queryset(classroom, classroom.master)
    getter, _fields = _PICKERS[kind]
    return getter(classroom)


def _search(qs, kind, query):
    if not query:
        return qs
    _getter, fields = _PICKERS[kind]
    q = Q()
    for field in fields:
        q |= Q(**{field: query})
    return qs.filter(q)


@login_required
def homework_detail(request, classroom_pk, hw_pk):
    """Master: what is in it, who has it, how far each pupil has got, plus the
    search-and-add panel. Pupil: their own copy with a tick per finished piece."""
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    homework = get_object_or_404(Homework, pk=hw_pk, classroom=classroom)
    is_master_user = classroom.is_master_user(request.user)
    panda = classroom.panda_for(request.user)

    if not is_master_user:
        assignment = get_object_or_404(HomeworkAssignment, homework=homework, panda=panda)
        assignment.refresh()
        return render(request, 'classroom/homework_detail.html', {
            'classroom': classroom,
            'homework': homework,
            'assignment': assignment,
            'rows': assignment.progress(),
            'is_master_user': False,
            'tab': 'homework',
        })

    # The add panel: one library at a time, narrowed by the room's subject and
    # then by whatever the master typed.
    kind = request.GET.get('kind', 'tutorial')
    if kind not in _PICKERS:
        kind = 'tutorial'
    query = request.GET.get('q', '').strip()
    already = set(getattr(homework, _FIELD[kind]).values_list('pk', flat=True))
    candidates = _search(_picker_queryset(kind, classroom), kind, query)
    candidates = [c for c in candidates.exclude(pk__in=already)[:40]]

    assignments = (homework.assignments
                   .select_related('panda__profile__user')
                   .order_by('panda__profile__user__first_name',
                             'panda__profile__user__username'))
    for assignment in assignments:
        assignment.refresh()

    return render(request, 'classroom/homework_detail.html', {
        'classroom': classroom,
        'homework': homework,
        'rows': homework.items(),
        'assignments': assignments,
        'kind': kind,
        'kinds': [
            ('tutorial', _('Tutorials'), 'bi-journal-text'),
            ('practice', _('Practices'), 'bi-journal-check'),
            ('story', _('Readings'), 'bi-stars'),
            ('exam_lesson', _('Exam prep'), 'bi-journal-bookmark'),
        ],
        'query': query,
        'candidates': candidates,
        'assign_form': HomeworkAssignForm(classroom),
        'is_master_user': True,
        'tab': 'homework',
    })


@login_required
def homework_add_item(request, classroom_pk, hw_pk):
    """Add one piece of content — and, for a tutorial, its practice and reading.

    That last part is the whole trick. A Prime lesson is three legs written
    together (tutorial → practice → reading) and already linked on the
    Tutorial itself, so a master who picks "PE-24" almost always wants all
    three. Adding them automatically saves two searches and, more importantly,
    stops a homework from quietly shipping only one leg of a lesson.
    """
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    homework = get_object_or_404(Homework, pk=hw_pk, classroom=classroom)

    if request.method != 'POST':
        return redirect('classroom:homework_detail', classroom_pk=classroom.pk, hw_pk=homework.pk)

    kind = request.POST.get('kind')
    raw_pk = request.POST.get('item')
    if kind not in _PICKERS or not (raw_pk or '').isdigit():
        messages.error(request, _('Nothing to add.'))
        return redirect('classroom:homework_detail', classroom_pk=classroom.pk, hw_pk=homework.pk)

    obj = _picker_queryset(kind, classroom).filter(pk=int(raw_pk)).first()
    if obj is None:
        messages.error(request, _('That item is not available in this classroom.'))
        return redirect('classroom:homework_detail', classroom_pk=classroom.pk, hw_pk=homework.pk)

    getattr(homework, _FIELD[kind]).add(obj)
    extra = 0
    if kind == 'tutorial' and request.POST.get('include_related'):
        practices, stories = content.expand_tutorials([obj])
        for practice in practices:
            if not homework.practices.filter(pk=practice.pk).exists():
                homework.practices.add(practice)
                extra += 1
        for story in stories:
            if not homework.stories.filter(pk=story.pk).exists():
                homework.stories.add(story)
                extra += 1

    if extra:
        messages.success(request, _('Added "%(title)s" and its %(n)s linked '
                                    'item(s).') % {'title': str(obj), 'n': extra})
    else:
        messages.success(request, _('Added "%(title)s".') % {'title': str(obj)})

    for assignment in homework.assignments.all():
        assignment.refresh()

    params = f"?kind={kind}"
    if request.POST.get('q'):
        params += f"&q={request.POST['q']}"
    return redirect(
        f"{_hw_url(classroom, homework)}{params}")


def _hw_url(classroom, homework):
    from django.urls import reverse
    return reverse('classroom:homework_detail', args=[classroom.pk, homework.pk])


@login_required
def homework_remove_item(request, classroom_pk, hw_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    homework = get_object_or_404(Homework, pk=hw_pk, classroom=classroom)
    if request.method == 'POST':
        kind = request.POST.get('kind')
        raw_pk = request.POST.get('item')
        if kind in _FIELD and (raw_pk or '').isdigit():
            getattr(homework, _FIELD[kind]).remove(int(raw_pk))
            messages.success(request, _('Removed from this homework.'))
            for assignment in homework.assignments.all():
                assignment.refresh()
    return redirect('classroom:homework_detail', classroom_pk=classroom.pk, hw_pk=homework.pk)


@login_required
def homework_assign(request, classroom_pk, hw_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    homework = get_object_or_404(Homework, pk=hw_pk, classroom=classroom)
    if request.method == 'POST':
        form = HomeworkAssignForm(classroom, request.POST)
        if form.is_valid():
            count = _assign(homework, form.get_all_pandas())
            if count:
                messages.success(request, _('Assigned to %(n)s new student(s).') % {'n': count})
            else:
                messages.info(request, _('Those students already have this homework.'))
    return redirect('classroom:homework_detail', classroom_pk=classroom.pk, hw_pk=homework.pk)


@login_required
def homework_unassign(request, classroom_pk, hw_pk, assignment_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    homework = get_object_or_404(Homework, pk=hw_pk, classroom=classroom)
    assignment = get_object_or_404(HomeworkAssignment, pk=assignment_pk, homework=homework)
    if request.method == 'POST':
        assignment.delete()
        messages.success(request, _('Student removed from this homework.'))
    return redirect('classroom:homework_detail', classroom_pk=classroom.pk, hw_pk=homework.pk)


@login_required
def homework_grade(request, classroom_pk, hw_pk, assignment_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    homework = get_object_or_404(Homework, pk=hw_pk, classroom=classroom)
    assignment = get_object_or_404(HomeworkAssignment, pk=assignment_pk, homework=homework)
    if request.method == 'POST':
        assignment.feedback = request.POST.get('feedback', '').strip()
        assignment.status = 'graded'
        if not assignment.submitted_at:
            assignment.submitted_at = timezone.now()
        assignment.save(update_fields=['feedback', 'status', 'submitted_at'])
        messages.success(request, _('Marked as graded.'))
    return redirect('classroom:homework_detail', classroom_pk=classroom.pk, hw_pk=homework.pk)


@login_required
def homework_edit(request, classroom_pk, hw_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    homework = get_object_or_404(Homework, pk=hw_pk, classroom=classroom)
    if request.method == 'POST':
        form = HomeworkForm(request.POST, instance=homework)
        if form.is_valid():
            form.save()
            messages.success(request, _('Homework updated.'))
            return redirect('classroom:homework_detail', classroom_pk=classroom.pk, hw_pk=homework.pk)
    else:
        form = HomeworkForm(instance=homework)
    return render(request, 'classroom/homework_form.html', {
        'classroom': classroom,
        'form': form,
        'homework': homework,
        'is_master_user': True,
        'tab': 'homework',
    })


@login_required
def homework_delete(request, classroom_pk, hw_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    homework = get_object_or_404(Homework, pk=hw_pk, classroom=classroom)
    if request.method == 'POST':
        homework.delete()
        messages.success(request, _('Homework deleted.'))
        return redirect('classroom:homework_list', classroom_pk=classroom.pk)
    return render(request, 'classroom/classroom_confirm_delete.html', {
        'classroom': classroom,
        'object_name': homework.title,
        'cancel_url': 'classroom:homework_list',
    })


@login_required
def lesson_assign_homework(request, classroom_pk, lesson_pk):
    """One click: turn a classroom lesson into a homework.

    The lesson already carries the tutorials and practices the master attached
    when they planned it, and each of those tutorials carries its own practice
    and reading. So the fastest correct homework is the one the lesson plan
    already describes — this builds it, assigns it to the whole room, and drops
    the master on the homework page to adjust.
    """
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, classroom=classroom)
    if request.method != 'POST':
        return redirect('classroom:lesson_detail', classroom_pk=classroom.pk, lesson_pk=lesson.pk)

    homework = Homework.objects.create(
        master=classroom.master, classroom=classroom,
        title=_('%(lesson)s — homework') % {'lesson': lesson.title},
        notes=lesson.description or '',
    )
    tutorials = list(lesson.tutorials.all())
    homework.tutorials.set(tutorials)
    practices, stories = content.expand_tutorials(tutorials)
    homework.practices.set({p.pk for p in practices} | set(
        lesson.practices.values_list('pk', flat=True)))
    homework.stories.set({s.pk for s in stories})
    lesson.homeworks.add(homework)

    count = _assign(homework, classroom.get_all_pandas())
    messages.success(request, _('Homework built from "%(lesson)s" and given to '
                                '%(n)s student(s).') % {'lesson': lesson.title, 'n': count})
    return redirect('classroom:homework_detail', classroom_pk=classroom.pk, hw_pk=homework.pk)


# ── Students ───────────────────────────────────────────────────────────────────

@login_required
def students(request, classroom_pk):
    """The roster: who is here, how they are doing, are they paid up."""
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)

    rows = []
    for panda in classroom.get_all_pandas().select_related('profile__user'):
        attendance = Attendance.objects.filter(
            master=classroom.master, panda=panda, classroom=classroom)
        assignments = HomeworkAssignment.objects.filter(
            panda=panda, homework__classroom=classroom)
        rows.append({
            'panda': panda,
            'attendance_total': attendance.count(),
            'attendance_present': attendance.filter(status=Attendance.PRESENT).count(),
            'homework_total': assignments.count(),
            'homework_done': assignments.filter(status__in=['submitted', 'graded']).count(),
            'unpaid': StudentPayment.objects.filter(
                classroom=classroom, panda=panda, status=StudentPayment.UNPAID).count(),
        })

    return render(request, 'classroom/students.html', {
        'classroom': classroom,
        'rows': rows,
        'add_form': AddStudentForm(),
        'groups': classroom.master.panda_groups.prefetch_related('members'),
        'is_master_user': True,
        'tab': 'students',
    })


@login_required
def student_add(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    master = classroom.master
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            panda = form.panda
            master.pandas.add(panda)
            StudentEnrollment.objects.get_or_create(master=master, panda=panda)
            classroom.individual_pandas.add(panda)
            master.recalc_stats()
            messages.success(request, _('%(name)s joined this classroom.')
                             % {'name': panda.profile.user.username})
        else:
            for error in form.errors.get('username', []):
                messages.error(request, error)
    return redirect('classroom:students', classroom_pk=classroom.pk)


@login_required
def student_remove(request, classroom_pk, panda_pk):
    """Take a pupil out of this room — not out of the master's student list.

    Removing someone from one class must not delete their history with a
    teacher they still study another subject with, so this only detaches them
    from this classroom.
    """
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    panda = get_object_or_404(Panda, pk=panda_pk)
    if request.method == 'POST':
        classroom.individual_pandas.remove(panda)
        for group in classroom.groups.all():
            group.members.remove(panda)
        messages.success(request, _('%(name)s removed from this classroom.')
                         % {'name': panda.profile.user.username})
    return redirect('classroom:students', classroom_pk=classroom.pk)


@login_required
def student_detail(request, classroom_pk, panda_pk):
    """One pupil, in this room: homework, register, money, certificates."""
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    panda = _member_or_404(classroom, panda_pk)
    master = classroom.master

    assignments = (HomeworkAssignment.objects
                   .filter(panda=panda, homework__classroom=classroom)
                   .select_related('homework')
                   .order_by('-homework__created_at'))
    for assignment in assignments:
        assignment.refresh()

    attendances = Attendance.objects.filter(master=master, panda=panda, classroom=classroom)
    payments = StudentPayment.objects.filter(master=master, panda=panda, classroom=classroom)
    certificates = Certificate.objects.filter(master=master, panda=panda)

    return render(request, 'classroom/student_detail.html', {
        'classroom': classroom,
        'panda': panda,
        'assignments': assignments,
        'attendances': attendances[:20],
        'att_total': attendances.count(),
        'att_present': attendances.filter(status=Attendance.PRESENT).count(),
        'att_late': attendances.filter(status=Attendance.LATE).count(),
        'payments': payments,
        'certificates': certificates,
        'attendance_form': AttendanceForm(initial={'date': timezone.now().date()}),
        'payment_form': PaymentForm(),
        'certificate_form': CertificateForm(),
        'is_master_user': True,
        'tab': 'students',
    })


@login_required
def attendance_mark(request, classroom_pk, panda_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    panda = _member_or_404(classroom, panda_pk)
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            # The classroom is part of the lookup, not the defaults: it is
            # part of the row's identity now, so leaving it out would find and
            # overwrite this pupil's mark in the master's *other* class.
            Attendance.objects.update_or_create(
                master=classroom.master, panda=panda, classroom=classroom,
                date=form.cleaned_data['date'],
                defaults={
                    'status': form.cleaned_data['status'],
                    'notes': form.cleaned_data['notes'],
                },
            )
            messages.success(request, _('Attendance saved.'))
        else:
            messages.error(request, _('Please check the date and try again.'))
    return redirect('classroom:student_detail', classroom_pk=classroom.pk, panda_pk=panda.pk)


@login_required
def attendance_register(request, classroom_pk):
    """Mark the whole room present/absent for one date, in a single submit."""
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    date = _parse_date(request.GET.get('date') or request.POST.get('date'))

    if request.method == 'POST':
        for panda in classroom.get_all_pandas():
            status = request.POST.get(f'status_{panda.pk}')
            if status not in dict(Attendance.STATUS_CHOICES):
                continue
            Attendance.objects.update_or_create(
                master=classroom.master, panda=panda, classroom=classroom,
                date=date, defaults={'status': status},
            )
        messages.success(request, _('Register saved for %(date)s.') % {'date': date})
        return redirect(f"{request.path}?date={date}")

    existing = {
        a.panda_id: a.status for a in
        Attendance.objects.filter(master=classroom.master, classroom=classroom, date=date)
    }
    rows = [{'panda': p, 'status': existing.get(p.pk, Attendance.PRESENT)}
            for p in classroom.get_all_pandas().select_related('profile__user')]
    return render(request, 'classroom/attendance_register.html', {
        'classroom': classroom,
        'rows': rows,
        'date': date,
        'status_choices': Attendance.STATUS_CHOICES,
        'is_master_user': True,
        'tab': 'students',
    })


@login_required
def certificate_issue(request, classroom_pk, panda_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    panda = _member_or_404(classroom, panda_pk)
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            cert = form.save(commit=False)
            cert.master = classroom.master
            cert.panda = panda
            cert.classroom = classroom
            cert.save()
            messages.success(request, _('Certificate issued.'))
        else:
            messages.error(request, _('A certificate needs a title.'))
    return redirect('classroom:student_detail', classroom_pk=classroom.pk, panda_pk=panda.pk)


@login_required
def certificate_delete(request, classroom_pk, cert_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    cert = get_object_or_404(Certificate, pk=cert_pk, master=classroom.master)
    panda_pk = cert.panda_id
    if request.method == 'POST':
        cert.delete()
        messages.success(request, _('Certificate revoked.'))
    return redirect('classroom:student_detail', classroom_pk=classroom.pk, panda_pk=panda_pk)


# ── Groups ─────────────────────────────────────────────────────────────────────

@login_required
def group_create(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    master = classroom.master
    if request.method == 'POST':
        form = PandaGroupForm(master, request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.master = master
            group.save()
            form.save_m2m()
            classroom.groups.add(group)
            messages.success(request, _('Group "%(name)s" created with %(n)s student(s).')
                             % {'name': group.name, 'n': group.member_count})
            return redirect('classroom:students', classroom_pk=classroom.pk)
    else:
        form = PandaGroupForm(master)
    return render(request, 'classroom/group_form.html', {
        'classroom': classroom, 'form': form, 'is_master_user': True, 'tab': 'students',
    })


@login_required
def group_edit(request, classroom_pk, group_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    group = get_object_or_404(PandaGroup, pk=group_pk, master=classroom.master)
    if request.method == 'POST':
        form = PandaGroupForm(classroom.master, request.POST, instance=group)
        if form.is_valid():
            form.save()
            messages.success(request, _('Group updated.'))
            return redirect('classroom:students', classroom_pk=classroom.pk)
    else:
        form = PandaGroupForm(classroom.master, instance=group)
    return render(request, 'classroom/group_form.html', {
        'classroom': classroom, 'form': form, 'group': group,
        'is_master_user': True, 'tab': 'students',
    })


@login_required
def group_delete(request, classroom_pk, group_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    group = get_object_or_404(PandaGroup, pk=group_pk, master=classroom.master)
    if request.method == 'POST':
        group.delete()
        messages.success(request, _('Group deleted.'))
    return redirect('classroom:students', classroom_pk=classroom.pk)


# ── Payments ───────────────────────────────────────────────────────────────────

def _back(request, classroom):
    """Return to the page the POST came from.

    Money is edited from two places — the room's payments table and one
    pupil's own page — and a master who marks a fee paid from the pupil page
    should land back on the pupil, not on a table they were not looking at.
    Only same-site paths are honoured, so a posted `next` cannot bounce anyone
    off to another host.
    """
    nxt = request.POST.get('next', '')
    if nxt.startswith('/') and not nxt.startswith('//'):
        return redirect(nxt)
    return redirect('classroom:payments', classroom_pk=classroom.pk)


@login_required
def payments(request, classroom_pk):
    """This room's money: who owes what, and the running total."""
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)

    rows = (StudentPayment.objects
            .filter(master=classroom.master, classroom=classroom)
            .select_related('panda__profile__user'))
    status = request.GET.get('status')
    if status in dict(StudentPayment.STATUS_CHOICES):
        rows = rows.filter(status=status)

    totals = StudentPayment.objects.filter(master=classroom.master, classroom=classroom).aggregate(
        paid=Sum('amount', filter=Q(status=StudentPayment.PAID)),
        unpaid=Sum('amount', filter=Q(status=StudentPayment.UNPAID)),
        partial=Sum('amount', filter=Q(status=StudentPayment.PARTIAL)),
    )

    return render(request, 'classroom/payments.html', {
        'classroom': classroom,
        'rows': rows,
        'totals': totals,
        'status': status or '',
        'status_choices': StudentPayment.STATUS_CHOICES,
        'members': classroom.get_all_pandas().select_related('profile__user'),
        'payment_form': PaymentForm(),
        'is_master_user': True,
        'tab': 'payments',
    })


@login_required
def payment_add(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    if request.method == 'POST':
        raw_pk = request.POST.get('panda')
        panda = classroom.get_all_pandas().filter(pk=raw_pk).first() if raw_pk else None
        form = PaymentForm(request.POST)
        if panda is None:
            messages.error(request, _('Pick a student from this classroom.'))
        elif form.is_valid():
            payment = form.save(commit=False)
            payment.master = classroom.master
            payment.panda = panda
            payment.classroom = classroom
            payment.save()
            messages.success(request, _('Payment recorded.'))
        else:
            messages.error(request, _('Check the amount and try again.'))
    return _back(request, classroom)


@login_required
def payment_mark_paid(request, classroom_pk, payment_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    payment = get_object_or_404(StudentPayment, pk=payment_pk, master=classroom.master,
                                classroom=classroom)
    if request.method == 'POST':
        payment.status = StudentPayment.PAID
        payment.payment_date = payment.payment_date or timezone.now().date()
        payment.save(update_fields=['status', 'payment_date'])
        messages.success(request, _('Marked as paid.'))
    return _back(request, classroom)


@login_required
def payment_delete(request, classroom_pk, payment_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    payment = get_object_or_404(StudentPayment, pk=payment_pk, master=classroom.master,
                                classroom=classroom)
    if request.method == 'POST':
        payment.delete()
        messages.success(request, _('Payment record deleted.'))
    return _back(request, classroom)


# ── Resources (notes and links) ────────────────────────────────────────────────

@login_required
def resources(request, classroom_pk):
    """The shelf: everything that outlives one lesson — a syllabus, a
    recording, the Telegram group, a vocabulary PDF."""
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    is_master_user = classroom.is_master_user(request.user)
    lesson_notes = (LessonNote.objects
                    .filter(lesson__classroom=classroom)
                    .select_related('lesson')
                    .order_by('lesson__order', 'uploaded_at'))
    if not is_master_user:
        lesson_notes = lesson_notes.filter(lesson__is_published=True)
    return render(request, 'classroom/resources.html', {
        'classroom': classroom,
        'resources': classroom.resources.all(),
        'lesson_notes': lesson_notes,
        'form': ClassroomResourceForm() if is_master_user else None,
        'is_master_user': is_master_user,
        'tab': 'resources',
    })


@login_required
def resource_add(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    if request.method == 'POST':
        form = ClassroomResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.classroom = classroom
            resource.save()
            messages.success(request, _('Added to the classroom shelf.'))
            return redirect('classroom:resources', classroom_pk=classroom.pk)
        messages.error(request, _('Add a link or upload a file.'))
    else:
        form = ClassroomResourceForm()
    return render(request, 'classroom/resource_form.html', {
        'classroom': classroom, 'form': form, 'is_master_user': True, 'tab': 'resources',
    })


@login_required
def resource_delete(request, classroom_pk, res_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    resource = get_object_or_404(ClassroomResource, pk=res_pk, classroom=classroom)
    if request.method == 'POST':
        resource.delete()
        messages.success(request, _('Removed from the shelf.'))
    return redirect('classroom:resources', classroom_pk=classroom.pk)


# ── Classroom Discussion ───────────────────────────────────────────────────────

@login_required
def discussion_list(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    return render(request, 'classroom/discussion_list.html', {
        'classroom': classroom,
        'discussions': classroom.discussions.select_related('author').all(),
        'is_master_user': classroom.is_master_user(request.user),
        'tab': 'discussion',
    })


@login_required
def discussion_create(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    if request.method == 'POST':
        form = ClassroomDiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.classroom = classroom
            discussion.author = request.user
            discussion.save()
            return redirect('classroom:discussion_thread', classroom_pk=classroom.pk, thread_pk=discussion.pk)
    else:
        form = ClassroomDiscussionForm()
    return render(request, 'classroom/discussion_form.html', {
        'form': form,
        'classroom': classroom,
        'tab': 'discussion',
    })


@login_required
def discussion_thread(request, classroom_pk, thread_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    discussion = get_object_or_404(ClassroomDiscussion, pk=thread_pk, classroom=classroom)
    ClassroomDiscussion.objects.filter(pk=thread_pk).update(view_count=F('view_count') + 1)
    reply_form = ClassroomReplyForm()
    if request.method == 'POST':
        reply_form = ClassroomReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.discussion = discussion
            reply.author = request.user
            reply.save()
            return redirect('classroom:discussion_thread', classroom_pk=classroom.pk, thread_pk=discussion.pk)
    return render(request, 'classroom/discussion_thread.html', {
        'classroom': classroom,
        'discussion': discussion,
        'replies': discussion.cr_replies.select_related('author').all(),
        'reply_form': reply_form,
        'is_master_user': classroom.is_master_user(request.user),
        'tab': 'discussion',
    })


@login_required
def discussion_delete(request, classroom_pk, thread_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    discussion = get_object_or_404(ClassroomDiscussion, pk=thread_pk, classroom=classroom)
    is_master_user = classroom.is_master_user(request.user)
    if discussion.author != request.user and not is_master_user:
        raise PermissionDenied
    if request.method == 'POST':
        discussion.delete()
        messages.success(request, _('Discussion deleted.'))
        return redirect('classroom:discussion_list', classroom_pk=classroom.pk)
    return render(request, 'classroom/classroom_confirm_delete.html', {
        'classroom': classroom,
        'object_name': discussion.title,
        'is_discussion': True,
        'cancel_url': 'classroom:discussion_list',
    })
