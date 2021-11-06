from session import views
from django.urls import path
from .views import SessionListView, SessionCreateView, SessionDetailView, SessionUpdateView, SessionDeleteView, SessionAssignView, SessionRunView

app_name = 'session'

urlpatterns = [
    path('', SessionListView.as_view(), name='session-list'),

    path('<int:pk>/', SessionDetailView.as_view(), name='session-detail'),
    path('<int:pk>/update/', SessionUpdateView.as_view(),
         name='session-update'),
    path('<int:pk>/delete/', SessionDeleteView.as_view(),
         name='session-delete'),
    path('<int:pk>/assign/', SessionAssignView.as_view(),
         name='session-assign'),
    path('<int:pk>/session-run/', SessionRunView.as_view(),
         name='session-run'),

    path('<int:pk>/patient-complete/', views.PatientComplete,
         name='patient-complete'),
    path('<int:pk>/patient-incomplete/', views.PatientIncomplete,
         name='patient-incomplete'),

    path('<int:pk>/session-complete/', views.SessionComplete,
         name='session-complete'),


    path('create/', SessionCreateView.as_view(), name='session-create'),



]
