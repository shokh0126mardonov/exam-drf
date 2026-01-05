from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    message = 'siz admin emassiz!'

    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
class PostPermissions(BasePermission):
    message = 'faqat post methodga ruxsat!'

    def has_permission(self, request, view):
        return request.method == 'POST'
    
class GetPermissions(BasePermission):
    message = 'faqat get methodga ruxsat!'

    def has_permission(self, request, view):
        return request.method == 'GET'