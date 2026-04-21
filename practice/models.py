from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.html import strip_tags
from masters.models import Master
from panda.models import Panda

class Practice(models.Model):
    TYPE_CHOICES = [
        ('math', 'Math'), ('english', 'English'), ('korean', 'Korean'),
        ('sat', 'SAT'), ('gmat', 'GMAT'), ('gre', 'GRE'), ('it', 'IT')
    ]
    LEVEL_CHOICES = [('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard'), ('real', 'Real')]
    PURPOSE_CHOICES = [('homework', 'Homework'), ('summary', 'Summary'), ('test', 'Test')]

    master = models.ForeignKey(Master, on_delete=models.CASCADE, related_name='practices')
    type = models.CharField(choices=TYPE_CHOICES, max_length=20)
    level = models.CharField(choices=LEVEL_CHOICES, default='medium', max_length=20)
    purpose = models.CharField(choices=PURPOSE_CHOICES, default='test', max_length=20)
    
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_free = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_type_display()}] {self.title}"

class PracticeQuestion(models.Model):
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE, related_name='questions')
    # CKEditor handles LaTeX/Math Formulas perfectly
    question_text = CKEditor5Field('Question Content', config_name='extends')
    image = models.ImageField(upload_to='practice_images/', null=True, blank=True)
    
    # Choices as separate fields for simple 1-5 logic
    choice1 = CKEditor5Field('Choice 1', config_name='extends')
    choice2 = CKEditor5Field('Choice 2', config_name='extends')
    choice3 = CKEditor5Field('Choice 3', config_name='extends', null=True, blank=True)
    choice4 = CKEditor5Field('Choice 4', config_name='extends', null=True, blank=True)
    choice5 = CKEditor5Field('Choice 5', config_name='extends', null=True, blank=True)
    
    # Logic for answers
    correct_answer = models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    is_multiple_choice = models.BooleanField(default=False, help_text="Check if multiple answers are allowed")
    explanation = CKEditor5Field('Explanation', config_name='extends', null=True, blank=True)
    
    made_by = models.ForeignKey(Master, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Q-{self.id}: {strip_tags(self.question_text)[:50]}"

class PracticeAttempt(models.Model):
    panda = models.ForeignKey(Panda, on_delete=models.CASCADE, related_name='attempts')
    practice = models.ForeignKey(Practice, on_delete=models.CASCADE)
    score = models.FloatField(default=0)
    start_time = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.panda.name} - {self.practice.title} - Score: {self.score}"

class UserAnswer(models.Model):
    attempt = models.ForeignKey(PracticeAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(PracticeQuestion, on_delete=models.CASCADE)
    selected_choice = models.IntegerField() # 1 through 5

    @property
    def is_correct(self):
        return self.selected_choice == self.question.correct_answer

class Subject(models.Model):  # Must match this name exactly
    name = models.CharField(max_length=50)