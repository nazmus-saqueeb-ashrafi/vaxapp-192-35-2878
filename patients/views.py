from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import Patient
from .forms import PatientModelForm, CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

from vaccinators.mixins import OrganisorAndLoginRequiredMixin

import random

from patients.models import User

# Create your views here.


class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")


# def landing_page(request):
#     return render(request, "landing.html")


class LandingPageView(generic.TemplateView):
    template_name = "landing.html"


# def patient_list(request):
#     patients = Patient.objects.all()
#     context = {
#         "patients": patients
#     }
#     return render(request, "patients/patient_list.html", context=context)


class PatientListView(LoginRequiredMixin, generic.ListView):
    template_name = "patients/patient_list.html"

    context_object_name = "patients"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of patient for the entire organisation
        if user.is_organisor:
            queryset = Patient.objects.filter(organisation=user.userprofile)
        elif user.is_vaccinator:
            queryset = Patient.objects.filter(
                organisation=user.vaccinator.organisation)
            # filter for the vaccinator that is logged in
            queryset = queryset.filter(patient_vaccinator__user=user)
        else:
            queryset = Patient.objects.all()
            queryset = Patient.objects.filter(user_id=user.id)

        return queryset


# def patient_details(request, pk):
#     print(pk)
#     patient = Patient.objects.get(id=pk)

#     context = {
#         "patient": patient
#     }
#     return render(request, "patients/patient_details.html", context=context)


class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    # TODO: OrganisorAndVaccinatorandLoginRequiredMixin

    template_name = "patients/patient_details.html"

    context_object_name = "patient"

    def get_queryset(self):
        user = self.request.user
        # initial queryset of leads for the entire organisation
        if user.is_organisor:
            queryset = Patient.objects.filter(organisation=user.userprofile)
        else:
            queryset = Patient.objects.filter(
                organisation=user.vaccinator.organisation)
            # filter for the agent that is logged in
            queryset = queryset.filter(patient_vaccinator__user=user)
        return queryset


# def patient_create(request):
#     form = PatientModelForm()

#     if request.method == "POST":
#         form = PatientModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#             return redirect("/patients")

#     context = {
#         "form": form
#     }

#     return render(request, "patients/patient_create.html", context)


class PatientCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "patients/patient_create.html"
    form_class = PatientModelForm

    def get_success_url(self):
        return reverse("patients:patient-list")

    def form_valid(self, form):
        patient = form.save(commit=False)

        user = User.objects.create(

            email=patient.patient_email,
            username=patient.patient_email,
            first_name=patient.patient_first_name,
            last_name=patient.patient_last_name,

            is_vaccinator=False,
            is_organisor=False,
            is_patient=True,

            password=f"{random.randint(0, 1000000)}"
        )

        patient.organisation = self.request.user.userprofile
        patient.user = user
        patient.patient_status = "Unassigned"

        # user.set_password(f"{random.randint(0, 1000000)}")

        patient.save()

        # send_mail(
        #     subject="You were registered as a patient",
        #     message="You were added as an patient at Vax App. Please come login to check your status.",
        #     from_email="admin@test.com",
        #     recipient_list=[user.email]
        # )

        return super(PatientCreateView, self).form_valid(form)


# def patient_update(request, pk):
#     patient = Patient.objects.get(id=pk)
#     form = PatientModelForm(instance=patient)

#     if request.method == "POST":
#         form = PatientModelForm(request.POST, instance=patient)
#         if form.is_valid():

#             form.save()
#             return redirect("/patients")
#             # redirect to / patients/pk

#     context = {
#         "form": form,
#         "patient": patient,
#     }

#     return render(request, "patients/patient_update.html", context)


class PatientUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "patients/patient_update.html"

    form_class = PatientModelForm

    def get_queryset(self):
        # initial queryset of leads for the entire organisation
        user = self.request.user
        return Patient.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("patients:patient-list")


# def patient_delete(request, pk):
#     patient = Patient.objects.get(id=pk)
#     patient.delete()

#     return redirect("/patients")


class PatientDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "patients/patient_delete.html"

    def get_queryset(self):
        # initial queryset of leads for the entire organisation
        user = self.request.user
        return Patient.objects.filter(organisation=user.userprofile)

    def get_success_url(self):
        return reverse("patients:patient-list")
