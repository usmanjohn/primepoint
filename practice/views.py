from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count
from panda.models import Panda
from masters.models import Master

from .models import Practice, PracticeQuestion, PracticeChoice, PracticeAttempt, UserAnswer, Subject
from .forms import PracticeForm, PracticeQuestionForm

# Avoid circular import — imported lazily in finish_practice
def _auto_link_homework(attempt):
    from homework.models import HomeworkAssignment
    HomeworkAssignment.objects.filter(
        panda=attempt.panda,
        homework__practice=attempt.practice,
        status='pending',
    ).update(attempt=attempt, status='submitted', submitted_at=attempt.completed_at)


# ─────────────────────────────────────────────
# 1. PRACTICE LIST — Browse & filter practices
# ─────────────────────────────────────────────
@login_required
def practice_list(request):
    practices = Practice.objects.filter(is_published=True).select_related(
        'subject', 'master__profile__user'
    ).annotate(
        question_count=Count('questions', distinct=True)
    )

    subject_id = request.GET.get('subject')
    if subject_id:
        practices = practices.filter(subject_id=subject_id)

    level = request.GET.get('level')
    if level:
        practices = practices.filter(level=level)

    master_id = request.GET.get('master')
    if master_id:
        practices = practices.filter(master_id=master_id)

    is_free = request.GET.get('is_free')
    if is_free == '1':
        practices = practices.filter(is_free=True)

    query = request.GET.get('q')
    if query:
        practices = practices.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    subjects = Subject.objects.all()
    masters = Master.objects.filter(practices__is_published=True).select_related(
        'profile__user'
    ).distinct()

    # Resolve selected master name for the active filter tag
    selected_master_name = ''
    if master_id:
        try:
            selected_master_name = masters.get(pk=master_id).name
        except Master.DoesNotExist:
            pass

    context = {
        'practices': practices,
        'subjects': subjects,
        'masters': masters,
        'selected_subject': subject_id,
        'selected_level': level,
        'selected_master': master_id,
        'selected_master_name': selected_master_name,
        'query': query or '',
    }
    return render(request, 'practice/practice_list.html', context)


# ─────────────────────────────────────────────
# 2. PRACTICE DETAIL — Info page before starting
# ─────────────────────────────────────────────
@login_required
def practice_detail(request, pk):
    practice = get_object_or_404(Practice, pk=pk, is_published=True)

    question_count = practice.questions.count()
    total_points = sum(q.points for q in practice.questions.all())

    # How many attempts has this panda already made?
    panda, _ = Panda.objects.get_or_create(profile=request.user.profile)
    attempt_count = PracticeAttempt.objects.filter(panda=panda, practice=practice).count()
    can_attempt = practice.max_attempts == 0 or attempt_count < practice.max_attempts

    # Last completed attempt (for showing previous score)
    last_attempt = (
        PracticeAttempt.objects
        .filter(panda=panda, practice=practice, status='completed')
        .order_by('-completed_at')
        .first()
    )

    context = {
        'practice': practice,
        'question_count': question_count,
        'total_points': total_points,
        'attempt_count': attempt_count,
        'can_attempt': can_attempt,
        'last_attempt': last_attempt,
    }
    return render(request, 'practice/practice_detail.html', context)


# ─────────────────────────────────────────────
# 3. START PRACTICE — Creates a new attempt
# ─────────────────────────────────────────────
@login_required
def start_practice(request, pk):
    practice = get_object_or_404(Practice, pk=pk, is_published=True)
    panda, _ = Panda.objects.get_or_create(profile=request.user.profile)

    # Check attempt limit
    attempt_count = PracticeAttempt.objects.filter(panda=panda, practice=practice).count()
    if practice.max_attempts > 0 and attempt_count >= practice.max_attempts:
        messages.error(request, "You've reached the maximum number of attempts for this practice.")
        return redirect('practice_detail', pk=pk)

    # Abandon any in-progress attempt
    PracticeAttempt.objects.filter(panda=panda, practice=practice, status='in_progress').update(
        status='abandoned'
    )

    # Create a fresh attempt
    attempt = PracticeAttempt.objects.create(panda=panda, practice=practice)
    return redirect('take_practice', attempt_id=attempt.id)


# ─────────────────────────────────────────────
# 4. TAKE PRACTICE — The quiz interface
# ─────────────────────────────────────────────
@login_required
def take_practice(request, attempt_id):
    attempt = get_object_or_404(PracticeAttempt, id=attempt_id, panda=request.user.profile.panda)

    if attempt.status != 'in_progress':
        return redirect('practice_result', attempt_id=attempt.id)

    practice = attempt.practice
    questions = list(
        practice.questions.prefetch_related('choices')
        .filter(choices__isnull=False).distinct().order_by('order')
    )

    # Which question index are we on?
    question_index = int(request.GET.get('q', 0))
    question_index = max(0, min(question_index, len(questions) - 1))
    current_question = questions[question_index]

    # Already-saved answer for this question
    existing_answer = UserAnswer.objects.filter(
        attempt=attempt, question=current_question
    ).prefetch_related('selected_choices').first()

    existing_choice_ids = []
    if existing_answer:
        existing_choice_ids = list(existing_answer.selected_choices.values_list('id', flat=True))

    if request.method == 'POST':
        selected_ids = request.POST.getlist('choices')

        # Save or update the answer
        answer, _ = UserAnswer.objects.get_or_create(attempt=attempt, question=current_question)
        answer.selected_choices.set(PracticeChoice.objects.filter(id__in=selected_ids))
        answer.save()

        # Move to next question or finish
        if 'finish' in request.POST or question_index >= len(questions) - 1:
            return redirect('finish_practice', attempt_id=attempt.id)
        return redirect(f"{request.path}?q={question_index + 1}")

    choices = list(current_question.choices.all())

    answered_ids = set(UserAnswer.objects.filter(attempt=attempt).values_list('question_id', flat=True))

    # Timer: calculate remaining seconds; redirect immediately if already expired
    seconds_remaining = None
    if practice.time_limit:
        elapsed = (timezone.now() - attempt.start_time).total_seconds()
        seconds_remaining = max(0, int(practice.time_limit * 60 - elapsed))
        if seconds_remaining == 0:
            return redirect('finish_practice', attempt_id=attempt.id)

    is_owner = (
        hasattr(request.user.profile, 'master')
        and practice.master == request.user.profile.master
    )

    context = {
        'attempt': attempt,
        'practice': practice,
        'questions': questions,
        'current_question': current_question,
        'current_index': question_index,
        'total_questions': len(questions),
        'choices': choices,
        'existing_choice_ids': existing_choice_ids,
        'answered_ids': answered_ids,
        'answered_count': len(answered_ids),
        'is_last_question': question_index == len(questions) - 1,
        'seconds_remaining': seconds_remaining,
        'is_owner': is_owner,
    }
    return render(request, 'practice/take_practice.html', context)


# ─────────────────────────────────────────────
# 5. FINISH PRACTICE — Score calculation
# ─────────────────────────────────────────────
@login_required
def finish_practice(request, attempt_id):
    attempt = get_object_or_404(PracticeAttempt, id=attempt_id, panda=request.user.profile.panda)

    if attempt.status == 'in_progress':
        practice = attempt.practice
        answers = attempt.answers.prefetch_related('selected_choices', 'question__choices')

        total_points = sum(q.points for q in practice.questions.all())
        earned_points = 0

        for answer in answers:
            question = answer.question
            correct_ids = set(
                question.choices.filter(is_correct=True).values_list('id', flat=True)
            )
            selected_ids = set(answer.selected_choices.values_list('id', flat=True))
            if correct_ids == selected_ids:
                earned_points += question.points

        score = (earned_points / total_points * 100) if total_points > 0 else 0

        attempt.score = score
        attempt.status = 'completed'
        attempt.completed_at = timezone.now()
        attempt.save()
        _auto_link_homework(attempt)

    return redirect('practice_result', attempt_id=attempt.id)


# ─────────────────────────────────────────────
# 6. PRACTICE RESULT — Score + answer review
# ─────────────────────────────────────────────
@login_required
def practice_result(request, attempt_id):
    attempt = get_object_or_404(PracticeAttempt, id=attempt_id, panda=request.user.profile.panda)
    practice = attempt.practice
    panda = request.user.profile.panda

    passed = attempt.score >= practice.pass_score
    duration = None
    if attempt.completed_at:
        delta = attempt.completed_at - attempt.start_time
        duration = int(delta.total_seconds() // 60)

    attempt_count = PracticeAttempt.objects.filter(panda=panda, practice=practice).count()
    can_retry = practice.max_attempts == 0 or attempt_count < practice.max_attempts

    total_questions = practice.questions.count()
    total_points = sum(q.points for q in practice.questions.all())
    earned_points = round(attempt.score / 100 * total_points, 1) if total_points > 0 else 0

    # Build per-question results for review (all questions, answered or not)
    question_results = []
    if practice.show_answers_after:
        # Index answers by question_id so we can look them up quickly
        answers_by_qid = {}
        for ans in attempt.answers.prefetch_related('selected_choices'):
            answers_by_qid[ans.question_id] = ans

        qs = (practice.questions.prefetch_related('choices')
              .filter(choices__isnull=False).distinct().order_by('order'))
        for question in qs:
            correct_ids = set(question.choices.filter(is_correct=True).values_list('id', flat=True))

            if question.id in answers_by_qid:
                selected_ids = set(answers_by_qid[question.id].selected_choices.values_list('id', flat=True))
                is_correct = correct_ids == selected_ids
                was_answered = True
            else:
                selected_ids = set()
                is_correct = False
                was_answered = False

            question_results.append({
                'question': question,
                'choices': question.choices.all(),
                'selected_ids': selected_ids,
                'correct_ids': correct_ids,
                'is_correct': is_correct,
                'was_answered': was_answered,
            })

    is_owner = (
        hasattr(request.user.profile, 'master')
        and practice.master == request.user.profile.master
    )

    context = {
        'attempt': attempt,
        'practice': practice,
        'passed': passed,
        'duration': duration,
        'can_retry': can_retry,
        'total_questions': total_questions,
        'earned_points': earned_points,
        'total_points': total_points,
        'question_results': question_results,
        'is_owner': is_owner,
    }
    return render(request, 'practice/practice_result.html', context)


# ─────────────────────────────────────────────
# 7. MANAGE PRACTICES — Master's dashboard
# ─────────────────────────────────────────────
@login_required
def manage_practices(request):
    if not hasattr(request.user.profile, 'master'):
        messages.error(request, "You need a Master profile to manage practices.")
        return redirect('masters-create')
    master = request.user.profile.master
    practices = Practice.objects.filter(master=master).annotate(
        question_count=Count('questions', distinct=True),
        attempt_count=Count('attempts', distinct=True),
    ).order_by('-created_at')
    return render(request, 'practice/manage_practices.html', {'practices': practices})


# ─────────────────────────────────────────────
# 8. TOGGLE PUBLISH
# ─────────────────────────────────────────────
@login_required
def toggle_publish(request, pk):
    practice = get_object_or_404(Practice, pk=pk, master=request.user.profile.master)
    practice.is_published = not practice.is_published
    practice.save()
    status = "published" if practice.is_published else "unpublished"
    messages.success(request, f'"{practice.title}" has been {status}.')
    return redirect('manage_practices')


# ─────────────────────────────────────────────
# 9. TOGGLE AVAILABLE FOR ALL
# ─────────────────────────────────────────────
@login_required
def toggle_available(request, pk):
    practice = get_object_or_404(Practice, pk=pk, master=request.user.profile.master)
    practice.is_available_for_all = not practice.is_available_for_all
    practice.save()
    state = "shared with all masters" if practice.is_available_for_all else "set to private"
    messages.success(request, f'"{practice.title}" {state}.')
    return redirect('manage_practices')


# ─────────────────────────────────────────────
# 10. CREATE PRACTICE
# ─────────────────────────────────────────────
@login_required
def create_practice(request):
    if not hasattr(request.user.profile, 'master'):
        messages.error(request, "You need a Master profile to create practices.")
        return redirect('masters-create')
    master = request.user.profile.master

    if request.method == 'POST':
        form = PracticeForm(request.POST)
        if form.is_valid():
            practice = form.save(commit=False)
            practice.master = master
            practice.save()
            messages.success(request, f'"{practice.title}" created. Now add questions.')
            return redirect('manage_questions', pk=practice.pk)
    else:
        form = PracticeForm()
    return render(request, 'practice/practice_form.html', {'form': form, 'action': 'create'})


# ─────────────────────────────────────────────
# 10. EDIT PRACTICE
# ─────────────────────────────────────────────
@login_required
def edit_practice(request, pk):
    practice = get_object_or_404(Practice, pk=pk, master=request.user.profile.master)
    if request.method == 'POST':
        form = PracticeForm(request.POST, instance=practice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Practice settings updated.')
            return redirect('manage_questions', pk=practice.pk)
    else:
        form = PracticeForm(instance=practice)
    return render(request, 'practice/practice_form.html', {
        'form': form, 'action': 'edit', 'practice': practice,
    })


# ─────────────────────────────────────────────
# 11. MANAGE QUESTIONS — Question list for a practice
# ─────────────────────────────────────────────
@login_required
def manage_questions(request, pk):
    practice = get_object_or_404(Practice, pk=pk, master=request.user.profile.master)
    questions = practice.questions.prefetch_related('choices').all()
    return render(request, 'practice/manage_questions.html', {
        'practice': practice,
        'questions': questions,
    })


# ─────────────────────────────────────────────
# 12. ADD QUESTION
# ─────────────────────────────────────────────
@login_required
def add_question(request, pk):
    practice = get_object_or_404(Practice, pk=pk, master=request.user.profile.master)

    if request.method == 'POST':
        form = PracticeQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.practice = practice
            question.made_by = practice.master
            question.save()
            for i in range(1, 5):
                text = request.POST.get(f'choice_text_{i}', '').strip()
                is_correct = f'choice_correct_{i}' in request.POST
                if text:
                    PracticeChoice.objects.create(question=question, text=text, is_correct=is_correct)
            messages.success(request, 'Question added.')
            return redirect('manage_questions', pk=practice.pk)
    else:
        form = PracticeQuestionForm(initial={'order': practice.questions.count() + 1})

    choice_slots = [{'num': i, 'text': '', 'is_correct': False} for i in range(1, 5)]
    return render(request, 'practice/question_form.html', {
        'practice': practice,
        'form': form,
        'action': 'add',
        'choice_slots': choice_slots,
    })


# ─────────────────────────────────────────────
# 13. EDIT QUESTION
# ─────────────────────────────────────────────
@login_required
def edit_question(request, pk, qpk):
    practice = get_object_or_404(Practice, pk=pk, master=request.user.profile.master)
    question = get_object_or_404(PracticeQuestion, pk=qpk, practice=practice)
    existing = list(question.choices.all())

    if request.method == 'POST':
        form = PracticeQuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            form.save()
            question.choices.all().delete()
            for i in range(1, 5):
                text = request.POST.get(f'choice_text_{i}', '').strip()
                is_correct = f'choice_correct_{i}' in request.POST
                if text:
                    PracticeChoice.objects.create(question=question, text=text, is_correct=is_correct)
            messages.success(request, 'Question updated.')
            return redirect('manage_questions', pk=practice.pk)
    else:
        form = PracticeQuestionForm(instance=question)

    # Build 4 pre-filled slots for the template
    choice_slots = []
    for i in range(1, 5):
        c = existing[i - 1] if i - 1 < len(existing) else None
        choice_slots.append({
            'num': i,
            'text': c.text if c else '',
            'is_correct': c.is_correct if c else False,
        })

    return render(request, 'practice/question_form.html', {
        'practice': practice,
        'form': form,
        'action': 'edit',
        'question': question,
        'choice_slots': choice_slots,
    })


# ─────────────────────────────────────────────
# 14. DELETE QUESTION
# ─────────────────────────────────────────────
@login_required
def delete_question(request, pk, qpk):
    practice = get_object_or_404(Practice, pk=pk, master=request.user.profile.master)
    question = get_object_or_404(PracticeQuestion, pk=qpk, practice=practice)
    if request.method == 'POST':
        question.delete()
        messages.success(request, 'Question deleted.')
    return redirect('manage_questions', pk=practice.pk)


# ─────────────────────────────────────────────
# 15. PRACTICE ATTEMPTS — Master views all student results
# ─────────────────────────────────────────────
@login_required
def practice_attempts(request, pk):
    practice = get_object_or_404(Practice, pk=pk, master=request.user.profile.master)
    attempts = (
        PracticeAttempt.objects
        .filter(practice=practice, status='completed')
        .select_related('panda__profile__user')
        .order_by('-completed_at')
    )
    total_points = sum(q.points for q in practice.questions.all())
    attempt_data = []
    for attempt in attempts:
        earned = round(attempt.score / 100 * total_points, 1) if total_points > 0 else 0
        duration = None
        if attempt.completed_at:
            delta = attempt.completed_at - attempt.start_time
            duration = int(delta.total_seconds() // 60)
        attempt_data.append({
            'attempt': attempt,
            'earned': earned,
            'duration': duration,
            'passed': attempt.score >= practice.pass_score,
        })
    context = {
        'practice': practice,
        'attempt_data': attempt_data,
        'total_points': total_points,
    }
    return render(request, 'practice/practice_attempts.html', context)


# ─────────────────────────────────────────────
# 16. REVIEW ATTEMPT — Master sees student's answers question by question
# ─────────────────────────────────────────────
@login_required
def review_attempt(request, attempt_id):
    attempt = get_object_or_404(PracticeAttempt, id=attempt_id)
    practice = attempt.practice
    # Only the master who owns the practice can review
    if not hasattr(request.user.profile, 'master') or practice.master != request.user.profile.master:
        messages.error(request, "You don't have permission to review this attempt.")
        return redirect('manage_practices')

    total_points = sum(q.points for q in practice.questions.all())
    earned_points = round(attempt.score / 100 * total_points, 1) if total_points > 0 else 0
    duration = None
    if attempt.completed_at:
        delta = attempt.completed_at - attempt.start_time
        duration = int(delta.total_seconds() // 60)

    answers_by_qid = {}
    for ans in attempt.answers.prefetch_related('selected_choices'):
        answers_by_qid[ans.question_id] = ans

    question_results = []
    qs = (practice.questions.prefetch_related('choices')
          .filter(choices__isnull=False).distinct().order_by('order'))
    for question in qs:
        correct_ids = set(question.choices.filter(is_correct=True).values_list('id', flat=True))
        if question.id in answers_by_qid:
            selected_ids = set(answers_by_qid[question.id].selected_choices.values_list('id', flat=True))
            is_correct = correct_ids == selected_ids
            was_answered = True
        else:
            selected_ids = set()
            is_correct = False
            was_answered = False

        question_results.append({
            'question': question,
            'choices': question.choices.all(),
            'selected_ids': selected_ids,
            'correct_ids': correct_ids,
            'is_correct': is_correct,
            'was_answered': was_answered,
        })

    context = {
        'attempt': attempt,
        'practice': practice,
        'passed': attempt.score >= practice.pass_score,
        'duration': duration,
        'total_points': total_points,
        'earned_points': earned_points,
        'question_results': question_results,
        'is_owner': True,
    }
    return render(request, 'practice/review_attempt.html', context)