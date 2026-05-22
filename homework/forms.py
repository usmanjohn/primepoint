from django import forms
from django.db.models import Q
from .models import Homework, HomeworkAssignment, PandaGroup
from panda.models import Panda
from practice.models import Practice


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        fields = ['title', 'practice', 'notes', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'e.g. Chapter 3 Review',
            }),
            'practice': forms.Select(attrs={'class': 'form-core'}),
            'notes': forms.Textarea(attrs={
                'class': 'form-core', 'rows': 3,
                'placeholder': 'Optional instructions for students…',
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-core', 'type': 'datetime-local',
            }),
        }

    def __init__(self, master=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if master:
            # Own published practices + other masters' shared published practices
            self.fields['practice'].queryset = Practice.objects.filter(
                Q(master=master, is_published=True) |
                Q(is_available_for_all=True, is_published=True)
            ).select_related('master').order_by('master__name', 'title')
        else:
            self.fields['practice'].queryset = Practice.objects.none()
        self.fields['practice'].required = True
        self.fields['notes'].required = False
        self.fields['due_date'].required = False


class HomeworkAssignForm(forms.Form):
    """Pick individual pandas and/or groups to assign homework to."""
    pandas = forms.ModelMultipleChoiceField(
        queryset=Panda.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        label='Individual students',
        required=False,
    )
    groups = forms.ModelMultipleChoiceField(
        queryset=PandaGroup.objects.none(),
        widget=forms.CheckboxSelectMultiple(),
        label='Groups',
        required=False,
    )

    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pandas'].queryset = Panda.objects.filter(masters=master).select_related('profile__user')
        self.fields['groups'].queryset = PandaGroup.objects.filter(master=master).prefetch_related('members')

    def get_all_pandas(self):
        selected = set(self.cleaned_data.get('pandas', []))
        for group in self.cleaned_data.get('groups', []):
            selected.update(group.members.all())
        return selected


class PandaGroupForm(forms.ModelForm):
    class Meta:
        model = PandaGroup
        fields = ['name', 'members']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-core', 'placeholder': 'e.g. Morning Class, Group A…',
            }),
            'members': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, master, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['members'].queryset = Panda.objects.filter(masters=master).select_related('profile__user')
        self.fields['members'].required = False
