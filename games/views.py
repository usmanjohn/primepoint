import random
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def games_home(request):
    return render(request, 'games/games_home.html')


@login_required
def number_guess(request):
    session = request.session

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'new':
            try:
                max_num = int(request.POST.get('max_num', 1000))
                max_num = max(10, min(max_num, 10000))
            except (ValueError, TypeError):
                max_num = 1000
            session['guess_target'] = random.randint(1, max_num)
            session['guess_attempts'] = 0
            session['guess_max'] = max_num
            session['guess_result'] = None
            session['guess_won'] = False
            session['guess_last'] = None
            return redirect('number_guess')

        if action == 'guess':
            target = session.get('guess_target')
            if target is None:
                return redirect('number_guess')

            try:
                guess = int(request.POST.get('guess', ''))
            except (ValueError, TypeError):
                session['guess_result'] = 'invalid'
                return redirect('number_guess')

            max_num = session.get('guess_max', 1000)
            if guess < 1 or guess > max_num:
                session['guess_result'] = 'out_of_range'
                return redirect('number_guess')

            session['guess_attempts'] = session.get('guess_attempts', 0) + 1
            session['guess_last'] = guess

            if guess < target:
                session['guess_result'] = 'low'
            elif guess > target:
                session['guess_result'] = 'high'
            else:
                session['guess_result'] = 'correct'
                session['guess_won'] = True

            return redirect('number_guess')

    target = session.get('guess_target')
    context = {
        'started': target is not None,
        'attempts': session.get('guess_attempts', 0),
        'max_num': session.get('guess_max', 1000),
        'result': session.get('guess_result'),
        'won': session.get('guess_won', False),
        'last_guess': session.get('guess_last'),
        'target': session.get('guess_target') if session.get('guess_won') else None,
    }
    return render(request, 'games/number_guess.html', context)
