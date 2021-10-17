from django.contrib import admin
from .models import User, Patient, Session, Vaccinator, UserProfile

# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Patient)
admin.site.register(Session)
admin.site.register(Vaccinator)
