from django.urls import path
from . import views

urlpatterns = [
    path('solicitud_prestamo/', views.solicitud_prestamo, name='solicitud_prestamo'),
    path('datosCliente/<int:customer_id>', views.verDatosCliente, name="verDatosCliente"),
    path('datosTarjeta/<int:tarjeta_id>', views.verTarjetas, name="verTarjetas"),
    path('datosTarjetaCliente/<int:customer_id>', views.verTarjetaCliente, name="verTarjetas"),
    path('crearCliente/', views.crearCliente, name="crearCliente"),
    path('crearCuentaBancaria/', views.crearCuentaBancaria, name="crearCuentaBancaria"),
    path('listarCuentasClientes/<int:customer_id>', views.listarCuentasClientes, name="listarCuentasClientes"),
]