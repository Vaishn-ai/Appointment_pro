from django.shortcuts import render, redirect
from .models import Appointment
from .forms import AppointmentForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


# Create our views here.
def create_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_urls')
    template_name='clinic_app/form.html'
    context = {'form' : form}
    return render(request, template_name, context)

def show_appointments(request):
    appointments =Appointment.objects.all()
    name = request.GET.get('patient_name')
    date = request.GET.get('date')
    time = request.GET.get('time')
    print(name, date, time)
    template_name="clinic_app/show.html"
    context={'appointments' : appointments}
    return render(request, template_name, context)

def info_appointment(request, pk):
    template_name="clinic_app/info.html"
    appointment = get_object_or_404 (Appointment, pk=pk)
    context={'appointment' : appointment}
    return render(request, template_name, context)


def update_appointment(request, pk):
    template_name = "clinic_app/form.html"
    appointment = get_object_or_404(Appointment, pk = pk)
    form = AppointmentForm(instance=appointment)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, request.FILES, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('show_appointment_urls')
    context = {'form' : form}
    return render(request, template_name, context)

def delete_appointment(request, pk):
    appointmnet = get_object_or_404(Appointment, pk=pk)
    appointmnet.delete()
    return redirect('show_appointment_urls')


def home(request):
    template_name = 'clinic_app/home.html'
    return render(request, template_name)
