from django.urls import path
from .views import SessionListView, SessionCreateView, SessionDetailView, SessionUpdateView, SessionDeleteView, SessionAssignView

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


    path('create/', SessionCreateView.as_view(), name='session-create'),



]
