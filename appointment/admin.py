from django.contrib import admin
from appointment.models import Appointment
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'doctor_name', 'appointment_type', 'appointment_status', 'time', 'cancel']

    def patient_name(self, obj):
        return obj.patient.user.username

    def doctor_name(self, obj):
        return obj.doctor.user.username

    def save_model(self, request, obj, form, change):
        obj.save()
        if obj.appointment_status == "Running" and obj.appointment_type == "Online":
            email_sub = "Your Online Appointment is Running!"
            email_body = render_to_string('appointment/running_appointment.html', {'user' : obj.patient.user, 'doctor':obj.doctor})
            email = EmailMultiAlternatives(email_sub, email_body, '', to=[obj.patient.user.email])
            email.attach_alternative(email_body, "text/html")
            email.send()

admin.site.register(Appointment, AppointmentAdmin)