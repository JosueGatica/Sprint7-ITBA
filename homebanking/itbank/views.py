# En views.py
from django.contrib.auth.backends import ModelBackend
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SolicitudPrestamoForm,ClienteForm,CuentaBancariaFormulario,ClienteLoginForm
from django.contrib import messages
from .models import Cliente, Tarjeta, Cuenta
from django.contrib.auth import login, logout, authenticate

def home(request):
    return render(request,'home.html')

#PROBLEMATICA 2: Vistas

#Ver datos del cliente (nombre, apellido, etc)
def verDatosCliente(request, customer_id):
    cliente = Cliente.objects.get(pk=customer_id)
    return render(request, 'verDatosCliente.html',{
        "cliente": cliente,
    })

#Ver tarjetas vinculadas con el cliente
def verTarjetaCliente(request, customer_id):
    cliente = Cliente.objects.get(pk=customer_id)
    return render(request, 'verTarjetaCliente.html',{
        "cliente": cliente,
    })

#Ver datos de la tarjeta (numero, cvv, etc)
def verTarjetas(request, tarjeta_id):
    tarjeta = Tarjeta.objects.get(pk=tarjeta_id)
    #print(tarjeta.id)
    return render(request, 'verDatosTarjeta.html',{
        "tarjeta": tarjeta
    })

#Crear cuenta banacaria
def crearCuentaBancaria(request):
    if request.method == 'POST':
        form = CuentaBancariaFormulario(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Cuenta bancaria creada")
        else:
            return HttpResponse("Hubo un error")
    else:
        form = CuentaBancariaFormulario()
    return render(request,'crearCuentaBancaria.html',{
        "form":form
    })

#Listar todas las cuentas de un cliente
def listarCuentasClientes(request, customer_id):

    cliente = Cliente.objects.get(pk=customer_id)
    cuentas = Cuenta.objects.filter(customer_id=customer_id)

    return render(request, 'listarCuentasClientes.html',{
        "cliente":cliente,
        "cuentas": cuentas,
    })

# PROBLEMATICA 3
def crearCliente(request):
    #Si es un metodo POST, debo verificar los datos y guarda el cliente
    if request.method == 'POST':
        form = ClienteForm(request.POST) #Obtengo los datos del formulario
        #Valido y guardo
        if form.is_valid():
            form.save()
            #login(request, form) #Una vez registrado se queda logeado
            return redirect('home')
        else:
            return HttpResponse("Hubo un error")
    else:
        #Si es un gest solo muestro el formulario
        form = ClienteForm()

    return render(request, 'crearCliente.html', {'form': form})

#Cerrar sesion
def signout(request):
    logout(request)
    return redirect('home')

#Agregado para validacion
class CustomModelBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        print("Backend Personalizado: kwargs =", kwargs)

        if 'customer_name' in kwargs and 'customer_surname' in kwargs:
            customer_name = kwargs['customer_name']
            customer_surname = kwargs['customer_surname']

            try:
                user = Cliente.objects.get(customer_name=customer_name, customer_surname=customer_surname)
            except Cliente.DoesNotExist:
                return None

            if user.check_password(kwargs.get('password')):
                return user
        return None

#Iniciar sesion
def signin(request):
    if request.method == 'POST':
        form = ClienteLoginForm(request, data=request.POST)
        if form.is_valid():
            # Obtener el customer_name y customer_surname del formulario
            customer_name = form.cleaned_data['customer_name']
            customer_surname = form.cleaned_data['customer_surname']
            print(customer_name)
            print(customer_surname)

            credentials = {'customer_name': customer_name, 'customer_surname': customer_surname}

            # Autenticar manualmente utilizando el customer_name y customer_surname
            user = authenticate(request, **credentials)

            print("Usuario después de la autenticación:", user)

            if user is not None:
                login(request, user)
                print('si')
                return redirect('Home')
            else:
                # Usuario no encontrado
                print('no')
                form.add_error(None, 'Credenciales incorrectas')
        # El formulario no es válido, puede haber errores de validación
        return render(request, 'signin.html', {'form': form})
    else:
        # Este bloque debería manejar el caso GET, no POST
        form = ClienteLoginForm()
        return render(request, 'signin.html', {'form': form})


# PROBLEMATICA 4 
def solicitud_prestamo(request):
    if request.method == 'POST':
        form = SolicitudPrestamoForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.customer_id = request.user
            solicitud.save()

            # Puedes realizar acciones adicionales aquí, como impactar en el saldo de la cuenta.

            messages.success(request, 'Solicitud de préstamo enviada con éxito.')
            return redirect('nombre_de_la_vista')  # Cambia 'nombre_de_la_vista' al nombre de la vista de préstamos

    else:
        form = SolicitudPrestamoForm()

    return render(request, 'soli_prestamo.html', {'form': form})



