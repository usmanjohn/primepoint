import re

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


STORY_POINTS = 5

# Inline vocab convention: <span class="cn-word" data-tr="uzbek translation">한국어</span>
WORD_RE = re.compile(
    r'<span[^>]*class="[^"]*cn-word[^"]*"[^>]*data-tr="([^"]*)"[^>]*>(.*?)</span>',
    re.DOTALL,
)


class Subject(models.Model):
    """A subject shelf in the Corner — Korean, English, Math, ..."""
    name         = models.CharField(max_length=120)
    slug         = models.SlugField(max_length=140, blank=True, unique=True)
    summary      = models.CharField(max_length=300, blank=True,
                                    help_text='Short description shown on the subject card.')
    icon         = models.CharField(max_length=50, default='bi-stars',
                                    help_text='Bootstrap-icons class, e.g. bi-translate.')
    color        = models.CharField(max_length=7, default='#d97706',
                                    help_text='Hex color for card accent, e.g. #d97706')
    order        = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'name']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.name) or 'subject'
            slug, n = base, 1
            while Subject.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Collection(models.Model):
    """A set of stories read in order — e.g. Keimyung Korean Readings."""
    subject      = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='collections')
    title        = models.CharField(max_length=200)
    slug         = models.SlugField(max_length=220, blank=True)
    description  = models.CharField(max_length=300, blank=True,
                                    help_text='Short description shown on the collection card.')
    cover        = models.ImageField(upload_to='corner/covers/', blank=True, null=True)
    order        = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']
        unique_together = ['subject', 'slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title) or 'collection'
            slug, n = base, 1
            while Collection.objects.filter(subject=self.subject, slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.subject.name} — {self.title}'


class Story(models.Model):
    """One readable story. Vocab is marked inline in the body as
    <span class="cn-word" data-tr="tarjima">단어</span>; StoryWord rows are
    rebuilt from those spans on every save, so the body is the single source
    of truth for both highlights and the end-of-story flashcards."""
    collection   = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='stories')
    title        = models.CharField(max_length=200)
    slug         = models.SlugField(max_length=220, blank=True)
    summary      = models.CharField(max_length=300, blank=True,
                                    help_text='Short description shown on listing cards.')
    body         = CKEditor5Field(config_name='tutorial')
    author       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='corner_stories')
    order        = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    views        = models.PositiveIntegerField(default=0)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'id']
        unique_together = ['collection', 'slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            # Korean titles slugify to '' — fall back to the story number.
            base = slugify(self.title) or (f'story-{self.order}' if self.order else 'story')
            slug, n = base, 1
            while Story.objects.filter(collection=self.collection, slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug
        super().save(*args, **kwargs)
        self._sync_words()

    def _sync_words(self):
        """Rebuild StoryWord rows from cn-word spans in the body."""
        seen, words = set(), []
        for translation, word_html in WORD_RE.findall(self.body or ''):
            word = re.sub(r'<[^>]+>', '', word_html).strip()
            translation = translation.strip()
            if not word or not translation or word in seen:
                continue
            seen.add(word)
            words.append((word, translation))
        self.words.all().delete()
        StoryWord.objects.bulk_create([
            StoryWord(story=self, word=w, translation=t, order=i)
            for i, (w, t) in enumerate(words)
        ])

    def __str__(self):
        return f'{self.collection.title} — {self.title}'


class StoryWord(models.Model):
    """A vocab entry extracted from the story body (derived — never hand-edited)."""
    story       = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='words')
    word        = models.CharField(max_length=100)
    translation = models.CharField(max_length=200)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.word} — {self.translation}'


class StoryProgress(models.Model):
    """A student finished a story; unique per user+story so points are awarded once."""
    user           = models.ForeignKey(User, on_delete=models.CASCADE, related_name='corner_progress')
    story          = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='progress')
    points_awarded = models.PositiveSmallIntegerField(default=STORY_POINTS)
    finished_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'story']

    def __str__(self):
        return f'{self.user.username} finished {self.story.title}'


class WritingTemplate(models.Model):
    """A downloadable/printable template file — e.g. a TOPIK writing sheet."""
    subject      = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='writing_templates')
    title        = models.CharField(max_length=200)
    description  = models.CharField(max_length=300, blank=True)
    file         = models.FileField(upload_to='corner/templates/')
    preview      = models.ImageField(upload_to='corner/previews/', blank=True, null=True,
                                     help_text='Optional preview image shown on the card.')
    author       = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                     related_name='corner_templates')
    order        = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    downloads    = models.PositiveIntegerField(default=0)
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return f'{self.subject.name} — {self.title}'
