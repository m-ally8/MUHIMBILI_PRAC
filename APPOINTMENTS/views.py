from django.shortcuts import render
from rest_framework import generics
from . serializers import *
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.
class DoctorListView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorListSerializer


class AppointmentListView(generics.ListAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentListSerializer 


class DoctorDetailsView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailsSerializer


class AppointmentDetailsView(generics.RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentDetailSerializer
    lookup_field = 'id'


class AppointmentCreateView(generics.CreateAPIView):
    serializer_class = AppointmentCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(patient=self.request.user, status='PENDING')


class AppointmentDeleteView(generics.DestroyAPIView):
    serializer_class = AppointmentDeleteSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return Appointment.objects.filter(patient = self.request.user)


class AppointmentUpdateView(generics.UpdateAPIView):
    serializer_class = AppointmentUpdateSerializer
    lookup_field = 'id'
    
    def get_queryset(self):
        return Appointment.objects.filter(patient=self.request.user)


class DoctorAvailabilityView(generics.ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorAvailabilitySerializer
    # permission_classes = [IsAuthenticated]
    
    
    # def get(self):
    #     doctor = self.request.user.doctor
    #     serializer = DoctorAvailabilitySerializer(doctor)
    #     return Response(serializer.data)