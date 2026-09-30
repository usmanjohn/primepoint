"""The workbook — a Prime lesson's fourth leg ("Ish daftari").

The other three legs are all recognition: the tutorial is read, the practice
is four choices to pick from, the reading is read. A textbook also makes the
pupil *produce* the language — type the form, rewrite the sentence, build it
from loose words, write five of their own, go and use it — and that is what a
workbook holds.

    Workbook      one per tutorial
      Task        one exercise: a section (A–E), a kind, an instruction
        TaskItem  one line of it: a stem, the accepted answers, a model answer

    WorkbookAttempt   one per user per workbook — resubmitting overwrites
      ItemResponse    what they typed / ticked for one item, and the verdict
    AnswerAppeal      "I was right" on a wrongly-marked item; the accepted
                      list grows from these

The five sections are always in this order, and each is submitted on its own
(one plain <form> per section — no JavaScript anywhere):

    A  Isinish   warm-up from earlier lessons (spaced retrieval)   auto
    B  Mashq     controlled drill: gap, conjugate, pick             auto
    C  Qoʻllash  transform, build, translate, fix the error         auto
    D  Ijod      one free piece of writing + a checklist            self + teacher
    E  Missiya   a real-world act                                   ticked done

A workbook is complete when every section it has has been sent once.
"""
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from . import grading

# Points: a flat part for finishing, and a part for how much of the marked
# work was right. Finishing counts for most of it on purpose — the sections
# that matter most (D, E) cannot be marked by a machine.
WORKBOOK_BASE_POINTS = 10
WORKBOOK_SCORE_POINTS = 10

SECTIONS = [
    ('A', _('Warm-up')),
    ('B', _('Drill')),
    ('C', _('Apply')),
    ('D', _('Create')),
    ('E', _('Mission')),
]
SECTION_ICONS = {
    'A': 'bi-arrow-repeat', 'B': 'bi-pencil', 'C': 'bi-tools',
    'D': 'bi-feather', 'E': 'bi-flag',
}

# Kinds marked against an accepted-answer list.
AUTO_KINDS = ('gap', 'conj', 'transform', 'build', 'translate', 'fix', 'hangul', 'pick')
# Kinds a machine cannot mark.
OPEN_KINDS = ('write', 'mission', 'copy')
KINDS = [
    ('gap', _('Fill the gap')),
    ('conj', _('Conjugate')),
    ('transform', _('Transform')),
    ('build', _('Build the sentence')),
    ('translate', _('Translate')),
    ('fix', _('Find and fix the error')),
    ('hangul', _('Letters and blocks')),
    ('pick', _('Choose')),
    ('write', _('Write')),
    ('mission', _('Mission')),
    ('copy', _('Copy by hand')),
]


class Workbook(models.Model):
    tutorial = models.OneToOneField(
        'tutorial.Tutorial', on_delete=models.CASCADE, related_name='workbook')
    intro = models.TextField(blank=True, help_text='HTML shown above the tasks.')
    is_published = models.BooleanField(default=True)
    # Hash of the data the workbook was imported from. The committed PDF is
    # only offered while its manifest entry carries the same hash, so a
    # worksheet edited after its PDF was generated can never ship stale.
    data_hash = models.CharField(max_length=64, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                   related_name='workbooks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['tutorial_id']

    def __str__(self):
        return f'Workbook — {self.tutorial.title}'

    @property
    def code(self):
        """'PK-9' from 'PK-9: Salomlashish…' — the lesson's short name."""
        return self.tutorial.title.split(':', 1)[0].strip()

    def sections(self):
        """[(code, label, icon, [tasks])] for the sections this workbook has."""
        tasks = list(self.tasks.prefetch_related('items'))
        out = []
        for code, label in SECTIONS:
            mine = [t for t in tasks if t.section == code]
            if mine:
                out.append((code, label, SECTION_ICONS[code], mine))
        return out

    def section_codes(self):
        return sorted(set(self.tasks.values_list('section', flat=True)))

    def auto_item_count(self):
        return TaskItem.objects.filter(task__workbook=self, task__kind__in=AUTO_KINDS).count()


class Task(models.Model):
    workbook = models.ForeignKey(Workbook, on_delete=models.CASCADE, related_name='tasks')
    section = models.CharField(max_length=1, choices=SECTIONS)
    kind = models.CharField(max_length=12, choices=KINDS)
    order = models.PositiveSmallIntegerField(default=0)
    title = models.CharField(max_length=200, blank=True)
    instruction = models.TextField(help_text='HTML — what to do, in Uzbek.')
    # 1 = everyone should do it, 2 = a push, 3 = the ⭐ stretch.
    stars = models.PositiveSmallIntegerField(default=1)

    class Meta:
        ordering = ['section', 'order', 'id']

    def __str__(self):
        return f'{self.workbook.code} {self.section}{self.order} {self.kind}'

    @property
    def is_auto(self):
        return self.kind in AUTO_KINDS

    @property
    def is_write(self):
        return self.kind == 'write'

    @property
    def is_mission(self):
        return self.kind == 'mission'

    @property
    def is_done_kind(self):
        """Kinds the pupil ticks off: a mission, or copying letters by hand."""
        return self.kind in ('mission', 'copy')

    @property
    def star_marks(self):
        return '⭐' * max(0, self.stars - 1)


class TaskItem(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='items')
    order = models.PositiveSmallIntegerField(default=0)
    stem = models.TextField(blank=True, help_text='HTML. A gap is written ___ .')
    answers = models.JSONField(default=list, blank=True,
                               help_text='Every accepted answer, as typed.')
    model_answer = models.TextField(blank=True, help_text='HTML — what a good answer looks like.')
    explanation = models.TextField(blank=True, help_text='HTML, Uzbek — why.')
    # `build`: the loose words to put in order. `pick`: the options of the <select>.
    words = models.JSONField(default=list, blank=True)
    options = models.JSONField(default=list, blank=True)
    # `write`: what a good answer must contain, ticked by the pupil.
    checklist = models.JSONField(default=list, blank=True)
    # Width hint for the answer box, so a one-syllable gap is not a full line.
    size = models.CharField(max_length=5, default='m',
                            choices=[('s', 'short'), ('m', 'medium'), ('l', 'long')])

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f'{self.task} #{self.order}'

    def mark(self, text):
        return grading.mark(text, self.answers,
                            ignore=grading.IGNORE_FOR_KIND.get(self.task.kind, ''))

    @property
    def stem_parts(self):
        """The stem split around its gap, so the box can sit inside the line."""
        if '___' in self.stem:
            before, after = self.stem.split('___', 1)
            return before, after
        return None


class WorkbookAttempt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workbook_attempts')
    workbook = models.ForeignKey(Workbook, on_delete=models.CASCADE, related_name='attempts')
    sections_done = models.CharField(max_length=8, blank=True,
                                     help_text='Section codes sent at least once, e.g. "ABD".')
    correct = models.PositiveSmallIntegerField(default=0)
    total = models.PositiveSmallIntegerField(default=0)
    completed_at = models.DateTimeField(null=True, blank=True)
    points_awarded = models.FloatField(default=0)
    teacher_note = models.TextField(blank=True)
    teacher_note_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,
                                        related_name='+')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'workbook')

    def __str__(self):
        return f'{self.user.username} — {self.workbook}'

    @property
    def is_complete(self):
        return self.completed_at is not None

    @property
    def percent(self):
        return round(self.correct * 100 / self.total) if self.total else 0

    def rescore(self):
        """Recount the marked items and, once every section is in, finish.

        Points only ever go up: a pupil who comes back and fixes their
        mistakes is rewarded, one who clears the form is not punished.
        """
        auto = self.responses.filter(item__task__kind__in=AUTO_KINDS)
        self.total = self.workbook.auto_item_count()
        self.correct = auto.filter(is_correct=True).count()
        needed = set(self.workbook.section_codes())
        if needed and needed <= set(self.sections_done):
            if self.completed_at is None:
                self.completed_at = timezone.now()
            ratio = self.correct / self.total if self.total else 1
            earned = round(WORKBOOK_BASE_POINTS + ratio * WORKBOOK_SCORE_POINTS, 1)
            self.points_awarded = max(self.points_awarded, earned)

    def mark_section_done(self, code):
        if code not in self.sections_done:
            self.sections_done = ''.join(sorted(self.sections_done + code))


class ItemResponse(models.Model):
    attempt = models.ForeignKey(WorkbookAttempt, on_delete=models.CASCADE, related_name='responses')
    item = models.ForeignKey(TaskItem, on_delete=models.CASCADE, related_name='responses')
    text = models.TextField(blank=True)
    verdict = models.CharField(max_length=8, blank=True)   # grading.RIGHT / NEARLY / WRONG / EMPTY
    is_correct = models.BooleanField(null=True)             # None for open kinds
    # `write`: the checklist lines the pupil ticked, and their own verdict
    # after seeing the model answer. `mission`: done or not.
    checks = models.JSONField(default=list, blank=True)
    self_mark = models.CharField(max_length=8, blank=True,
                                 choices=[('good', 'good'), ('again', 'again')])
    done = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('attempt', 'item')

    def __str__(self):
        return f'{self.attempt} / {self.item_id}: {self.text[:30]}'

    def regrade(self):
        self.verdict = self.item.mark(self.text)
        self.is_correct = grading.is_correct(self.verdict)


class AnswerAppeal(models.Model):
    STATUS = [('open', 'open'), ('accepted', 'accepted'), ('rejected', 'rejected')]

    item = models.ForeignKey(TaskItem, on_delete=models.CASCADE, related_name='appeals')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workbook_appeals')
    text = models.CharField(max_length=500)
    status = models.CharField(max_length=10, choices=STATUS, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    decided_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['status', '-created_at']
        unique_together = ('item', 'user', 'text')

    def __str__(self):
        return f'{self.item}: {self.text} ({self.status})'
