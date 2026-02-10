
from django.urls import path

from .views import *

urlpatterns = [
 
    path('doctors/list/', DoctorListView.as_view()),
    path('doctors/availability/', DoctorAvailabilityView.as_view() ),
    path('appointments/list/', AppointmentListView.as_view()),
    path('appointments/delete/<int:id>/', AppointmentDeleteView.as_view()),
    path('appointments/details/<int:id>/', AppointmentDetailsView.as_view()),
    path('appointments/create/', AppointmentCreateView.as_view()),
    path('appointments/update/<int:id>/', AppointmentUpdateView.as_view()),
    
]