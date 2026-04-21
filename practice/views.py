from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Practice, PracticeAttempt, UserAnswer
def home(request):
    practices = Practice.objects.all().order_by('-created_at')
    return render(request, 'practice/practice_home.html', {'practices': practices})

# Results view: Detailed breakdown of a specific attempt
def attempt_result(request, attempt_id):
    attempt = get_object_or_404(PracticeAttempt, id=attempt_id)
    return render(request, 'practice/practice_results.html', {'attempt': attempt})

def practice_detail(request, pk):
    practice = get_object_or_404(Practice, pk=pk)
    questions = practice.questions.all()

    if request.method == 'POST':
        # 1. Create the Attempt record
        # Assumes request.user has a .panda profile
        attempt = PracticeAttempt.objects.create(
            panda=request.user.profile.panda, 
            practice=practice
        )
        
        correct_count = 0
        for q in questions:
            # Get selected choice from the form (named like "question_5")
            selected = request.POST.get(f'question_{q.id}')
            if selected:
                selected_int = int(selected)
                UserAnswer.objects.create(
                    attempt=attempt,
                    question=q,
                    selected_choice=selected_int
                )
                if selected_int == q.correct_answer:
                    correct_count += 1
        
        # 2. Calculate and save score
        attempt.score = (correct_count / questions.count()) * 100 if questions.count() > 0 else 0
        attempt.save()
        
        return render(request, 'practice/practrice_results.html', {'attempt': attempt})

    return render(request, 'practice/practice_detail.html', {
        'practice': practice,
        'questions': questions
    })
