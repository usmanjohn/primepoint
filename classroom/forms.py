from django import forms
from .models import Classroom, Lesson, LessonNote, ClassroomDiscussion, ClassroomReply
from homework.models import PandaGroup
from panda.models import Panda
from practice.models import Practice
from homework.models import Homework
from tutorial.models import Tutorial
from django.db.models import Q


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'description', 'cover_color', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-core',
                'placeholder': 'e.g. Korean Classroom 1',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 3,
                'placeholder': 'What is this classroom about?',
            }),
            'cover_color': forms.TextInput(attrs={
                'class': 'form-core color-input', 'type': 'color',
            }),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ClassroomMembershipForm(forms.Form):
    groups = forms.ModelMultipleChoiceField(
        queryset=PandaGroup.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label='Attach groups',
    )
    individual_pandas = forms.ModelMultipleChoiceField(
        queryset=Panda.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label='Add individual students',
    )

    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].queryset = PandaGroup.objects.filter(master=master)
        self.fields['individual_pandas'].queryset = (
            Panda.objects.filter(masters=master).select_related('profile__user')
        )


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'description', 'order', 'is_published', 'practices', 'homeworks', 'tutorials']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'e.g. Lesson 1 — Greetings',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 3,
            }),
            'order': forms.NumberInput(attrs={'class': 'form-core', 'min': 0}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'practices': forms.CheckboxSelectMultiple(),
            'homeworks': forms.CheckboxSelectMultiple(),
            'tutorials': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['practices'].queryset = Practice.objects.filter(
            Q(master=master, is_published=True) | Q(is_available_for_all=True, is_published=True)
        )
        self.fields['homeworks'].queryset = Homework.objects.filter(master=master)
        self.fields['tutorials'].queryset = Tutorial.objects.filter(
            author=master.profile.user, is_published=True
        )
        self.fields['practices'].required = False
        self.fields['homeworks'].required = False
        self.fields['tutorials'].required = False


class LessonNoteForm(forms.ModelForm):
    class Meta:
        model = LessonNote
        fields = ['title', 'file']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'Note title (optional)',
            }),
            'file': forms.ClearableFileInput(attrs={'class': 'form-core'}),
        }


class ClassroomDiscussionForm(forms.ModelForm):
    class Meta:
        model = ClassroomDiscussion
        fields = ['title', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'Discussion title…',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 5,
                'placeholder': 'Start the discussion…',
            }),
        }


class ClassroomReplyForm(forms.ModelForm):
    class Meta:
        model = ClassroomReply
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 3,
                'placeholder': 'Write your reply…',
            }),
        }
        labels = {'body': ''}
