"""Workbook views — all function-based, all server-rendered, no JavaScript.

Each section of a workbook is its own <form>. Sending it marks the typed
items on the server and redirects back to that section, where every line now
shows ✓ or ✗ and the explanation opens in a native <details>. That is the
whole interaction: type, send, read why.
"""
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext as _

from . import grading, pdfs
from .models import (
    AUTO_KINDS, AnswerAppeal, ItemResponse, TaskItem, Workbook, WorkbookAttempt,
)

MAX_TEXT = 2000


def _visible(user):
    qs = Workbook.objects.select_related('tutorial')
    return qs if user.is_staff else qs.filter(is_published=True, tutorial__is_published=True)


def _decorate(sections, responses):
    """Hang each item's saved response on it for the template."""
    for _code, _label, _icon, tasks in sections:
        for task in tasks:
            for item in task.items.all():
                item.resp = responses.get(item.pk)
    return sections


def _section_stats(sections, responses):
    """{code: (right, marked)} for the chips on each section header."""
    stats = {}
    for code, _label, _icon, tasks in sections:
        right = marked = 0
        for task in tasks:
            if task.kind not in AUTO_KINDS:
                continue
            for item in task.items.all():
                r = responses.get(item.pk)
                if r and r.verdict and r.verdict != grading.EMPTY:
                    marked += 1
                    right += bool(r.is_correct)
        stats[code] = (right, marked)
    return stats


def workbook_detail(request, pk):
    workbook = get_object_or_404(_visible(request.user), pk=pk)

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{reverse('login')}?next={request.path}")
        return _submit(request, workbook)

    attempt, responses = None, {}
    if request.user.is_authenticated:
        attempt = WorkbookAttempt.objects.filter(user=request.user, workbook=workbook).first()
        if attempt:
            responses = {r.item_id: r for r in attempt.responses.all()}

    sections = _decorate(workbook.sections(), responses)
    stats = _section_stats(sections, responses)
    practice = workbook.tutorial.practices.filter(is_published=True).first()
    story = (workbook.tutorial.stories.filter(is_published=True)
             .select_related('collection__subject').first())

    return render(request, 'workbook/workbook.html', {
        'workbook': workbook,
        'tutorial': workbook.tutorial,
        'sections': [
            {'code': c, 'label': l, 'icon': i, 'tasks': t,
             'sent': bool(attempt and c in attempt.sections_done),
             'right': stats[c][0], 'marked': stats[c][1]}
            for c, l, i, t in sections
        ],
        'attempt': attempt,
        'pdf_url': pdfs.pdf_url(workbook),
        'practice': practice,
        'story': story,
    })


@transaction.atomic
def _submit(request, workbook):
    """Save and mark one section, or one self-mark, then go back to it."""
    action = request.POST.get('action', 'section')
    attempt, _created = WorkbookAttempt.objects.get_or_create(
        user=request.user, workbook=workbook)
    url = reverse('workbook_detail', args=[workbook.pk])

    if action == 'selfmark':
        item = get_object_or_404(TaskItem, pk=request.POST.get('item'),
                                 task__workbook=workbook, task__kind='write')
        value = request.POST.get('value')
        if value in ('good', 'again'):
            ItemResponse.objects.filter(attempt=attempt, item=item).update(self_mark=value)
        return redirect(f'{url}#t{item.task_id}')

    code = request.POST.get('section', '')
    tasks = list(workbook.tasks.filter(section=code).prefetch_related('items'))
    if not tasks:
        return redirect(url)

    anything = False
    for task in tasks:
        for item in task.items.all():
            response, _new = ItemResponse.objects.get_or_create(attempt=attempt, item=item)
            if task.kind in AUTO_KINDS:
                response.text = (request.POST.get(f'i{item.pk}') or '')[:MAX_TEXT]
                response.regrade()
                anything |= response.verdict != grading.EMPTY
            elif task.kind == 'write':
                text = (request.POST.get(f'i{item.pk}') or '').strip()[:MAX_TEXT]
                if text != response.text:
                    response.self_mark = ''      # a new text needs a new verdict
                response.text = text
                response.checks = sorted({int(c) for c in request.POST.getlist(f'c{item.pk}')
                                          if c.isdigit() and int(c) < len(item.checklist)})
                anything |= bool(text)
            else:  # mission / copy — ticked done
                response.done = request.POST.get(f'd{item.pk}') == '1'
                response.text = (request.POST.get(f'i{item.pk}') or '').strip()[:MAX_TEXT]
                anything |= response.done
            response.save()

    if not anything:
        messages.info(request, _('Nothing was filled in yet — write your answers, then send.'))
        return redirect(f'{url}#sec-{code}')

    was_complete = attempt.is_complete
    attempt.mark_section_done(code)
    attempt.rescore()
    attempt.save()

    if attempt.is_complete and not was_complete:
        messages.success(request, _('Workbook finished! +%(points)s points.')
                         % {'points': f'{attempt.points_awarded:g}'})
        from homework.items import tick_off
        tick_off(request.user, 'workbook', workbook)
    panda = getattr(getattr(request.user, 'profile', None), 'panda', None)
    if panda and attempt.is_complete:
        panda.recalc_rating()
    return redirect(f'{url}#sec-{code}')


@login_required
def appeal(request, item_pk):
    """"My answer was right" — queue it for a human to look at."""
    item = get_object_or_404(TaskItem, pk=item_pk, task__kind__in=AUTO_KINDS)
    url = reverse('workbook_detail', args=[item.task.workbook_id])
    if request.method != 'POST':
        return redirect(url)
    response = ItemResponse.objects.filter(
        attempt__user=request.user, item=item).first()
    if response and response.text.strip() and not response.is_correct:
        AnswerAppeal.objects.get_or_create(item=item, user=request.user,
                                           text=response.text.strip()[:500])
        messages.success(request, _('Thank you — a teacher will look at your answer. '
                                    'If it is right, it will be marked right for everyone.'))
    return redirect(f'{url}#t{item.task_id}')


def worksheet(request, pk):
    """The A4 worksheet. Open to everyone on purpose: it is homework, not the
    lesson, and the watermark makes every printed copy an advert."""
    workbook = get_object_or_404(_visible(request.user), pk=pk)
    show_key = request.GET.get('key', '1') != '0'
    sections = workbook.sections()
    for _code, _label, _icon, tasks in sections:
        for task in tasks:
            for item in task.items.all():
                # 원고지 squares: one per letter of the answer, so a Hangul
                # item is written into boxes exactly like a Korean copybook.
                letters = ''.join((item.answers or [''])[0].split())
                item.ws_boxes = range(max(len(letters), 1))
    return render(request, 'workbook/worksheet.html', {
        'workbook': workbook,
        'tutorial': workbook.tutorial,
        'sections': sections,
        'show_key': show_key,
        'bare': request.GET.get('bare') == '1',
        'back_url': reverse('workbook_detail', args=[workbook.pk]),
        'url_key_on': '?key=1',
        'url_key_off': '?key=0',
        'pdf_url': pdfs.pdf_url(workbook),
    })


# ── Teachers ──────────────────────────────────────────────────────────────

def _teaches(user, pupil):
    """Staff, or a master who has this pupil — directly or in a classroom."""
    if user.is_staff:
        return True
    from masters.models import Master
    master = Master.objects.filter(profile__user=user).first()
    panda = getattr(getattr(pupil, 'profile', None), 'panda', None)
    if master is None or panda is None:
        return False
    if master.pandas.filter(pk=panda.pk).exists():
        return True
    return any(c.get_all_pandas().filter(pk=panda.pk).exists()
               for c in master.classrooms.all())


@login_required
def review(request, pk, user_pk):
    """A teacher reads one pupil's workbook — the writing above all — and
    leaves a note the pupil sees at the top of their workbook."""
    workbook = get_object_or_404(Workbook.objects.select_related('tutorial'), pk=pk)
    pupil = get_object_or_404(User, pk=user_pk)
    if not _teaches(request.user, pupil):
        raise PermissionDenied
    attempt = WorkbookAttempt.objects.filter(user=pupil, workbook=workbook).first()

    if request.method == 'POST' and attempt:
        attempt.teacher_note = (request.POST.get('teacher_note') or '').strip()[:MAX_TEXT]
        attempt.teacher_note_by = request.user
        attempt.save(update_fields=['teacher_note', 'teacher_note_by', 'updated_at'])
        messages.success(request, _('Note saved — the pupil sees it on their workbook.'))
        return redirect('workbook_review', pk=pk, user_pk=user_pk)

    responses = {r.item_id: r for r in attempt.responses.all()} if attempt else {}
    sections = _decorate(workbook.sections(), responses)
    return render(request, 'workbook/review.html', {
        'workbook': workbook,
        'pupil': pupil,
        'attempt': attempt,
        'sections': sections,
        'back': request.GET.get('back', ''),
    })


@login_required
def appeals(request):
    """Staff: the queue of "I was right" appeals. Accepting one adds the text
    to the item's accepted answers and re-marks everyone who typed it."""
    if not request.user.is_staff:
        raise PermissionDenied
    if request.method == 'POST':
        appeal_obj = get_object_or_404(AnswerAppeal, pk=request.POST.get('appeal'))
        decision = request.POST.get('decision')
        if decision == 'accept':
            item = appeal_obj.item
            accept_answer(item, appeal_obj.text)
            item.refresh_from_db()
            # Other pupils may have appealed the same answer — settle them too.
            for other in item.appeals.filter(status='open'):
                if grading.is_correct(item.mark(other.text)):
                    other.status, other.decided_at = 'accepted', timezone.now()
                    other.save(update_fields=['status', 'decided_at'])
            messages.success(request, _('Accepted — added to the answers and re-marked.'))
        elif decision == 'reject':
            appeal_obj.status = 'rejected'
            appeal_obj.decided_at = timezone.now()
            appeal_obj.save(update_fields=['status', 'decided_at'])
        return redirect('workbook_appeals')

    open_appeals = (AnswerAppeal.objects.filter(status='open')
                    .select_related('item__task__workbook__tutorial', 'user'))
    return render(request, 'workbook/appeals.html', {'appeals': open_appeals})


@transaction.atomic
def accept_answer(item, text):
    """Add `text` to the item's accepted answers and re-mark every response."""
    text = text.strip()
    if grading.mark(text, item.answers) == grading.RIGHT:
        return
    item.answers = list(item.answers) + [text]
    item.save(update_fields=['answers'])
    touched = set()
    for response in item.responses.select_related('attempt'):
        before = response.is_correct
        response.regrade()
        if response.is_correct != before:
            response.save(update_fields=['verdict', 'is_correct', 'updated_at'])
            touched.add(response.attempt)
    for attempt in touched:
        attempt.rescore()
        attempt.save()
