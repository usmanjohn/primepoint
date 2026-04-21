from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q, Count, Avg
from panda.models import Panda
from masters.models import Master   

from .models import Practice, PracticeQuestion, PracticeChoice, PracticeAttempt, UserAnswer, Subject


# ─────────────────────────────────────────────
# 1. PRACTICE LIST — Browse & filter practices
# ─────────────────────────────────────────────
def practice_list(request):
    practices = Practice.objects.filter(is_published=True).select_related('subject', 'master')

    # Filter by subject
    subject_id = request.GET.get('subject')
    if subject_id:
        practices = practices.filter(subject_id=subject_id)

    # Filter by level
    level = request.GET.get('level')
    if level:
        practices = practices.filter(level=level)

    # Filter free/paid
    is_free = request.GET.get('is_free')
    if is_free == '1':
        practices = practices.filter(is_free=True)

    # Search by title
    query = request.GET.get('q')
    if query:
        practices = practices.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        )

    subjects = Subject.objects.all()

    context = {
        'practices': practices,
        'subjects': subjects,
        'selected_subject': subject_id,
        'selected_level': level,
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
    panda, created = Panda.objects.get_or_create(profile=request.user.profile)
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
    panda, created = Panda.objects.get_or_create(profile=request.user.profile)

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
    attempt = get_object_or_404(PracticeAttempt, id=attempt_id, panda=request.user.panda)

    if attempt.status != 'in_progress':
        return redirect('practice_result', attempt_id=attempt.id)

    practice = attempt.practice
    questions = list(practice.questions.prefetch_related('choices').order_by('order'))

    if practice.shuffle_questions:
        import random
        random.shuffle(questions)

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
    if practice.shuffle_choices:
        import random
        random.shuffle(choices)

    # Progress: how many questions have been answered
    answered_count = UserAnswer.objects.filter(attempt=attempt).count()

    context = {
        'attempt': attempt,
        'practice': practice,
        'questions': questions,
        'current_question': current_question,
        'current_index': question_index,
        'total_questions': len(questions),
        'choices': choices,
        'existing_choice_ids': existing_choice_ids,
        'answered_count': answered_count,
        'is_last_question': question_index == len(questions) - 1,
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

    return redirect('practice_result', attempt_id=attempt.id)


# ─────────────────────────────────────────────
# 6. PRACTICE RESULT — Score + answer review
# ─────────────────────────────────────────────
@login_required
def practice_result(request, attempt_id):
    attempt = get_object_or_404(PracticeAttempt, id=attempt_id, panda=request.user.profile.panda)
    practice = attempt.practice

    passed = attempt.score >= practice.pass_score
    duration = None
    if attempt.completed_at:
        delta = attempt.completed_at - attempt.start_time
        duration = int(delta.total_seconds() // 60)  # minutes

    # Build per-question results for review
    question_results = []
    if practice.show_answers_after:
        answers = attempt.answers.prefetch_related(
            'question__choices', 'selected_choices'
        ).select_related('question')

        for answer in answers.order_by('question__order'):
            question = answer.question
            correct_ids = set(question.choices.filter(is_correct=True).values_list('id', flat=True))
            selected_ids = set(answer.selected_choices.values_list('id', flat=True))
            is_correct = correct_ids == selected_ids

            question_results.append({
                'question': question,
                'choices': question.choices.all(),
                'selected_ids': selected_ids,
                'correct_ids': correct_ids,
                'is_correct': is_correct,
            })

    context = {
        'attempt': attempt,
        'practice': practice,
        'passed': passed,
        'duration': duration,
        'question_results': question_results,
    }
    return render(request, 'practice/practice_result.html', context)


# ─────────────────────────────────────────────
# 7. MANAGE practice — Master's dashboard
# ─────────────────────────────────────────────
@login_required
def manage_practices(request):
    master = request.user.profile.master  # Adjust to your Master lookup
    practices = Practice.objects.filter(master=master).annotate(
        question_count=Count('questions'),
        attempt_count=Count('practiceattempt'),
    ).order_by('-created_at')

    context = {
        'practices': practices,
    }
    return render(request, 'practice/manage_practices.html', context)


# ─────────────────────────────────────────────
# 8. TOGGLE PUBLISH — Quick publish/unpublish
# ─────────────────────────────────────────────
@login_required
def toggle_publish(request, pk):
    practice = get_object_or_404(Practice, pk=pk, master=request.user.profile.master)
    practice.is_published = not practice.is_published
    practice.save()
    status = "published" if practice.is_published else "unpublished"
    messages.success(request, f'"{practice.title}" has been {status}.')
    return redirect('manage_practices')