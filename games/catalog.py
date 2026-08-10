"""The catalogue of playable games, and how they map onto study subjects.

Every game used to be a hand-written card in `games_home.html`, with a
`GAME_COUNT = 12` constant next to a comment asking future editors to keep the
two in sync. This module is the single source of truth instead: the home page
renders from it, the nav badge counts it, and platform search reads it so games
turn up alongside lessons and practices.

`subjects` holds canonical slugs from `prime.subjects`, so a game can be filtered
by the same study-subject preference that filters the rest of the platform. A
game listing no subject at all is always visible (same rule as everywhere else).
`tag` is only a display label — it can be more specific than the subject, e.g.
Sorting Race is filed under Math but tagged "Algorithms".
"""
from django.utils.translation import gettext_lazy as _

GAMES = [
    {
        'slug': 'math-championship',
        'url': 'mathchamp_home',
        'name': _('Math Championship'),
        'description': _('15 questions, 3 rounds, 3 lives — climb from qualification to the final and win a medal!'),
        'emoji': '\U0001F3C6',
        'gradient': ('#f59e0b', '#b45309'),
        'badge': ('#fef3c7', '#b45309'),
        'subjects': ['math'],
        'tag': _('Math'),
    },
    {
        'slug': 'english-championship',
        'url': 'englishchamp_home',
        'name': _('English Championship'),
        'description': _('15 questions, 3 rounds, 3 lives — grammar and vocabulary from A1 to B1. Climb to the final and win a medal!'),
        'emoji': '\U0001F3C5',
        'gradient': ('#6366f1', '#3730a3'),
        'badge': ('#e0e7ff', '#3730a3'),
        'subjects': ['english'],
        'tag': _('English'),
    },
    {
        'slug': 'number-guess',
        'url': 'number_guess',
        'name': _('Number Guess'),
        'description': _('The system picks a secret number. Guess it with as few tries as possible!'),
        'emoji': '\U0001F522',
        'gradient': ('#3b82f6', '#1d4ed8'),
        'badge': ('#dbeafe', '#1d4ed8'),
        'subjects': ['math'],
        'tag': _('Math'),
    },
    {
        'slug': 'korean-crossword',
        'url': 'crossword_list',
        'name': _('Korean Crossword'),
        'description': _('Read the clue and fill in the Korean syllable blocks. Both Uzbek and Korean clues included!'),
        'emoji': '\U0001F9E9',
        'gradient': ('#7c3aed', '#4f46e5'),
        'badge': ('#ede9fe', '#6d28d9'),
        'subjects': ['korean'],
        'tag': _('Korean'),
    },
    {
        'slug': 'word-search',
        'url': 'wordsearch_list',
        'name': _('Word Search'),
        'description': _('Find hidden words across, down, and diagonally in the letter grid!'),
        'emoji': '\U0001F50D',
        'gradient': ('#059669', '#047857'),
        'badge': ('#d1fae5', '#065f46'),
        'subjects': ['english'],
        'tag': _('English'),
    },
    {
        'slug': 'english-crossword',
        'url': 'english_crossword_list',
        'name': _('English Crossword'),
        'description': _('Read the clue and fill in the English letters. Clues in English and Uzbek!'),
        'emoji': '\U0001F9E9',
        'gradient': ('#0369a1', '#0284c7'),
        'badge': ('#e0f2fe', '#0369a1'),
        'subjects': ['english'],
        'tag': _('English'),
    },
    {
        'slug': 'code-breaker',
        'url': 'codebreaker_list',
        'name': _('Code Breaker'),
        'description': _('Solve math problems to decode the secret word letter by letter!'),
        'emoji': '\U0001F510',
        'gradient': ('#1f6feb', '#0d419d'),
        'badge': ('#dbeafe', '#1d4ed8'),
        'subjects': ['math'],
        'tag': _('Math'),
    },
    {
        'slug': 'math-square',
        'url': 'mathsquare_list',
        'name': _('Math Square'),
        'description': _('Fill the empty squares so every row and column adds up to a true equation!'),
        'emoji': '\U0001F9EE',
        'gradient': ('#0d9488', '#0f766e'),
        'badge': ('#ccfbf1', '#0f766e'),
        'subjects': ['math'],
        'tag': _('Math'),
    },
    {
        'slug': 'prime-climb',
        'url': 'primeclimb_list',
        'name': _('Prime Climb Grid'),
        'description': _('Find primes, squares, or multiples on the 1–100 grid. Learn number theory visually!'),
        'emoji': '\U0001F522',
        'gradient': ('#2ea043', '#196c2e'),
        'badge': ('#d1fae5', '#065f46'),
        'subjects': ['math'],
        'tag': _('Math'),
    },
    {
        # Packs carry a language field (en / ko / uz / mixed), so this belongs to
        # both language subjects rather than to one.
        'slug': 'odd-one-out',
        'url': 'oddoneout_list',
        'name': _('Odd One Out'),
        'description': _('Three words belong together — one does not. Spot the odd one out!'),
        'emoji': '\U0001F9E0',
        'gradient': ('#0891b2', '#0e7490'),
        'badge': ('#cffafe', '#0e7490'),
        'subjects': ['english', 'korean'],
        'tag': _('Grammar'),
    },
    {
        'slug': 'word-order',
        'url': 'wordorder_list',
        'name': _('Word Order Chaos'),
        'description': _('Drag and drop shuffled word tiles to rebuild the correct sentence!'),
        'emoji': '\U0001F4DD',
        'gradient': ('#7c3aed', '#4f46e5'),
        'badge': ('#ede9fe', '#6d28d9'),
        'subjects': ['english', 'korean'],
        'tag': _('Language'),
    },
    {
        'slug': 'sorting-race',
        'url': 'sortingrace_list',
        'name': _('Sorting Race'),
        'description': _('Swap elements to sort a tricky mix of fractions, roots, and negatives — smallest to largest!'),
        'emoji': '\U0001F500',
        'gradient': ('#f97316', '#c2410c'),
        'badge': ('#ffedd5', '#c2410c'),
        'subjects': ['math'],
        'tag': _('Algorithms'),
    },
    {
        'slug': 'target-number',
        'url': 'target_number',
        'name': _('Target Number'),
        'description': _('Combine 6 numbers with +, −, ×, ÷ to hit the target. Three difficulty levels!'),
        'emoji': '\U0001F3AF',
        'gradient': ('#d97706', '#92400e'),
        'badge': ('#fef3c7', '#92400e'),
        'subjects': ['math'],
        'tag': _('Math'),
    },
]

GAME_COUNT = len(GAMES)


def subject_facets():
    """Canonical subjects that actually have games, in registry order.

    Returns dicts carrying the subject's own slug/name/icon so the filter pills
    look like the rest of the platform without games restating that metadata.
    """
    from prime.subjects import SUBJECTS

    counts = {}
    for game in GAMES:
        for slug in game['subjects']:
            counts[slug] = counts.get(slug, 0) + 1

    return [
        dict(subject, count=counts[subject['slug']])
        for subject in SUBJECTS
        if subject['slug'] in counts
    ]


def filter_games(subject=None, slugs=None):
    """Games for an explicit `subject`, else narrowed to the visitor's `slugs`.

    A game claiming no subject is always shown — the same rule the libraries use,
    so general-purpose games never disappear behind a study-subject preference.
    """
    games = GAMES
    if subject:
        games = [g for g in games if subject in g['subjects']]
    elif slugs:
        games = [g for g in games if not g['subjects'] or set(g['subjects']) & set(slugs)]
    return games


def search_games(query):
    """Games whose name, description or tag matches — for platform search."""
    q = query.casefold()
    return [
        g for g in GAMES
        if q in str(g['name']).casefold()
        or q in str(g['description']).casefold()
        or q in str(g['tag']).casefold()
    ]
