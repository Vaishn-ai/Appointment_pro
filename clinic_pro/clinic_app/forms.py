from .models import Appointment
from django import forms
from django.core import validators

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = "__all__"

        widgets = {
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_age': forms.NumberInput(attrs={'class': 'form-control'}),  
            'patient_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'appointment_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'appointment_time': forms.TimeInput (attrs={'class': 'form-control', 'type': 'time'}),
        }

    def clean_patient_age(self):
        age = self.cleaned_data['patient_age']
        if age < 0:
            raise validators.ValidationError("Enter valid age.")
        return age

    def clean_patient_phone(self):
        phone=self.cleaned_data['patient_phone']
        if len(str(phone)) != 10:
            print(phone)
            raise validators.ValidationError('Phone number must be 10 digits')
        if phone[0] not in ['7', '8', '9']:
            raise validators.ValidationError("Phone number must start with 7, 8, or 9")
        return phone

    def clean_patient_name(self):
        name=self.cleaned_data['patient_name']
        if len(name) < 3:
            raise validators.ValidationError('Name must be at least 3 characters long')
        return name
        