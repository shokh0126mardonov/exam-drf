from rest_framework.permissions import BasePermission


class IsDoctor(BasePermission):
    message = 'siz doctor emassiz'

    def has_permission(self, request, view):
        return request.user.is_doctor
    
class IsPatient(BasePermission):
    message = 'siz patient emassiz'

    def has_permission(self, request, view):
        return request.user and request.is_patient