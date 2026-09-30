"""Study abroad — "Xorijda oʻqish".

How to apply to a university abroad: the letters, the documents, what each
certificate is worth, how tuition is paid, and when the deadlines are.

Three kinds of content, kept apart on purpose because they age differently:

    Guide, Sample, ChecklistItem   evergreen — how to write a study plan
                                   does not change from year to year
    Scholarship, University        slow — rewritten when a programme changes
    Deadline                       dated — true for one cycle only

Every dated fact carries `source_url` and `last_checked`, both shown to the
pupil. A deadline not checked for a year stops counting down and tells the
pupil to check the official site instead: a confident wrong date is worse
than no date, because a pupil plans a year around it.

Content is bilingual *in the data* (English + `*_uz` columns), like the Logic
Arena: the text is content, not interface. `display_*` picks the column for
the visitor's language and falls back to whichever is filled.
"""
from zoneinfo import ZoneInfo

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import get_language
from django.utils.translation import gettext_lazy as _

# A fact older than this is not shown as a countdown.
STALE_AFTER_DAYS = 365

# Countdowns are for pupils in Uzbekistan: "today" is Tashkent's date, not
# the server's UTC one (which is still yesterday until 05:00 in Tashkent).
TASHKENT = ZoneInfo('Asia/Tashkent')


def today():
    return timezone.localdate(timezone=TASHKENT)


class Bilingual(models.Model):
    class Meta:
        abstract = True

    def _pick(self, base):
        uz = getattr(self, f'{base}_uz', '')
        if (get_language() or 'uz').startswith('uz'):
            return uz or getattr(self, base)
        return getattr(self, base) or uz

    def __getattr__(self, name):
        # display_title → _pick('title'), for any field that has a *_uz twin.
        if name.startswith('display_'):
            base = name[len('display_'):]
            try:
                self._meta.get_field(f'{base}_uz')
            except Exception:  # noqa: BLE001
                raise AttributeError(name)
            return self._pick(base)
        raise AttributeError(name)


class Guide(Bilingual):
    CATEGORIES = [
        ('start', _('Start here')),
        ('letters', _('Letters')),
        ('documents', _('Documents')),
        ('money', _('Money')),
        ('after', _('Visa and arrival')),
        ('choose', _('Choosing')),
    ]
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField(default=0)
    category = models.CharField(max_length=12, choices=CATEGORIES, default='start')
    icon = models.CharField(max_length=40, default='bi-compass')
    minutes = models.PositiveSmallIntegerField(default=5)
    title = models.CharField(max_length=200)
    title_uz = models.CharField(max_length=200)
    summary = models.CharField(max_length=300)
    summary_uz = models.CharField(max_length=300)
    body = models.TextField()
    body_uz = models.TextField()
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('abroad_guide', args=[self.slug])


class Scholarship(Bilingual):
    DEPTHS = [('full', 'full page'), ('card', 'card only')]
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=120, help_text='Official short name, e.g. "GKS".')
    full_name = models.CharField(max_length=200, blank=True)
    country = models.CharField(max_length=60)
    country_uz = models.CharField(max_length=60)
    flag = models.CharField(max_length=8, blank=True)
    depth = models.CharField(max_length=4, choices=DEPTHS, default='card')
    # Finder filters — comma-separated codes, matched by `accepts`.
    levels = models.CharField(max_length=40, default='bachelor,master',
                              help_text='bachelor, master, phd')
    languages = models.CharField(max_length=60, default='english',
                                 help_text='english, korean, japanese, any — what you can study in')
    fully_funded = models.BooleanField(default=True)
    summary = models.CharField(max_length=300)
    summary_uz = models.CharField(max_length=300)
    covers = models.TextField(blank=True, help_text='HTML list of what it pays for.')
    covers_uz = models.TextField(blank=True)
    usual_period = models.CharField(max_length=160, blank=True,
                                    help_text='e.g. "Sep–Oct (bachelor), Feb–Mar (master)"')
    usual_period_uz = models.CharField(max_length=160, blank=True)
    body = models.TextField(blank=True, help_text='HTML, for depth=full.')
    body_uz = models.TextField(blank=True)
    official_url = models.URLField()
    last_checked = models.DateField()
    is_published = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('abroad_scholarship', args=[self.slug])

    def level_list(self):
        return [c.strip() for c in self.levels.split(',') if c.strip()]

    def language_list(self):
        return [c.strip() for c in self.languages.split(',') if c.strip()]

    @property
    def is_stale(self):
        return (today() - self.last_checked).days > STALE_AFTER_DAYS


class Deadline(Bilingual):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name='deadlines')
    label = models.CharField(max_length=160, help_text='e.g. "GKS-U 2027 — Embassy track"')
    label_uz = models.CharField(max_length=160)
    opens = models.DateField(null=True, blank=True)
    closes = models.DateField()
    is_estimate = models.BooleanField(default=False,
                                      help_text='Not yet announced — based on last year.')
    note = models.CharField(max_length=300, blank=True)
    note_uz = models.CharField(max_length=300, blank=True)
    source_url = models.URLField()
    last_checked = models.DateField()

    class Meta:
        ordering = ['closes']

    def __str__(self):
        return f'{self.label} — {self.closes}'

    @property
    def is_stale(self):
        return (today() - self.last_checked).days > STALE_AFTER_DAYS

    @property
    def days_left(self):
        return (self.closes - today()).days

    @property
    def is_open(self):
        d_today = today()
        return (self.opens is None or self.opens <= d_today) and d_today <= self.closes

    @property
    def state(self):
        """upcoming / open / closed / stale / estimate — what the chip says.

        An estimate never counts down: "106 days left" on a call that has not
        opened would tell a pupil it is accepting applications."""
        if self.is_stale:
            return 'stale'
        d_today = today()
        if self.closes < d_today:
            return 'closed'
        if self.is_estimate:
            return 'estimate'
        if self.opens and self.opens > d_today:
            return 'upcoming'
        return 'open'


class Sample(Bilingual):
    KINDS = [
        ('statement', _('Personal statement')),
        ('study_plan', _('Study plan')),
        ('recommendation', _('Recommendation letter')),
        ('cv', _('CV')),
        ('email', _('Email to a professor')),
    ]
    slug = models.SlugField(unique=True)
    order = models.PositiveSmallIntegerField(default=0)
    kind = models.CharField(max_length=16, choices=KINDS)
    scholarship = models.ForeignKey(Scholarship, on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='samples')
    title = models.CharField(max_length=200)
    title_uz = models.CharField(max_length=200)
    intro = models.TextField(blank=True, help_text='HTML — who wrote it, for what.')
    intro_uz = models.TextField(blank=True)
    # The letter itself is written in the language it is submitted in (English);
    # the margin notes explaining it are bilingual.
    letter = models.TextField(help_text='HTML, one <p> per paragraph.')
    notes = models.JSONField(default=list,
                             help_text='[{"para": 1, "en": "...", "uz": "..."}] — para is 1-based.')
    # The printable planner: questions to answer before writing your own.
    prompts = models.JSONField(default=list, help_text='[{"en": "...", "uz": "...", "lines": 4}]')
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('abroad_sample', args=[self.slug])


class University(Bilingual):
    order = models.PositiveSmallIntegerField(default=0)
    name = models.CharField(max_length=160)
    name_local = models.CharField(max_length=160, blank=True)
    country = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    url = models.URLField()
    gks_university_track = models.BooleanField(default=False)
    strengths = models.CharField(max_length=300)
    strengths_uz = models.CharField(max_length=300)
    rank_label = models.CharField(max_length=60, blank=True, help_text='e.g. "QS 2026: #31"')
    rank_source = models.URLField(blank=True)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'universities'

    def __str__(self):
        return self.name


class ChecklistItem(Bilingual):
    """One document or step on a target's checklist ("general", "gks-u"…)."""
    target = models.CharField(max_length=40)
    order = models.PositiveSmallIntegerField(default=0)
    text = models.CharField(max_length=300)
    text_uz = models.CharField(max_length=300)
    hint = models.CharField(max_length=300, blank=True)
    hint_uz = models.CharField(max_length=300, blank=True)

    class Meta:
        ordering = ['target', 'order']
        unique_together = ('target', 'order')

    def __str__(self):
        return f'{self.target} #{self.order}: {self.text}'


class ChecklistTick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='abroad_ticks')
    item = models.ForeignKey(ChecklistItem, on_delete=models.CASCADE, related_name='ticks')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'item')

