from django.db import models


class KoreanWord(models.Model):
    word        = models.CharField(max_length=30)
    clue_korean = models.TextField()
    clue_uzbek  = models.TextField()

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['word']


GRID_SIZE_CHOICES = [(s, f'{s} × {s}') for s in (10, 12, 13, 15, 17, 20)]


class CrosswordPuzzle(models.Model):
    title        = models.CharField(max_length=100)
    cover_image  = models.ImageField(upload_to='crossword/', null=True, blank=True)
    grid_size    = models.IntegerField(default=15, choices=GRID_SIZE_CHOICES,
                                       help_text='Working grid size — larger allows more words but creates a bigger puzzle.')
    words        = models.ManyToManyField(KoreanWord, blank=True)
    grid_data    = models.JSONField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
