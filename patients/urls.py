from django.urls import path
from .views import PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView, AssignVaccinatorView, StatisticsView

app_name = "patients"

urlpatterns = [
    path('', PatientListView.as_view(), name='patient-list'),
    path('create/', PatientCreateView.as_view(), name='patient-create'),
    path('statistics/', StatisticsView.as_view(), name='patient-statistics'),
    path('<pk>/', PatientDetailView.as_view(), name='patient-details'),
    path('<pk>/update', PatientUpdateView.as_view(), name='patient-update'),
    path('<pk>/delete', PatientDeleteView.as_view(), name='patient-delete'),
    path('<int:pk>/assign-vaccinator/',
         AssignVaccinatorView.as_view(), name='assign-vaccinator'),

]
