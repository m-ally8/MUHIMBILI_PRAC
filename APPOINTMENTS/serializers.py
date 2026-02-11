from rest_framework import serializers 
from .models import *
from django.utils import timezone 
import datetime 

class DoctorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'        

class DoctorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class AppointmentDetailSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Appointment
        fields = ['patient', 'doctor', 'date', 'time_slot', 'status']


class AppointmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time_slot']

    # Function ya kuvalidate Mgonjwa asiweze kubook appointment ya tarehe ya nyuma
    # na asiweze kufanya double booking kweny time slot inayofanana

    def validate(self, attrs):
        dt = datetime.datetime.combine(attrs['date'], attrs['time_slot'])

        dt = timezone.make_aware(dt)

        if dt < timezone.now():
            raise serializers.ValidationError("You can not book appointment in the past")
        
        if Appointment.objects.filter(
            doctor= attrs['doctor'],
            date = attrs['date'],
            time_slot = attrs['time_slot'],
        ).exists():
            raise serializers.ValidationError("This time slot is already booked")
        return attrs  


class AppointmentDeleteSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Appointment
        fields = '__all__'

class AppointmentUpdateSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = Appointment
        fields = '__all__'

class DoctorAvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = ['specialization','availability']