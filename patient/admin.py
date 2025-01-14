from django.contrib import admin
from patient.models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'mobile']

    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name

admin.site.register(Patient, PatientAdmin)
