from django.contrib import admin
from .models import Cliente, Tarjeta, Cuenta, Direcciones,Empleado, Marcatarjeta, Prestamo, Sucursal, Tipocliente, Tipocuenta

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Tarjeta)
admin.site.register(Cuenta)
admin.site.register(Direcciones)
admin.site.register(Empleado)
admin.site.register(Marcatarjeta)
admin.site.register(Prestamo)
admin.site.register(Sucursal)
admin.site.register(Tipocliente)
admin.site.register(Tipocuenta)