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


class AssignSessionForm(forms.Form):
    session = forms.ModelChoiceField(queryset=Session.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop("request")

        user = request.user

        sessions = Session.objects.filter(
            session_vaccinator=user.vaccinator)

        super(AssignSessionForm, self).__init__(*args, **kwargs)
        self.fields["session"].queryset = sessions
