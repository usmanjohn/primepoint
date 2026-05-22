from django.db import models


class KoreanWord(models.Model):
    word        = models.CharField(max_length=30)
    clue_korean = models.TextField()
    clue_uzbek  = models.TextField()

    def __str__(self):
        return self.word

    class Meta:
        ordering = ['word']


class CrosswordPuzzle(models.Model):
    title        = models.CharField(max_length=100)
    words        = models.ManyToManyField(KoreanWord, blank=True)
    grid_data    = models.JSONField(null=True, blank=True)
    is_published = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
