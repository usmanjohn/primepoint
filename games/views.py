import json
import math
import random
import time
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CrosswordPuzzle, CodeBreakerPuzzle, CodeBreakerClue, PrimeClimbChallenge, SortingRaceChallenge, WordOrderChallenge


# ---------------------------------------------------------------------------
# Code Breaker — math-expression generator
# ---------------------------------------------------------------------------

def _cb_candidates(target, difficulty):
    """Return a list of math expression strings whose value equals `target`."""
    t = target
    exprs = []

    if difficulty == CodeBreakerPuzzle.DIFFICULTY_EASY:
        for a in range(0, t + 1):
            exprs.append(f"{a} + {t - a}")
        for b in range(1, 19):
            exprs.append(f"{t + b} - {b}")
        for b in range(1, 10):
            c = random.randint(1, max(1, t - b))
            exprs.append(f"{t + b + c} - {b} - {c}")

    elif difficulty == CodeBreakerPuzzle.DIFFICULTY_MEDIUM:
        for i in range(2, t + 1):
            if t % i == 0 and t // i >= 2:
                exprs.append(f"{i} × {t // i}")
        for a in range(2, 11):
            b = a * a - t
            if 0 <= b <= 60:
                exprs.append(f"{a}² - {b}")
            b = t - a * a
            if 0 <= b <= 60:
                exprs.append(f"{a}² + {b}")
        for a in range(2, 9):
            for b in range(2, 9):
                c = t - a * b
                if 0 <= c <= 25:
                    exprs.append(f"{a} × {b} + {c}")
                c = a * b - t
                if 1 <= c <= 25:
                    exprs.append(f"{a} × {b} - {c}")

    elif difficulty == CodeBreakerPuzzle.DIFFICULTY_HARD:
        for b in range(1, 25):
            exprs.append(f"2x + {b} = {2*t + b},  find x")
        for b in range(1, 20):
            if 3 * t - b > 0:
                exprs.append(f"3x - {b} = {3*t - b},  find x")
        for b in range(2, 7):
            for c in range(2, 7):
                exprs.append(f"{t + b*c} - {b} × {c}")
        for c in range(2, t + 1):
            if t % c == 0:
                prod = t // c
                if 2 <= prod <= 20:
                    for a in range(1, prod):
                        exprs.append(f"({a} + {prod - a}) × {c}")

    return exprs


def _generate_cb_expression(target, difficulty, used_exprs):
    """Return a unique math expression string for `target` (1–26)."""
    candidates = _cb_candidates(target, difficulty)
    random.shuffle(candidates)
    for expr in candidates:
        if expr not in used_exprs:
            return expr
    a = random.randint(0, target)
    return f"{a} + {target - a}"


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

    number_map = {}
    for word in words:
        key = (word['row'], word['col'])
        if key not in number_map:
            number_map[key] = word['number']

    grid_rows_data = []
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
        grid_rows_data.append(row_cells)

    all_correct = checked and total_cells > 0 and total_correct == total_cells

    across_clues = sorted([w for w in words if w['direction'] == 'across'], key=lambda x: x['number'])
    down_clues   = sorted([w for w in words if w['direction'] == 'down'],   key=lambda x: x['number'])

    context = {
        'puzzle':       puzzle,
        'grid_rows':    grid_rows_data,
        'across_clues': across_clues,
        'down_clues':   down_clues,
        'checked':      checked,
        'all_correct':  all_correct,
        'words_json':   json.dumps(words),
    }
    return render(request, 'games/crossword_play.html', context)


@login_required
def crossword_edit(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    puzzle = get_object_or_404(CrosswordPuzzle, pk=pk)

    if request.method == 'POST':
        try:
            data  = json.loads(request.body)
            rows  = max(1, min(int(data.get('rows', puzzle.grid_rows)), 20))
            cols  = max(1, min(int(data.get('cols', puzzle.grid_cols)), 10))
            words = data.get('words', [])
            cells = data.get('cells', [])
            puzzle.grid_data = {'rows': rows, 'cols': cols, 'words': words, 'cells': cells}
            puzzle.save()
            return JsonResponse({'ok': True, 'word_count': len(words)})
        except Exception as e:
            return JsonResponse({'ok': False, 'error': str(e)}, status=400)

    return render(request, 'games/crossword_edit.html', {'puzzle': puzzle})


# ---------------------------------------------------------------------------
# Code Breaker views
# ---------------------------------------------------------------------------

@login_required
def codebreaker_list(request):
    puzzles = CodeBreakerPuzzle.objects.filter(is_active=True)
    return render(request, 'games/codebreaker_list.html', {'puzzles': puzzles})


@login_required
def codebreaker_play(request, pk):
    puzzle = get_object_or_404(CodeBreakerPuzzle, pk=pk, is_active=True)
    clues  = list(puzzle.clues.order_by('letter_index'))

    start_key  = f'cb_{pk}_start'
    solved_key = f'cb_{pk}_solved'

    if request.method == 'POST' and request.POST.get('action') == 'reset':
        request.session.pop(start_key, None)
        request.session.pop(solved_key, None)
        request.session.pop(f'cb_{pk}_attempts', None)
        return redirect('codebreaker_play', pk=pk)

    if start_key not in request.session:
        request.session[start_key] = int(time.time())

    solved_indices = request.session.get(solved_key, [])

    clue_data = []
    for clue in clues:
        clue_data.append({
            'letter_index':    clue.letter_index,
            'math_expression': clue.math_expression,
            'solved':          clue.letter_index in solved_indices,
            'letter':          clue.letter if clue.letter_index in solved_indices else '_',
        })

    all_solved = len(clue_data) > 0 and len(solved_indices) >= len(clue_data)
    elapsed    = None
    if all_solved:
        elapsed = int(time.time()) - request.session.get(start_key, int(time.time()))

    alphabet = [(i, chr(64 + i)) for i in range(1, 27)]

    context = {
        'puzzle':       puzzle,
        'clues':        clue_data,
        'solved_count': len(solved_indices),
        'total_clues':  len(clue_data),
        'all_solved':   all_solved,
        'elapsed':      elapsed,
        'alphabet':     alphabet,
    }
    return render(request, 'games/codebreaker_play.html', context)


@login_required
def codebreaker_check(request, pk):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    puzzle = get_object_or_404(CodeBreakerPuzzle, pk=pk, is_active=True)

    try:
        data         = json.loads(request.body)
        letter_index = int(data['letter_index'])
        user_answer  = int(data['answer'])
    except (KeyError, ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({'correct': False})

    try:
        clue = puzzle.clues.get(letter_index=letter_index)
    except CodeBreakerClue.DoesNotExist:
        return JsonResponse({'correct': False})

    solved_key   = f'cb_{pk}_solved'
    attempts_key = f'cb_{pk}_attempts'
    start_key    = f'cb_{pk}_start'

    attempts = request.session.get(attempts_key, {})
    str_idx  = str(letter_index)
    attempts[str_idx] = attempts.get(str_idx, 0) + 1
    request.session[attempts_key] = attempts

    if user_answer == clue.answer:
        solved = request.session.get(solved_key, [])
        if letter_index not in solved:
            solved.append(letter_index)
        request.session[solved_key] = solved

        total      = puzzle.clues.count()
        all_solved = len(solved) >= total
        elapsed    = None
        if all_solved:
            elapsed = int(time.time()) - request.session.get(start_key, int(time.time()))

        return JsonResponse({
            'correct':    True,
            'letter':     clue.letter,
            'all_solved': all_solved,
            'elapsed':    elapsed,
        })

    return JsonResponse({'correct': False})


@login_required
def codebreaker_create(request):
    is_master = hasattr(request.user, 'profile') and request.user.profile.is_master
    if not request.user.is_staff and not is_master:
        raise PermissionDenied

    errors = []

    if request.method == 'POST':
        title       = request.POST.get('title', '').strip()
        secret_word = request.POST.get('secret_word', '').strip().upper()
        hint        = request.POST.get('hint', '').strip()
        difficulty  = request.POST.get('difficulty', CodeBreakerPuzzle.DIFFICULTY_EASY)

        if not title:
            errors.append('Title is required.')
        if not secret_word:
            errors.append('Secret word is required.')
        elif not all(c.isalpha() or c.isspace() for c in secret_word):
            errors.append('Secret word must contain only letters (spaces allowed).')
        elif not any(c.isalpha() for c in secret_word):
            errors.append('Secret word must contain at least one letter.')
        if difficulty not in (CodeBreakerPuzzle.DIFFICULTY_EASY,
                               CodeBreakerPuzzle.DIFFICULTY_MEDIUM,
                               CodeBreakerPuzzle.DIFFICULTY_HARD):
            errors.append('Invalid difficulty.')

        if not errors:
            puzzle = CodeBreakerPuzzle.objects.create(
                title=title,
                secret_word=secret_word,
                hint=hint,
                difficulty=difficulty,
                created_by=request.user,
            )
            used_exprs = set()
            for i, ch in enumerate(secret_word):
                if not ch.isalpha():
                    continue
                letter_num = ord(ch) - ord('A') + 1
                expr       = _generate_cb_expression(letter_num, difficulty, used_exprs)
                used_exprs.add(expr)
                CodeBreakerClue.objects.create(
                    puzzle=puzzle,
                    letter_index=i,
                    letter=ch,
                    math_expression=expr,
                    answer=letter_num,
                )
            return redirect('codebreaker_play', pk=puzzle.pk)

    context = {
        'errors':      errors,
        'difficulties': CodeBreakerPuzzle.DIFFICULTY_CHOICES,
        'post':        request.POST if request.method == 'POST' else {},
    }
    return render(request, 'games/codebreaker_create.html', context)


# ---------------------------------------------------------------------------
# Prime Climb Grid views
# ---------------------------------------------------------------------------

def _pc_correct_numbers(mode, target=None):
    """Return the list of correct numbers (1–100) for a given challenge mode."""
    if mode == PrimeClimbChallenge.PRIMES:
        sieve = [True] * 101
        sieve[0] = sieve[1] = False
        for i in range(2, 11):
            if sieve[i]:
                for j in range(i * i, 101, i):
                    sieve[j] = False
        return [i for i in range(2, 101) if sieve[i]]
    elif mode == PrimeClimbChallenge.SQUARES:
        return [i * i for i in range(1, 11)]
    elif mode == PrimeClimbChallenge.MULTIPLES and target:
        return list(range(target, 101, target))
    return []


@login_required
def primeclimb_list(request):
    challenges = PrimeClimbChallenge.objects.filter(is_active=True)
    return render(request, 'games/primeclimb_list.html', {'challenges': challenges})


@login_required
def primeclimb_play(request, pk):
    challenge = get_object_or_404(PrimeClimbChallenge, pk=pk, is_active=True)

    checked_key  = f'pc_{pk}_checked'
    selected_key = f'pc_{pk}_selected'
    score_key    = f'pc_{pk}_score'

    if request.method == 'POST' and request.POST.get('action') == 'reset':
        for k in (checked_key, selected_key, score_key):
            request.session.pop(k, None)
        return redirect('primeclimb_play', pk=pk)

    prev_checked  = request.session.get(checked_key, False)
    prev_selected = request.session.get(selected_key, [])
    prev_score    = request.session.get(score_key, None)

    correct_nums = _pc_correct_numbers(challenge.mode, challenge.target)

    grid_rows = [list(range(r, r + 10)) for r in range(1, 101, 10)]

    context = {
        'challenge':      challenge,
        'grid_rows':      grid_rows,
        'prev_selected':  json.dumps(prev_selected),
        'prev_checked':   prev_checked,
        'prev_score':     json.dumps(prev_score) if prev_score else 'null',
        'correct_nums_json': json.dumps(correct_nums) if prev_checked else 'null',
        'total_answer':   len(correct_nums),
    }
    return render(request, 'games/primeclimb_play.html', context)


@login_required
def primeclimb_check(request, pk):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    challenge = get_object_or_404(PrimeClimbChallenge, pk=pk, is_active=True)

    try:
        data     = json.loads(request.body)
        selected = [int(n) for n in data.get('selected', [])]
    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({'error': 'Invalid data'}, status=400)

    answer_set   = set(_pc_correct_numbers(challenge.mode, challenge.target))
    selected_set = set(selected)

    correct = sorted(answer_set & selected_set)
    wrong   = sorted(selected_set - answer_set)
    missed  = sorted(answer_set - selected_set)

    score = {
        'correct': correct,
        'wrong':   wrong,
        'missed':  missed,
        'score':   len(correct),
        'total':   len(answer_set),
    }

    request.session[f'pc_{pk}_checked']  = True
    request.session[f'pc_{pk}_selected'] = selected
    request.session[f'pc_{pk}_score']    = score

    return JsonResponse(score)


@login_required
def primeclimb_create(request):
    is_master = hasattr(request.user, 'profile') and request.user.profile.is_master
    if not request.user.is_staff and not is_master:
        raise PermissionDenied

    errors = []

    if request.method == 'POST':
        title  = request.POST.get('title', '').strip()
        mode   = request.POST.get('mode', '')
        hint   = request.POST.get('hint', '').strip()
        target = None

        if not title:
            errors.append('Title is required.')
        if mode not in (PrimeClimbChallenge.PRIMES,
                         PrimeClimbChallenge.SQUARES,
                         PrimeClimbChallenge.MULTIPLES):
            errors.append('Select a valid challenge type.')
        if mode == PrimeClimbChallenge.MULTIPLES:
            try:
                target = int(request.POST.get('target', ''))
                if not (2 <= target <= 50):
                    errors.append('Multiples target must be between 2 and 50.')
            except (ValueError, TypeError):
                errors.append('Enter a valid number for the multiples target.')

        if not errors:
            challenge = PrimeClimbChallenge.objects.create(
                title=title,
                mode=mode,
                target=target,
                hint=hint,
                created_by=request.user,
            )
            return redirect('primeclimb_play', pk=challenge.pk)

    context = {
        'errors':  errors,
        'modes':   PrimeClimbChallenge.MODE_CHOICES,
        'post':    request.POST if request.method == 'POST' else {},
    }
    return render(request, 'games/primeclimb_create.html', context)


# ---------------------------------------------------------------------------
# Sorting Race — number pools
# ---------------------------------------------------------------------------

_SR_MEDIUM_POOL = [
    {"display": "-8",   "value": -8.0},
    {"display": "-5",   "value": -5.0},
    {"display": "-3",   "value": -3.0},
    {"display": "-1",   "value": -1.0},
    {"display": "0",    "value":  0.0},
    {"display": "2",    "value":  2.0},
    {"display": "4",    "value":  4.0},
    {"display": "7",    "value":  7.0},
    {"display": "-1/2", "value": -0.5},
    {"display": "1/3",  "value":  1/3},
    {"display": "2/3",  "value":  2/3},
    {"display": "3/4",  "value":  0.75},
    {"display": "-3/4", "value": -0.75},
    {"display": "5/4",  "value":  1.25},
    {"display": "5/3",  "value":  5/3},
    {"display": "-5/3", "value": -5/3},
    {"display": "0.28", "value":  0.28},
    {"display": "1.5",  "value":  1.5},
    {"display": "-2.5", "value": -2.5},
]

_SR_HARD_POOL = [
    {"display": "-π/4",  "value": -math.pi / 4},
    {"display": "-3/4",       "value": -0.75},
    {"display": "-√2/2", "value": -math.sqrt(2) / 2},
    {"display": "-3/8",       "value": -3 / 8},
    {"display": "5/7",        "value":  5 / 7},
    {"display": "3/4",        "value":  0.75},
    {"display": "π/2",   "value":  math.pi / 2},
    {"display": "5/3",        "value":  5 / 3},
    {"display": "√3",    "value":  math.sqrt(3)},
    {"display": "-7/4",       "value": -7 / 4},
    {"display": "-√3",   "value": -math.sqrt(3)},
    {"display": "√5",    "value":  math.sqrt(5)},
    {"display": "7/3",        "value":  7 / 3},
    {"display": "√2",    "value":  math.sqrt(2)},
    {"display": "-5/3",       "value": -5 / 3},
    {"display": "π/4",   "value":  math.pi / 4},
    {"display": "-√5",   "value": -math.sqrt(5)},
    {"display": "11/8",       "value":  11 / 8},
    {"display": "√2/2",  "value":  math.sqrt(2) / 2},
]


def _sr_generate_array(difficulty):
    if difficulty == SortingRaceChallenge.EASY:
        nums  = random.sample(range(-20, 31), 7)
        items = [{"display": str(n), "value": float(n)} for n in nums]
    elif difficulty == SortingRaceChallenge.MEDIUM:
        items = random.sample(_SR_MEDIUM_POOL, 8)
    else:
        items = random.sample(_SR_HARD_POOL, 9)

    # Shuffle; ensure the result is not already sorted
    items = list(items)
    random.shuffle(items)
    sorted_vals = sorted(items, key=lambda x: x['value'])
    attempts = 0
    while items == sorted_vals and attempts < 20:
        random.shuffle(items)
        attempts += 1

    return items


# ---------------------------------------------------------------------------
# Sorting Race views
# ---------------------------------------------------------------------------

@login_required
def sortingrace_list(request):
    challenges = SortingRaceChallenge.objects.filter(is_active=True)
    return render(request, 'games/sortingrace_list.html', {'challenges': challenges})


@login_required
def sortingrace_play(request, pk):
    challenge = get_object_or_404(SortingRaceChallenge, pk=pk, is_active=True)

    items_key = f'sr_{pk}_items'
    order_key = f'sr_{pk}_order'
    moves_key = f'sr_{pk}_moves'
    start_key = f'sr_{pk}_start'
    done_key  = f'sr_{pk}_done'

    if request.method == 'POST' and request.POST.get('action') == 'reset':
        for k in (items_key, order_key, moves_key, start_key, done_key):
            request.session.pop(k, None)
        return redirect('sortingrace_play', pk=pk)

    if items_key not in request.session:
        items = _sr_generate_array(challenge.difficulty)
        n = len(items)
        sorted_order = sorted(range(n), key=lambda i: items[i]['value'])
        order = list(range(n))
        random.shuffle(order)
        while order == sorted_order:
            random.shuffle(order)
        request.session[items_key] = items
        request.session[order_key] = order
        request.session[moves_key] = 0
        request.session[start_key] = int(time.time())
        request.session[done_key]  = False

    items      = request.session[items_key]
    order      = request.session[order_key]
    moves      = request.session[moves_key]
    start_time = request.session[start_key]
    done       = request.session[done_key]
    elapsed    = int(time.time()) - start_time if done else None

    initial_items = [{'display': items[i]['display'], 'pos': pos} for pos, i in enumerate(order)]

    context = {
        'challenge':     challenge,
        'initial_items': initial_items,
        'items_json':    json.dumps(items),
        'order_json':    json.dumps(order),
        'moves':         moves,
        'start_ms':      start_time * 1000,
        'done':          done,
        'elapsed':       elapsed,
    }
    return render(request, 'games/sortingrace_play.html', context)


@login_required
def sortingrace_check(request, pk):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    challenge = get_object_or_404(SortingRaceChallenge, pk=pk, is_active=True)

    try:
        data  = json.loads(request.body)
        order = [int(i) for i in data.get('order', [])]
        moves = int(data.get('moves', 0))
    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({'error': 'Invalid data'}, status=400)

    items_key = f'sr_{pk}_items'
    order_key = f'sr_{pk}_order'
    moves_key = f'sr_{pk}_moves'
    start_key = f'sr_{pk}_start'
    done_key  = f'sr_{pk}_done'

    items = request.session.get(items_key)
    if not items or len(order) != len(items):
        return JsonResponse({'error': 'No active game'}, status=400)

    request.session[order_key] = order
    request.session[moves_key] = moves

    values    = [items[i]['value'] for i in order]
    is_sorted = all(values[j] <= values[j + 1] for j in range(len(values) - 1))

    if is_sorted:
        elapsed = int(time.time()) - request.session.get(start_key, int(time.time()))
        request.session[done_key] = True
        return JsonResponse({'correct': True, 'moves': moves, 'elapsed': elapsed})

    # Check if one swap away
    n      = len(order)
    nearly = False
    for a in range(n):
        for b in range(a + 1, n):
            test = order[:]
            test[a], test[b] = test[b], test[a]
            tv = [items[i]['value'] for i in test]
            if all(tv[j] <= tv[j + 1] for j in range(len(tv) - 1)):
                nearly = True
                break
        if nearly:
            break

    return JsonResponse({'correct': False, 'nearly': nearly})


@login_required
def sortingrace_create(request):
    is_master = hasattr(request.user, 'profile') and request.user.profile.is_master
    if not request.user.is_staff and not is_master:
        raise PermissionDenied

    errors = []

    if request.method == 'POST':
        title      = request.POST.get('title', '').strip()
        difficulty = request.POST.get('difficulty', SortingRaceChallenge.EASY)
        hint       = request.POST.get('hint', '').strip()

        if not title:
            errors.append('Title is required.')
        if difficulty not in (SortingRaceChallenge.EASY,
                               SortingRaceChallenge.MEDIUM,
                               SortingRaceChallenge.HARD):
            errors.append('Invalid difficulty.')

        if not errors:
            challenge = SortingRaceChallenge.objects.create(
                title=title,
                difficulty=difficulty,
                hint=hint,
                created_by=request.user,
            )
            return redirect('sortingrace_play', pk=challenge.pk)

    context = {
        'errors':      errors,
        'difficulties': SortingRaceChallenge.DIFFICULTY_CHOICES,
        'post':        request.POST if request.method == 'POST' else {},
    }
    return render(request, 'games/sortingrace_create.html', context)


# ---------------------------------------------------------------------------
# Word Order Chaos views
# ---------------------------------------------------------------------------

@login_required
def wordorder_list(request):
    challenges = WordOrderChallenge.objects.filter(is_active=True)
    return render(request, 'games/wordorder_list.html', {'challenges': challenges})


@login_required
def wordorder_play(request, pk):
    challenge = get_object_or_404(WordOrderChallenge, pk=pk, is_active=True)

    words_key  = f'wo_{pk}_words'
    answer_key = f'wo_{pk}_answer'
    bank_key   = f'wo_{pk}_bank'
    start_key  = f'wo_{pk}_start'
    done_key   = f'wo_{pk}_done'

    if request.method == 'POST' and request.POST.get('action') == 'reset':
        for k in (words_key, answer_key, bank_key, start_key, done_key):
            request.session.pop(k, None)
        return redirect('wordorder_play', pk=pk)

    if words_key not in request.session:
        words = challenge.sentence.split()
        bank  = list(range(len(words)))
        random.shuffle(bank)
        request.session[words_key]  = words
        request.session[answer_key] = []
        request.session[bank_key]   = bank
        request.session[start_key]  = int(time.time())
        request.session[done_key]   = False

    words      = request.session[words_key]
    answer     = request.session[answer_key]
    bank       = request.session[bank_key]
    start_time = request.session[start_key]
    done       = request.session[done_key]
    elapsed    = int(time.time()) - start_time if done else None

    context = {
        'challenge':   challenge,
        'words_json':  json.dumps(words),
        'answer_json': json.dumps(answer),
        'bank_json':   json.dumps(bank),
        'start_ms':    start_time * 1000,
        'done':        done,
        'elapsed':     elapsed,
    }
    return render(request, 'games/wordorder_play.html', context)


@login_required
def wordorder_check(request, pk):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    challenge = get_object_or_404(WordOrderChallenge, pk=pk, is_active=True)

    try:
        data   = json.loads(request.body)
        answer = [int(i) for i in data.get('answer', [])]
        bank   = [int(i) for i in data.get('bank', [])]
    except (ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({'error': 'Invalid data'}, status=400)

    words_key  = f'wo_{pk}_words'
    answer_key = f'wo_{pk}_answer'
    bank_key   = f'wo_{pk}_bank'
    start_key  = f'wo_{pk}_start'
    done_key   = f'wo_{pk}_done'

    words = request.session.get(words_key)
    if not words:
        return JsonResponse({'error': 'No active game'}, status=400)

    request.session[answer_key] = answer
    request.session[bank_key]   = bank

    if bank:
        return JsonResponse({'error': 'incomplete'})

    correct = (answer == list(range(len(words))))
    if correct:
        elapsed = int(time.time()) - request.session.get(start_key, int(time.time()))
        request.session[done_key] = True
        return JsonResponse({'correct': True, 'elapsed': elapsed})

    return JsonResponse({'correct': False})


@login_required
def wordorder_create(request):
    is_master = hasattr(request.user, 'profile') and request.user.profile.is_master
    if not request.user.is_staff and not is_master:
        raise PermissionDenied

    errors = []

    if request.method == 'POST':
        title    = request.POST.get('title', '').strip()
        sentence = request.POST.get('sentence', '').strip()
        hint     = request.POST.get('hint', '').strip()

        if not title:
            errors.append('Title is required.')
        if not sentence:
            errors.append('Sentence is required.')
        else:
            word_count = len(sentence.split())
            if word_count < 3:
                errors.append('Sentence must have at least 3 words.')
            elif word_count > 20:
                errors.append('Sentence must have 20 words or fewer.')

        if not errors:
            challenge = WordOrderChallenge.objects.create(
                title=title,
                sentence=sentence,
                hint=hint,
                created_by=request.user,
            )
            return redirect('wordorder_play', pk=challenge.pk)

    context = {
        'errors': errors,
        'post':   request.POST if request.method == 'POST' else {},
    }
    return render(request, 'games/wordorder_create.html', context)
