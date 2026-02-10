from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Patient(models.Model):
    GENDER_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)

    def __str__(self):
        return self.user.username
    
    
class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('DENTISTRY', 'Dentistry'),
        ('CARDIOLOGIST', 'Cardiologist'),
        ('ORTHOPEDIST', 'Orthopedist'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(
        max_length=100,
        choices=SPECIALIZATION_CHOICES
    )
    availability = models.JSONField()

    def __str__(self):
        return f"Dr. {self.user.username} ({self.specialization})"


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    patient = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='appointments'
    )
    date = models.DateField(default=timezone.now)
    time_slot = models.TimeField(max_length=20)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    def __str__(self):
        return f"{self.patient.username} → {self.doctor}"
