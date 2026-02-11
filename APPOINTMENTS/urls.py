
from django.urls import path

from .views import *

urlpatterns = [
 
    path('doctors/list/', DoctorListView.as_view(), name="doctors_list"),
    path('doctors/availability/', DoctorAvailabilityView.as_view(), name="doctors_availability" ),
    path('appointments/list/', AppointmentListView.as_view(), name="appointments_list"),
    path('appointments/delete/<int:id>/', AppointmentDeleteView.as_view(), name="appointments_delete"),
    path('appointments/details/<int:id>/', AppointmentDetailsView.as_view(), name="appointments_details"),
    path('appointments/create/', AppointmentCreateView.as_view(), name="appointments_create"),
    path('appointments/update/<int:id>/', AppointmentUpdateView.as_view(), name="appointments_update"),
    
]