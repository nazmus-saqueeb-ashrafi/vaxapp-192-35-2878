from django import forms
from patients.models import Session


class SessionModelForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = {
            'session_name',
            'session_date',
            'session_time',
            'session_status',

        }
