from django.contrib import admin
from .models import Cliente, Tarjeta, Cuenta

# Register your models here.
admin.site.register(Cliente)
admin.site.register(Tarjeta)
admin.site.register(Cuenta)
