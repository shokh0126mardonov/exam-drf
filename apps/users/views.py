from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .permissons import IsAdmin,PostPermissions
from .serializers import RegisterSerializer,UserSerializer


class Register(APIView):
    permission_classes = [IsAdmin,IsAuthenticated,PostPermissions]
    authentication_classes = [JWTAuthentication]

    def post(self,requets:Request)->Response:
        serializers = RegisterSerializer(data = requets.data)
        if serializers.is_valid(raise_exception=True):
            user = serializers.save()
            data = UserSerializer(user).data
            return Response(data=data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)