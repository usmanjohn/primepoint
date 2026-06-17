import ast
import json
import math
import operator
import random
import time
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
import string
from .models import CrosswordPuzzle, EnglishCrossword, WordSearchPuzzle, CodeBreakerPuzzle, CodeBreakerClue, PrimeClimbChallenge, SortingRaceChallenge, WordOrderChallenge, OddOneOutPack, OddOneOutQuestion, MathSquarePuzzle
from .generator import generate_math_square, empty_math_square, eval_line


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


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _can_manage_games(user):
    """Only staff/admins and masters (teachers) may print/download puzzles."""
    if user.is_staff:
        return True
    return hasattr(user, 'profile') and user.profile.is_master


def _build_print_context(puzzle, primary_field, secondary_field, show_answers):
    """Assemble an A4-friendly print context for a crossword puzzle.

    `primary_field`/`secondary_field` are the per-word clue keys in grid_data
    (e.g. 'clue_korean'/'clue_uzbek' or 'clue_english'/'clue_uzbek').
    """
    grid_data = puzzle.grid_data or {}
    words = grid_data.get('words', [])
    cells = grid_data.get('cells', [])
    rows  = grid_data.get('rows', 0)
    cols  = grid_data.get('cols', 0)

    # Which directions start at each cell, plus the clue number.
    start_map = {}
    # Which directions END at each cell (last letter of a word). Used on the
    # printout to mark where a word stops, since adjacent white cells from
    # crossing words can otherwise make a word's length ambiguous on paper.
    end_map = {}
    for w in words:
        key = (w['row'], w['col'])
        entry = start_map.setdefault(key, {'number': w['number'], 'across': False, 'down': False})
        entry[w['direction']] = True

        last = w['length'] - 1
        er = w['row'] + (last if w['direction'] == 'down'   else 0)
        ec = w['col'] + (last if w['direction'] == 'across' else 0)
        ed = end_map.setdefault((er, ec), {'across': False, 'down': False})
        ed[w['direction']] = True

    grid_rows = []
    for r in range(rows):
        row_cells = []
        for c in range(cols):
            cell_val = cells[r][c] if cells else None
            if cell_val is None:
                row_cells.append({'is_black': True})
            else:
                s = start_map.get((r, c))
                e = end_map.get((r, c))
                row_cells.append({
                    'is_black':   False,
                    'letter':     cell_val if show_answers else '',
                    'number':     s['number'] if s else None,
                    'across':     s['across'] if s else False,
                    'down':       s['down'] if s else False,
                    'end_across': e['across'] if e else False,
                    'end_down':   e['down'] if e else False,
                })
        grid_rows.append(row_cells)

    def clue_list(direction):
        items = sorted((w for w in words if w['direction'] == direction),
                       key=lambda x: x['number'])
        return [{
            'number':    w['number'],
            'length':    w['length'],
            'primary':   w.get(primary_field, ''),
            'secondary': w.get(secondary_field, ''),
        } for w in items]

    # Size each cell so the whole grid fits one A4 page (≈186mm usable width,
    # leaving room below for the clue lists). Clamp to a readable range.
    if cols and rows:
        cell_mm = min(11.0, 182.0 / cols, 150.0 / rows)
    else:
        cell_mm = 10.0
    cell_mm = round(max(cell_mm, 5.5), 2)

    return {
        'puzzle':       puzzle,
        'grid_rows':    grid_rows,
        'across_clues': clue_list('across'),
        'down_clues':   clue_list('down'),
        'has_grid':     bool(grid_rows),
        'show_answers': show_answers,
        'cell_mm':      cell_mm,
        'num_mm':       round(max(2.2, cell_mm * 0.30), 2),
        'arrow_mm':     round(max(2.6, cell_mm * 0.38), 2),
        'letter_mm':    round(max(3.0, cell_mm * 0.52), 2),
    }


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

        if action == 'reset':
            # Clear the active game and return to the start screen so the
            # player can choose a different range. The last range is kept in
            # 'guess_max' so the setup form can pre-fill it.
            session['guess_target'] = None
            session['guess_attempts'] = 0
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
        'can_manage':   _can_manage_games(request.user),
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


@login_required
def crossword_print(request, pk):
    if not _can_manage_games(request.user):
        raise PermissionDenied
    puzzle = get_object_or_404(CrosswordPuzzle, pk=pk)
    show_answers = request.GET.get('answers') == '1'
    context = _build_print_context(puzzle, 'clue_korean', 'clue_uzbek', show_answers)
    context.update({
        'accent':     '#7c3aed',
        'back_url':   'crossword_play',
        'print_url':  'crossword_print',
    })
    return render(request, 'games/crossword_print.html', context)


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
    active_lang = request.GET.get('lang', '')

    all_qs = WordOrderChallenge.objects.filter(is_active=True)

    LANG_META = [
        {'code': 'en', 'label': 'English',  'flag': '🇬🇧'},
        {'code': 'ko', 'label': '한국어',    'flag': '🇰🇷'},
        {'code': 'uz', 'label': "O'zbek",   'flag': '🇺🇿'},
    ]
    lang_cards = [
        {**m, 'count': all_qs.filter(language=m['code']).count(),
         'active': active_lang == m['code']}
        for m in LANG_META
        if all_qs.filter(language=m['code']).exists()
    ]

    DIFF_LABELS = {
        'en': {'easy': 'Easy', 'medium': 'Medium', 'hard': 'Hard'},
        'ko': {'easy': '쉬운 문제', 'medium': '중간 문제', 'hard': '어려운 문제'},
        'uz': {'easy': 'Oson',   'medium': "O'rta",     'hard': 'Qiyin'},
    }

    grouped = []
    if active_lang:
        diff_labels = DIFF_LABELS.get(active_lang, DIFF_LABELS['en'])
        challenges  = all_qs.filter(language=active_lang).order_by('difficulty', 'pk')
        bucket = {}
        for ch in challenges:
            bucket.setdefault(ch.difficulty, []).append(ch)
        for diff in ('easy', 'medium', 'hard'):
            if diff in bucket:
                grouped.append({'label': diff_labels[diff], 'items': bucket[diff]})

    return render(request, 'games/wordorder_list.html', {
        'lang_cards':   lang_cards,
        'grouped':      grouped,
        'active_lang':  active_lang,
    })


@login_required
def wordorder_play(request, pk):
    challenge = get_object_or_404(WordOrderChallenge, pk=pk, is_active=True)

    sibling_ids = list(
        WordOrderChallenge.objects.filter(is_active=True, language=challenge.language)
        .order_by('difficulty', 'pk')
        .values_list('pk', flat=True)
    )
    try:
        pos     = sibling_ids.index(challenge.pk)
        prev_pk = sibling_ids[pos - 1] if pos > 0 else None
        next_pk = sibling_ids[pos + 1] if pos < len(sibling_ids) - 1 else None
        position_label = f'{pos + 1} / {len(sibling_ids)}'
    except ValueError:
        prev_pk = next_pk = None
        position_label = ''

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
        'challenge':      challenge,
        'words_json':     json.dumps(words),
        'answer_json':    json.dumps(answer),
        'bank_json':      json.dumps(bank),
        'start_ms':       start_time * 1000,
        'done':           done,
        'elapsed':        elapsed,
        'prev_pk':        prev_pk,
        'next_pk':        next_pk,
        'position_label': position_label,
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


# ---------------------------------------------------------------------------
# Odd One Out views
# ---------------------------------------------------------------------------

@login_required
def oddoneout_list(request):
    packs = OddOneOutPack.objects.filter(is_active=True)
    return render(request, 'games/oddoneout_list.html', {'packs': packs})


@login_required
def oddoneout_create(request):
    is_master = hasattr(request.user, 'profile') and request.user.profile.is_master
    if not request.user.is_staff and not is_master:
        raise PermissionDenied

    errors = []
    if request.method == 'POST':
        title    = request.POST.get('title', '').strip()
        desc     = request.POST.get('description', '').strip()
        language = request.POST.get('language', OddOneOutPack.LANG_ANY)

        if not title:
            errors.append('Title is required.')
        if language not in (OddOneOutPack.LANG_EN, OddOneOutPack.LANG_KO,
                             OddOneOutPack.LANG_UZ, OddOneOutPack.LANG_ANY):
            errors.append('Select a valid language.')

        if not errors:
            pack = OddOneOutPack.objects.create(
                title=title,
                description=desc,
                language=language,
                created_by=request.user,
            )
            return redirect('oddoneout_manage', pk=pack.pk)

    context = {
        'errors':    errors,
        'languages': OddOneOutPack.LANGUAGE_CHOICES,
        'post':      request.POST if request.method == 'POST' else {},
    }
    return render(request, 'games/oddoneout_create.html', context)


@login_required
def oddoneout_manage(request, pk):
    is_master = hasattr(request.user, 'profile') and request.user.profile.is_master
    if not request.user.is_staff and not is_master:
        raise PermissionDenied

    pack   = get_object_or_404(OddOneOutPack, pk=pk)
    errors = []

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'add':
            w1  = request.POST.get('word_1', '').strip()
            w2  = request.POST.get('word_2', '').strip()
            w3  = request.POST.get('word_3', '').strip()
            w4  = request.POST.get('word_4', '').strip()
            odd = request.POST.get('odd_index', '')
            expl = request.POST.get('explanation', '').strip()

            if not all([w1, w2, w3, w4]):
                errors.append('All four words are required.')
            try:
                odd_i = int(odd)
                if odd_i not in range(4):
                    raise ValueError
            except (ValueError, TypeError):
                errors.append('Select which word is the odd one out.')

            if not errors:
                next_order = pack.questions.count()
                OddOneOutQuestion.objects.create(
                    pack=pack,
                    word_1=w1, word_2=w2, word_3=w3, word_4=w4,
                    odd_index=odd_i,
                    explanation=expl,
                    order=next_order,
                )
                return redirect('oddoneout_manage', pk=pk)

        elif action == 'delete':
            qpk = request.POST.get('qpk')
            OddOneOutQuestion.objects.filter(pk=qpk, pack=pack).delete()
            return redirect('oddoneout_manage', pk=pk)

    questions = pack.questions.all()
    context = {
        'pack':      pack,
        'questions': questions,
        'errors':    errors,
        'post':      request.POST if request.method == 'POST' else {},
    }
    return render(request, 'games/oddoneout_manage.html', context)


@login_required
def oddoneout_play(request, pk):
    pack = get_object_or_404(OddOneOutPack, pk=pk, is_active=True)
    questions = list(pack.questions.all())

    if not questions:
        return render(request, 'games/oddoneout_play.html', {
            'pack': pack, 'empty': True,
        })

    cur_key     = f'oo_{pk}_current'
    results_key = f'oo_{pk}_results'
    disp_key    = f'oo_{pk}_display'
    start_key   = f'oo_{pk}_start'

    if request.method == 'POST' and request.POST.get('action') == 'reset':
        for k in (cur_key, results_key, disp_key, start_key):
            request.session.pop(k, None)
        return redirect('oddoneout_play', pk=pk)

    if request.method == 'POST' and request.POST.get('action') == 'next':
        cur = request.session.get(cur_key, 0)
        request.session[cur_key] = min(cur + 1, len(questions) - 1)
        return redirect('oddoneout_play', pk=pk)

    # Initialise session
    if cur_key not in request.session:
        # Pre-compute a shuffled display order for every question
        display_orders = []
        for q in questions:
            order = list(range(4))
            random.shuffle(order)
            display_orders.append(order)
        request.session[disp_key]     = display_orders
        request.session[cur_key]      = 0
        request.session[results_key]  = [None] * len(questions)
        request.session[start_key]    = int(time.time())

    cur            = request.session.get(cur_key, 0)
    results        = request.session.get(results_key, [None] * len(questions))
    display_orders = request.session.get(disp_key, [list(range(4))] * len(questions))
    start_time     = request.session.get(start_key, int(time.time()))

    # Clamp current in case questions were deleted
    cur = min(cur, len(questions) - 1)

    q           = questions[cur]
    disp_order  = display_orders[cur]        # e.g. [2, 0, 3, 1]
    all_words   = q.words_list()
    disp_words  = [all_words[i] for i in disp_order]
    odd_display = disp_order.index(q.odd_index)  # which display position is odd

    already_answered = results[cur] is not None
    done_all         = all(r is not None for r in results)
    elapsed          = int(time.time()) - start_time if done_all else None

    context = {
        'pack':             pack,
        'question':         q,
        'disp_words':       disp_words,
        'odd_display':      odd_display,
        'q_index':          cur,
        'q_total':          len(questions),
        'results':          results,
        'already_answered': already_answered,
        'done_all':         done_all,
        'elapsed':          elapsed,
        'score':            sum(1 for r in results if r),
        'start_ms':         start_time * 1000,
    }
    return render(request, 'games/oddoneout_play.html', context)


@login_required
def oddoneout_check(request, pk):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    pack = get_object_or_404(OddOneOutPack, pk=pk, is_active=True)

    try:
        data          = json.loads(request.body)
        q_index       = int(data['q_index'])
        selected_disp = int(data['selected'])
    except (KeyError, ValueError, TypeError, json.JSONDecodeError):
        return JsonResponse({'error': 'Invalid data'}, status=400)

    questions = list(pack.questions.all())
    if q_index >= len(questions):
        return JsonResponse({'error': 'Bad index'}, status=400)

    q           = questions[q_index]
    disp_key    = f'oo_{pk}_display'
    results_key = f'oo_{pk}_results'
    start_key   = f'oo_{pk}_start'

    display_orders = request.session.get(disp_key, [list(range(4))] * len(questions))
    disp_order     = display_orders[q_index]
    original_idx   = disp_order[selected_disp]
    correct        = (original_idx == q.odd_index)
    odd_display    = disp_order.index(q.odd_index)

    results = request.session.get(results_key, [None] * len(questions))
    if results[q_index] is None:
        results[q_index] = correct
        request.session[results_key] = results

    done_all = all(r is not None for r in results)
    elapsed  = int(time.time()) - request.session.get(start_key, int(time.time())) if done_all else None

    return JsonResponse({
        'correct':     correct,
        'odd_display': odd_display,
        'explanation': q.explanation,
        'done_all':    done_all,
        'elapsed':     elapsed,
        'score':       sum(1 for r in results if r),
        'total':       len(questions),
    })


# ---------------------------------------------------------------------------
# English Crossword views
# ---------------------------------------------------------------------------

@login_required
def english_crossword_list(request):
    puzzles = EnglishCrossword.objects.filter(is_published=True)
    return render(request, 'games/english_crossword_list.html', {'puzzles': puzzles})


@login_required
def english_crossword_play(request, pk):
    puzzle    = get_object_or_404(EnglishCrossword, pk=pk, is_published=True)
    grid_data = puzzle.grid_data or {}
    words     = grid_data.get('words', [])
    cells     = grid_data.get('cells', [])
    rows      = grid_data.get('rows', 0)
    cols      = grid_data.get('cols', 0)

    session_key = f'encw_{pk}_answers'
    check_key   = f'encw_{pk}_checked'

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'reset':
            request.session.pop(session_key, None)
            request.session.pop(check_key, None)
            return redirect('english_crossword_play', pk=pk)

        if action == 'check':
            answers = {}
            for word in words:
                direction = word['direction']
                for i in range(word['length']):
                    r = word['row'] + (i if direction == 'down' else 0)
                    c = word['col'] + (i if direction == 'across' else 0)
                    key = f'{r}_{c}'
                    val = request.POST.get(f'cell_{r}_{c}', '').strip().upper()
                    if val:
                        answers[key] = val
            request.session[session_key] = answers
            request.session[check_key]   = True
            return redirect('english_crossword_play', pk=pk)

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
                correct = (answer.upper() == cell_val.upper()) if checked else None
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
        'can_manage':   _can_manage_games(request.user),
    }
    return render(request, 'games/english_crossword_play.html', context)


@login_required
def english_crossword_edit(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    puzzle = get_object_or_404(EnglishCrossword, pk=pk)

    if request.method == 'POST':
        try:
            data  = json.loads(request.body)
            rows  = max(1, min(int(data.get('rows', puzzle.grid_rows)), 25))
            cols  = max(1, min(int(data.get('cols', puzzle.grid_cols)), 25))
            words = data.get('words', [])
            cells = data.get('cells', [])
            puzzle.grid_data = {'rows': rows, 'cols': cols, 'words': words, 'cells': cells}
            puzzle.save()
            return JsonResponse({'ok': True, 'word_count': len(words)})
        except Exception as e:
            return JsonResponse({'ok': False, 'error': str(e)}, status=400)

    return render(request, 'games/english_crossword_edit.html', {'puzzle': puzzle})


@login_required
def english_crossword_print(request, pk):
    if not _can_manage_games(request.user):
        raise PermissionDenied
    puzzle = get_object_or_404(EnglishCrossword, pk=pk)
    show_answers = request.GET.get('answers') == '1'
    context = _build_print_context(puzzle, 'clue_english', 'clue_uzbek', show_answers)
    context.update({
        'accent':     '#2563eb',
        'back_url':   'english_crossword_play',
        'print_url':  'english_crossword_print',
    })
    return render(request, 'games/crossword_print.html', context)


# ---------------------------------------------------------------------------
# Word Search — generator + views
# ---------------------------------------------------------------------------

_WS_DIRS = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]

def generate_word_search(words, size=15):
    words = [w.strip().upper() for w in words if w.strip() and w.strip().isalpha()]
    grid  = [[None] * size for _ in range(size)]
    placed = []

    random.shuffle(words)
    for word in words:
        for _ in range(200):
            dr, dc = random.choice(_WS_DIRS)
            r_min = max(0, -(dr * (len(word)-1)))
            r_max = min(size-1, size-1 - max(0, dr*(len(word)-1)))
            c_min = max(0, -(dc * (len(word)-1)))
            c_max = min(size-1, size-1 - max(0, dc*(len(word)-1)))
            if r_min > r_max or c_min > c_max:
                continue
            r = random.randint(r_min, r_max)
            c = random.randint(c_min, c_max)
            ok = all(
                grid[r+dr*i][c+dc*i] in (None, word[i])
                for i in range(len(word))
            )
            if ok:
                for i, letter in enumerate(word):
                    grid[r+dr*i][c+dc*i] = letter
                placed.append({
                    'word':    word,
                    'start_r': r,            'start_c': c,
                    'end_r':   r+dr*(len(word)-1),
                    'end_c':   c+dc*(len(word)-1),
                })
                break

    for r in range(size):
        for c in range(size):
            if grid[r][c] is None:
                grid[r][c] = random.choice(string.ascii_uppercase)

    return grid, placed


@login_required
def wordsearch_list(request):
    puzzles = WordSearchPuzzle.objects.filter(is_published=True)
    return render(request, 'games/wordsearch_list.html', {'puzzles': puzzles})


@login_required
def wordsearch_play(request, pk):
    puzzle    = get_object_or_404(WordSearchPuzzle, pk=pk, is_published=True)
    grid_data = puzzle.grid_data or {}
    context = {
        'puzzle':     puzzle,
        'grid_json':  json.dumps(grid_data.get('grid', [])),
        'words_json': json.dumps(grid_data.get('words', [])),
        'size':       grid_data.get('size', 15),
    }
    return render(request, 'games/wordsearch_play.html', context)


# ---------------------------------------------------------------------------
# Target Number
# ---------------------------------------------------------------------------

_TN_DIFFICULTY = {
    'easy':   {'small': (1, 9),   'large': [],                'small_count': 4, 'large_count': 0, 'target_range': (10, 50)},
    'medium': {'small': (1, 15),  'large': [10, 25, 50],      'small_count': 4, 'large_count': 2, 'target_range': (50, 200)},
    'hard':   {'small': (1, 9),   'large': [25, 50, 75, 100], 'small_count': 4, 'large_count': 2, 'target_range': (100, 999)},
}

_TN_OPS = {
    ast.Add:  operator.add,
    ast.Sub:  operator.sub,
    ast.Mult: operator.mul,
    ast.Div:  operator.truediv,
}

def _tn_eval(node):
    if isinstance(node, ast.Expression):
        return _tn_eval(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _TN_OPS:
        left, right = _tn_eval(node.left), _tn_eval(node.right)
        if isinstance(node.op, ast.Div):
            if right == 0:
                raise ValueError("Division by zero")
            result = operator.truediv(left, right)
            if result != int(result):
                raise ValueError("Non-integer result")
            return int(result)
        return _TN_OPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -_tn_eval(node.operand)
    raise ValueError(f"Unsafe node: {type(node).__name__}")


def _tn_extract_numbers(node):
    if isinstance(node, ast.Expression):
        return _tn_extract_numbers(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return [int(node.value)]
    if isinstance(node, ast.BinOp):
        return _tn_extract_numbers(node.left) + _tn_extract_numbers(node.right)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return _tn_extract_numbers(node.operand)
    return []


def _tn_generate(difficulty):
    cfg = _TN_DIFFICULTY[difficulty]
    nums = [random.randint(cfg['small'][0], cfg['small'][1]) for _ in range(cfg['small_count'])]
    if cfg['large_count']:
        nums += random.sample(cfg['large'], cfg['large_count'])

    lo, hi = cfg['target_range']
    ops = [operator.add, operator.sub, operator.mul]
    target = lo - 1

    for _ in range(50):
        use_count = random.randint(3, min(5, len(nums)))
        seed = random.sample(nums, use_count)
        acc = seed[0]
        for n in seed[1:]:
            candidate = random.choice(ops)(acc, n)
            if isinstance(candidate, int) and candidate > 0:
                acc = candidate
        if lo <= acc <= hi:
            target = acc
            break
    else:
        target = max(lo, min(hi, nums[0] + nums[1]))

    return nums, target


@login_required
def target_number(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'new':
            difficulty = request.POST.get('difficulty', 'easy')
            if difficulty not in ('easy', 'medium', 'hard'):
                difficulty = 'easy'
            nums, target = _tn_generate(difficulty)
            request.session.update({
                'tn_numbers':    nums,
                'tn_target':     target,
                'tn_difficulty': difficulty,
                'tn_start':      int(time.time()),
                'tn_attempts':   0,
                'tn_solved':     False,
            })
            return redirect('target_number')

        if action == 'reset':
            # Clear the active game and return to the start screen so the
            # player can choose a different difficulty. The last difficulty is
            # kept in 'tn_difficulty' so the setup form can pre-select it.
            request.session['tn_numbers'] = None
            request.session.pop('tn_target', None)
            request.session['tn_attempts'] = 0
            request.session['tn_solved'] = False
            return redirect('target_number')

    context = {
        'started':    request.session.get('tn_numbers') is not None,
        'numbers':    request.session.get('tn_numbers', []),
        'target':     request.session.get('tn_target'),
        'difficulty': request.session.get('tn_difficulty', 'easy'),
        'attempts':   request.session.get('tn_attempts', 0),
        'solved':     request.session.get('tn_solved', False),
        'best':       request.session.get('tn_best'),
        'start_ms':   (request.session['tn_start'] * 1000) if request.session.get('tn_start') else 0,
    }
    return render(request, 'games/target_number.html', context)


@login_required
def target_number_check(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    numbers = request.session.get('tn_numbers')
    target  = request.session.get('tn_target')
    if numbers is None or target is None:
        return JsonResponse({'error': 'No active game'}, status=400)

    try:
        data = json.loads(request.body)
        expression = str(data.get('expression', '')).strip()
    except (ValueError, json.JSONDecodeError):
        return JsonResponse({'error': 'Invalid JSON'}, status=400)

    if not expression:
        return JsonResponse({'error': 'Empty expression'}, status=400)

    safe_expr = expression.replace('×', '*').replace('÷', '/').replace('−', '-')

    try:
        tree = ast.parse(safe_expr, mode='eval')
    except SyntaxError:
        return JsonResponse({'error': 'Syntax error', 'result': None, 'correct': False, 'distance': None})

    try:
        used = _tn_extract_numbers(tree)
    except ValueError:
        return JsonResponse({'error': 'Invalid expression', 'result': None, 'correct': False, 'distance': None})

    pool_copy = list(numbers)
    for n in used:
        if n in pool_copy:
            pool_copy.remove(n)
        else:
            return JsonResponse({'error': 'Number not in pool', 'result': None, 'correct': False, 'distance': None})

    try:
        result = _tn_eval(tree)
    except (ValueError, ZeroDivisionError):
        return JsonResponse({'error': 'Invalid operation', 'result': None, 'correct': False, 'distance': None})

    correct  = (result == target)
    distance = abs(result - target)
    elapsed  = int(time.time()) - request.session.get('tn_start', int(time.time()))
    request.session['tn_attempts'] = request.session.get('tn_attempts', 0) + 1
    attempts = request.session['tn_attempts']

    if correct and not request.session.get('tn_solved'):
        request.session['tn_solved'] = True
        best = request.session.get('tn_best')
        if best is None or attempts < best:
            request.session['tn_best'] = attempts

    return JsonResponse({
        'result':   result,
        'correct':  correct,
        'distance': distance,
        'attempts': attempts,
        'elapsed':  elapsed,
    })


# ---------------------------------------------------------------------------
# Math Square (Cross-Math) views
# ---------------------------------------------------------------------------

_MS_SIZE_FOR = {'easy': 2, 'medium': 3, 'hard': 4}


def _ms_fmt(values, ops):
    """Render 'a + b × c' for an equation line (for validation messages)."""
    out = str(values[0])
    for op, v in zip(ops, values[1:]):
        out += f' {op} {v}'
    return out


def _ms_validate(grid):
    """Return a list of human-readable errors for any row/column whose
    equation is not true under BODMAS. Empty list ⇒ the grid is valid."""
    n     = grid.get('n', 0)
    cells = grid.get('cells', [])
    errors = []

    def num(r, c):
        cell = cells[r][c]
        return cell.get('v')

    msg_fill   = _('fill every number')
    msg_divide = _('division is not exact')

    def line(values, ops, res, label):
        if any(v is None for v in values) or res is None:
            errors.append(f'{label}: {msg_fill}.')
            return
        r = eval_line(values, ops)
        if r is None:
            errors.append(f'{label}: {msg_divide}.')
        elif r != res:
            errors.append(f'{label}: {_ms_fmt(values, ops)} = {r} ≠ {res}.')

    for i in range(n):
        line([num(2 * i, 2 * j) for j in range(n)],
             [cells[2 * i][2 * j + 1].get('v') for j in range(n - 1)],
             num(2 * i, 2 * n), f'{_("Row")} {i + 1}')
    for j in range(n):
        line([num(2 * i, 2 * j) for i in range(n)],
             [cells[2 * i + 1][2 * j].get('v') for i in range(n - 1)],
             num(2 * n, 2 * j), f'{_("Column")} {j + 1}')
    return errors


@login_required
def mathsquare_list(request):
    can_manage = _can_manage_games(request.user)
    puzzles = MathSquarePuzzle.objects.filter(is_published=True)
    if can_manage:
        own = MathSquarePuzzle.objects.filter(created_by=request.user)
        puzzles = (puzzles | own).distinct()
    return render(request, 'games/mathsquare_list.html',
                  {'puzzles': puzzles, 'can_manage': can_manage})


@login_required
def mathsquare_create(request):
    if not _can_manage_games(request.user):
        raise PermissionDenied

    errors = []
    if request.method == 'POST':
        title      = request.POST.get('title', '').strip()
        difficulty = request.POST.get('difficulty', MathSquarePuzzle.DIFFICULTY_EASY)
        method     = request.POST.get('method', 'generate')

        if not title:
            errors.append(_('Title is required.'))
        if difficulty not in _MS_SIZE_FOR:
            errors.append(_('Invalid difficulty.'))

        grid = None
        if not errors:
            if method == 'manual':
                grid = empty_math_square(_MS_SIZE_FOR[difficulty])
            else:
                grid = generate_math_square(difficulty)
                if grid is None:
                    errors.append(_('Could not generate a puzzle. Please try again.'))

        if not errors:
            puzzle = MathSquarePuzzle.objects.create(
                title=title,
                difficulty=difficulty,
                size=grid['n'],
                grid_data=grid,
                created_by=request.user,
                is_published=(method == 'generate'),
            )
            return redirect('mathsquare_edit', pk=puzzle.pk)

    context = {
        'errors':       errors,
        'difficulties': MathSquarePuzzle.DIFFICULTY_CHOICES,
        'post':         request.POST if request.method == 'POST' else {},
    }
    return render(request, 'games/mathsquare_create.html', context)


@login_required
def mathsquare_edit(request, pk):
    if not _can_manage_games(request.user):
        raise PermissionDenied
    puzzle = get_object_or_404(MathSquarePuzzle, pk=pk)

    if request.method == 'POST':
        try:
            data  = json.loads(request.body)
            n     = puzzle.size
            cells = data.get('cells', [])
            grid  = {'rows': 2 * n + 1, 'cols': 2 * n + 1, 'n': n,
                     'eval': 'bodmas', 'difficulty': puzzle.difficulty, 'cells': cells}
            errors = _ms_validate(grid)
            puzzle.grid_data    = grid
            puzzle.is_published = (len(errors) == 0)
            puzzle.save()
            return JsonResponse({'ok': True, 'errors': errors,
                                 'published': puzzle.is_published})
        except Exception as e:
            return JsonResponse({'ok': False, 'error': str(e)}, status=400)

    return render(request, 'games/mathsquare_edit.html', {
        'puzzle':    puzzle,
        'grid_json': json.dumps(puzzle.grid_data or {}),
    })


@login_required
def mathsquare_play(request, pk):
    puzzle = get_object_or_404(MathSquarePuzzle, pk=pk, is_published=True)
    grid   = puzzle.grid_data or {}
    cells  = grid.get('cells', [])
    rows   = grid.get('rows', 0)
    cols   = grid.get('cols', 0)

    answers_key = f'mathsquare_{pk}_answers'
    check_key   = f'mathsquare_{pk}_checked'

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'reset':
            request.session.pop(answers_key, None)
            request.session.pop(check_key, None)
            return redirect('mathsquare_play', pk=pk)
        if action == 'check':
            answers = {}
            for r in range(rows):
                for c in range(cols):
                    cell = cells[r][c]
                    if cell.get('t') == 'num' and not cell.get('given'):
                        val = request.POST.get(f'cell_{r}_{c}', '').strip()
                        if val:
                            answers[f'{r}_{c}'] = val
            request.session[answers_key] = answers
            request.session[check_key]   = True
            return redirect('mathsquare_play', pk=pk)

    saved   = request.session.get(answers_key, {})
    checked = request.session.get(check_key, False)

    grid_rows = []
    total = correct_count = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            cell = cells[r][c] if cells else {'t': 'blank'}
            t = cell.get('t', 'blank')
            if t == 'num' and cell.get('given'):
                row.append({'t': 'num', 'given': True, 'value': cell.get('v')})
            elif t == 'num':
                total += 1
                ans = saved.get(f'{r}_{c}', '')
                is_corr = None
                if checked:
                    is_corr = (ans != '' and str(cell.get('v')) == ans)
                    if is_corr:
                        correct_count += 1
                row.append({'t': 'num', 'given': False, 'r': r, 'c': c,
                            'answer': ans, 'correct': is_corr})
            elif t == 'op':
                row.append({'t': 'op', 'glyph': cell.get('v')})
            elif t == 'eq':
                row.append({'t': 'eq'})
            else:
                row.append({'t': 'blank'})
        grid_rows.append(row)

    all_correct = checked and total > 0 and correct_count == total

    context = {
        'puzzle':       puzzle,
        'grid_rows':    grid_rows,
        'checked':      checked,
        'all_correct':  all_correct,
        'can_manage':   _can_manage_games(request.user),
    }
    return render(request, 'games/mathsquare_play.html', context)


def _build_mathsquare_print_context(puzzle, show_answers):
    """A4-friendly print context for a math square (mirrors _build_print_context)."""
    grid  = puzzle.grid_data or {}
    cells = grid.get('cells', [])
    rows  = grid.get('rows', 0)
    cols  = grid.get('cols', 0)

    grid_rows = []
    for r in range(rows):
        row = []
        for c in range(cols):
            cell = cells[r][c] if cells else {'t': 'blank'}
            t = cell.get('t', 'blank')
            if t == 'num':
                given = cell.get('given', True)
                row.append({
                    't':        'num',
                    'is_blank': not given,
                    'text':     cell.get('v') if (given or show_answers) else '',
                })
            elif t == 'op':
                row.append({'t': 'op', 'text': cell.get('v')})
            elif t == 'eq':
                row.append({'t': 'eq', 'text': '='})
            else:
                row.append({'t': 'blank'})
        grid_rows.append(row)

    # Fewer cells than a crossword, so make them larger; clamp to a sane range.
    if cols and rows:
        cell_mm = min(16.0, 182.0 / cols, 210.0 / rows)
    else:
        cell_mm = 14.0
    cell_mm = round(max(cell_mm, 8.0), 2)

    return {
        'puzzle':       puzzle,
        'grid_rows':    grid_rows,
        'has_grid':     bool(grid_rows),
        'show_answers': show_answers,
        'cell_mm':      cell_mm,
        'num_mm':       round(max(4.0, cell_mm * 0.42), 2),
        'op_mm':        round(max(3.4, cell_mm * 0.34), 2),
    }


@login_required
def mathsquare_print(request, pk):
    if not _can_manage_games(request.user):
        raise PermissionDenied
    puzzle = get_object_or_404(MathSquarePuzzle, pk=pk)
    show_answers = request.GET.get('answers') == '1'
    context = _build_mathsquare_print_context(puzzle, show_answers)
    context.update({'accent': '#0d9488'})
    return render(request, 'games/mathsquare_print.html', context)
