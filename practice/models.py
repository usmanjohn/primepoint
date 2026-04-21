from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.html import strip_tags
from masters.models import Master
from panda.models import Panda
class Practice(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='practices')
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    subject = models.ForeignKey('Subject', on_delete=models.SET_NULL, null=True)
    level = models.CharField(max_length=20, default='medium')

    is_free = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    # Test behavior
    time_limit = models.IntegerField(null=True, blank=True)  # minutes
    pass_score = models.FloatField(default=50)
    max_attempts = models.IntegerField(default=1)

    shuffle_questions = models.BooleanField(default=False)
    shuffle_choices = models.BooleanField(default=False)
    show_answers_after = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

class PracticeQuestion(models.Model):
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, related_name='questions')

    question_text = CKEditor5Field(config_name='extends')
    image = models.ImageField(upload_to='practice_images/', null=True, blank=True)

    explanation = CKEditor5Field(null=True, blank=True)
    hint = CKEditor5Field(null=True, blank=True)

    order = models.PositiveIntegerField(default=0)
    points = models.FloatField(default=1)

    made_by = models.ForeignKey(Master, on_delete=models.CASCADE, null=True, blank=True)

class PracticeChoice(models.Model):
    question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE, related_name='choices')
    text = models.TextField()
    is_correct = models.BooleanField(default=False)

class PracticeAttempt(models.Model):
    panda = models.ForeignKey(Panda, on_delete=models.CASCADE, related_name='attempts')
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)

    status = models.CharField(
        max_length=20,
        choices=[
            ('in_progress', 'In Progress'),
            ('completed', 'Completed'),
            ('abandoned', 'Abandoned')
        ],
        default='in_progress'
    )

    score = models.FloatField(default=0)

    start_time = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

class UserAnswer(models.Model):
    attempt = models.ForeignKey(PracticeAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE)

    selected_choices = models.ManyToManyField(PracticeChoice)

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name