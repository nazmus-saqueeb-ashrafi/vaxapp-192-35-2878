from django.http.response import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import Patient
from .forms import PatientModelForm, CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

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
    queryset = Patient.objects.all()
    context_object_name = "patients"


# def patient_details(request, pk):
#     print(pk)
#     patient = Patient.objects.get(id=pk)

#     context = {
#         "patient": patient
#     }
#     return render(request, "patients/patient_details.html", context=context)


class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "patients/patient_details.html"
    queryset = Patient.objects.all()
    context_object_name = "patient"


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


class PatientCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "patients/patient_create.html"
    form_class = PatientModelForm

    def get_success_url(self):
        return reverse("patients:patient-list")


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


class PatientUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "patients/patient_update.html"
    queryset = Patient.objects.all()
    form_class = PatientModelForm

    def get_success_url(self):
        return reverse("patients:patient-list")


# def patient_delete(request, pk):
#     patient = Patient.objects.get(id=pk)
#     patient.delete()

#     return redirect("/patients")


class PatientDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "patients/patient_delete.html"
    queryset = Patient.objects.all()

    def get_success_url(self):
        return reverse("patients:patient-list")
