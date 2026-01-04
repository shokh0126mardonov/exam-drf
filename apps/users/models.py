from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    class Role(models.TextChoices):
        Admin = 'ADMIN' , 'Admin'
        Doctor = 'DOCTOR' , 'Doctor'
        Patient = 'PATIENT' , 'Patient'

    role = models.CharField(max_length=10, choices=Role.choices)
 
    @property
    def is_patient(self):
        return self.role == self.Role.Patient
    
    @property
    def is_admin(self):
        return self.role == self.Role.Admin
    
    @property
    def is_doctor(self):
        return self.role == self.Role.Doctor