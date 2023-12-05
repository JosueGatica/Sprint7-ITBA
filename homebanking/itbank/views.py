# En views.py
from django.shortcuts import render, redirect
from .forms import SolicitudPrestamoForm
from django.contrib import messages

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

    return render(request, 'solicitud_prestamo.html', {'form': form})

