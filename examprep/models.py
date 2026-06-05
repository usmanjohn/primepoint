from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


SKILL_CHOICES = [
    ('reading',   'Reading'),
    ('writing',   'Writing'),
    ('listening', 'Listening'),
    ('speaking',  'Speaking'),
    ('vocab',     'Vocabulary'),
    ('strategy',  'Strategy'),
]

SKILL_ICONS = {
    'reading':   'bi-book',
    'writing':   'bi-pencil-square',
    'listening': 'bi-headphones',
    'speaking':  'bi-mic',
    'vocab':     'bi-translate',
    'strategy':  'bi-lightbulb',
}


class ExamTrack(models.Model):
    """An exam family students prepare for — IELTS, TOPIK, GMAT, SAT, ..."""
    name         = models.CharField(max_length=120)
    slug         = models.SlugField(max_length=140, blank=True, unique=True)
    summary      = models.CharField(max_length=300, blank=True,
                                    help_text='Short description shown on the track card.')
    icon         = models.CharField(max_length=50, default='bi-mortarboard',
                                    help_text='Bootstrap-icons class, e.g. bi-mortarboard.')
    color        = models.CharField(max_length=7, default='#6366f1',
                                    help_text='Hex color for card accent, e.g. #6366f1')
    order        = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name) or 'track'
            slug, n = base, 1
            while ExamTrack.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """A single interactive lesson made of ordered content blocks."""
    track        = models.ForeignKey(ExamTrack, on_delete=models.CASCADE, related_name='lessons')
    skill        = models.CharField(max_length=20, choices=SKILL_CHOICES, default='reading')
    title        = models.CharField(max_length=200)
    slug         = models.SlugField(max_length=220, blank=True)
    summary      = models.CharField(max_length=300, blank=True,
                                    help_text='Short description shown on listing cards.')
    thumbnail    = models.ImageField(upload_to='examprep/thumbs/', blank=True, null=True)
    author       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='examprep_lessons')
    order        = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    views        = models.PositiveIntegerField(default=0)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_at']
        unique_together = ['track', 'slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'lesson'
            slug, n = base, 1
            while Lesson.objects.filter(track=self.track, slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.track.name} — {self.title}'

    @property
    def skill_icon(self):
        return SKILL_ICONS.get(self.skill, 'bi-journal-text')


class LessonBlock(models.Model):
    """One ordered content block inside a lesson.

    Fields are type-driven and nullable so new block types (writing template,
    keyword glossary, tip callout) can be added later by extending BLOCK_TYPES,
    with no schema redesign.
    """
    BLOCK_TYPES = [
        ('text',  'Explanation'),
        ('image', 'Image / screenshot'),
        ('mcq',   'Multiple choice'),
    ]
    lesson      = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='blocks')
    block_type  = models.CharField(max_length=20, choices=BLOCK_TYPES, default='text')
    order       = models.PositiveIntegerField(default=0)
    rich_text   = CKEditor5Field(config_name='tutorial', blank=True, null=True,
                                 help_text='Body text, or the question prompt for MCQ blocks.')
    image       = models.ImageField(upload_to='examprep/blocks/', blank=True, null=True)
    caption     = models.CharField(max_length=300, blank=True)
    explanation = CKEditor5Field(blank=True, null=True,
                                 help_text='Shown after the student submits an MCQ answer.')

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.lesson.title} — {self.get_block_type_display()} #{self.order}'


class BlockChoice(models.Model):
    """An MCQ option — only used when its block_type is 'mcq'."""
    block      = models.ForeignKey(LessonBlock, on_delete=models.CASCADE, related_name='choices')
    text       = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)
    order      = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.text[:60]
