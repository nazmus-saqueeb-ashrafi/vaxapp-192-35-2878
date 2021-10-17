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

PATIENT_TYPE_CHOICES = (
    ('Pregnant', 'Pregnant'),
    ('Not Pregnant', 'Not Pregnant'),
)

PATIENT_GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

PATIENT_STATUS = (
    ('Assigned', 'Assigned'),
    ('Unassigned', 'Unassigned'),
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
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# ------

# Leads
class Patient(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    patient_first_name = models.CharField(max_length=100)
    patient_last_name = models.CharField(max_length=100)

    # patient_age_group = models.CharField(
    #     choices=AGE_GROUP_CHOICES, max_length=100)

    patient_age = models.IntegerField()
    patient_type = models.CharField(
        choices=PATIENT_TYPE_CHOICES, max_length=100)
    patient_gender = models.CharField(
        choices=PATIENT_GENDER_CHOICES, max_length=100)
    patient_status = models.CharField(
        choices=PATIENT_STATUS, max_length=100)
    patient_job_status = models.CharField(
        choices=PATIENT_JOB_STATUS, max_length=100)
    patient_NID = models.IntegerField()

    patient_session = models.ForeignKey("Session", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient_first_name} {self.patient_last_name}"


# Catagory !
class Session(models.Model):
    session_name = models.CharField(max_length=100)
    session_date = models.DateField()
    session_time = models.TimeField()
    session_status = models.CharField(
        choices=SESSION_STATUS, max_length=100)

    session_vaccinator = models.ForeignKey(
        "Vaccinator", on_delete=models.CASCADE)

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
