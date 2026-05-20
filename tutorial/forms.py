from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from practice.models import Practice
from .models import Tutorial, TutorialPlaylist


class TutorialPlaylistForm(forms.ModelForm):
    class Meta:
        model  = TutorialPlaylist
        fields = ['title', 'category', 'description', 'thumbnail', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-core',
                'placeholder': 'Playlist title…',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-core',
                'rows': 2,
                'placeholder': 'Short description shown on the playlist card (optional)…',
            }),
            'category': forms.Select(attrs={'class': 'form-core'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class': 'form-core'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


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

    playlist = forms.ModelChoiceField(
        queryset=TutorialPlaylist.objects.none(),
        required=False,
        empty_label='— No playlist —',
        label='Add to Playlist',
        widget=forms.Select(attrs={'class': 'form-core'}),
    )

    playlist_order = forms.IntegerField(
        required=False,
        initial=0,
        min_value=0,
        label='Order in Playlist',
        widget=forms.NumberInput(attrs={'class': 'form-core', 'min': '0'}),
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
            self.fields['playlist'].queryset = TutorialPlaylist.objects.filter(author=user)
        else:
            self.fields['practices'].queryset = Practice.objects.none()
            self.fields['playlist'].queryset = TutorialPlaylist.objects.none()

        # Pre-populate playlist + order when editing an existing tutorial
        if self.instance and self.instance.pk:
            item = self.instance.playlist_items.first()
            if item:
                self.fields['playlist'].initial  = item.playlist_id
                self.fields['playlist_order'].initial = item.order
