from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from practice.models import Practice
from .models import Tutorial


class TutorialForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditor5Widget(
            config_name='tutorial',
            attrs={'class': 'django_ckeditor_5'},
        ),
        required=True,
    )

    practices = forms.ModelMultipleChoiceField(
        queryset=Practice.objects.none(),
        required=False,
        widget=forms.CheckboxSelectMultiple(),
        label='Linked Practices',
    )

    class Meta:
        model  = Tutorial
        fields = ['title', 'category', 'thumbnail', 'summary', 'content', 'is_published', 'practices']
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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and user.is_authenticated:
            try:
                master = user.profile.master
                own = Practice.objects.filter(master=master, is_published=True)
            except Exception:
                own = Practice.objects.none()
            public = Practice.objects.filter(is_available_for_all=True, is_published=True)
            self.fields['practices'].queryset = (own | public).distinct()
        else:
            self.fields['practices'].queryset = Practice.objects.none()
