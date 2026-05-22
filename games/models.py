from django.db import models


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
