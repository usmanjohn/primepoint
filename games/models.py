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
