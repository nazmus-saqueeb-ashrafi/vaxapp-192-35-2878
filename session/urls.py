from django.urls import path
from .views import SessionListView, SessionCreateView

app_name = 'session'

urlpatterns = [
    path('', SessionListView.as_view(), name='session-list'),
    path('create/', SessionCreateView.as_view(), name='session-create'),

]
