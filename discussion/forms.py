from django import forms
from .models import Thread, Reply, Category


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'category', 'body', 'is_announcement']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Give your thread a clear, descriptive title…',
            }),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Share your question, idea, or announcement in detail…',
            }),
            'is_announcement': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        if user and not (user.is_staff or getattr(getattr(user, 'profile', None), 'is_master', False)):
            self.fields.pop('is_announcement', None)
        else:
            self.fields['is_announcement'].label = 'Post as Announcement'
            self.fields['is_announcement'].help_text = 'Announcements are highlighted for all users.'


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your answer or comment here…',
            }),
        }
        labels = {'body': ''}
