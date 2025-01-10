from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime


APPOINTMENT_STATUS = [
    ("Completed", "Completed"),
    ("Running", "Running"),
    ("Pending", "Pending"),
]
APPOINTMENT_TYPE = [
    ("Online", "Online"),
    ("Offline", "Offline"),
]

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=10, choices=APPOINTMENT_TYPE)
    appointment_status = models.CharField(max_length=10, choices=APPOINTMENT_STATUS, default="Pending")
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
