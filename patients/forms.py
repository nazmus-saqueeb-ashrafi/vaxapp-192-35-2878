from django import forms
from django.db import models
from django.forms import fields
from .models import Patient, PATIENT_MATERNAL_STATUS, PATIENT_SMOKING_STATUS, PATIENT_GENDER_CHOICES, PATIENT_STATUS, PATIENT_JOB_STATUS

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField


User = get_user_model()


class PatientModelForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = {
            'patient_first_name',
            'patient_last_name',
            'patient_email',
            'patient_username',


            'patient_age',
            'patient_gender',
            'patient_maternal_status',
            'patient_smoking_status',
            'patient_job_status',
            'patient_NID',
            'patient_vaccinator',
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
