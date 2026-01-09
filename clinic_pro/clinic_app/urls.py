from .views import create_appointment, show_appointments
from django.urls import path
from .views import info_appointment, update_appointment, delete_appointment, home


urlpatterns = [
    path('create-appointment/', create_appointment, name='create_appointment_urls'),
    path('show-appointment/', show_appointments, name='show_appointment_urls'),
    path('info-appointment/<int:pk>/', info_appointment, name='info_appointment_urls'),
    path('update-appointment/<int:pk>/', update_appointment, name='update_appointment_urls'),
    path('delete-appointment/<int:pk>/', delete_appointment, name='delete_appointment_urls'),
    path('', home, name='home_urls'),
]