"""The one form of the app: which date, and whether to ask the database again."""
from django import forms


class DayForm(forms.Form):
    date = forms.DateField(
        label="Дата",
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}, format="%Y-%m-%d"),
    )
    refresh = forms.BooleanField(
        label="Загрузить заново из базы",
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
    )
