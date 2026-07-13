import re

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field


STORY_POINTS = 5

# Inline vocab convention:
#   <span class="cn-word" data-pos="verb" data-tr="uzbek translation">한국어</span>
# data-pos is optional and one of: verb, adj, adv (anything else / missing =
# neutral). We match the whole cn-word span, then pull data-tr / data-pos out of
# its attribute string so the two attributes may appear in any order.
CN_SPAN_RE = re.compile(
    r'<span\b([^>]*class="[^"]*cn-word[^"]*"[^>]*)>(.*?)</span>',
    re.DOTALL,
)
_TR_RE  = re.compile(r'data-tr="([^"]*)"')
_POS_RE = re.compile(r'data-pos="([^"]*)"')

# Parts of speech we colour-code (matches the CSS in static/css/corner.css).
POS_CHOICES = [
    ('verb', 'Verb'),        # 동사   — green
    ('adj',  'Adjective'),   # 형용사 — blue
    ('adv',  'Adverb'),      # 부사   — purple
]
VALID_POS = {code for code, _label in POS_CHOICES}


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
        for attrs, word_html in CN_SPAN_RE.findall(self.body or ''):
            tr_m = _TR_RE.search(attrs)
            if not tr_m:
                continue
            translation = tr_m.group(1).strip()
            word = re.sub(r'<[^>]+>', '', word_html).strip()
            if not word or not translation or word in seen:
                continue
            pos_m = _POS_RE.search(attrs)
            pos = pos_m.group(1).strip() if pos_m else ''
            if pos not in VALID_POS:
                pos = ''
            seen.add(word)
            words.append((word, translation, pos))
        self.words.all().delete()
        StoryWord.objects.bulk_create([
            StoryWord(story=self, word=w, translation=t, pos=p, order=i)
            for i, (w, t, p) in enumerate(words)
        ])

    def sync_grammar(self, grammar):
        """Replace this story's grammar points with `grammar`, a list of dicts:
        {pattern, meaning, examples=[...]}. Silently drops malformed entries so a
        bad grammar point can't break an import."""
        self.grammar.all().delete()
        rows, order = [], 0
        for g in grammar or []:
            pattern = (g.get('pattern') or '').strip()
            meaning = (g.get('meaning') or '').strip()
            if not pattern or not meaning:
                continue
            examples = [str(e).strip() for e in (g.get('examples') or []) if str(e).strip()]
            rows.append(StoryGrammar(
                story=self, pattern=pattern, meaning=meaning,
                examples=examples, order=order,
            ))
            order += 1
        StoryGrammar.objects.bulk_create(rows)

    def sync_questions(self, questions):
        """Replace this story's comprehension questions with `questions`, a list
        of dicts: {text, choices=[...], answer=<int>, explanation}. Silently
        drops malformed entries so a bad question can't break an import."""
        self.questions.all().delete()
        rows, order = [], 0
        for q in questions or []:
            text = (q.get('text') or '').strip()
            choices = [str(c).strip() for c in (q.get('choices') or []) if str(c).strip()]
            if not text or len(choices) < 2:
                continue
            try:
                answer = int(q.get('answer', 0))
            except (TypeError, ValueError):
                answer = 0
            answer = max(0, min(answer, len(choices) - 1))
            rows.append(StoryQuestion(
                story=self, text=text, choices=choices, answer=answer,
                explanation=(q.get('explanation') or '').strip(), order=order,
            ))
            order += 1
        StoryQuestion.objects.bulk_create(rows)

    def __str__(self):
        return f'{self.collection.title} — {self.title}'


class StoryWord(models.Model):
    """A vocab entry extracted from the story body (derived — never hand-edited)."""
    story       = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='words')
    word        = models.CharField(max_length=100)
    translation = models.CharField(max_length=200)
    pos         = models.CharField(max_length=10, blank=True, choices=POS_CHOICES,
                                   help_text='Part of speech (colour tag); blank = neutral.')
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.word} — {self.translation}'


class StoryQuestion(models.Model):
    """An inference / comprehension MCQ shown at the end of a story. Authored in
    the story data file (not derived from the body) and rebuilt on import."""
    story       = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='questions')
    text        = models.TextField(help_text='The question, in the target language.')
    choices     = models.JSONField(default=list, help_text='List of answer choices (strings).')
    answer      = models.PositiveSmallIntegerField(default=0,
                                                   help_text='0-based index of the correct choice.')
    explanation = models.TextField(blank=True,
                                   help_text='Why the answer is right — in Uzbek.')
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.story.title} — Q{self.order + 1}'


class StoryGrammar(models.Model):
    """A grammar point drawn from the story, shown after the vocabulary. Authored
    in the story data file (not derived from the body) and rebuilt on import.
    Intermediate/advanced patterns only — the ones a reader meets in the text."""
    story    = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='grammar')
    pattern  = models.CharField(max_length=100,
                                help_text='The grammar form, e.g. -는 바람에.')
    meaning  = models.TextField(help_text='Short explanation in Uzbek.')
    examples = models.JSONField(default=list,
                                help_text='List of Korean example sentences (strings).')
    order    = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.story.title} — {self.pattern}'


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
