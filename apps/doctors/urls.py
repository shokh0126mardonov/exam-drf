from django.urls import path

from .views import DoctorViewsets,DoctortimeslotViewsets,DoctorProfileViewsets,PatientViewSets,TimeSlotViewSets

urlpatterns = [
    # Dcotor Api
    path('doctor/',DoctorViewsets.as_view({'get': 'list'})),
    path('doctor/<int:pk>/',DoctorViewsets.as_view({'get': 'retrieve'})),
    path('doctor/<int:pk>/timeslots/',DoctortimeslotViewsets.as_view()),

    #Doctor Profile Api
    path('doctor/profile/',DoctorProfileViewsets.as_view()),

    #Patient Api
    path('patient/profile/',PatientViewSets.as_view()),

    #Timeslot Api
    path('timeslots/',TimeSlotViewSets.as_view({'get': 'list'})),
    path('timeslots/<int:pk>/',TimeSlotViewSets.as_view({'get': 'retrieve','delete':'destroy','post':'create'})),
]
