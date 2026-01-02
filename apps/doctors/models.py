from django.db import models
from django.conf import settings

from ..users.models import CustomUser

class Doctor(models.Model):
    class Gender(models.TextChoices):
        Male = 'MALE','Erkak'
        Female = 'FEMALE','Ayol'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    specialization = models.CharField()
    experience_years = models.IntegerField()
    gender = models.CharField(choices=Gender.choices)