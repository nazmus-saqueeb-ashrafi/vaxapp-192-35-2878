from django.views import generic
from vaccinators.mixins import VaccinatorAndLoginRequiredMixin
from patients.models import Session


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
