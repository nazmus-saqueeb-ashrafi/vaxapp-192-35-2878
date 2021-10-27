from django.urls import path
from .views import SessionListView

app_name = 'session'

urlpatterns = [
    path('', SessionListView.as_view(), name='session-list'),

]
