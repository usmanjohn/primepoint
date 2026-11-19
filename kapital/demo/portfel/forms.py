from django import forms
from datetime import datetime

class DateInputForm(forms.Form):
    selected_date = forms.DateField(label = 'выберите дату',
    widget = forms.DateInput(attrs = {'type':'date', 'value':datetime.now().strftime("%d%m%Y")}))