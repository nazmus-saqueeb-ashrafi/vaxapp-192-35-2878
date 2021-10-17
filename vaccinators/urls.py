from django.urls import path
from .views import (VaccinatorListView, VaccinatorCreateView, VaccinatorDetailView,
                    VaccinatorUpdateView, VaccinatorDeleteView)

app_name = 'vaccinators'

urlpatterns = [
    path('', VaccinatorListView.as_view(), name='vaccinator-list'),
    path('<int:pk>/', VaccinatorDetailView.as_view(), name='vaccinator-detail'),
    path('<int:pk>/update/', VaccinatorUpdateView.as_view(),
         name='vaccinator-update'),
    path('<int:pk>/delete/', VaccinatorDeleteView.as_view(),
         name='vaccinator-delete'),
    path('create/', VaccinatorCreateView.as_view(), name='vaccinator-create'),
]
