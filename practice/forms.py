from django import forms
from .models import Practice, PracticeQuestion


class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = [
            'title', 'description', 'subject', 'level',
            'is_free', 'time_limit', 'pass_score', 'max_attempts', 'show_answers_after',
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'e.g. Python Basics Quiz',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 3,
                'placeholder': 'Brief description shown on the practice card…',
            }),
            'subject': forms.Select(attrs={'class': 'form-core'}),
            'level': forms.Select(attrs={'class': 'form-core'}),
            'time_limit': forms.NumberInput(attrs={
                'class': 'form-core', 'placeholder': 'Leave blank for no limit',
            }),
            'pass_score': forms.NumberInput(attrs={'class': 'form-core', 'step': '1', 'min': '0', 'max': '100'}),
            'max_attempts': forms.NumberInput(attrs={'class': 'form-core', 'min': '0'}),
        }
        help_texts = {
            'max_attempts': '0 = unlimited',
            'pass_score': 'Percentage (0–100)',
            'time_limit': 'Minutes',
        }


class PracticeQuestionForm(forms.ModelForm):
    class Meta:
        model = PracticeQuestion
        fields = ['question_text', 'image', 'explanation', 'hint', 'order', 'points']
        widgets = {
            'question_text': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 3,
                'placeholder': 'Write the question here…',
            }),
            'explanation': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 2,
                'placeholder': 'Explain the correct answer (shown after submission)…',
            }),
            'hint': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 2,
                'placeholder': 'Optional hint shown during the quiz…',
            }),
            'order': forms.NumberInput(attrs={'class': 'form-core', 'min': '0'}),
            'points': forms.NumberInput(attrs={'class': 'form-core', 'step': '0.5', 'min': '0'}),
        }
