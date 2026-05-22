"""
Korean crossword generator.

Each grid cell holds one Korean syllable block (가, 나, 일, 본 …).
Words intersect when they share the exact same syllable at the same cell,
and the two words must be perpendicular (one across, one down).
"""
import random

GRID_SIZE = 21


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

    # Bounds check
    if end_r >= rows or end_c >= cols:
        return False

    # Cell immediately before the start must be empty
    br, bc = row - dr, col - dc
    if 0 <= br < rows and 0 <= bc < cols and syl[br][bc] is not None:
        return False

    # Cell immediately after the end must be empty
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
                return False  # Syllable conflict
            if direction in cell_dirs:
                return False  # Same-direction word already here — would merge
            # Perpendicular intersection — valid
            has_intersection = True
        else:
            # Empty cell: no parallel neighbour allowed
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

                # Try across — only if cell is NOT already part of an across word
                if 'across' not in cell_dirs:
                    start_c = c - idx
                    if start_c >= 0 and start_c + length <= cols:
                        if _valid(syl, dirs, syllables, r, start_c, 'across', rows, cols):
                            results.add((r, start_c, 'across'))

                # Try down — only if cell is NOT already part of a down word
                if 'down' not in cell_dirs:
                    start_r = r - idx
                    if start_r >= 0 and start_r + length <= rows:
                        if _valid(syl, dirs, syllables, start_r, c, 'down', rows, cols):
                            results.add((start_r, c, 'down'))

    return list(results)


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


# ── Main entry point ──────────────────────────────────────────────────────────

def generate_crossword(word_objects, max_attempts=50):
    """
    Generate a crossword from a queryset/list of KoreanWord objects.
    Returns a dict with keys: rows, cols, cells, words — or None on failure.
    """
    words = list(word_objects)
    if not words:
        return None

    # Score each word by how many others share at least one syllable
    def connectivity(wo):
        syls = set(wo.word)
        return sum(1 for other in words if other.pk != wo.pk and syls & set(other.word))

    scored = sorted(words, key=connectivity, reverse=True)
    n_first = min(len(scored), 10)  # try top-10 most connected words as first word

    best_placed = []
    best_grid = None

    for attempt in range(max_attempts):
        first = scored[attempt % n_first]
        rest  = [w for w in scored if w.pk != first.pk]

        # Shuffle the bottom half for variety; keep top half in order
        split = len(rest) // 2
        bottom = rest[split:]
        random.shuffle(bottom)
        rest = rest[:split] + bottom

        rows = cols = GRID_SIZE
        syl  = _empty_syl(rows, cols)
        dirs = _empty_dir(rows, cols)
        placed = []

        # First word: horizontally centred
        r0 = rows // 2
        c0 = (cols - len(first.word)) // 2
        _place_word(syl, dirs, first.word, r0, c0, 'across')
        placed.append((first, r0, c0, 'across'))

        for wo in rest:
            cands = _candidates(syl, dirs, wo.word, rows, cols)
            if not cands:
                continue
            random.shuffle(cands)
            r, c, direction = cands[0]
            _place_word(syl, dirs, wo.word, r, c, direction)
            placed.append((wo, r, c, direction))

        if len(placed) > len(best_placed):
            best_placed = placed
            best_grid   = syl

    if not best_placed:
        return None

    # Crop to tight bounds
    cropped, row_off, col_off = _crop(best_grid, GRID_SIZE, GRID_SIZE)
    final_rows = len(cropped)
    final_cols = len(cropped[0]) if cropped else 0

    # Adjust word positions for crop offset and build number map
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
