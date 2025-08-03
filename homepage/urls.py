from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='homeurl'),
    path('op/',views.Patientop.as_view(),name='patientopurl'),
    path('doctor/',views.AddDoctor.as_view(),name='adddoctorurl'),
    path('appointment/',views.Appointments.as_view(),name='appointmenturl'),
    path('ourdoctors/',views.OurDoctors.as_view(),name='ourdoctorsurl'),
    path('doc_slots/<int:pk>/',views.DoctorSlots.as_view(),name='doctorslotsurl'),

    
]