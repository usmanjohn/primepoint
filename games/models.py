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
