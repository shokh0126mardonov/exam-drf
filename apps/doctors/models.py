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
    gender = models.CharField(max_length=6, choices=Gender.choices)


class TImeSlot(models.Model):
    class Available(models.TextChoices):
        bosh = 'bo\'sh', 'Bo\'sh'
        band = 'band', 'Band'

    doctor = models.ForeignKey("Doctor", verbose_name=("shifokor qabul vaqti"), on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.CharField(choices=Available.choices,default=Available.bosh, max_length=5)