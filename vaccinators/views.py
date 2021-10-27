from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import reverse
from patients.models import Vaccinator
from .forms import VaccinatorModelForm
from .mixins import OrganisorAndLoginRequiredMixin, VaccinatorAndLoginRequiredMixin

import random

from django.core.mail import send_mail


class VaccinatorListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = "vaccinators/vaccinator_list.html"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Vaccinator.objects.filter(organisation=organisation)


class VaccinatorCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = "vaccinators/vaccinator_create.html"
    form_class = VaccinatorModelForm

    def get_success_url(self):
        return reverse("vaccinators:vaccinator-list")

    def form_valid(self, form):

        user = form.save(commit=False)

        user.is_vaccinator = True
        user.is_organisor = False
        user.is_patient = False

        user.set_password(f"{random.randint(0, 1000000)}")

        user.save()

        Vaccinator.objects.create(
            user=user,
            organisation=self.request.user.userprofile
        )

        # send_mail(
        #     subject="You are invited to be an vaccinator",
        #     message="You were added as an vaccinator at Vax App. Please come login to start working.",
        #     from_email="admin@test.com",
        #     recipient_list=[user.email]
        # )

        return super(VaccinatorCreateView, self).form_valid(form)


class VaccinatorDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "vaccinators/vaccinator_detail.html"
    context_object_name = "vaccinator"

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Vaccinator.objects.filter(organisation=organisation)


class VaccinatorUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "vaccinators/vaccinator_update.html"

    form_class = VaccinatorModelForm

    def get_success_url(self):
        return reverse("vaccinators:vaccinator-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Vaccinator.objects.filter(organisation=organisation)


class VaccinatorDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "vaccinators/vaccinator_delete.html"
    context_object_name = "vaccinator"

    def get_success_url(self):
        return reverse("vaccinators:vaccinator-list")

    def get_queryset(self):
        organisation = self.request.user.userprofile
        return Vaccinator.objects.filter(organisation=organisation)
