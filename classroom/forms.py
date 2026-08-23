from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

from .models import (
    Classroom, Lesson, LessonNote, ClassroomDiscussion, ClassroomReply,
    ClassroomResource,
)
from homework.models import PandaGroup, Homework
from panda.models import Panda
from practice.models import Practice
from tutorial.models import Tutorial
from masters.models import StudentPayment, Attendance, Certificate
from . import content


class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['name', 'subject', 'description', 'cover_color', 'is_active']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-core',
                'placeholder': 'e.g. Korean Classroom 1',
            }),
            'subject': forms.Select(attrs={'class': 'form-core'}),
            'description': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 3,
                'placeholder': 'What is this classroom about?',
            }),
            'cover_color': forms.TextInput(attrs={
                'class': 'form-core color-input', 'type': 'color',
            }),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['subject'].required = False
        self.fields['subject'].empty_label = _('All subjects (no filtering)')


class ClassroomMembershipForm(forms.Form):
    groups = forms.ModelMultipleChoiceField(
        queryset=PandaGroup.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label=_('Attach groups'),
    )
    individual_pandas = forms.ModelMultipleChoiceField(
        queryset=Panda.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        required=False,
        label=_('Add individual students'),
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
        fields = ['title', 'description', 'youtube_url', 'order', 'status',
                  'is_published', 'practices', 'tutorials']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'e.g. Lesson 1 — Greetings',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 3,
            }),
            'youtube_url': forms.URLInput(attrs={
                'class': 'form-core', 'placeholder': 'https://www.youtube.com/watch?v=...',
            }),
            'order': forms.NumberInput(attrs={'class': 'form-core', 'min': 0}),
            'status': forms.Select(attrs={'class': 'form-core'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'practices': forms.SelectMultiple(attrs={'class': 'form-core', 'size': 8}),
            'tutorials': forms.SelectMultiple(attrs={'class': 'form-core', 'size': 8}),
        }

    def __init__(self, master, classroom=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Narrowed to what this room teaches — see classroom/content.py.
        self.fields['practices'].queryset = content.practice_queryset(classroom, master)
        self.fields['tutorials'].queryset = content.tutorial_queryset(classroom)
        self.fields['practices'].required = False
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


class ClassroomResourceForm(forms.ModelForm):
    class Meta:
        model = ClassroomResource
        fields = ['kind', 'title', 'description', 'link', 'file', 'order']
        widgets = {
            'kind': forms.Select(attrs={'class': 'form-core'}),
            'title': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'e.g. Unit 3 vocabulary sheet',
            }),
            'description': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'One line about it (optional)',
            }),
            'link': forms.URLInput(attrs={
                'class': 'form-core', 'placeholder': 'https://…',
            }),
            'file': forms.ClearableFileInput(attrs={'class': 'form-core'}),
            'order': forms.NumberInput(attrs={'class': 'form-core', 'min': 0}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ('description', 'link', 'file', 'order'):
            self.fields[name].required = False

    def clean(self):
        data = super().clean()
        if not data.get('link') and not data.get('file'):
            raise forms.ValidationError(_('Add a link or upload a file.'))
        return data


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


# ── Homework ───────────────────────────────────────────────────────────────

class HomeworkForm(forms.ModelForm):
    """Just the wrapper: what it is called, when it is due, who gets it.

    The contents are added afterwards, one at a time, on the homework page.
    That is deliberate: a picker holding 400 tutorials cannot be searched and
    submitted in one form without JavaScript, and a master who searches twice
    would lose the first selection every time. Adding items one by one against
    a search box keeps the whole flow server-rendered and never loses state.
    """

    class Meta:
        model = Homework
        fields = ['title', 'notes', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': _('e.g. Lesson 12 — home work'),
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 3,
                'placeholder': _('Instructions for your students (optional)…'),
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-core', 'type': 'datetime-local',
            }, format='%Y-%m-%dT%H:%M'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['notes'].required = False
        self.fields['due_date'].required = False


class HomeworkAssignForm(forms.Form):
    """Who in this room gets it. Scoped to the room, not to the whole school."""
    pandas = forms.ModelMultipleChoiceField(
        queryset=Panda.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        label=_('Students'),
        required=False,
    )
    groups = forms.ModelMultipleChoiceField(
        queryset=PandaGroup.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        label=_('Groups'),
        required=False,
    )
    everyone = forms.BooleanField(
        required=False, initial=True, label=_('Everyone in this classroom'),
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    def __init__(self, classroom, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.classroom = classroom
        self.fields['pandas'].queryset = (
            classroom.get_all_pandas().select_related('profile__user'))
        self.fields['groups'].queryset = classroom.groups.prefetch_related('members')

    def get_all_pandas(self):
        if self.cleaned_data.get('everyone'):
            return set(self.classroom.get_all_pandas())
        selected = set(self.cleaned_data.get('pandas', []))
        members = {p.pk for p in self.classroom.get_all_pandas()}
        for group in self.cleaned_data.get('groups', []):
            selected.update(group.members.all())
        # Never assign to someone who is not in this room, whatever was posted.
        return {p for p in selected if p.pk in members}


class PandaGroupForm(forms.ModelForm):
    """A named subset of a master's pupils — 'Morning class', 'Group B'."""

    class Meta:
        model = PandaGroup
        fields = ['name', 'members']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': _('e.g. Morning Class, Group A…'),
            }),
            'members': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['members'].queryset = (
            Panda.objects.filter(masters=master).select_related('profile__user'))
        self.fields['members'].required = False


# ── Money, attendance, certificates ────────────────────────────────────────

class PaymentForm(forms.ModelForm):
    class Meta:
        model = StudentPayment
        fields = ['amount', 'period_label', 'status', 'due_date', 'payment_date', 'notes']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-core', 'step': '1000', 'min': 0, 'placeholder': '500000',
            }),
            'period_label': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': _('e.g. Sentabr 2026'),
            }),
            'status': forms.Select(attrs={'class': 'form-core'}),
            'due_date': forms.DateInput(attrs={'class': 'form-core', 'type': 'date'}),
            'payment_date': forms.DateInput(attrs={'class': 'form-core', 'type': 'date'}),
            'notes': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': _('Note (optional)'),
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in ('period_label', 'due_date', 'payment_date', 'notes'):
            self.fields[name].required = False


class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['date', 'status', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-core', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-core'}),
            'notes': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': _('Note (optional)'),
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['notes'].required = False


class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': _('e.g. Beginner Korean — completed'),
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 2,
                'placeholder': _('What it is for (optional)'),
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].required = False


class AddStudentForm(forms.Form):
    """Pull an existing pupil into this room by username."""
    username = forms.CharField(
        label=_('Student username'),
        widget=forms.TextInput(attrs={
            'class': 'form-core', 'placeholder': _('their username'),
        }),
    )

    def clean_username(self):
        from django.contrib.auth.models import User
        username = self.cleaned_data['username'].strip()
        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            raise forms.ValidationError(
                _('No user found with username "%(name)s".') % {'name': username})
        panda = getattr(getattr(user, 'profile', None), 'panda', None)
        if panda is None:
            raise forms.ValidationError(_('That user does not have a student profile.'))
        self.panda = panda
        return username
