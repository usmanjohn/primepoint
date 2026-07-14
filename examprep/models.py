from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


SKILL_CHOICES = [
    ('reading',   _('Reading')),
    ('writing',   _('Writing')),
    ('listening', _('Listening')),
    ('speaking',  _('Speaking')),
    ('vocab',     _('Vocabulary')),
    ('strategy',  _('Strategy')),
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


class Topic(models.Model):
    """A question type / theme inside a track + skill — e.g. TOPIK Reading →
    'Advertisements (광고)'. Lessons hang off a topic so the skill page can show
    tidy cards instead of one long lesson list."""
    track        = models.ForeignKey(ExamTrack, on_delete=models.CASCADE, related_name='topics')
    skill        = models.CharField(max_length=20, choices=SKILL_CHOICES, default='reading')
    title        = models.CharField(max_length=200)
    slug         = models.SlugField(max_length=220, blank=True)
    summary      = models.CharField(max_length=300, blank=True,
                                    help_text='Short description shown on the topic card.')
    icon         = models.CharField(max_length=50, default='bi-collection',
                                    help_text='Bootstrap-icons class, e.g. bi-megaphone.')
    order        = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']
        unique_together = ['track', 'skill', 'slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'topic'
            slug, n = base, 1
            while Topic.objects.filter(track=self.track, skill=self.skill,
                                       slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.track.name} / {self.get_skill_display()} — {self.title}'


class Lesson(models.Model):
    """A single interactive lesson made of ordered content blocks."""
    track        = models.ForeignKey(ExamTrack, on_delete=models.CASCADE, related_name='lessons')
    skill        = models.CharField(max_length=20, choices=SKILL_CHOICES, default='reading')
    topic        = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='lessons',
                                     help_text='Optional question-type group inside the skill.')
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

    Every field is optional, so a single block can hold any mix of: an image
    (with caption), explanatory rich text, and — if you add choices — a
    multiple-choice question with an explanation. The template renders whatever
    is filled in, in this order: image → text → question → explanation. No block
    "type" to set; just fill the parts you want.
    """
    lesson      = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='blocks')
    order       = models.PositiveIntegerField(default=0)
    image       = models.ImageField(upload_to='examprep/blocks/', blank=True, null=True,
                                    help_text='Optional image / book screenshot, shown at the top of the block.')
    caption     = models.CharField(max_length=300, blank=True,
                                   help_text='Optional caption under the image.')
    rich_text   = CKEditor5Field(config_name='tutorial', blank=True, null=True,
                                 help_text='Explanation text, or the question prompt if this block has choices.')
    explanation = CKEditor5Field(blank=True, null=True,
                                 help_text='Shown after the student answers. Only used when the block has choices.')

    class Meta:
        ordering = ['order', 'id']

    @property
    def is_question(self):
        return self.choices.exists()

    def __str__(self):
        return f'{self.lesson.title} — block #{self.order}'


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
