# En forms.py
from django import forms
from .models import Prestamo, Cliente, Cuenta

class SolicitudPrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = ['loan_type', 'loan_date']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'  # Incluye todos los campos del modelo

class CuentaBancariaFormulario(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = '__all__'