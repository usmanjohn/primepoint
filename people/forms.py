from django import forms
from django.contrib.auth.models import User
from .models import People
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username']

class PeopleUpdateForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ['first_name', 'date_of_birth', 'biography', 'image']
        widgets = {
            # This triggers the browser's date picker
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            # This makes the bio box larger
            'biography': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Tell us about yourself...'}),
        }