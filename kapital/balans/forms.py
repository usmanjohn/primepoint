import datetime

from django import forms


def last_working_day():
    day = datetime.date.today() - datetime.timedelta(days=1)
    while day.weekday() >= 5:              # Saturday, Sunday -> Friday
        day -= datetime.timedelta(days=1)
    return day


class DateInputForm(forms.Form):
    selected_date = forms.DateField(
        label='Дата баланса',
        initial=last_working_day,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control form-control-lg'}, format='%Y-%m-%d'),
    )
