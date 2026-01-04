from django.db import models

from apps.doctors.models import Doctor,TImeSlot,Patient


class Appointment(models.Model):
    class AppoinrmentStatus(models.TextChoices):
        pending = 'pending','Pending'
        confirmed = 'confirmed','Confirmed'
        cancelled = 'cancelled','Cancelled'

    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointment')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,related_name='appointment')
    timeslot = models.OneToOneField(TImeSlot,  on_delete=models.CASCADE,related_name='appointment')
    status = models.CharField(choices=AppoinrmentStatus.choices, max_length=10)
    created_at = models.DateTimeField(auto_now_add=False)