from django import forms
from django.forms import inlineformset_factory
from django.utils.translation import gettext_lazy as _

from .models import Master, MasterCredential, MasterReview, MasterSubject, MAX_STARS

CORE = {'class': 'form-core'}


class MasterForm(forms.ModelForm):
    """Everything a master may edit about themselves.

    `is_powerty` and `powerty_role` are deliberately absent — the team badge is
    granted in the admin by the platform owner, never claimed on this form.
    """

    class Meta:
        model = Master
        fields = [
            'name', 'headline', 'photo', 'subject', 'category', 'description',
            'about', 'teaching_since', 'location', 'languages', 'lesson_format',
            'accepting_students', 'how_to_join',
            'telegram', 'phone', 'public_email', 'website',
        ]
        widgets = {
            'name': forms.TextInput(attrs={**CORE, 'placeholder': _('Your display name')}),
            'headline': forms.TextInput(attrs={
                **CORE, 'placeholder': _('e.g. IELTS and SAT tutor, 8 years teaching')}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-core', 'accept': 'image/*'}),
            'subject': forms.TextInput(attrs={
                **CORE, 'placeholder': _('e.g. Mathematics, Programming…')}),
            'category': forms.TextInput(attrs={
                **CORE, 'placeholder': _('e.g. Science, Languages…')}),
            'description': forms.Textarea(attrs={
                **CORE, 'rows': 3,
                'placeholder': _('One short paragraph shown on the masters list.')}),
            'about': forms.Textarea(attrs={
                **CORE, 'rows': 6,
                'placeholder': _('How you started teaching, how you teach, what your '
                                 'pupils achieve…')}),
            'teaching_since': forms.NumberInput(attrs={
                **CORE, 'min': 1950, 'max': 2100, 'placeholder': '2018'}),
            'location': forms.TextInput(attrs={
                **CORE, 'placeholder': _('e.g. Tashkent, Chilonzor')}),
            'languages': forms.TextInput(attrs={
                **CORE, 'placeholder': _('e.g. Uzbek, English, Russian')}),
            'lesson_format': forms.Select(attrs=CORE),
            'how_to_join': forms.Textarea(attrs={
                **CORE, 'rows': 4,
                'placeholder': _('Trial lesson, level test, when groups start, price…')}),
            'telegram': forms.TextInput(attrs={**CORE, 'placeholder': 'username'}),
            'phone': forms.TextInput(attrs={**CORE, 'placeholder': '+998 90 000 00 00'}),
            'public_email': forms.EmailInput(attrs={**CORE}),
            'website': forms.URLInput(attrs={**CORE, 'placeholder': 'https://…'}),
        }

    def clean_telegram(self):
        return self.cleaned_data['telegram'].strip().lstrip('@')


# Both formsets render a fixed number of blank rows rather than an "add row"
# button, so the edit page stays pure HTML — no JavaScript, per house rules.
MasterSubjectFormSet = inlineformset_factory(
    Master, MasterSubject,
    # `order` stays out: a teacher should not have to think about it, and the
    # model already falls back to creation order.
    fields=['name', 'level', 'note'],
    extra=3, can_delete=True,
    widgets={
        'name': forms.TextInput(attrs={**CORE, 'placeholder': _('e.g. IELTS')}),
        'level': forms.TextInput(attrs={**CORE, 'placeholder': _('e.g. Beginner → 7.5')}),
        'note': forms.TextInput(attrs={**CORE, 'placeholder': _('One line about it')}),
    },
)

MasterCredentialFormSet = inlineformset_factory(
    Master, MasterCredential,
    fields=['kind', 'title', 'issuer', 'year', 'note', 'image'],
    extra=2, can_delete=True,
    widgets={
        'kind': forms.Select(attrs=CORE),
        'title': forms.TextInput(attrs={**CORE, 'placeholder': _('e.g. IELTS 8.0')}),
        'issuer': forms.TextInput(attrs={**CORE, 'placeholder': _('University, board…')}),
        'year': forms.NumberInput(attrs={**CORE, 'min': 1950, 'max': 2100}),
        'note': forms.TextInput(attrs={**CORE}),
        'image': forms.ClearableFileInput(attrs={'class': 'form-core', 'accept': 'image/*'}),
    },
)


class MasterReviewForm(forms.ModelForm):
    """A pupil's 1-10 rating of their own master. The stars are a plain radio
    group styled with CSS — no script, and it works on a phone."""

    stars = forms.TypedChoiceField(
        choices=[(i, str(i)) for i in range(1, MAX_STARS + 1)],
        coerce=int, label=_('Your rating'),
        widget=forms.RadioSelect(attrs={'class': 'mrv-star-input'}),
    )

    class Meta:
        model = MasterReview
        fields = ['stars', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                **CORE, 'rows': 4, 'maxlength': 2000,
                'placeholder': _('What are their lessons like? What did you learn? '
                                 'Be honest and be fair.')}),
        }
