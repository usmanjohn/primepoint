from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.db.models import Q, F

from .models import Classroom, Lesson, LessonNote, ClassroomDiscussion, ClassroomReply
from .forms import (
    ClassroomForm, ClassroomMembershipForm, LessonForm,
    LessonNoteForm, ClassroomDiscussionForm, ClassroomReplyForm,
)


def _get_master(request):
    try:
        return request.user.profile.master
    except Exception:
        return None


def _require_master_owns(request, classroom):
    if classroom.master.profile.user != request.user:
        raise PermissionDenied


def _require_member(request, classroom):
    if not classroom.is_member(request.user):
        raise PermissionDenied


# ── Classroom CRUD ─────────────────────────────────────────────────────────────

@login_required
def classroom_list(request):
    master = _get_master(request)
    if master:
        classrooms = master.classrooms.all()
        is_master = True
    else:
        try:
            panda = request.user.profile.panda
            classrooms = Classroom.objects.filter(
                Q(groups__members=panda) | Q(individual_pandas=panda)
            ).distinct()
        except Exception:
            classrooms = Classroom.objects.none()
        is_master = False
    return render(request, 'classroom/classroom_list.html', {
        'classrooms': classrooms,
        'is_master': is_master,
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
            messages.success(request, 'Classroom created. Now add members.')
            return redirect('classroom:manage', pk=classroom.pk)
    else:
        form = ClassroomForm()
    return render(request, 'classroom/classroom_form.html', {
        'form': form,
        'form_title': 'Create Classroom',
        'form_subtitle': 'Set up a new private classroom for your students.',
    })


@login_required
def classroom_detail(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    _require_member(request, classroom)
    is_master_user = (request.user == classroom.master.profile.user)
    if is_master_user:
        lessons = classroom.lessons.all()
    else:
        lessons = classroom.lessons.filter(is_published=True)
    return render(request, 'classroom/classroom_detail.html', {
        'classroom': classroom,
        'lessons': lessons,
        'is_master_user': is_master_user,
    })


@login_required
def classroom_edit(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    _require_master_owns(request, classroom)
    if request.method == 'POST':
        form = ClassroomForm(request.POST, instance=classroom)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classroom updated.')
            return redirect('classroom:detail', pk=classroom.pk)
    else:
        form = ClassroomForm(instance=classroom)
    return render(request, 'classroom/classroom_form.html', {
        'form': form,
        'classroom': classroom,
        'form_title': 'Edit Classroom',
        'form_subtitle': 'Update classroom details.',
    })


@login_required
def classroom_delete(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    _require_master_owns(request, classroom)
    if request.method == 'POST':
        classroom.delete()
        messages.success(request, 'Classroom deleted.')
        return redirect('classroom:list')
    return render(request, 'classroom/classroom_confirm_delete.html', {
        'classroom': classroom,
        'object_name': classroom.name,
        'cancel_url': 'classroom:detail',
        'cancel_pk': classroom.pk,
    })


@login_required
def classroom_manage(request, pk):
    classroom = get_object_or_404(Classroom, pk=pk)
    _require_master_owns(request, classroom)
    master = classroom.master
    if request.method == 'POST':
        form = ClassroomMembershipForm(master, request.POST)
        if form.is_valid():
            classroom.groups.set(form.cleaned_data['groups'])
            classroom.individual_pandas.set(form.cleaned_data['individual_pandas'])
            messages.success(request, 'Membership updated.')
            return redirect('classroom:manage', pk=classroom.pk)
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
    })


# ── Lesson CRUD ────────────────────────────────────────────────────────────────

@login_required
def lesson_create(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    master = classroom.master
    if request.method == 'POST':
        form = LessonForm(master, request.POST)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.classroom = classroom
            lesson.save()
            form.save_m2m()
            messages.success(request, 'Lesson created.')
            return redirect('classroom:lesson_detail', classroom_pk=classroom.pk, lesson_pk=lesson.pk)
    else:
        next_order = classroom.lessons.count()
        form = LessonForm(master, initial={'order': next_order})
    return render(request, 'classroom/lesson_form.html', {
        'form': form,
        'classroom': classroom,
        'form_title': 'Add Lesson',
    })


@login_required
def lesson_detail(request, classroom_pk, lesson_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, classroom=classroom)
    is_master_user = (request.user == classroom.master.profile.user)
    if not is_master_user and not lesson.is_published:
        raise PermissionDenied
    notes = lesson.notes.all()
    practices = lesson.practices.all()
    homeworks = lesson.homeworks.all()
    tutorials = lesson.tutorials.all()
    note_form = LessonNoteForm() if is_master_user else None
    return render(request, 'classroom/lesson_detail.html', {
        'classroom': classroom,
        'lesson': lesson,
        'notes': notes,
        'practices': practices,
        'homeworks': homeworks,
        'tutorials': tutorials,
        'note_form': note_form,
        'is_master_user': is_master_user,
    })


@login_required
def lesson_edit(request, classroom_pk, lesson_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, classroom=classroom)
    master = classroom.master
    if request.method == 'POST':
        form = LessonForm(master, request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson updated.')
            return redirect('classroom:lesson_detail', classroom_pk=classroom.pk, lesson_pk=lesson.pk)
    else:
        form = LessonForm(master, instance=lesson)
    return render(request, 'classroom/lesson_form.html', {
        'form': form,
        'classroom': classroom,
        'lesson': lesson,
        'form_title': 'Edit Lesson',
    })


@login_required
def lesson_delete(request, classroom_pk, lesson_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, classroom=classroom)
    if request.method == 'POST':
        lesson.delete()
        messages.success(request, 'Lesson deleted.')
        return redirect('classroom:detail', pk=classroom.pk)
    return render(request, 'classroom/lesson_confirm_delete.html', {
        'classroom': classroom,
        'lesson': lesson,
    })


# ── Lesson Notes ───────────────────────────────────────────────────────────────

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
            messages.success(request, 'Note uploaded.')
        else:
            messages.error(request, 'Please select a valid file.')
    return redirect('classroom:lesson_detail', classroom_pk=classroom.pk, lesson_pk=lesson.pk)


@login_required
def lesson_note_delete(request, classroom_pk, lesson_pk, note_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_master_owns(request, classroom)
    lesson = get_object_or_404(Lesson, pk=lesson_pk, classroom=classroom)
    note = get_object_or_404(LessonNote, pk=note_pk, lesson=lesson)
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted.')
    return redirect('classroom:lesson_detail', classroom_pk=classroom.pk, lesson_pk=lesson.pk)


# ── Classroom Discussion ───────────────────────────────────────────────────────

@login_required
def discussion_list(request, classroom_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    is_master_user = (request.user == classroom.master.profile.user)
    discussions = classroom.discussions.select_related('author').all()
    return render(request, 'classroom/discussion_list.html', {
        'classroom': classroom,
        'discussions': discussions,
        'is_master_user': is_master_user,
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
    })


@login_required
def discussion_thread(request, classroom_pk, thread_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    discussion = get_object_or_404(ClassroomDiscussion, pk=thread_pk, classroom=classroom)
    ClassroomDiscussion.objects.filter(pk=thread_pk).update(view_count=F('view_count') + 1)
    is_master_user = (request.user == classroom.master.profile.user)
    replies = discussion.cr_replies.select_related('author').all()
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
        'replies': replies,
        'reply_form': reply_form,
        'is_master_user': is_master_user,
    })


@login_required
def discussion_delete(request, classroom_pk, thread_pk):
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    _require_member(request, classroom)
    discussion = get_object_or_404(ClassroomDiscussion, pk=thread_pk, classroom=classroom)
    is_master_user = (request.user == classroom.master.profile.user)
    if discussion.author != request.user and not is_master_user:
        raise PermissionDenied
    if request.method == 'POST':
        discussion.delete()
        messages.success(request, 'Discussion deleted.')
        return redirect('classroom:discussion_list', classroom_pk=classroom.pk)
    return render(request, 'classroom/classroom_confirm_delete.html', {
        'classroom': classroom,
        'object_name': discussion.title,
        'is_discussion': True,
        'cancel_url': 'classroom:discussion_list',
    })
