from django.db import models
from django.conf import settings


class Doctor(models.Model):
    class Gender(models.TextChoices):
        Male = 'MALE','Erkak'
        Female = 'FEMALE','Ayol'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='doctor')
    specialization = models.CharField()
    experience_years = models.IntegerField()
    gender = models.CharField(choices=Gender.choices)


class Patient(models.Model):
    class Gender(models.TextChoices):
        Male = 'MALE','Erkak'
        Female = 'FEMALE','Ayol'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='patient')
    phone = models.CharField( max_length=13)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=6, choices=Gender)