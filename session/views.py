from django.http import request
from django.http.response import HttpResponse
from django.views import generic
from vaccinators.mixins import VaccinatorAndLoginRequiredMixin
from patients.models import Session, Patient
from .forms import SessionModelForm, AssignSessionForm
from django.shortcuts import redirect, reverse

from django.http import HttpResponseRedirect


# Create your views here.


class SessionListView(VaccinatorAndLoginRequiredMixin, generic.ListView):
    template_name = "session/session_list.html"

    def get_queryset(self):
        user = self.request.user
        queryset = Session.objects.filter(
            organisation=user.vaccinator.organisation,
            session_status="Incomplete")
        # filter for the vaccinator that is logged in
        queryset = queryset.filter(session_vaccinator__user=user)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(SessionListView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_vaccinator:
            queryset = Session.objects.filter(
                organisation=user.vaccinator.organisation,
                session_status="Complete"
            )
            context.update({
                "completed_sessions": queryset
            })

            return context


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
        session.session_status = "Incomplete"

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


class SessionRunView(VaccinatorAndLoginRequiredMixin, generic.ListView):
    template_name = "session/session_run.html"
    context_object_name = "session_patients"

    def get_queryset(self):
        user = self.request.user

        session = Session.objects.get(id=self.kwargs["pk"])
        return Patient.objects.filter(patient_session=session)

    def get_context_data(self, **kwargs):
        context = super(SessionRunView, self).get_context_data(**kwargs)

        context['session'] = Session.objects.get(id=self.kwargs["pk"])

        return context

    def get_success_url(self):
        return reverse("patients:patient-list")


def PatientComplete(request, pk):
    patient = Patient.objects.get(pk=pk)
    patient.patient_status = "Complete"

    print(patient.patient_status)
    patient.save()

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def PatientIncomplete(request, pk):
    patient = Patient.objects.get(pk=pk)
    patient.patient_status = "Incomplete"
    patient.save()

    return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))


def SessionComplete(request, pk):

    session = Session.objects.get(pk=pk)
    session.session_status = "Complete"
    session.save()

    return redirect("session:session-list")


# 2:44
