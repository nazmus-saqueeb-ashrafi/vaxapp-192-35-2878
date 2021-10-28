from django.views import generic
from vaccinators.mixins import VaccinatorAndLoginRequiredMixin
from patients.models import Session
from .forms import SessionModelForm
from django.shortcuts import reverse


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
