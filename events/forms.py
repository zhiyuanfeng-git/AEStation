from typing import Any
from django.forms import ModelForm
from .models import EventsModel
from django import forms

class DatePickerInput(forms.DateInput):
    input_type = 'date'

class EventsForm(ModelForm):
    class Meta:
        model = EventsModel
        fields = ('title', 'description', 'start_date', 'end_date', 'event_url',)
        widgets = {
            'start_date': DatePickerInput(),
            'end_date': DatePickerInput(),
        }
