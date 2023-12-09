# En forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
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

class ClienteLoginForm(AuthenticationForm):
    customer_name = forms.CharField(max_length=100, required=True, label='Nombre')
    customer_surname = forms.CharField(max_length=100, required=True, label='Apellido')

    def __init__(self, *args, **kwargs):
        super(ClienteLoginForm, self).__init__(*args, **kwargs)
        # Elimina los campos no deseados
        del self.fields['username']
        del self.fields['password']