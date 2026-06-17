"""
Korean crossword generator.

Each grid cell holds one Korean syllable block (가, 나, 일, 본 …).
Words intersect when they share the exact same syllable at the same cell,
and the two words must be perpendicular (one across, one down).
"""
import random

DEFAULT_GRID_SIZE = 15
MIN_INTERNAL_SIZE = 42   # internal canvas is always at least this large


# ── Grid helpers ──────────────────────────────────────────────────────────────

def _empty_syl(r, c):
    return [[None] * c for _ in range(r)]

def _empty_dir(r, c):
    return [[set() for _ in range(c)] for _ in range(r)]

def _place_word(syl, dirs, word, row, col, direction):
    dr = 1 if direction == 'down' else 0
    dc = 1 if direction == 'across' else 0
    for i, syllable in enumerate(list(word)):
        r, c = row + dr * i, col + dc * i
        syl[r][c] = syllable
        dirs[r][c].add(direction)


# ── Placement validation ──────────────────────────────────────────────────────

def _valid(syl, dirs, syllables, row, col, direction, rows, cols):
    length = len(syllables)
    dr = 1 if direction == 'down' else 0
    dc = 1 if direction == 'across' else 0
    end_r = row + dr * (length - 1)
    end_c = col + dc * (length - 1)

    if end_r >= rows or end_c >= cols:
        return False

    br, bc = row - dr, col - dc
    if 0 <= br < rows and 0 <= bc < cols and syl[br][bc] is not None:
        return False

    ar, ac = end_r + dr, end_c + dc
    if 0 <= ar < rows and 0 <= ac < cols and syl[ar][ac] is not None:
        return False

    has_intersection = False

    for i, syllable in enumerate(syllables):
        r, c = row + dr * i, col + dc * i
        cell_syl = syl[r][c]
        cell_dirs = dirs[r][c]

        if cell_syl is not None:
            if cell_syl != syllable:
                return False
            if direction in cell_dirs:
                return False
            has_intersection = True
        else:
            if direction == 'across':
                if r > 0 and syl[r - 1][c] is not None:
                    return False
                if r < rows - 1 and syl[r + 1][c] is not None:
                    return False
            else:
                if c > 0 and syl[r][c - 1] is not None:
                    return False
                if c < cols - 1 and syl[r][c + 1] is not None:
                    return False

    return has_intersection


# ── Candidate finder ──────────────────────────────────────────────────────────

def _candidates(syl, dirs, word, rows, cols):
    syllables = list(word)
    length = len(syllables)
    results = set()

    for r in range(rows):
        for c in range(cols):
            cell_syl = syl[r][c]
            if cell_syl is None:
                continue
            for idx, syllable in enumerate(syllables):
                if syllable != cell_syl:
                    continue
                cell_dirs = dirs[r][c]

                if 'across' not in cell_dirs:
                    start_c = c - idx
                    if start_c >= 0 and start_c + length <= cols:
                        if _valid(syl, dirs, syllables, r, start_c, 'across', rows, cols):
                            results.add((r, start_c, 'across'))

                if 'down' not in cell_dirs:
                    start_r = r - idx
                    if start_r >= 0 and start_r + length <= rows:
                        if _valid(syl, dirs, syllables, start_r, c, 'down', rows, cols):
                            results.add((start_r, c, 'down'))

    return list(results)


# ── Candidate scoring ─────────────────────────────────────────────────────────

def _score_candidate(syllables, remaining_words):
    """Count how many unplaced words share a syllable with this placement."""
    placement_syls = set(syllables)
    return sum(1 for wo in remaining_words if set(wo.word) & placement_syls)


# ── Grid cropping ─────────────────────────────────────────────────────────────

def _crop(syl, rows, cols):
    min_r, max_r = rows, 0
    min_c, max_c = cols, 0
    for r in range(rows):
        for c in range(cols):
            if syl[r][c] is not None:
                min_r = min(min_r, r)
                max_r = max(max_r, r)
                min_c = min(min_c, c)
                max_c = max(max_c, c)
    if min_r > max_r:
        return [], 0, 0
    min_r = max(0, min_r - 1)
    min_c = max(0, min_c - 1)
    max_r = min(rows - 1, max_r + 1)
    max_c = min(cols - 1, max_c + 1)
    cropped = [row[min_c:max_c + 1] for row in syl[min_r:max_r + 1]]
    return cropped, min_r, min_c


# ── Single attempt ────────────────────────────────────────────────────────────

def _single_attempt(first, rest, size):
    rows = cols = size
    syl  = _empty_syl(rows, cols)
    dirs = _empty_dir(rows, cols)
    placed = []
    placed_pks = set()

    r0 = rows // 2
    c0 = (cols - len(first.word)) // 2
    _place_word(syl, dirs, first.word, r0, c0, 'across')
    placed.append((first, r0, c0, 'across'))
    placed_pks.add(first.pk)

    for wo in rest:
        if wo.pk in placed_pks:
            continue
        cands = _candidates(syl, dirs, wo.word, rows, cols)
        if not cands:
            continue

        remaining = [w for w in rest if w.pk not in placed_pks and w.pk != wo.pk]
        syllables  = list(wo.word)

        if len(cands) > 1:
            scored = [(
                _score_candidate(syllables, remaining),
                random.random(),   # tiebreak
                r, c, d
            ) for r, c, d in cands]
            scored.sort(key=lambda x: (-x[0], x[1]))
            r, c, direction = scored[0][2], scored[0][3], scored[0][4]
        else:
            r, c, direction = cands[0]

        _place_word(syl, dirs, wo.word, r, c, direction)
        placed.append((wo, r, c, direction))
        placed_pks.add(wo.pk)

    return placed, syl


# ── Main entry point ──────────────────────────────────────────────────────────

def generate_crossword(word_objects, grid_size=None, max_attempts=300):
    """
    Generate a crossword from a queryset/list of KoreanWord objects.
    Returns a dict with keys: rows, cols, cells, words — or None on failure.
    """
    words = list(word_objects)
    if not words:
        return None

    requested = max(10, min(grid_size or DEFAULT_GRID_SIZE, 25))
    # Use a much larger internal canvas so word placement is rarely blocked by bounds
    size = max(requested * 3, MIN_INTERNAL_SIZE)

    def connectivity(wo):
        syls = set(wo.word)
        return sum(1 for other in words if other.pk != wo.pk and syls & set(other.word))

    scored = sorted(words, key=connectivity, reverse=True)
    n = len(scored)

    best_placed = []
    best_grid   = None

    for attempt in range(max_attempts):
        first = scored[attempt % n]
        rest  = [w for w in scored if w.pk != first.pk]
        random.shuffle(rest)

        placed, syl = _single_attempt(first, rest, size)

        if len(placed) > len(best_placed):
            best_placed = placed
            best_grid   = [row[:] for row in syl]

        # Early exit if we placed everything
        if len(best_placed) == n:
            break

    if not best_placed:
        return None

    cropped, row_off, col_off = _crop(best_grid, size, size)
    final_rows = len(cropped)
    final_cols = len(cropped[0]) if cropped else 0

    adjusted = [(wo, r - row_off, c - col_off, d) for wo, r, c, d in best_placed]

    across = sorted([(wo, r, c, d) for wo, r, c, d in adjusted if d == 'across'], key=lambda x: (x[1], x[2]))
    down   = sorted([(wo, r, c, d) for wo, r, c, d in adjusted if d == 'down'],   key=lambda x: (x[1], x[2]))

    number_map = {}
    num = 1
    for entry in across + down:
        key = (entry[1], entry[2])
        if key not in number_map:
            number_map[key] = num
            num += 1

    words_data = []
    for direction_group in (across, down):
        for wo, r, c, d in direction_group:
            words_data.append({
                'number':      number_map[(r, c)],
                'word':        wo.word,
                'direction':   d,
                'row':         r,
                'col':         c,
                'length':      len(wo.word),
                'clue_korean': wo.clue_korean,
                'clue_uzbek':  wo.clue_uzbek,
            })

    return {
        'rows':  final_rows,
        'cols':  final_cols,
        'cells': cropped,
        'words': words_data,
    }


# ═══════════════════════════════════════════════════════════════════════════
# Math Square (Cross-Math) — evaluator + generator
#
# A math square of size N renders on a (2N+1)×(2N+1) grid. Even indices hold
# numbers; the N×N interior numbers are shared between a row equation and a
# column equation. The "=" sign sits at index 2N-1 and the result at index 2N.
# grid_data schema (one dict per cell):
#   {"t":"num","v":<int>,"given":<bool>}   number (given=False ⇒ solver fills it)
#   {"t":"op","v":"+|-|×|÷"}               operator
#   {"t":"eq"}                              equals sign
#   {"t":"blank"}                           spacer / corner
# ═══════════════════════════════════════════════════════════════════════════

MS_OPS = ('+', '-', '×', '÷')


def eval_line(values, ops):
    """Evaluate ``a op b op c …`` under BODMAS (× ÷ before + −, left to right).

    Returns the integer result, or ``None`` if a division isn't exact (so the
    same routine is the single source of truth for "is this equation valid").
    """
    if not values:
        return None
    # First pass: resolve × and ÷ left-to-right, collapsing into running terms.
    terms = [values[0]]
    add_ops = []
    for op, v in zip(ops, values[1:]):
        if op == '×':
            terms[-1] = terms[-1] * v
        elif op == '÷':
            if v == 0 or terms[-1] % v != 0:
                return None
            terms[-1] = terms[-1] // v
        else:
            add_ops.append(op)
            terms.append(v)
    # Second pass: + and −.
    result = terms[0]
    for op, v in zip(add_ops, terms[1:]):
        result = result + v if op == '+' else result - v
    return result


def _ms_params(difficulty):
    if difficulty == 'hard':
        return {'n': 4, 'ops': ['+', '-', '×', '÷'], 'lo': 1, 'hi': 15,
                'blanks': 9, 'allow_result_blank': True}
    if difficulty == 'medium':
        return {'n': 3, 'ops': ['+', '-', '×'], 'lo': 1, 'hi': 12,
                'blanks': 5, 'allow_result_blank': False}
    return {'n': 2, 'ops': ['+', '-'], 'lo': 1, 'hi': 9,
            'blanks': 2, 'allow_result_blank': False}


def _ms_build_solution(p, attempts=4000):
    """Pick random interior numbers + operators; keep only grids whose every
    row and column evaluates to a non-negative integer. Returns the solution
    tuple or ``None`` if no valid grid turned up within ``attempts``."""
    n = p['n']
    for _ in range(attempts):
        interior = [[random.randint(p['lo'], p['hi']) for _ in range(n)] for _ in range(n)]
        row_ops  = [[random.choice(p['ops']) for _ in range(n - 1)] for _ in range(n)]
        col_ops  = [[random.choice(p['ops']) for _ in range(n)] for _ in range(n - 1)]

        row_res, ok = [], True
        for i in range(n):
            r = eval_line(interior[i], row_ops[i])
            if r is None or r < 0:
                ok = False
                break
            row_res.append(r)
        if not ok:
            continue

        col_res = []
        for j in range(n):
            r = eval_line([interior[i][j] for i in range(n)],
                          [col_ops[i][j] for i in range(n - 1)])
            if r is None or r < 0:
                ok = False
                break
            col_res.append(r)
        if not ok:
            continue

        return interior, row_ops, col_ops, row_res, col_res
    return None


def _ms_equations(n, interior, row_ops, col_ops, row_res, col_res):
    """Build (equations, value_map) keyed by (r, c) grid coordinates."""
    value_map = {}
    equations = []
    for i in range(n):
        for j in range(n):
            value_map[(2 * i, 2 * j)] = interior[i][j]
    for i in range(n):
        value_map[(2 * i, 2 * n)] = row_res[i]
        equations.append({
            'cells': [(2 * i, 2 * j) for j in range(n)],
            'ops':   list(row_ops[i]),
            'res':   (2 * i, 2 * n),
        })
    for j in range(n):
        value_map[(2 * n, 2 * j)] = col_res[j]
        equations.append({
            'cells': [(2 * i, 2 * j) for i in range(n)],
            'ops':   [col_ops[i][j] for i in range(n - 1)],
            'res':   (2 * n, 2 * j),
        })
    return equations, value_map


def _ms_solvable(equations, value_map, blanks, p):
    """True if every blanked cell can be recovered uniquely by constraint
    propagation (repeatedly solving an equation that has a single unknown).
    Guarantees the puzzle has a unique, human-deducible solution."""
    known   = {c: v for c, v in value_map.items() if c not in blanks}
    unknown = set(blanks)
    progress = True
    while unknown and progress:
        progress = False
        for eq in equations:
            members = eq['cells'] + [eq['res']]
            unk = [m for m in members if m in unknown]
            if len(unk) != 1:
                continue
            u = unk[0]
            if u == eq['res']:
                r = eval_line([known[c] for c in eq['cells']], eq['ops'])
                if r is None:
                    continue
                known[u] = r
                unknown.discard(u)
                progress = True
            else:
                target = known[eq['res']]
                cand = []
                for v in range(p['lo'], p['hi'] + 1):
                    vals = [known[c] if c != u else v for c in eq['cells']]
                    if eval_line(vals, eq['ops']) == target:
                        cand.append(v)
                        if len(cand) > 1:
                            break
                if len(cand) == 1:
                    known[u] = cand[0]
                    unknown.discard(u)
                    progress = True
    return not unknown


def _ms_choose_blanks(equations, value_map, p):
    """Greedily blank cells (interior first, then results on hard) while the
    puzzle stays uniquely solvable by deduction."""
    n = p['n']
    interior = [(2 * i, 2 * j) for i in range(n) for j in range(n)]
    random.shuffle(interior)
    candidates = list(interior)
    if p['allow_result_blank']:
        results = [(2 * i, 2 * n) for i in range(n)] + [(2 * n, 2 * j) for j in range(n)]
        random.shuffle(results)
        candidates += results

    blanks = set()
    for cell in candidates:
        if len(blanks) >= p['blanks']:
            break
        trial = blanks | {cell}
        if _ms_solvable(equations, value_map, trial, p):
            blanks = trial
    return blanks


def _ms_to_cells(n, interior, row_ops, col_ops, row_res, col_res, blanks):
    D = 2 * n + 1
    cells = [[{'t': 'blank'} for _ in range(D)] for _ in range(D)]

    def put_num(r, c, v):
        cells[r][c] = {'t': 'num', 'v': v, 'given': (r, c) not in blanks}

    for i in range(n):
        for j in range(n):
            put_num(2 * i, 2 * j, interior[i][j])
    for i in range(n):
        for j in range(n - 1):
            cells[2 * i][2 * j + 1] = {'t': 'op', 'v': row_ops[i][j]}
        cells[2 * i][2 * n - 1] = {'t': 'eq'}
        put_num(2 * i, 2 * n, row_res[i])
    for j in range(n):
        for i in range(n - 1):
            cells[2 * i + 1][2 * j] = {'t': 'op', 'v': col_ops[i][j]}
        cells[2 * n - 1][2 * j] = {'t': 'eq'}
        put_num(2 * n, 2 * j, col_res[j])
    return cells


def generate_math_square(difficulty):
    """Return a ready-to-save grid_data dict for a crossed math square, or
    ``None`` if generation failed."""
    p = _ms_params(difficulty)
    sol = _ms_build_solution(p)
    if sol is None and '÷' in p['ops']:
        # ÷ makes exact-integer grids rare; fall back to + − × so creation
        # always succeeds (hard stays hard via the larger grid + more blanks).
        p = {**p, 'ops': ['+', '-', '×']}
        sol = _ms_build_solution(p)
    if sol is None:
        return None

    interior, row_ops, col_ops, row_res, col_res = sol
    n = p['n']
    equations, value_map = _ms_equations(n, interior, row_ops, col_ops, row_res, col_res)
    blanks = _ms_choose_blanks(equations, value_map, p)
    cells = _ms_to_cells(n, interior, row_ops, col_ops, row_res, col_res, blanks)
    return {'rows': 2 * n + 1, 'cols': 2 * n + 1, 'n': n,
            'eval': 'bodmas', 'difficulty': difficulty, 'cells': cells}


def empty_math_square(n):
    """Build a blank grid_data of size N for the manual editor (all numbers 0
    and given, all operators '+'); the creator fills in real values."""
    D = 2 * n + 1
    cells = [[{'t': 'blank'} for _ in range(D)] for _ in range(D)]
    for i in range(n):
        for j in range(n):
            cells[2 * i][2 * j] = {'t': 'num', 'v': 0, 'given': True}
    for i in range(n):
        for j in range(n - 1):
            cells[2 * i][2 * j + 1] = {'t': 'op', 'v': '+'}
        cells[2 * i][2 * n - 1] = {'t': 'eq'}
        cells[2 * i][2 * n] = {'t': 'num', 'v': 0, 'given': True}
    for j in range(n):
        for i in range(n - 1):
            cells[2 * i + 1][2 * j] = {'t': 'op', 'v': '+'}
        cells[2 * n - 1][2 * j] = {'t': 'eq'}
        cells[2 * n][2 * j] = {'t': 'num', 'v': 0, 'given': True}
    return {'rows': D, 'cols': D, 'n': n, 'eval': 'bodmas',
            'difficulty': 'easy', 'cells': cells}
