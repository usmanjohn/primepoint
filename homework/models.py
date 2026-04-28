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
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='homeworks')
    title = models.CharField(max_length=200)
    notes = models.TextField(blank=True, help_text='Optional instructions shown to students.')
    practice = models.ForeignKey(
        Practice, on_delete=models.SET_NULL, null=True, blank=True, related_name='homeworks'
    )
    due_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

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
