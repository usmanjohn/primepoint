from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.html import strip_tags
from masters.models import Master
from panda.models import Panda


LEVEL_CHOICES = [('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')]


class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Practice(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='practices')

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='medium')

    is_free = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    is_available_for_all = models.BooleanField(default=False, help_text='Allow other masters to assign this as homework.')

    time_limit = models.PositiveIntegerField(null=True, blank=True, help_text='Minutes. Leave blank for no limit.')
    pass_score = models.FloatField(default=50)
    max_attempts = models.PositiveIntegerField(default=1, help_text='Set to 0 for unlimited attempts.')

    show_answers_after = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PracticeQuestion(models.Model):
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, related_name='questions')

    question_text = CKEditor5Field(config_name='extends')
    image = models.ImageField(upload_to='practice_images/', null=True, blank=True)

    explanation = CKEditor5Field(null=True, blank=True)
    hint = CKEditor5Field(null=True, blank=True)

    order = models.PositiveIntegerField(default=0)
    points = models.FloatField(default=1)

    made_by = models.ForeignKey(Master, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        clean_text = strip_tags(self.question_text).strip()
        return f"{clean_text[:40]}... ({self.practice.title[:20]})"


class PracticeChoice(models.Model):
    question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE, related_name='choices')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return strip_tags(self.text)[:40]


class PracticeAttempt(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('abandoned', 'Abandoned'),
    ]

    panda = models.ForeignKey(Panda, on_delete=models.CASCADE, related_name='attempts')
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, related_name='attempts')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    score = models.FloatField(default=0)

    start_time = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.panda.profile.user.username} — {self.practice.title} ({self.status})"


class UserAnswer(models.Model):
    attempt = models.ForeignKey(PracticeAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE, related_name='answers')

    selected_choices = models.ManyToManyField(PracticeChoice, blank=True)
