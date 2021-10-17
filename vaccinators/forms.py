from django import forms
from patients.models import Vaccinator


class VaccinatorModelForm(forms.ModelForm):
    class Meta:
        model = Vaccinator
        fields = (
            'user',
        )
