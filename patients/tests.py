from django.test import TestCase
from django.shortcuts import reverse

from .forms import PatientModelForm


class LandingPageTest(TestCase):

    def test_get(self):
        response = self.client.get(reverse("landing-page"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")


class TestPatientCreateForm(TestCase):
    def test_login_form_valid_data(self):
        form = PatientModelForm(data={
            'patient_first_name': 'Nazmus',
            'patient_last_name': 'Ashrafi',
            'patient_email': 'nazmus.as@gmail.com',
            'patient_username': 'nazmus',

            'patient_age': '10',
            'patient_gender': 'Male',
            'patient_maternal_status': 'Not Pregnant',
            'patient_smoking_status': 'Smoker',
            'patient_job_status': 'Unemployed',
            'patient_NID': '2222',
            'patient_vaccinator': '',
            'organisation': 'nazmus'

        })

        self.assertTrue(form.is_valid())

    def test_login_form_no_data(self):
        form = PatientModelForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 10)
