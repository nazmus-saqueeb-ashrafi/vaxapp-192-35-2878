from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.

AGE_GROUP_CHOICES = (
    ('0-14', '0-14'),
    ('15-24', '15-24'),
    ('25-64', '25-64'),
    ('65+', '65+'),
)

PATIENT_MATERNAL_STATUS = (
    ('Pregnant', 'Pregnant'),
    ('Not Pregnant', 'Not Pregnant'),
)

PATIENT_SMOKING_STATUS = (
    ('Smoker', 'Smoker'),
    ('Non smoker', 'Non smoker'),
)

PATIENT_GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

PATIENT_STATUS = (
    ('Incomplete', 'Incomplete'),
    ('Complete', 'Complete'),
)

PATIENT_JOB_STATUS = (
    ('Unemployed', 'Unemployed'),
    ('Employed', 'Employed'),
    ('Student', 'Student'),
    ('Retired', 'Retired'),
)


SESSION_STATUS = (
    ('Complete', 'Complete'),
    ('Incomplete', 'Incomplete'),
)


# ------


class User(AbstractUser):
    is_organisor = models.BooleanField(default=True)
    is_vaccinator = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# ------

# Leads
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    patient_first_name = models.CharField(max_length=100)
    patient_last_name = models.CharField(max_length=100)
    patient_email = models.EmailField(max_length=70)
    patient_username = models.CharField(max_length=100)

    # patient_age_group = models.CharField(
    #     choices=AGE_GROUP_CHOICES, max_length=100)

    patient_age = models.IntegerField()
    patient_maternal_status = models.CharField(
        choices=PATIENT_MATERNAL_STATUS, max_length=100)
    patient_smoking_status = models.CharField(
        choices=PATIENT_SMOKING_STATUS, max_length=100)
    patient_gender = models.CharField(
        choices=PATIENT_GENDER_CHOICES, max_length=100)
    patient_status = models.CharField(
        choices=PATIENT_STATUS, max_length=100)
    patient_job_status = models.CharField(
        choices=PATIENT_JOB_STATUS, max_length=100)
    patient_NID = models.IntegerField()

    patient_vaccinator = models.ForeignKey(
        "Vaccinator", null=True, blank=True, on_delete=models.SET_NULL)
    patient_session = models.ForeignKey(
        "Session", null=True, blank=True, on_delete=models.SET_NULL)

    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient_first_name


# Catagory !
class Session(models.Model):
    session_name = models.CharField(max_length=100)
    session_date = models.DateField()
    session_time = models.TimeField()
    session_status = models.CharField(
        choices=SESSION_STATUS, max_length=100)

    session_vaccinator = models.ForeignKey(
        "Vaccinator", on_delete=models.CASCADE)
    organisation = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.session_name


# Agent !
class Vaccinator(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email

# -------

# create UserProfile when User is created using post_save signal


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
