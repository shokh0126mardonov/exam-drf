from rest_framework import serializers

from .models import Doctor,TImeSlot,Patient
from apps.users.serializers import UserSerializer


class DoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)
    class Meta:
        model = Doctor
        fields = ['specialization','experience_years','gender','user']


class TimeSlotSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only = True)
    class Meta:
        model = TImeSlot
        fields = ['doctor','date','start_time','end_time','is_available']


class DoctorUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ['user']


class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class TimeslotSerializers(serializers.ModelSerializer):
    doctor = DoctorSerializer(read_only = True)
    class Meta:
        model = TImeSlot
        fields = ['doctor','date','start_time','end_time','is_available']