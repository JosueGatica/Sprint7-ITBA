# En forms.py
from django import forms
from .models import Prestamo

class SolicitudPrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['loan_type', 'loan_date']
