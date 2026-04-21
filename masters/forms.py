from django import forms
from .models import Master

class MasterForm(forms.ModelForm):
    # Change __dict__ to Meta
    class Meta: 
        model = Master
        fields = ['profile', 'name', 'subject', 'category', 'description', 'certificates', 'url']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell us about your expertise...'}),
            'name': forms.TextInput(attrs={'placeholder': 'Master Name'}),
        }
