from django import forms
from .models import Master


class MasterForm(forms.ModelForm):
    class Meta:
        model = Master
        fields = ['name', 'subject', 'category', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'Your display name',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'e.g. Mathematics, Programming…',
            }),
            'category': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'e.g. Science, Languages…',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 4,
                'placeholder': 'Tell students about your expertise and teaching style…',
            }),
        }
