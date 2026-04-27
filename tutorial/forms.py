from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from .models import Tutorial


class TutorialForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditor5Widget(
            config_name='tutorial',
            attrs={'class': 'django_ckeditor_5'},
        ),
        required=True,
    )

    class Meta:
        model  = Tutorial
        fields = ['title', 'category', 'thumbnail', 'summary', 'content', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-core',
                'placeholder': 'Tutorial title…',
            }),
            'summary': forms.Textarea(attrs={
                'class': 'form-core',
                'rows': 2,
                'placeholder': 'Short description shown on listing cards (optional)…',
            }),
            'category': forms.Select(attrs={'class': 'form-core'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-core'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
