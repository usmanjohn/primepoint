import json
import random
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CrosswordPuzzle


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
        'started':    target is not None,
        'attempts':   session.get('guess_attempts', 0),
        'max_num':    session.get('guess_max', 1000),
        'result':     session.get('guess_result'),
        'won':        session.get('guess_won', False),
        'last_guess': session.get('guess_last'),
        'target':     session.get('guess_target') if session.get('guess_won') else None,
    }
    return render(request, 'games/number_guess.html', context)


@login_required
def crossword_list(request):
    puzzles = CrosswordPuzzle.objects.filter(is_published=True)
    return render(request, 'games/crossword_list.html', {'puzzles': puzzles})


@login_required
def crossword_play(request, pk):
    puzzle    = get_object_or_404(CrosswordPuzzle, pk=pk, is_published=True)
    grid_data = puzzle.grid_data or {}
    words     = grid_data.get('words', [])
    cells     = grid_data.get('cells', [])
    rows      = grid_data.get('rows', 0)
    cols      = grid_data.get('cols', 0)

    session_key = f'crossword_{pk}_answers'
    check_key   = f'crossword_{pk}_checked'

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'reset':
            request.session.pop(session_key, None)
            request.session.pop(check_key, None)
            return redirect('crossword_play', pk=pk)

        if action == 'check':
            answers = {}
            for word in words:
                direction = word['direction']
                for i in range(word['length']):
                    r = word['row'] + (i if direction == 'down' else 0)
                    c = word['col'] + (i if direction == 'across' else 0)
                    key = f'{r}_{c}'
                    val = request.POST.get(f'cell_{r}_{c}', '').strip()
                    if val:
                        answers[key] = val
            request.session[session_key] = answers
            request.session[check_key]   = True
            return redirect('crossword_play', pk=pk)

    saved_answers = request.session.get(session_key, {})
    checked       = request.session.get(check_key, False)

    # Build number map: (r, c) -> number for word-start cells
    number_map = {}
    for word in words:
        key = (word['row'], word['col'])
        if key not in number_map:
            number_map[key] = word['number']

    # Build grid_rows: list of rows, each a list of cell dicts
    grid_rows = []
    total_correct = 0
    total_cells   = 0
    for r in range(rows):
        row_cells = []
        for c in range(cols):
            cell_val = cells[r][c] if cells else None
            if cell_val is None:
                row_cells.append({'is_black': True})
            else:
                total_cells += 1
                answer  = saved_answers.get(f'{r}_{c}', '')
                correct = (answer == cell_val) if checked else None
                if correct:
                    total_correct += 1
                row_cells.append({
                    'is_black': False,
                    'r':        r,
                    'c':        c,
                    'answer':   answer,
                    'correct':  correct,
                    'number':   number_map.get((r, c)),
                })
        grid_rows.append(row_cells)

    all_correct = checked and total_cells > 0 and total_correct == total_cells

    across_clues = sorted([w for w in words if w['direction'] == 'across'], key=lambda x: x['number'])
    down_clues   = sorted([w for w in words if w['direction'] == 'down'],   key=lambda x: x['number'])

    context = {
        'puzzle':       puzzle,
        'grid_rows':    grid_rows,
        'across_clues': across_clues,
        'down_clues':   down_clues,
        'checked':      checked,
        'all_correct':  all_correct,
        'words_json':   json.dumps(words),
    }
    return render(request, 'games/crossword_play.html', context)
