
from os import name
from django.contrib import admin
from django.urls import path, include
from patients.views import LandingPageView, SignupView

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LandingPageView.as_view(), name='landing-page'),
    path('patients/', include('patients.urls', namespace="patients")),
    path('vaccinators/', include('vaccinators.urls', namespace="vaccinators")),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
