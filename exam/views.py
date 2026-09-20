import json
from datetime import timedelta

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone

from panda.models import Panda
from . import satscore
from .models import (
    Exam, ExamModule, ExamModuleAttempt, ExamPassage, ExamQuestion, ExamChoice,
    ExamAttempt, ExamAnswer,
)
from prime.subjects import get_study_subjects, allowed_values, mapped_values


def _get_panda(request):
    panda, _ = Panda.objects.get_or_create(profile=request.user.profile)
    return panda


# ─────────────────────────────────────────────
# Flow: which module comes next
# ─────────────────────────────────────────────
def _route_target(attempt, module):
    """For a stage-1 module, the stage-2 branch this taker has earned."""
    branches = attempt.exam.modules.filter(kind=module.kind, stage=2)
    if not branches.exists():
        return None
    ma = attempt.module_attempt(module)
    raw = (ma.raw_score if ma and ma.raw_score is not None else 0)
    threshold = module.route_threshold
    wanted = 'hard' if (threshold is not None and raw >= threshold) else 'easy'
    return branches.filter(difficulty=wanted).first() or branches.first()


def _next_module(attempt, module):
    """What follows `module` — its stage-2 branch, or the next kind. None = done."""
    if module.stage == 1:
        branch = _route_target(attempt, module)
        if branch:
            return branch
    return attempt.exam.modules.filter(
        stage=1, order__gt=module.order).order_by('order').first()


def _start_module(attempt, module, now=None):
    """Put the attempt on `module` and start its clock if it is not already running."""
    now = now or timezone.now()
    ma, _ = ExamModuleAttempt.objects.get_or_create(
        attempt=attempt, module=module,
        defaults={'total_questions': module.questions_count()},
    )
    if not ma.started_at:
        ma.started_at = now
        ma.total_questions = module.questions_count()
        ma.save(update_fields=['started_at', 'total_questions'])
    attempt.current_module = module
    attempt.current_section = module.code
    attempt.status = 'in_progress'
    attempt.break_until = None
    attempt.save(update_fields=['current_module', 'current_section', 'status', 'break_until'])
    return ma


def _finish(attempt):
    attempt.current_module = None
    attempt.current_section = 'completed'
    attempt.status = 'completed'
    attempt.completed_at = timezone.now()
    attempt.break_until = None
    _score_attempt(attempt)
    attempt.save()


# ─────────────────────────────────────────────
# Scoring
# ─────────────────────────────────────────────
def _grade_module(attempt, module):
    """Count the correct answers in one module and store them on its row."""
    questions = list(module.questions().prefetch_related('choices'))
    answers = {
        a.question_id: a for a in ExamAnswer.objects.filter(
            attempt=attempt, question__section=module.code).select_related('selected_choice')
    }
    gradable = [q for q in questions if q.answer_type != 'essay' and not q.is_writing]
    raw = 0
    for question in gradable:
        answer = answers.get(question.id)
        if answer and answer.is_correct():
            raw += 1
    ma, _ = ExamModuleAttempt.objects.get_or_create(
        attempt=attempt, module=module, defaults={'total_questions': len(questions)})
    ma.total_questions = len(gradable) or len(questions)
    ma.raw_score = raw if gradable else None
    ma.submitted_at = timezone.now()
    ma.save(update_fields=['total_questions', 'raw_score', 'submitted_at'])

    # Legacy TOPIK fields — the old result template and prime/progress read them.
    if module.kind in ('listening', 'reading') and gradable:
        setattr(attempt, f'{module.kind}_score', round(raw / len(gradable) * 100))
        attempt.save(update_fields=[f'{module.kind}_score'])
    return ma


def _section_result(attempt, kind):
    """Raw total, question total and route taken for one SAT section."""
    rows = attempt.module_attempts.filter(module__kind=kind).select_related('module')
    if not rows:
        return None
    raw = sum(r.raw_score or 0 for r in rows)
    total = sum(r.total_questions or 0 for r in rows)
    branch = next((r.module for r in rows if r.module.stage == 2), None)
    route = branch.difficulty if branch else 'easy'
    return {
        'kind': kind,
        'label': satscore.SECTION_LABELS.get(kind, kind),
        'raw': raw,
        'total': total,
        'route': route,
        'scaled': satscore.scale(kind, route, raw),
        'modules': list(rows),
    }


def _score_attempt(attempt):
    if not attempt.exam.is_sat:
        return None
    rw = _section_result(attempt, 'rw')
    math = _section_result(attempt, 'math')
    attempt.rw_score = rw['scaled'] if rw else None
    attempt.math_score = math['scaled'] if math else None
    if attempt.rw_score is not None and attempt.math_score is not None:
        attempt.total_score = attempt.rw_score + attempt.math_score
    return {'rw': rw, 'math': math}


# ─────────────────────────────────────────────
# 1. EXAM LIST
# ─────────────────────────────────────────────
def exam_list(request):
    exams = Exam.objects.filter(is_published=True).prefetch_related('modules')
    personalized = False
    slugs = get_study_subjects(request)
    if slugs and not request.GET.get('all'):
        chosen = allowed_values(slugs, 'exam_languages')
        unmapped = {c for c, _ in Exam.LANGUAGE_CHOICES} - mapped_values('exam_languages')
        exams = exams.filter(language__in=chosen | unmapped)
        personalized = True
    attempts_by_exam = {}
    if request.user.is_authenticated:
        panda = _get_panda(request)
        attempts_by_exam = {
            a.exam_id: a
            for a in ExamAttempt.objects.filter(panda=panda).order_by('-start_time')
        }
    context = {
        'exams': exams,
        'attempts_by_exam': attempts_by_exam,
        'personalized': personalized,
    }
    return render(request, 'exam/exam_list.html', context)


# ─────────────────────────────────────────────
# 2. EXAM DETAIL
# ─────────────────────────────────────────────
def exam_detail(request, pk):
    exam = get_object_or_404(Exam, pk=pk, is_published=True)
    last_attempt = None
    if request.user.is_authenticated:
        panda = _get_panda(request)
        last_attempt = ExamAttempt.objects.filter(panda=panda, exam=exam).first()
    spine = []
    for module in exam.spine():
        branches = exam.modules.filter(kind=module.kind, stage=2).order_by('difficulty')
        spine.append({
            'module': module,
            'count': module.questions_count(),
            'branches': list(branches),
            'branch_count': branches[0].questions_count() if branches else 0,
            'branch_minutes': max((b.minutes for b in branches), default=0),
            # A break follows the module it is declared on, which for an
            # adaptive section is the branch, not the spine module.
            'break_minutes': max(
                [module.break_minutes] + [b.break_minutes for b in branches]),
        })
    context = {
        'exam': exam,
        'last_attempt': last_attempt,
        'spine': spine,
        'is_adaptive': exam.modules.filter(stage=2).exists(),
        # Legacy TOPIK counts, still used by the non-SAT half of the template.
        'listening_count': exam.questions.filter(section='listening').count(),
        'reading_count': exam.questions.filter(section='reading').count(),
        'writing_count': exam.questions.filter(section='writing').count(),
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

    first = exam.spine().first()
    if not first:
        messages.error(request, 'This exam has no modules yet.')
        return redirect('exam_detail', pk=pk)

    # Abandon any in-progress attempt
    ExamAttempt.objects.filter(panda=panda, exam=exam).exclude(current_section='completed').update(
        current_section='completed', status='completed', completed_at=timezone.now(),
    )

    attempt = ExamAttempt.objects.create(panda=panda, exam=exam, current_section=first.code)
    _start_module(attempt, first)
    return redirect('take_section', attempt_id=attempt.id)


# ─────────────────────────────────────────────
# 4. TAKE MODULE (main scrolling exam page)
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
    if attempt.status == 'break':
        return redirect('exam_break', attempt_id=attempt.id)

    module = attempt.current_module
    if not module:
        module = attempt.exam.spine().first()
        if not module:
            return redirect('exam_detail', pk=attempt.exam_id)
    _start_module(attempt, module)

    questions = module.questions().prefetch_related('choices')
    passages_qs = ExamPassage.objects.filter(exam=attempt.exam, section=module.code)
    passage_map = {p.question_from: p for p in passages_qs}

    existing_answers = ExamAnswer.objects.filter(
        attempt=attempt, question__section=module.code,
    ).select_related('selected_choice')
    selected_choices = {a.question_id: a.selected_choice_id for a in existing_answers if a.selected_choice_id}
    written_answers = {a.question_id: a.written_answer for a in existing_answers if a.written_answer}

    spine = list(attempt.exam.spine())
    position = next((i for i, m in enumerate(spine) if m.kind == module.kind), 0)
    steps_per_kind = 2 if attempt.exam.modules.filter(kind=module.kind, stage=2).exists() else 1
    step = position * steps_per_kind + module.stage
    total_steps = sum(
        2 if attempt.exam.modules.filter(kind=m.kind, stage=2).exists() else 1 for m in spine
    )

    context = {
        'attempt': attempt,
        'exam': attempt.exam,
        'module': module,
        'questions': questions,
        'passage_map': passage_map,
        'selected_choices': selected_choices,
        'written_answers': written_answers,
        'seconds_remaining': attempt.section_seconds_remaining(),
        'section_label': module.label,
        'section_order_index': step,
        'total_sections': total_steps,
        'is_last_module': _next_module(attempt, module) is None,
    }
    return render(request, 'exam/take_section.html', context)


# ─────────────────────────────────────────────
# 5. SUBMIT MODULE
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

    module = attempt.current_module
    if not module:
        return redirect('take_section', attempt_id=attempt.id)

    for question in module.questions():
        key = f'q{question.id}'
        if question.is_writing or question.answer_type in ('essay', 'grid'):
            written = request.POST.get(key, '').strip()
            ExamAnswer.objects.update_or_create(
                attempt=attempt, question=question,
                defaults={'written_answer': written, 'selected_choice': None},
            )
        else:
            choice_id = request.POST.get(key)
            if choice_id:
                try:
                    choice = ExamChoice.objects.get(pk=choice_id, question=question)
                    ExamAnswer.objects.update_or_create(
                        attempt=attempt, question=question,
                        defaults={'selected_choice': choice, 'written_answer': ''},
                    )
                except ExamChoice.DoesNotExist:
                    pass

    _grade_module(attempt, module)

    following = _next_module(attempt, module)
    if following is None:
        _finish(attempt)
        return redirect('exam_result', attempt_id=attempt.id)

    if module.break_minutes:
        attempt.current_module = following
        attempt.current_section = following.code
        attempt.status = 'break'
        attempt.break_until = timezone.now() + timedelta(minutes=module.break_minutes)
        attempt.save(update_fields=['current_module', 'current_section', 'status', 'break_until'])
        return redirect('exam_break', attempt_id=attempt.id)

    _start_module(attempt, following)
    return redirect('take_section', attempt_id=attempt.id)


# ─────────────────────────────────────────────
# 5b. BREAK
# ─────────────────────────────────────────────
@login_required
def exam_break(request, attempt_id):
    attempt = get_object_or_404(ExamAttempt, pk=attempt_id)
    panda = _get_panda(request)
    if attempt.panda != panda:
        return redirect('exam_list')
    if attempt.current_section == 'completed':
        return redirect('exam_result', attempt_id=attempt.id)
    if attempt.status != 'break' or not attempt.current_module:
        return redirect('take_section', attempt_id=attempt.id)

    resuming = request.method == 'POST' or attempt.break_seconds_remaining() <= 0
    if resuming:
        _start_module(attempt, attempt.current_module)
        return redirect('take_section', attempt_id=attempt.id)

    context = {
        'attempt': attempt,
        'exam': attempt.exam,
        'next_module': attempt.current_module,
        'seconds_remaining': attempt.break_seconds_remaining(),
    }
    return render(request, 'exam/exam_break.html', context)


# ─────────────────────────────────────────────
# 5c. AUTOSAVE (AJAX)
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
    module = attempt.current_module
    if not module:
        return JsonResponse({'ok': False}, status=400)
    questions = {q.id: q for q in module.questions()}
    for qid_str, value in data.items():
        try:
            qid = int(qid_str)
        except (ValueError, TypeError):
            continue
        question = questions.get(qid)
        if not question:
            continue
        if question.is_writing or question.answer_type in ('essay', 'grid'):
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
# 6. RESULT
# ─────────────────────────────────────────────
def _domain_breakdown(attempt, kind):
    """Correct-per-domain for the SAT score report."""
    rows = {}
    modules = [ma.module for ma in attempt.module_attempts.select_related('module')
               if ma.module.kind == kind]
    codes = [m.code for m in modules]
    questions = attempt.exam.questions.filter(section__in=codes).prefetch_related('choices')
    answers = {a.question_id: a for a in ExamAnswer.objects.filter(
        attempt=attempt, question__section__in=codes).select_related('selected_choice')}
    for question in questions:
        if question.answer_type == 'essay' or question.is_writing:
            continue
        name = question.skill or 'Boshqa'
        row = rows.setdefault(name, {'skill': name, 'correct': 0, 'total': 0})
        row['total'] += 1
        answer = answers.get(question.id)
        if answer and answer.is_correct():
            row['correct'] += 1
    for row in rows.values():
        row['percent'] = round(row['correct'] / row['total'] * 100) if row['total'] else 0
    return sorted(rows.values(), key=lambda r: (-r['percent'], r['skill']))


@login_required
def exam_result(request, attempt_id):
    attempt = get_object_or_404(ExamAttempt, pk=attempt_id)
    panda = _get_panda(request)
    if attempt.panda != panda:
        return redirect('exam_list')

    answers = ExamAnswer.objects.filter(attempt=attempt).select_related(
        'question', 'selected_choice')
    answer_map = {a.question_id: a for a in answers}

    context = {
        'attempt': attempt,
        'exam': attempt.exam,
        'answer_map': answer_map,
    }

    if attempt.exam.is_sat:
        passages = {
            (p.section, p.question_from): p
            for p in ExamPassage.objects.filter(exam=attempt.exam)
        }
        sections = []
        for kind in ('rw', 'math'):
            result = _section_result(attempt, kind)
            if not result:
                continue
            result['breakdown'] = _domain_breakdown(attempt, kind)
            result['review'] = []
            for ma in result['modules']:
                questions = list(ma.module.questions().prefetch_related('choices'))
                # Hang each question's own stimulus on it. Without the passage a
                # Words in Context review reads "Which choice completes the text"
                # with no text — the explanation has nothing to point at.
                for question in questions:
                    question.stimulus = passages.get((question.section, question.number))
                result['review'].append({'module': ma.module, 'questions': questions})
            sections.append(result)
        context.update({
            'sat_sections': sections,
            'band': satscore.band(attempt.total_score),
        })
        return render(request, 'exam/exam_result_sat.html', context)

    context.update({
        'listening_questions': attempt.exam.questions.filter(section='listening').prefetch_related('choices'),
        'reading_questions': attempt.exam.questions.filter(section='reading').prefetch_related('choices'),
        'writing_questions': attempt.exam.questions.filter(section='writing'),
    })
    return render(request, 'exam/exam_result.html', context)
