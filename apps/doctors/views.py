from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Doctor,TImeSlot
from .serializers import DoctorSerializer,TimeSlotSerializer,DoctorUpdateSerializers
from apps.users.models import CustomUser


class DoctorViewsets(ModelViewSet):
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = DoctorSerializer

class DoctortimeslotViewsets(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self,request:Request,pk)->Response:
        doctor = get_object_or_404(Doctor,pk=pk)
        data = doctor.timeslot.filter(is_available = "bo'sh")
        return Response(TimeSlotSerializer(data,many = True).data)
    
class DoctorProfileViewsets(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    def get(self,request:Request)->Response:
        return Response(DoctorSerializer(request.user.doctor).data)
    
    def patch(self,request:Request)->Response:
        serializer = DoctorUpdateSerializers(data = request.data,partial = True, instance=request.user.doctor,)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
