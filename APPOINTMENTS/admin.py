from django.contrib import admin
from .models  import *

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['gender']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [ "specialization", "availability"]


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ["patient", "doctor", "date", "time_slot", "status"]