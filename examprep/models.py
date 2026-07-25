import re

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
    audio       = models.FileField(upload_to='examprep/audio/', blank=True, null=True,
                                   help_text='Optional audio clip (listening lessons), played above the text.')
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


# Points for finishing one exam-prep lesson. Sits between a Corner story (5)
# and a writing drill (8): a lesson is longer than a story but less work than
# producing a full written answer.
LESSON_POINTS = 6


class LessonProgress(models.Model):
    """A student finished a lesson; unique per user+lesson so points are
    awarded once. Mirrors corner.StoryProgress deliberately — the whole points
    system reads these tables the same way."""
    user           = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name='examprep_progress')
    lesson         = models.ForeignKey(Lesson, on_delete=models.CASCADE,
                                       related_name='progress')
    points_awarded = models.PositiveSmallIntegerField(default=LESSON_POINTS)
    finished_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'lesson']

    def __str__(self):
        return f'{self.user.username} finished {self.lesson.title}'


# ── Writing drills ─────────────────────────────────────────────────────────
# Moved here from `corner` in July 2026: Corner is the reading library, and an
# exam-writing drill belongs with the exam it prepares you for. The old model
# hung off a Corner subject ("Korean"), which could not express that a drill is
# TOPIK 쓰기 rather than IELTS Task 2 — it now hangs off the ExamTrack instead.

WRITING_DRILL_POINTS = 8

# Question types, grouped by the exam they belong to. Flat so the field stays a
# plain CharField; the list page groups by whichever types the track actually
# has, so IELTS never shows TOPIK's numbering or vice versa.
QTYPE_CHOICES = [
    ('51', '51 — 실용문 빈칸'),
    ('52', '52 — 설명문 빈칸'),
    ('53', '53 — 도표 분석 (200~300자)'),
    ('54', '54 — 주제 글쓰기 (600~700자)'),
    ('t1', 'Task 1 — Report'),
    ('t2', 'Task 2 — Essay'),
]

# Reuse Corner's vocab-span parsing: drills mark template-ready expressions with
# the same `cn-word` spans stories use, and the flashcards are built from them.
from corner.models import (  # noqa: E402 — placed here to keep the model block together
    CN_SPAN_RE, POS_CHOICES, VALID_POS, _TR_RE, _POS_RE,
)


class WritingDrill(models.Model):
    """An interactive exam-writing drill (e.g. TOPIK 쓰기 53): an exam-style
    question with a chart/graph, a scaffold text the student completes by
    reading the chart, and a model answer revealed at the end.

    Blanks are marked inline in `template_body` as
        <span class="wp-blank" data-answer="증가하였다" data-alt="증가했다|늘었다"></span>
    (data-alt = accepted alternatives, |-separated). Template-ready expressions
    are marked with the same cn-word spans stories use; WritingDrillWord rows
    are rebuilt from the spans in `template_body` + `model_answer` on save."""
    track         = models.ForeignKey(ExamTrack, on_delete=models.CASCADE,
                                      related_name='writing_drills')
    qtype         = models.CharField(max_length=2, choices=QTYPE_CHOICES, default='53')
    title         = models.CharField(max_length=200)
    summary       = models.CharField(max_length=300, blank=True,
                                     help_text='Short card blurb in Uzbek.')
    prompt        = models.TextField(help_text='The exam question, HTML — instruction text as it '
                                               'would appear on the test paper.')
    chart         = models.TextField(blank=True,
                                     help_text='The graph/table as inline HTML/SVG (wp-chart markup).')
    template_body = models.TextField(blank=True,
                                     help_text='Scaffold text with wp-blank gaps and cn-word marks.')
    model_answer  = models.TextField(help_text='Full model answer, HTML, with cn-word marks.')
    tips          = models.TextField(blank=True,
                                     help_text='Strategy notes in Uzbek, HTML (shown under the answer).')
    author        = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='examprep_writing_drills')
    order         = models.PositiveIntegerField(default=0)
    is_published  = models.BooleanField(default=True)
    views         = models.PositiveIntegerField(default=0)
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['qtype', 'order', 'id']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self._sync_words()

    def _sync_words(self):
        """Rebuild word rows from cn-word spans in the scaffold + model answer."""
        seen, words = set(), []
        source = f'{self.template_body or ""} {self.model_answer or ""}'
        for attrs, word_html in CN_SPAN_RE.findall(source):
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
        WritingDrillWord.objects.bulk_create([
            WritingDrillWord(drill=self, word=w, translation=t, pos=p, order=i)
            for i, (w, t, p) in enumerate(words)
        ])

    def __str__(self):
        return f'{self.get_qtype_display()} — {self.title}'


class WritingDrillWord(models.Model):
    """A vocab entry extracted from a drill (derived — never hand-edited)."""
    drill       = models.ForeignKey(WritingDrill, on_delete=models.CASCADE, related_name='words')
    word        = models.CharField(max_length=100)
    translation = models.CharField(max_length=200)
    pos         = models.CharField(max_length=10, blank=True, choices=POS_CHOICES)
    order       = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.word} — {self.translation}'


class WritingDrillProgress(models.Model):
    """A student finished a drill; unique per user+drill so points are awarded once."""
    user           = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name='examprep_writing_progress')
    drill          = models.ForeignKey(WritingDrill, on_delete=models.CASCADE,
                                       related_name='progress')
    points_awarded = models.PositiveSmallIntegerField(default=WRITING_DRILL_POINTS)
    finished_at    = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'drill']

    def __str__(self):
        return f'{self.user.username} finished {self.drill.title}'
