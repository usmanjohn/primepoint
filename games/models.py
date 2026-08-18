from django.db import models
from django.contrib.auth.models import User


class CrosswordPuzzle(models.Model):
    title        = models.CharField(max_length=100)
    cover_image  = models.ImageField(upload_to='crossword/', null=True, blank=True)
    grid_rows    = models.IntegerField(default=10, help_text='Height of the grid (1–20).')
    grid_cols    = models.IntegerField(default=8,  help_text='Width of the grid (1–10).')
    grid_data    = models.JSONField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class CodeBreakerPuzzle(models.Model):
    DIFFICULTY_EASY   = 'easy'
    DIFFICULTY_MEDIUM = 'medium'
    DIFFICULTY_HARD   = 'hard'
    DIFFICULTY_CHOICES = [
        (DIFFICULTY_EASY,   'Easy'),
        (DIFFICULTY_MEDIUM, 'Medium'),
        (DIFFICULTY_HARD,   'Hard'),
    ]

    title       = models.CharField(max_length=200)
    secret_word = models.CharField(max_length=100)
    hint        = models.TextField(blank=True)
    difficulty  = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default=DIFFICULTY_EASY)
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='codebreaker_puzzles')
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.get_difficulty_display()})'

    class Meta:
        ordering = ['-created_at']


class CodeBreakerClue(models.Model):
    puzzle          = models.ForeignKey(CodeBreakerPuzzle, on_delete=models.CASCADE, related_name='clues')
    letter_index    = models.PositiveSmallIntegerField()
    letter          = models.CharField(max_length=1)
    math_expression = models.CharField(max_length=300)
    answer          = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'[{self.puzzle}] pos {self.letter_index}: {self.letter} = {self.math_expression}'

    class Meta:
        ordering = ['letter_index']


class OddOneOutPack(models.Model):
    LANG_EN  = 'en'
    LANG_KO  = 'ko'
    LANG_UZ  = 'uz'
    LANG_ANY = 'any'
    LANGUAGE_CHOICES = [
        (LANG_EN,  'English'),
        (LANG_KO,  'Korean'),
        (LANG_UZ,  'Uzbek'),
        (LANG_ANY, 'Mixed'),
    ]

    title       = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    language    = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default=LANG_ANY)
    created_by  = models.ForeignKey(User, on_delete=models.CASCADE, related_name='oddoneout_packs')
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    def question_count(self):
        return self.questions.count()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class OddOneOutQuestion(models.Model):
    pack        = models.ForeignKey(OddOneOutPack, on_delete=models.CASCADE, related_name='questions')
    word_1      = models.CharField(max_length=120)
    word_2      = models.CharField(max_length=120)
    word_3      = models.CharField(max_length=120)
    word_4      = models.CharField(max_length=120)
    odd_index   = models.PositiveSmallIntegerField(help_text='0-based index of the odd word (0=word_1, 1=word_2, …)')
    explanation = models.CharField(max_length=400, blank=True)
    order       = models.PositiveSmallIntegerField(default=0)

    def words_list(self):
        return [self.word_1, self.word_2, self.word_3, self.word_4]

    def __str__(self):
        return f'[{self.pack}] {self.word_1} / {self.word_2} / {self.word_3} / {self.word_4}'

    class Meta:
        ordering = ['order', 'pk']


class WordOrderChallenge(models.Model):
    LANG_EN  = 'en'
    LANG_KO  = 'ko'
    LANG_UZ  = 'uz'
    LANGUAGE_CHOICES = [
        (LANG_EN, 'English'),
        (LANG_KO, 'Korean'),
        (LANG_UZ, 'Uzbek'),
    ]

    EASY   = 'easy'
    MEDIUM = 'medium'
    HARD   = 'hard'
    DIFFICULTY_CHOICES = [
        (EASY,   'Easy'),
        (MEDIUM, 'Medium'),
        (HARD,   'Hard'),
    ]

    title      = models.CharField(max_length=200)
    sentence   = models.CharField(max_length=500)
    hint       = models.TextField(blank=True)
    language   = models.CharField(max_length=10, choices=LANGUAGE_CHOICES, default=LANG_EN)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default=EASY)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wordorder_challenges')
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def word_count(self):
        return len(self.sentence.split())

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['language', 'difficulty', 'pk']


class WordSearchPuzzle(models.Model):
    title      = models.CharField(max_length=100)
    word_list  = models.TextField(help_text='One word per line (English letters only).')
    grid_size  = models.IntegerField(default=15, help_text='Grid width/height (10–20).')
    grid_data  = models.JSONField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Word Search Puzzle'
        verbose_name_plural = 'Word Search Puzzles'


class EnglishCrossword(models.Model):
    title        = models.CharField(max_length=100)
    cover_image  = models.ImageField(upload_to='crossword_en/', null=True, blank=True)
    grid_rows    = models.IntegerField(default=15, help_text='Height of the grid (1–25).')
    grid_cols    = models.IntegerField(default=15, help_text='Width of the grid (1–25).')
    grid_data    = models.JSONField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'English Crossword'
        verbose_name_plural = 'English Crosswords'


class SortingRaceChallenge(models.Model):
    EASY   = 'easy'
    MEDIUM = 'medium'
    HARD   = 'hard'
    DIFFICULTY_CHOICES = [
        (EASY,   'Easy'),
        (MEDIUM, 'Medium'),
        (HARD,   'Hard'),
    ]

    title      = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default=EASY)
    hint       = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sortingrace_challenges')
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.get_difficulty_display()})'

    class Meta:
        ordering = ['-created_at']


class PrimeClimbChallenge(models.Model):
    PRIMES    = 'primes'
    SQUARES   = 'squares'
    MULTIPLES = 'multiples'
    MODE_CHOICES = [
        (PRIMES,    'Primes'),
        (SQUARES,   'Perfect Squares'),
        (MULTIPLES, 'Multiples of N'),
    ]

    title      = models.CharField(max_length=200)
    mode       = models.CharField(max_length=20, choices=MODE_CHOICES)
    target     = models.IntegerField(null=True, blank=True)
    hint       = models.TextField(blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='primeclimb_challenges')
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        label = f' of {self.target}' if self.mode == self.MULTIPLES and self.target else ''
        return f'{self.title} ({self.get_mode_display()}{label})'

    class Meta:
        ordering = ['-created_at']


class MathChampResult(models.Model):
    """One finished (or eliminated) run of the Math Championship quiz."""
    GRADE_CHOICES = [(5, '5-sinf'), (6, '6-sinf'), (7, '7-sinf')]
    MEDAL_GOLD   = 'gold'
    MEDAL_SILVER = 'silver'
    MEDAL_BRONZE = 'bronze'
    MEDAL_CHOICES = [
        (MEDAL_GOLD,   'Gold'),
        (MEDAL_SILVER, 'Silver'),
        (MEDAL_BRONZE, 'Bronze'),
        ('',           'None'),
    ]

    user          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mathchamp_results')
    grade         = models.PositiveSmallIntegerField(choices=GRADE_CHOICES, default=5)
    score         = models.IntegerField(default=0)
    stage_reached = models.PositiveSmallIntegerField(default=1)
    finished      = models.BooleanField(default=False)
    hearts_left   = models.PositiveSmallIntegerField(default=0)
    best_streak   = models.PositiveSmallIntegerField(default=0)
    elapsed       = models.PositiveIntegerField(default=0, help_text='Seconds from start to finish.')
    medal         = models.CharField(max_length=10, choices=MEDAL_CHOICES, blank=True, default='')
    created_at    = models.DateTimeField(auto_now_add=True)

    MEDAL_EMOJI = {MEDAL_GOLD: '🥇', MEDAL_SILVER: '🥈', MEDAL_BRONZE: '🥉'}

    @property
    def medal_emoji(self):
        return self.MEDAL_EMOJI.get(self.medal, '')

    @property
    def elapsed_display(self):
        return f'{self.elapsed // 60}:{self.elapsed % 60:02d}'

    def __str__(self):
        return f'{self.user.username} — {self.grade}-sinf, {self.score} ball'

    class Meta:
        ordering = ['-score', 'elapsed']


class EnglishChampResult(models.Model):
    """One finished (or eliminated) run of the English Championship quiz.
    The English twin of MathChampResult — same shape, but the three tracks are
    CEFR levels instead of school grades."""
    LEVEL_A1 = 'a1'
    LEVEL_A2 = 'a2'
    LEVEL_B1 = 'b1'
    LEVEL_CHOICES = [
        (LEVEL_A1, 'A1 — Beginner'),
        (LEVEL_A2, 'A2 — Elementary'),
        (LEVEL_B1, 'B1 — Intermediate'),
    ]
    MEDAL_GOLD   = 'gold'
    MEDAL_SILVER = 'silver'
    MEDAL_BRONZE = 'bronze'
    MEDAL_CHOICES = [
        (MEDAL_GOLD,   'Gold'),
        (MEDAL_SILVER, 'Silver'),
        (MEDAL_BRONZE, 'Bronze'),
        ('',           'None'),
    ]

    user          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='englishchamp_results')
    level         = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=LEVEL_A1)
    score         = models.IntegerField(default=0)
    stage_reached = models.PositiveSmallIntegerField(default=1)
    finished      = models.BooleanField(default=False)
    hearts_left   = models.PositiveSmallIntegerField(default=0)
    best_streak   = models.PositiveSmallIntegerField(default=0)
    elapsed       = models.PositiveIntegerField(default=0, help_text='Seconds from start to finish.')
    medal         = models.CharField(max_length=10, choices=MEDAL_CHOICES, blank=True, default='')
    created_at    = models.DateTimeField(auto_now_add=True)

    MEDAL_EMOJI = {MEDAL_GOLD: '🥇', MEDAL_SILVER: '🥈', MEDAL_BRONZE: '🥉'}

    @property
    def medal_emoji(self):
        return self.MEDAL_EMOJI.get(self.medal, '')

    @property
    def elapsed_display(self):
        return f'{self.elapsed // 60}:{self.elapsed % 60:02d}'

    def __str__(self):
        return f'{self.user.username} — {self.get_level_display()}, {self.score} ball'

    class Meta:
        ordering = ['-score', 'elapsed']


class DuelResult(models.Model):
    """One finished Chempionlar Dueli match — either two teams against each
    other (`duel`) or two pupils playing as one team (`together`)."""
    MODE_DUEL     = 'duel'
    MODE_TOGETHER = 'together'
    MODE_CHOICES  = [(MODE_DUEL, 'Duel'), (MODE_TOGETHER, 'Together')]

    SUBJECT_CHOICES = [('math', 'Matematika'), ('english', 'Ingliz tili'),
                       ('both', 'Ikkalasi ham')]
    WINNER_CHOICES  = [('a', 'A'), ('b', 'B'), ('', 'Draw / co-op')]

    mode       = models.CharField(max_length=10, choices=MODE_CHOICES, default=MODE_DUEL)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,
                                   related_name='duel_results')

    name_a     = models.CharField(max_length=40)
    name_b     = models.CharField(max_length=40)
    subject_a  = models.CharField(max_length=10, choices=SUBJECT_CHOICES, blank=True,
                                  help_text='Together mode: what this pupil studies.')
    subject_b  = models.CharField(max_length=10, choices=SUBJECT_CHOICES, blank=True)

    grade      = models.PositiveSmallIntegerField(default=5, help_text='Math difficulty (5-7).')
    level      = models.CharField(max_length=2, default='a1', help_text='English level (a1/a2/b1).')
    limit_math    = models.PositiveSmallIntegerField(default=0, help_text='Seconds per math question; 0 = no limit.')
    limit_english = models.PositiveSmallIntegerField(default=0, help_text='Seconds per English question; 0 = no limit.')

    score_a    = models.IntegerField(default=0)
    score_b    = models.IntegerField(default=0)
    hearts_a   = models.PositiveSmallIntegerField(default=0)
    hearts_b   = models.PositiveSmallIntegerField(default=0)
    stages_done = models.PositiveSmallIntegerField(default=0)
    finished   = models.BooleanField(default=False)
    winner     = models.CharField(max_length=1, choices=WINNER_CHOICES, blank=True, default='')
    elapsed    = models.PositiveIntegerField(default=0, help_text='Seconds from start to finish.')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_score(self):
        """Together mode keeps the shared score in score_a."""
        return self.score_a if self.mode == self.MODE_TOGETHER else self.score_a + self.score_b

    @property
    def winner_name(self):
        if self.mode == self.MODE_TOGETHER:
            return f'{self.name_a} + {self.name_b}'
        return {'a': self.name_a, 'b': self.name_b}.get(self.winner, 'Durrang')

    @property
    def elapsed_display(self):
        return f'{self.elapsed // 60}:{self.elapsed % 60:02d}'

    def __str__(self):
        if self.mode == self.MODE_TOGETHER:
            return f'{self.name_a} + {self.name_b} — {self.score_a} ball'
        return f'{self.name_a} {self.score_a} : {self.score_b} {self.name_b}'

    class Meta:
        ordering = ['-created_at']


class MathSquarePuzzle(models.Model):
    """A crossed math square: every row and every column forms an arithmetic
    equation, and the solver fills the empty number cells so all equations are
    true. The full grid (cell types, operators, solution values, which numbers
    are blank) is stored in ``grid_data`` — see games/views.py for the schema."""
    DIFFICULTY_EASY   = 'easy'
    DIFFICULTY_MEDIUM = 'medium'
    DIFFICULTY_HARD   = 'hard'
    DIFFICULTY_ULTRA  = 'ultra'
    DIFFICULTY_CHOICES = [
        (DIFFICULTY_EASY,   'Easy'),
        (DIFFICULTY_MEDIUM, 'Medium'),
        (DIFFICULTY_HARD,   'Hard'),
        (DIFFICULTY_ULTRA,  'Ultra-hard'),
    ]

    title        = models.CharField(max_length=200)
    difficulty   = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default=DIFFICULTY_EASY)
    size         = models.IntegerField(default=2, help_text='Numbers per row/column (N): 2–5.')
    grid_data    = models.JSONField(null=True, blank=True)
    created_by   = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mathsquare_puzzles')
    is_published = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.get_difficulty_display()})'

    class Meta:
        ordering = ['-created_at']


# ---------------------------------------------------------------------------
# Prime Journey
# ---------------------------------------------------------------------------
# The travelling adventure built on the Prime courses. The rules live in
# `games/journey.py`; these four models are only what has to outlive a request.
#
# A guest's whole journey lives in the session, exactly like the championships.
# A logged-in traveller gets a JourneyRun row instead, because the game's core
# loop *depends* on being able to walk away: running out of strength pauses the
# journey rather than ending it, and the fastest way to resume is to go and
# finish a lesson. That only works if the road is still there tomorrow.


class JourneyRun(models.Model):
    """One traveller's journey along one leg of one road."""
    STATUS_TRAVELLING = 'travelling'
    STATUS_STOPPED    = 'stopped'      # out of hearts, one reprieve still unspent
    STATUS_FINISHED   = 'finished'
    STATUS_FAILED     = 'failed'       # out of hearts for good; the stage is lost
    STATUS_ABANDONED  = 'abandoned'
    STATUS_CHOICES = [
        (STATUS_TRAVELLING, 'Travelling'),
        (STATUS_STOPPED,    'Stopped'),
        (STATUS_FINISHED,   'Finished'),
        (STATUS_FAILED,     'Failed'),
        (STATUS_ABANDONED,  'Abandoned'),
    ]

    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journey_runs')
    road       = models.CharField(max_length=20)
    leg        = models.PositiveSmallIntegerField(default=1)
    seed       = models.BigIntegerField(default=0)

    # The whole journey — map, position, strength, diary. See journey.new_state().
    state      = models.JSONField(default=dict, blank=True)

    status     = models.CharField(max_length=12, choices=STATUS_CHOICES, default=STATUS_TRAVELLING)
    coins      = models.IntegerField(default=0)
    kuch_left  = models.PositiveSmallIntegerField(default=0)
    detours    = models.PositiveSmallIntegerField(default=0)
    elapsed    = models.PositiveIntegerField(default=0, help_text='Seconds from setting out to arriving.')

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-updated_at']
        indexes  = [
            models.Index(fields=['user', 'status']),
            models.Index(fields=['road', 'leg', '-coins']),
        ]

    @property
    def is_open(self):
        return self.status in (self.STATUS_TRAVELLING, self.STATUS_STOPPED)

    @property
    def elapsed_display(self):
        return f'{self.elapsed // 60}:{self.elapsed % 60:02d}'

    def __str__(self):
        return f'{self.user.username} — {self.road} {self.leg}-leg ({self.status})'


class JourneySeenQuestion(models.Model):
    """A question this traveller has already met on the road.

    The point of the game is that coming back after studying gets you a
    *different* question, so nothing is ever solved by memorising an answer.
    Twenty questions per lesson gives plenty of headroom.
    """
    user       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journey_seen')
    question   = models.ForeignKey('practice.PracticeQuestion', on_delete=models.CASCADE,
                                   related_name='journey_sightings')
    seen_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('user', 'question')]
        indexes = [models.Index(fields=['user', 'question'])]

    def __str__(self):
        return f'{self.user.username} saw Q{self.question_id}'


class JourneyReward(models.Model):
    """The teacher's prize catalogue — the real pens, notebooks and books.

    A chest on the road hands out one of these, and the pupil redeems it in the
    classroom. Edited in admin; `stock` is what is physically on the shelf, so
    a prize stops appearing once it runs out.
    """
    RARITY_COMMON    = 'common'
    RARITY_RARE      = 'rare'
    RARITY_LEGENDARY = 'legendary'
    RARITY_CHOICES = [
        (RARITY_COMMON,    'Common'),
        (RARITY_RARE,      'Rare'),
        (RARITY_LEGENDARY, 'Legendary'),
    ]

    name        = models.CharField(max_length=120)
    emoji       = models.CharField(max_length=8, blank=True, default='\U0001F381')
    description = models.CharField(max_length=300, blank=True)
    rarity      = models.CharField(max_length=12, choices=RARITY_CHOICES, default=RARITY_COMMON)
    stock       = models.PositiveIntegerField(default=0, help_text='0 = unlimited.')
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['rarity', 'name']

    def __str__(self):
        return f'{self.emoji} {self.name}'


class JourneyPrize(models.Model):
    """A prize a traveller actually won, waiting to be handed over in real life."""
    user        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='journey_prizes')
    reward      = models.ForeignKey(JourneyReward, on_delete=models.CASCADE, related_name='prizes')
    run         = models.ForeignKey(JourneyRun, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='prizes')

    # Carried from the chest (banked at once, but it costs strength to carry) or
    # left on the road and collected — doubled — at the destination.
    carried     = models.BooleanField(default=True)
    won_at      = models.DateTimeField(auto_now_add=True)

    handed_over = models.BooleanField(default=False)
    handed_at   = models.DateTimeField(null=True, blank=True)
    handed_by   = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='journey_prizes_handed')

    class Meta:
        ordering = ['handed_over', '-won_at']

    def __str__(self):
        return f'{self.user.username} won {self.reward.name}'
