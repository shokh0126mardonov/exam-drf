from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import Register,Userdata,AdminManageApi

urlpatterns = [

    # Auth api
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', Register.as_view(), name='register_page'),
    path('auth/me/', Userdata.as_view(), name='register_page'),

    #Admin api
    path('users/',AdminManageApi.as_view({'get':'list'}),name='Admin-managment'),
    path('users/<int:pk>/',AdminManageApi.as_view({'get':'retrieve','patch':'partial_update','delete':'destroy'}),name='Admin-managment-detail')
]