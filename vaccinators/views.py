from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from patients.models import Vaccinator
from .forms import VaccinatorModelForm


class VaccinatorListView(LoginRequiredMixin, generic.ListView):
    template_name = "vaccinators/vaccinator_list.html"

    def get_queryset(self):
        return Vaccinator.objects.all()


class VaccinatorCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "vaccinators/vaccinator_create.html"
    form_class = VaccinatorModelForm

    def get_success_url(self):
        return reverse("vaccinators:vaccinator-list")

    def form_valid(self, form):
        vaccinator = form.save(commit=False)
        vaccinator.organisation = self.request.user.userprofile
        vaccinator.save()
        return super(VaccinatorCreateView, self).form_valid(form)


class VaccinatorDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "vaccinators/vaccinator_detail.html"
    context_object_name = "vaccinator"

    def get_queryset(self):
        return Vaccinator.objects.all()


class VaccinatorUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = "vaccinators/vaccinator_update.html"

    form_class = VaccinatorModelForm

    def get_success_url(self):
        return reverse("vaccinators:vaccinator-list")

    def get_queryset(self):
        return Vaccinator.objects.all()


class VaccinatorDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "vaccinators/vaccinator_delete.html"
    context_object_name = "vaccinator"

    def get_success_url(self):
        return reverse("vaccinators:vaccinator-list")

    def get_queryset(self):
        return Vaccinator.objects.all()
