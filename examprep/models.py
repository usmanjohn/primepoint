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


# ── Grammar bank ───────────────────────────────────────────────────────────
# A reference table rather than a lesson: every grammar pattern the exam can
# throw at you, on one filterable, printable page. Lessons teach one thing
# deeply; this answers "what was -더니 again, and how is it different from
# -았/었더니?" in five seconds — which is what students actually need while
# revising. Hangs off the ExamTrack so IELTS could one day get its own bank.

# What kind of thing the pattern is — grammatical shape.
GRAMMAR_CATEGORY_CHOICES = [
    ('particle',   '조사 — Qo‘shimchalar (kelishik/yuklama)'),
    ('ending',     '종결어미 — Tugallovchi qo‘shimchalar'),
    ('connective', '연결어미 — Bog‘lovchi qo‘shimchalar'),
    ('tense',      '시제 — Zamon va nisbat'),
    ('modifier',   '관형형 — Aniqlovchi shakllar'),
    ('expression', '문형 — Grammatik iboralar'),
    ('voice',      '피동·사동 — Majhul va orttirma'),
    ('quotation',  '인용 — Ko‘chirma gap'),
    ('honorific',  '높임 — Hurmat shakllari'),
    ('adverb',     '접속부사 — Bog‘lovchi ravishlar'),
]

# What the pattern MEANS — the meaning group. This is the axis synonyms live
# on: everything that expresses "sabab" sits together, so a student comparing
# -아서 / -니까 / -기 때문에 / -느라고 sees all four at once.
GRAMMAR_FUNCTION_CHOICES = [
    ('reason',      'Sabab — 이유·원인'),
    ('contrast',    'Qarama-qarshilik — 대조·반대'),
    ('condition',   'Shart — 조건·가정'),
    ('concession',  'Qarshi qo‘yish — 양보'),
    ('time',        'Vaqt — 시간·순서'),
    ('purpose',     'Maqsad — 목적'),
    ('intention',   'Niyat va reja — 의도·계획'),
    ('guess',       'Taxmin — 추측'),
    ('ability',     'Imkoniyat va qobiliyat — 가능·능력'),
    ('obligation',  'Majburiyat va ruxsat — 의무·허락'),
    ('experience',  'Tajriba va odat — 경험·습관'),
    ('change',      'O‘zgarish va holat — 변화·상태'),
    ('comparison',  'Taqqoslash — 비교'),
    ('listing',     'Sanash va qo‘shish — 나열·첨가'),
    ('choice',      'Tanlov — 선택'),
    ('quote',       'Ko‘chirma gap — 인용'),
    ('feeling',     'His-tuyg‘u va baho — 감정·평가'),
    ('discovery',   'Bilib qolish — 발견·깨달음'),
    ('degree',      'Daraja va miqdor — 정도·수량'),
    ('case',        'Gap bo‘lagi — 문장 성분'),
    ('politeness',  'Muomala darajasi — 높임·말투'),
]

# How formal the pattern is. Drives a small chip in the table — students lose
# marks on 쓰기 for writing 해요체 in an essay, so it is worth showing.
GRAMMAR_REGISTER_CHOICES = [
    ('written', 'Yozma / rasmiy — 문어·격식'),
    ('formal',  'Rasmiy nutq — 하십시오체'),
    ('polite',  'Muloyim — 해요체'),
    ('casual',  'Erkin — 반말'),
    ('both',    'Ikkalasi ham'),
]


class GrammarPoint(models.Model):
    """One grammar pattern — a row in the summary table.

    The row is deliberately shallow (pattern, meaning, where it attaches, one
    example) so the table scans fast; everything deeper lives in the expandable
    detail: all examples, nuance notes, common mistakes and the synonym set.
    """
    track        = models.ForeignKey(ExamTrack, on_delete=models.CASCADE,
                                     related_name='grammar_points')
    pattern      = models.CharField(max_length=120,
                                    help_text='The pattern itself, e.g. -(으)니까 or -기 때문에.')
    # Hangul slug: the pattern IS the name, and transliterating it would make
    # the URL unreadable to the audience. Needs allow_unicode here and the
    # `str` URL converter (`slug` only matches ASCII).
    slug         = models.SlugField(max_length=160, blank=True, allow_unicode=True)
    reading      = models.CharField(max_length=120, blank=True,
                                    help_text='Optional romanization, e.g. -(eu)nikka.')
    category     = models.CharField(max_length=20, choices=GRAMMAR_CATEGORY_CHOICES,
                                    default='expression')
    function     = models.CharField(max_length=20, choices=GRAMMAR_FUNCTION_CHOICES,
                                    default='reason',
                                    help_text='Meaning group — synonyms are grouped by this.')
    level        = models.PositiveSmallIntegerField(default=3,
                                                    help_text='TOPIK level 1–6 where it first appears.')
    meaning      = models.CharField(max_length=200,
                                    help_text='Short Uzbek gloss shown in the table, e.g. "sabab — chunki".')
    attach       = models.CharField(max_length=160, blank=True,
                                    help_text='Where it attaches, e.g. 동사/형용사 + -(으)니까.')
    form_rule    = models.TextField(blank=True,
                                    help_text='Conjugation rule in Uzbek, HTML allowed.')
    note         = models.TextField(blank=True,
                                    help_text='Nuance / usage notes in Uzbek, HTML allowed.')
    mistake      = models.TextField(blank=True,
                                    help_text='Common mistake in Uzbek, HTML allowed.')
    register     = models.CharField(max_length=10, choices=GRAMMAR_REGISTER_CHOICES,
                                    default='both')
    freq         = models.PositiveSmallIntegerField(default=2,
                                                    help_text='How often it shows up in TOPIK: 1–3 stars.')
    order        = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'id']
        unique_together = ['track', 'slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            # Hangul slugifies to an empty string with allow_unicode off, so
            # fall back to a transliteration-free stem plus a counter.
            base = slugify(self.pattern, allow_unicode=True).strip('-') or 'grammar'
            slug, n = base, 1
            while GrammarPoint.objects.filter(track=self.track,
                                              slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug[:160]
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.pattern} — {self.meaning}'

    @property
    def stars(self):
        """'★★☆' for the frequency column."""
        n = max(0, min(3, self.freq))
        return '★' * n + '☆' * (3 - n)

    @property
    def level_label(self):
        return f'TOPIK {self.level}'

    @property
    def first_example(self):
        return self.examples.first()


class GrammarExample(models.Model):
    """A Korean example sentence with its Uzbek translation."""
    point   = models.ForeignKey(GrammarPoint, on_delete=models.CASCADE,
                                related_name='examples')
    korean  = models.CharField(max_length=400)
    uz      = models.CharField(max_length=400, blank=True)
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.korean[:60]


class GrammarSynonym(models.Model):
    """A near-synonym of a grammar point, plus what actually differs.

    `related` is filled in at import time when the named pattern is itself in
    the bank, which turns the table into a cross-linked web: from -아서/어서 you
    can jump straight to -(으)니까 and read the difference from either side.
    """
    point   = models.ForeignKey(GrammarPoint, on_delete=models.CASCADE,
                                related_name='synonyms')
    pattern = models.CharField(max_length=120)
    note    = models.CharField(max_length=400, blank=True,
                               help_text='Farqi — how it differs, in Uzbek.')
    related = models.ForeignKey(GrammarPoint, on_delete=models.SET_NULL,
                                null=True, blank=True, related_name='synonym_of')
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.point.pattern} ≈ {self.pattern}'


# ── Vocabulary bank ────────────────────────────────────────────────────────
# Sibling of the grammar bank, same shape: a filterable, printable reference
# rather than a lesson. Its own idea is the ROOT FAMILY — most TOPIK II
# vocabulary is Sino-Korean, so 출구 / 출근 / 출발 / 출석 all share 출(出) =
# "chiqmoq". Learning the root turns dozens of unseen words into guessable
# ones, which is exactly the skill the reading paper rewards. Words therefore
# hang off VocabRoot as well as sitting in the flat table.

VOCAB_POS_CHOICES = [
    ('noun',   '명사 — Ot'),
    ('verb',   '동사 — Fe’l'),
    ('adj',    '형용사 — Sifat'),
    ('adv',    '부사 — Ravish'),
    ('phrase', '표현 — Ibora'),
    ('count',  '수사·단위 — Son va o‘lchov'),
]

# Theme the word belongs to — drives the topical filter and the print sheet's
# sections. Chosen to match the subject areas TOPIK actually draws on.
VOCAB_TOPIC_CHOICES = [
    ('daily',       'Kundalik hayot — 일상생활'),
    ('person',      'Odamlar va munosabat — 사람·관계'),
    ('emotion',     'His-tuyg‘u va fe’l-atvor — 감정·성격'),
    ('body',        'Tana va sog‘liq — 신체·건강'),
    ('food',        'Ovqat — 음식'),
    ('home',        'Uy va turar joy — 집·주거'),
    ('shopping',    'Xarid va pul — 쇼핑·경제생활'),
    ('transport',   'Transport va harakat — 교통·이동'),
    ('work',        'Ish va kasb — 직장·업무'),
    ('school',      'Ta’lim — 학교·교육'),
    ('society',     'Jamiyat — 사회'),
    ('economy',     'Iqtisod — 경제'),
    ('environment', 'Tabiat va ekologiya — 환경·자연'),
    ('science',     'Fan va texnologiya — 과학·기술'),
    ('culture',     'Madaniyat va san’at — 문화·예술'),
    ('media',       'Axborot va OAV — 언론·정보'),
    ('time',        'Vaqt — 시간·날짜'),
    ('place',       'Joy va yo‘nalish — 장소·위치'),
    ('abstract',    'Mavhum tushunchalar — 추상 개념'),
]


class VocabRoot(models.Model):
    """A shared morpheme and its meaning — 출(出) 'chiqmoq', 학(學) 'ilm'.

    This is the reason the vocab bank exists in this shape. A student who
    knows 출 = chiqish can read 출구, 출근, 출발, 제출 and 수출 without ever
    having met four of them.
    """
    track      = models.ForeignKey(ExamTrack, on_delete=models.CASCADE,
                                   related_name='vocab_roots')
    syllable   = models.CharField(max_length=10,
                                  help_text='The shared syllable, e.g. 출.')
    hanja      = models.CharField(max_length=10, blank=True,
                                  help_text='Its Hanja, e.g. 出. Blank for native-Korean roots.')
    slug       = models.SlugField(max_length=120, blank=True, allow_unicode=True)
    meaning    = models.CharField(max_length=200,
                                  help_text='Uzbek gloss, e.g. "chiqmoq — chiqish, tashqariga".')
    note       = models.TextField(blank=True,
                                  help_text='How the root behaves / what to watch for, Uzbek HTML.')
    order      = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', 'id']
        unique_together = ['track', 'slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.syllable, allow_unicode=True).strip('-') or 'root'
            slug, n = base, 1
            while VocabRoot.objects.filter(track=self.track,
                                           slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug[:120]
        super().save(*args, **kwargs)

    def __str__(self):
        label = f'{self.syllable}({self.hanja})' if self.hanja else self.syllable
        return f'{label} — {self.meaning}'

    @property
    def label(self):
        return f'{self.syllable}({self.hanja})' if self.hanja else self.syllable


class VocabEntry(models.Model):
    """One word — a row in the vocabulary table."""
    track        = models.ForeignKey(ExamTrack, on_delete=models.CASCADE,
                                     related_name='vocab_entries')
    word         = models.CharField(max_length=100)
    slug         = models.SlugField(max_length=140, blank=True, allow_unicode=True)
    hanja        = models.CharField(max_length=40, blank=True,
                                    help_text='Hanja spelling, e.g. 出口. Blank for native words.')
    roots        = models.ManyToManyField(VocabRoot, blank=True, related_name='entries',
                                          help_text='Root morphemes this word is built from.')
    pos          = models.CharField(max_length=10, choices=VOCAB_POS_CHOICES, default='noun')
    topic        = models.CharField(max_length=20, choices=VOCAB_TOPIC_CHOICES, default='daily')
    level        = models.PositiveSmallIntegerField(default=3,
                                                    help_text='TOPIK level 1–6.')
    meaning      = models.CharField(max_length=200,
                                    help_text='Short Uzbek gloss shown in the table.')
    note         = models.TextField(blank=True,
                                    help_text='Usage note in Uzbek, HTML allowed.')
    collocation  = models.CharField(max_length=300, blank=True,
                                    help_text='Typical partners, e.g. "출근하다 · 출근길 · 출근 시간".')
    freq         = models.PositiveSmallIntegerField(default=2,
                                                    help_text='How often it shows up in TOPIK: 1–3 stars.')
    order        = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', 'id']
        unique_together = ['track', 'slug']
        verbose_name_plural = 'Vocab entries'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.word, allow_unicode=True).strip('-') or 'word'
            slug, n = base, 1
            while VocabEntry.objects.filter(track=self.track,
                                            slug=slug).exclude(pk=self.pk).exists():
                slug = f'{base}-{n}'
                n += 1
            self.slug = slug[:140]
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.word} — {self.meaning}'

    @property
    def stars(self):
        n = max(0, min(3, self.freq))
        return '★' * n + '☆' * (3 - n)

    @property
    def first_example(self):
        return self.examples.first()


class VocabExample(models.Model):
    """A Korean example sentence with its Uzbek translation."""
    entry  = models.ForeignKey(VocabEntry, on_delete=models.CASCADE, related_name='examples')
    korean = models.CharField(max_length=400)
    uz     = models.CharField(max_length=400, blank=True)
    order  = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.korean[:60]


# What a related word is to the entry. Antonyms matter as much as synonyms for
# TOPIK: 수출/수입 and 증가/감소 are routinely the answer pair.
VOCAB_RELATION_CHOICES = [
    ('syn', '유의어 — Sinonim'),
    ('ant', '반의어 — Antonim'),
    ('rel', '관련어 — Bog‘liq so‘z'),
]


class VocabRelation(models.Model):
    """A synonym / antonym / related word, cross-linked at import time."""
    entry   = models.ForeignKey(VocabEntry, on_delete=models.CASCADE, related_name='relations')
    kind    = models.CharField(max_length=3, choices=VOCAB_RELATION_CHOICES, default='syn')
    word    = models.CharField(max_length=100)
    note    = models.CharField(max_length=300, blank=True,
                               help_text='Farqi — how it differs, in Uzbek.')
    related = models.ForeignKey(VocabEntry, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='related_from')
    order   = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['kind', 'order', 'id']

    def __str__(self):
        return f'{self.entry.word} [{self.kind}] {self.word}'
