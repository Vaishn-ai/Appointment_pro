from django.contrib import admin
from .models import Appointment

# Register your models here.

#way-1
#admin.site.register(Appointment)

#way-2
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient_name']
