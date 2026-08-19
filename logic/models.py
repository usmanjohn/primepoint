"""Logic Arena — sealed-answer logic puzzles.

The idea the whole app is built around: **you answer, but you don't find out
whether you were right until the reveal date.** A puzzle opens on a Wednesday,
everyone who wants to think about it submits an answer, and on the following
Wednesday the solution — and the wall of everyone who got it — appears at once.
That week of not knowing is the entire point; it is what makes a pupil check
their reasoning twice instead of guessing and reading the answer.

Three states, all derived from two datetimes, so nothing has to be switched on
by hand and no cron job is needed:

    upcoming   now < opens_at     teaser only, body hidden
    open       opens_at <= now < reveal_at    answers accepted, verdict sealed
    revealed   reveal_at <= now   solution public, verdict shown

A puzzle stays solvable forever after its reveal — the archive is the section's
real library — but a late solve is worth half, because the sealed week is the
part that costs courage. Correctness is computed and stored at submission time
either way; it is simply never *shown* until the reveal, and `prime.progress`
filters on the reveal date so a sealed correct answer cannot leak through the
points total on the progress page.

Puzzles are bilingual in the data itself (English + Uzbek columns), not through
gettext: their bodies are content, not interface. Figures are inline SVG in the
body — no uploads, nothing to make the page heavy.
"""
import re

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


# Points are per-puzzle, but a sensible default follows the difficulty so the
# importer rarely has to state one.
DIFFICULTY_POINTS = {1: 8, 2: 12, 3: 16, 4: 22, 5: 30}

# A puzzle solved after its solution went up is worth half: the reasoning is
# the same, the nerve is not.
LATE_FACTOR = 0.5


CATEGORIES = [
    {'code': 'weighing', 'name': _('Weighing'),     'emoji': '⚖️', 'color': '#f59e0b'},
    {'code': 'crossing', 'name': _('Crossing'),     'emoji': '\U0001F6F6', 'color': '#0ea5e9'},
    {'code': 'liars',    'name': _('Liars & Truth'),'emoji': '\U0001F921', 'color': '#a855f7'},
    {'code': 'cutting',  'name': _('Cut & Measure'),'emoji': '✂️', 'color': '#ef4444'},
    {'code': 'numbers',  'name': _('Numbers'),      'emoji': '\U0001F522', 'color': '#22c55e'},
    {'code': 'shapes',   'name': _('Shapes & Grids'),'emoji': '◻️', 'color': '#6366f1'},
    {'code': 'chance',   'name': _('Chance'),       'emoji': '\U0001F3B2', 'color': '#ec4899'},
    {'code': 'strategy', 'name': _('Strategy'),     'emoji': '♟️', 'color': '#14b8a6'},
]
CATEGORY_CHOICES = [(c['code'], c['name']) for c in CATEGORIES]
CATEGORY_MAP = {c['code']: c for c in CATEGORIES}


# Answers are short strings typed by a teenager on a phone, so comparison
# ignores case, spacing and the punctuation people sprinkle around a number.
# It deliberately does NOT ignore letters: "9" and "9 coins" both normalise to
# something containing the 9, and the accepted-answers list carries the rest.
_STRIP = re.compile(r'[\s.,;:!?\'"«»()\[\]\-–—_/]+')
_UZ_FOLD = str.maketrans({'ʻ': "'", 'ʼ': "'", '‘': "'", '’': "'", 'ʹ': "'"})


def normalise(text):
    """Lowercase, fold Uzbek apostrophes, drop spacing and punctuation."""
    return _STRIP.sub('', (text or '').strip().lower().translate(_UZ_FOLD))


def _as_number(text):
    """The value of an answer that is just a number, else None."""
    cleaned = (text or '').strip().replace(',', '.').replace(' ', '')
    try:
        return float(cleaned)
    except ValueError:
        return None


class LogicPuzzle(models.Model):
    """One logic problem, its sealed answer, and its dated reveal."""

    UPCOMING = 'upcoming'
    OPEN     = 'open'
    REVEALED = 'revealed'

    # ── identity ────────────────────────────────────────────────────────────
    title      = models.CharField(max_length=200, help_text='English title.')
    title_uz   = models.CharField(max_length=200, blank=True, help_text='Oʻzbekcha sarlavha.')
    slug       = models.SlugField(max_length=220, unique=True, blank=True)
    number     = models.PositiveIntegerField(default=0,
                                             help_text='Puzzle number shown on the card (#7).')
    category   = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='numbers')
    difficulty = models.PositiveSmallIntegerField(
        default=2, choices=[(i, '★' * i) for i in range(1, 6)])

    # ── the problem ─────────────────────────────────────────────────────────
    teaser     = models.CharField(max_length=300, blank=True,
                                  help_text='One-line hook shown on the card and while upcoming.')
    teaser_uz  = models.CharField(max_length=300, blank=True)
    body       = CKEditor5Field(config_name='extends',
                                help_text='The problem. Figures are inline SVG.')
    body_uz    = CKEditor5Field(config_name='extends', blank=True)
    hint       = models.TextField(blank=True, help_text='Optional nudge, hidden behind a toggle.')
    hint_uz    = models.TextField(blank=True)

    # ── the answer ──────────────────────────────────────────────────────────
    answer_key = models.CharField(max_length=200,
                                  help_text='The canonical short answer, e.g. "2" or "17".')
    accepted   = models.TextField(blank=True,
                                  help_text='Other spellings that count as correct, one per line.')
    answer_hint = models.CharField(max_length=160, blank=True,
                                   help_text='What shape of answer to type, e.g. "a number".')
    answer_hint_uz = models.CharField(max_length=160, blank=True)
    solution    = CKEditor5Field(config_name='extends',
                                 help_text='Full reasoning, revealed on the reveal date.')
    solution_uz = CKEditor5Field(config_name='extends', blank=True)

    # ── the schedule ────────────────────────────────────────────────────────
    opens_at   = models.DateTimeField(help_text='When the problem becomes readable and answerable.')
    reveal_at  = models.DateTimeField(help_text='When the solution and everyone’s verdict appear.')
    points     = models.PositiveSmallIntegerField(default=0,
                                                  help_text='0 = derive from difficulty.')

    author       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='logic_puzzles')
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-opens_at', '-number']
        indexes = [
            models.Index(fields=['is_published', 'opens_at']),
            models.Index(fields=['reveal_at']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'puzzle'
            slug, n = base, 1
            while LogicPuzzle.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        if not self.points:
            self.points = DIFFICULTY_POINTS.get(self.difficulty, 10)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'#{self.number} {self.title}'

    # ── bilingual display ───────────────────────────────────────────────────
    def _pick(self, base):
        """The Uzbek column when the interface is Uzbek, else the English one.

        Falls back to whichever column is filled, so a puzzle that only exists
        in one language still reads rather than rendering an empty page."""
        uz = getattr(self, f'{base}_uz', '')
        if (get_language() or 'en').startswith('uz'):
            return uz or getattr(self, base)
        return getattr(self, base) or uz

    @property
    def display_title(self):       return self._pick('title')

    @property
    def display_teaser(self):      return self._pick('teaser')

    @property
    def display_body(self):        return self._pick('body')

    @property
    def display_hint(self):        return self._pick('hint')

    @property
    def display_solution(self):    return self._pick('solution')

    @property
    def display_answer_hint(self): return self._pick('answer_hint')

    # ── category / difficulty chrome ────────────────────────────────────────
    @property
    def cat(self):
        return CATEGORY_MAP.get(self.category, CATEGORIES[0])

    @property
    def stars(self):
        return '★' * self.difficulty + '☆' * (5 - self.difficulty)

    # ── state ───────────────────────────────────────────────────────────────
    @property
    def state(self):
        now = timezone.now()
        if now < self.opens_at:
            return self.UPCOMING
        return self.OPEN if now < self.reveal_at else self.REVEALED

    @property
    def is_upcoming(self):  return self.state == self.UPCOMING

    @property
    def is_open(self):      return self.state == self.OPEN

    @property
    def is_revealed(self):  return self.state == self.REVEALED

    @property
    def days_left(self):
        """Whole days until the reveal — 0 means it lands today."""
        delta = self.reveal_at - timezone.now()
        return max(delta.days, 0) if delta.total_seconds() > 0 else 0

    @property
    def hours_left(self):
        delta = self.reveal_at - timezone.now()
        return max(int(delta.total_seconds() // 3600), 0)

    @property
    def days_to_open(self):
        delta = self.opens_at - timezone.now()
        return max(delta.days, 0) if delta.total_seconds() > 0 else 0

    # ── grading ─────────────────────────────────────────────────────────────
    @property
    def accepted_list(self):
        return [line for line in self.accepted.splitlines() if line.strip()]

    def accepts(self, answer):
        """Does this typed answer count as correct?

        Compares normalised text against the key and every accepted spelling,
        and — when both sides are plain numbers — compares them as numbers, so
        "17", "17 minutes" and "17.0" all land the same way."""
        given = normalise(answer)
        if not given:
            return False
        for candidate in [self.answer_key, *self.accepted_list]:
            if given == normalise(candidate):
                return True
            a, b = _as_number(answer), _as_number(candidate)
            if a is not None and b is not None and abs(a - b) < 1e-9:
                return True
        return False

    def award(self, sealed):
        """Points a correct answer earns: full if sealed, half if late."""
        return self.points if sealed else round(self.points * LATE_FACTOR, 1)

    # ── the wall ────────────────────────────────────────────────────────────
    def solvers(self, limit=30):
        """Everyone who got it, earliest first — only meaningful after reveal."""
        return (self.submissions.filter(is_correct=True)
                .select_related('user')
                .order_by('created_at')[:limit])

    def stats(self):
        """(answers, correct) — shown once the puzzle is revealed."""
        total = self.submissions.count()
        return total, self.submissions.filter(is_correct=True).count()


class LogicSubmission(models.Model):
    """One person's sealed answer to one puzzle.

    Unique per (user, puzzle): re-answering edits the same envelope rather than
    stacking attempts, which is what keeps the solver wall honest. `sealed`
    remembers whether the answer went in before the reveal, because that is
    what the points depend on — and it must be decided at submission time, not
    read off the clock later.
    """
    puzzle    = models.ForeignKey(LogicPuzzle, on_delete=models.CASCADE, related_name='submissions')
    user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logic_submissions')

    answer    = models.CharField(max_length=200)
    reasoning = models.TextField(blank=True,
                                 help_text='How they got there — optional, but the good part.')

    is_correct     = models.BooleanField(default=False)
    sealed         = models.BooleanField(default=True,
                                         help_text='Submitted before the reveal date.')
    points_awarded = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [('puzzle', 'user')]
        ordering = ['created_at']
        indexes = [models.Index(fields=['user', 'is_correct'])]

    def grade(self):
        """Re-derive correctness and points from the current answer."""
        self.is_correct = self.puzzle.accepts(self.answer)
        self.points_awarded = self.puzzle.award(self.sealed) if self.is_correct else 0

    def __str__(self):
        mark = '✓' if self.is_correct else '✗'
        return f'{self.user.username} → #{self.puzzle.number} {mark}'
