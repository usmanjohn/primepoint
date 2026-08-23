from django.db import models
from masters.models import Master
from panda.models import Panda
from practice.models import Practice, PracticeAttempt


class PandaGroup(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='panda_groups')
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(Panda, blank=True, related_name='groups')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        unique_together = ('master', 'name')

    def __str__(self):
        return self.name

    @property
    def member_count(self):
        return self.members.count()


class Homework(models.Model):
    """One evening's work, set by a master and handed to a set of pupils.

    A homework used to be exactly one practice. But a lesson here has three
    legs — the tutorial teaches the pattern, the practice drills it, the
    reading shows it living in a text — so a homework that can only carry the
    middle leg forced a master to set three homeworks for one evening. It now
    carries any mix of the four libraries, and `classroom` says which room it
    was set in: that is what narrows the pickers to the room's own subject and
    what makes a homework show up on the classroom page.
    """
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='homeworks')
    classroom = models.ForeignKey(
        'classroom.Classroom', on_delete=models.SET_NULL, null=True, blank=True,
        related_name='homeworks',
        help_text='The classroom this homework was set in.',
    )
    title = models.CharField(max_length=200)
    notes = models.TextField(blank=True, help_text='Optional instructions shown to students.')

    # ── What the pupil actually has to do ─────────────────────────────────
    practices = models.ManyToManyField(Practice, blank=True, related_name='homeworks')
    tutorials = models.ManyToManyField('tutorial.Tutorial', blank=True, related_name='homeworks')
    stories = models.ManyToManyField('corner.Story', blank=True, related_name='homeworks')
    exam_lessons = models.ManyToManyField('examprep.Lesson', blank=True, related_name='homeworks')

    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    # ── Contents ───────────────────────────────────────────────────────────
    def items(self):
        """Everything inside, as uniform rows — see `homework.items`."""
        from .items import homework_items
        return homework_items(self)

    @property
    def item_count(self):
        return (self.practices.count() + self.tutorials.count()
                + self.stories.count() + self.exam_lessons.count())

    @property
    def is_empty(self):
        return self.item_count == 0

    # ── Assignment tallies ─────────────────────────────────────────────────
    @property
    def pending_count(self):
        return self.assignments.filter(status='pending').count()

    @property
    def submitted_count(self):
        return self.assignments.filter(status='submitted').count()

    @property
    def graded_count(self):
        return self.assignments.filter(status='graded').count()


class HomeworkAssignment(models.Model):
    STATUS = [('pending', 'Pending'), ('submitted', 'Submitted'), ('graded', 'Graded')]

    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='assignments')
    panda = models.ForeignKey(Panda, on_delete=models.CASCADE, related_name='homework_assignments')
    status = models.CharField(max_length=20, choices=STATUS, default='pending')
    submitted_at = models.DateTimeField(null=True, blank=True)
    attempt = models.ForeignKey(
        PracticeAttempt, on_delete=models.SET_NULL, null=True, blank=True, related_name='homework_assignments'
    )
    feedback = models.TextField(blank=True)

    class Meta:
        unique_together = ('homework', 'panda')
        ordering = ['status', 'panda__name']

    def __str__(self):
        return f"{self.panda} — {self.homework.title}"

    # ── Progress ───────────────────────────────────────────────────────────
    def progress(self):
        """The homework's rows with a `done` flag for this pupil."""
        from .items import mark_done
        return mark_done(self.homework.items(), self.panda)

    @property
    def done_count(self):
        return sum(1 for row in self.progress() if row['done'])

    @property
    def percent_done(self):
        total = self.homework.item_count
        if not total:
            return 0
        return round(self.done_count * 100 / total)

    def refresh(self, save=True):
        """Mark submitted once every piece of the homework is finished.

        A homework is only as done as its least-done leg: reading the tutorial
        but never sitting the practice is not a submission. Graded assignments
        are left alone — the master's verdict outranks the tally.
        """
        if self.status == 'graded':
            return self
        rows = self.progress()
        finished = bool(rows) and all(r['done'] for r in rows)
        new_status = 'submitted' if finished else 'pending'
        if new_status != self.status:
            self.status = new_status
            from django.utils import timezone
            self.submitted_at = timezone.now() if finished else None
            if save:
                self.save(update_fields=['status', 'submitted_at'])
        return self
