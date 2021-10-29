from django.views import generic
from vaccinators.mixins import VaccinatorAndLoginRequiredMixin
from patients.models import Session
from .forms import SessionModelForm, AssignSessionForm
from django.shortcuts import reverse

from patients.models import Patient


# Create your views here.


class SessionListView(VaccinatorAndLoginRequiredMixin, generic.ListView):
    template_name = "session/session_list.html"

    def get_queryset(self):
        user = self.request.user
        queryset = Session.objects.filter(
            organisation=user.vaccinator.organisation)
        # filter for the vaccinator that is logged in
        queryset = queryset.filter(session_vaccinator__user=user)

        return queryset


class SessionCreateView(VaccinatorAndLoginRequiredMixin, generic.CreateView):
    template_name = "session/session_create.html"
    form_class = SessionModelForm

    def get_success_url(self):
        return reverse("session:session-list")

    def form_valid(self, form):
        user = self.request.user

        session = form.save(commit=False)

        session.session_vaccinator = user.vaccinator
        session.organisation = user.vaccinator.organisation

        session.save()

        return super(SessionCreateView, self).form_valid(form)


class SessionDetailView(VaccinatorAndLoginRequiredMixin, generic.DetailView):
    template_name = "session/session_detail.html"
    context_object_name = "session"

    def get_queryset(self):
        # organisation = self.request.user.userprofile

        user = self.request.user
        return Session.objects.filter(session_vaccinator=user.vaccinator)


class SessionUpdateView(VaccinatorAndLoginRequiredMixin, generic.UpdateView):
    template_name = "session/session_update.html"

    form_class = SessionModelForm

    def get_success_url(self):
        return reverse("session:session-list")

    def get_queryset(self):
        user = self.request.user
        return Session.objects.filter(session_vaccinator=user.vaccinator)


class SessionDeleteView(VaccinatorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "session/session_delete.html"
    context_object_name = "session"

    def get_success_url(self):
        return reverse("session:session-list")

    def get_queryset(self):
        user = self.request.user
        return Session.objects.filter(session_vaccinator=user.vaccinator)


class SessionAssignView(VaccinatorAndLoginRequiredMixin, generic.FormView):
    template_name = "session/session_assign.html"
    form_class = AssignSessionForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(SessionAssignView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            "request": self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse("patients:patient-list")

    def form_valid(self, form):
        session = form.cleaned_data["session"]
        patient = Patient.objects.get(id=self.kwargs["pk"])
        patient.patient_session = session
        patient.save()
        return super(SessionAssignView, self).form_valid(form)


# 2:44
