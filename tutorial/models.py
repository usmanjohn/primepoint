from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from django.utils.html import strip_tags


CATEGORY_CHOICES = [
    ('math',        'Mathematics'),
    ('science',     'Science'),
    ('programming', 'Programming'),
    ('language',    'Language'),
    ('history',     'History'),
    ('other',       'Other'),
]

CATEGORY_ICONS = {
    'math':        'bi-calculator',
    'science':     'bi-flask',
    'programming': 'bi-code-slash',
    'language':    'bi-translate',
    'history':     'bi-hourglass-split',
    'other':       'bi-lightbulb',
}


class Tutorial(models.Model):
    title        = models.CharField(max_length=200)
    slug         = models.SlugField(max_length=220, blank=True)
    author       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutorials')
    category     = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    thumbnail    = models.ImageField(upload_to='tutorials/thumbnails/', blank=True, null=True)
    summary      = models.CharField(
        max_length=300, blank=True,
        help_text='Short description shown on listing cards.'
    )
    content      = CKEditor5Field(config_name='tutorial')
    is_published = models.BooleanField(default=True)
    views        = models.PositiveIntegerField(default=0)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'tutorial'
            slug, n = base, 1
            while Tutorial.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    @property
    def category_icon(self):
        return CATEGORY_ICONS.get(self.category, 'bi-lightbulb')

    @property
    def read_time(self):
        words = len(strip_tags(str(self.content)).split())
        return max(1, round(words / 200))


class TutorialReaction(models.Model):
    LIKE    = 'like'
    DISLIKE = 'dislike'
    CHOICES = [(LIKE, 'Like'), (DISLIKE, 'Dislike')]

    user     = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutorial_reactions')
    tutorial = models.ForeignKey(Tutorial, on_delete=models.CASCADE, related_name='reactions')
    reaction = models.CharField(max_length=10, choices=CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('user', 'tutorial')]

    def __str__(self):
        return f'{self.user} {self.reaction}s "{self.tutorial}"'
