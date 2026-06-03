import json

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone

from panda.models import Panda
from .models import Exam, ExamQuestion, ExamChoice, ExamAttempt, ExamAnswer

SECTION_ORDER = ['listening', 'reading', 'writing']
SECTION_LABELS = {
    'listening': '듣기 (Listening)',
    'reading': '읽기 (Reading)',
    'writing': '쓰기 (Writing)',
}


def _get_panda(request):
    panda, _ = Panda.objects.get_or_create(profile=request.user.profile)
    return panda


def _next_section(current):
    idx = SECTION_ORDER.index(current)
    if idx + 1 < len(SECTION_ORDER):
        return SECTION_ORDER[idx + 1]
    return 'completed'


def _record_section_start(attempt):
    now = timezone.now()
    if attempt.current_section == 'listening' and not attempt.listening_started_at:
        attempt.listening_started_at = now
        attempt.save(update_fields=['listening_started_at'])
    elif attempt.current_section == 'reading' and not attempt.reading_started_at:
        attempt.reading_started_at = now
        attempt.save(update_fields=['reading_started_at'])
    elif attempt.current_section == 'writing' and not attempt.writing_started_at:
        attempt.writing_started_at = now
        attempt.save(update_fields=['writing_started_at'])


def _calculate_mcq_score(attempt, section):
    questions = attempt.exam.questions.filter(section=section, is_writing=False)
    total = questions.count()
    if total == 0:
        return None
    answers = ExamAnswer.objects.filter(attempt=attempt, question__section=section).select_related('selected_choice')
    answer_map = {a.question_id: a.selected_choice for a in answers}
    correct = sum(
        1 for q in questions
        if answer_map.get(q.id) and answer_map[q.id].is_correct
    )
    return round((correct / total) * 100)


# ─────────────────────────────────────────────
# 1. EXAM LIST
# ─────────────────────────────────────────────
@login_required
def exam_list(request):
    exams = Exam.objects.filter(is_published=True)
    panda = _get_panda(request)
    attempts_by_exam = {
        a.exam_id: a
        for a in ExamAttempt.objects.filter(panda=panda).order_by('-start_time')
    }
    context = {
        'exams': exams,
        'attempts_by_exam': attempts_by_exam,
    }
    return render(request, 'exam/exam_list.html', context)


# ─────────────────────────────────────────────
# 2. EXAM DETAIL
# ─────────────────────────────────────────────
@login_required
def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk=pk, is_published=True)
    panda = _get_panda(request)
    last_attempt = ExamAttempt.objects.filter(panda=panda, exam=exam).first()
    listening_count = exam.questions.filter(section='listening').count()
    reading_count = exam.questions.filter(section='reading').count()
    writing_count = exam.questions.filter(section='writing').count()
    context = {
        'exam': exam,
        'last_attempt': last_attempt,
        'listening_count': listening_count,
        'reading_count': reading_count,
        'writing_count': writing_count,
    }
    return render(request, 'exam/exam_detail.html', context)


# ─────────────────────────────────────────────
# 3. START EXAM
# ─────────────────────────────────────────────
@login_required
def start_exam(request, pk):
    if request.method != 'POST':
        return redirect('exam_detail', pk=pk)
    exam = get_object_or_404(Exam, pk=pk, is_published=True)
    panda = _get_panda(request)

    # Abandon any in-progress attempt
    ExamAttempt.objects.filter(panda=panda, exam=exam).exclude(current_section='completed').update(
        current_section='completed',
        completed_at=timezone.now(),
    )

    attempt = ExamAttempt.objects.create(
        panda=panda,
        exam=exam,
        current_section='listening',
        listening_started_at=timezone.now(),
    )
    return redirect('take_section', attempt_id=attempt.id)


# ─────────────────────────────────────────────
# 4. TAKE SECTION (main scrolling exam page)
# ─────────────────────────────────────────────
@login_required
def take_section(request, attempt_id):
    attempt = get_object_or_404(ExamAttempt, pk=attempt_id)
    panda = _get_panda(request)
    if attempt.panda != panda:
        messages.error(request, 'Access denied.')
        return redirect('exam_list')
    if attempt.current_section == 'completed':
        return redirect('exam_result', attempt_id=attempt.id)

    _record_section_start(attempt)
    seconds_remaining = attempt.section_seconds_remaining()

    questions = attempt.exam.questions.filter(section=attempt.current_section).prefetch_related('choices')

    # Build maps of existing answers for pre-populating the form
    existing_answers = ExamAnswer.objects.filter(
        attempt=attempt,
        question__section=attempt.current_section,
    ).select_related('selected_choice')
    selected_choices = {a.question_id: a.selected_choice_id for a in existing_answers if a.selected_choice_id}
    written_answers = {a.question_id: a.written_answer for a in existing_answers if a.written_answer}

    context = {
        'attempt': attempt,
        'exam': attempt.exam,
        'questions': questions,
        'selected_choices': selected_choices,
        'written_answers': written_answers,
        'seconds_remaining': seconds_remaining,
        'section_label': SECTION_LABELS.get(attempt.current_section, attempt.current_section),
        'section_order_index': SECTION_ORDER.index(attempt.current_section) + 1,
        'total_sections': len(SECTION_ORDER),
    }
    return render(request, 'exam/take_section.html', context)


# ─────────────────────────────────────────────
# 5. SUBMIT SECTION
# ─────────────────────────────────────────────
@login_required
def submit_section(request, attempt_id):
    if request.method != 'POST':
        return redirect('take_section', attempt_id=attempt_id)

    attempt = get_object_or_404(ExamAttempt, pk=attempt_id)
    panda = _get_panda(request)
    if attempt.panda != panda:
        return redirect('exam_list')
    if attempt.current_section == 'completed':
        return redirect('exam_result', attempt_id=attempt.id)

    current = attempt.current_section
    questions = attempt.exam.questions.filter(section=current)

    for question in questions:
        key = f'q{question.id}'
        if question.is_writing:
            written = request.POST.get(key, '').strip()
            ExamAnswer.objects.update_or_create(
                attempt=attempt,
                question=question,
                defaults={'written_answer': written, 'selected_choice': None},
            )
        else:
            choice_id = request.POST.get(key)
            if choice_id:
                try:
                    choice = ExamChoice.objects.get(pk=choice_id, question=question)
                    ExamAnswer.objects.update_or_create(
                        attempt=attempt,
                        question=question,
                        defaults={'selected_choice': choice, 'written_answer': ''},
                    )
                except ExamChoice.DoesNotExist:
                    pass

    # Score MCQ sections immediately
    if current == 'listening':
        attempt.listening_score = _calculate_mcq_score(attempt, 'listening')
    elif current == 'reading':
        attempt.reading_score = _calculate_mcq_score(attempt, 'reading')

    # Advance to next section
    next_section = _next_section(current)
    attempt.current_section = next_section
    if next_section == 'completed':
        attempt.completed_at = timezone.now()
    attempt.save()

    if next_section == 'completed':
        return redirect('exam_result', attempt_id=attempt.id)
    return redirect('take_section', attempt_id=attempt.id)


# ─────────────────────────────────────────────
# 5b. AUTOSAVE (AJAX)
# ─────────────────────────────────────────────
@login_required
def autosave_section(request, attempt_id):
    if request.method != 'POST':
        return JsonResponse({'ok': False}, status=405)
    attempt = get_object_or_404(ExamAttempt, pk=attempt_id)
    panda = _get_panda(request)
    if attempt.panda != panda or attempt.current_section == 'completed':
        return JsonResponse({'ok': False}, status=403)
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, ValueError):
        return JsonResponse({'ok': False}, status=400)
    questions = {q.id: q for q in attempt.exam.questions.filter(section=attempt.current_section)}
    for qid_str, value in data.items():
        try:
            qid = int(qid_str)
        except (ValueError, TypeError):
            continue
        question = questions.get(qid)
        if not question:
            continue
        if question.is_writing:
            ExamAnswer.objects.update_or_create(
                attempt=attempt, question=question,
                defaults={'written_answer': str(value)[:10000], 'selected_choice': None},
            )
        elif value:
            try:
                choice = ExamChoice.objects.get(pk=int(value), question=question)
                ExamAnswer.objects.update_or_create(
                    attempt=attempt, question=question,
                    defaults={'selected_choice': choice, 'written_answer': ''},
                )
            except (ExamChoice.DoesNotExist, ValueError, TypeError):
                pass
    return JsonResponse({'ok': True})


# ─────────────────────────────────────────────
# 6. EXAM RESULT
# ─────────────────────────────────────────────
@login_required
def exam_result(request, attempt_id):
    attempt = get_object_or_404(ExamAttempt, pk=attempt_id)
    panda = _get_panda(request)
    if attempt.panda != panda:
        return redirect('exam_list')

    answers = ExamAnswer.objects.filter(attempt=attempt).select_related(
        'question', 'selected_choice'
    )
    answer_map = {a.question_id: a for a in answers}

    listening_questions = attempt.exam.questions.filter(section='listening').prefetch_related('choices')
    reading_questions = attempt.exam.questions.filter(section='reading').prefetch_related('choices')
    writing_questions = attempt.exam.questions.filter(section='writing')

    context = {
        'attempt': attempt,
        'exam': attempt.exam,
        'answer_map': answer_map,
        'listening_questions': listening_questions,
        'reading_questions': reading_questions,
        'writing_questions': writing_questions,
    }
    return render(request, 'exam/exam_result.html', context)
