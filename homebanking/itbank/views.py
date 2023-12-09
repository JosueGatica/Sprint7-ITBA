# En views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SolicitudPrestamoForm,ClienteForm,CuentaBancariaFormulario
from django.contrib import messages
from .models import Cliente, Tarjeta, Cuenta
from django.contrib.auth import login

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
            return HttpResponse("Cliente creado y logeado")
            login(request, form) #Una vez registrado se queda logeado
        else:
            return HttpResponse("Hubo un error")
    else:
        #Si es un gest solo muestro el formulario
        form = ClienteForm()

    return render(request, 'crearCliente.html', {'form': form})




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

