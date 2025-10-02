from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import CapacitacionDocente, HojaDeVidaDocente
from core.forms import CapacitacionDocenteForm


@login_required
def docente_capacitacion_view(request):
    usuario = request.user

    # Verificar que sea docente
    if not usuario.rol or usuario.rol.nombre != 'Docente':
        messages.error(request, "Acceso denegado. Solo para docentes.")
        return redirect('inicio')

    # Obtener hoja de vida
    try:
        hoja_de_vida = HojaDeVidaDocente.objects.get(usuario=usuario)
    except HojaDeVidaDocente.DoesNotExist:
        messages.error(request, "Primero debes completar tus datos básicos.")
        return redirect('docente_datos_basicos')

    # Listar capacitaciones
    capacitaciones = CapacitacionDocente.objects.filter(hoja_de_vida=hoja_de_vida)

    # Procesar formulario de nueva capacitación
    if request.method == 'POST':
        form = CapacitacionDocenteForm(request.POST, request.FILES)
        if form.is_valid():
            capacitacion = form.save(commit=False)
            capacitacion.hoja_de_vida = hoja_de_vida
            capacitacion.save()
            messages.success(request, "Capacitación agregada correctamente.")
            return redirect('docente_capacitacion')
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = CapacitacionDocenteForm()

    context = {
        'capacitaciones': capacitaciones,
        'form': form,
        'hoja_de_vida': hoja_de_vida,
    }
    return render(request, 'panel_docente/capacitacion.html', context)


@login_required
def editar_capacitacion(request, capacitacion_id):
    usuario = request.user

    # Verificar rol
    if not usuario.rol or usuario.rol.nombre != 'Docente':
        messages.error(request, "Acceso denegado. Solo para docentes.")
        return redirect('inicio')

    capacitacion = get_object_or_404(
        CapacitacionDocente, id=capacitacion_id, hoja_de_vida__usuario=usuario
    )

    if request.method == "POST":
        form = CapacitacionDocenteForm(request.POST, request.FILES, instance=capacitacion)
        if form.is_valid():
            form.save()
            messages.success(request, "Capacitación actualizada correctamente.")
            return redirect("docente_capacitacion")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = CapacitacionDocenteForm(instance=capacitacion)

    context = {
        "form": form,
        "capacitacion": capacitacion,
    }
    return render(request, "panel_docente/editar_capacitacion.html", context)


@login_required
def eliminar_capacitacion(request, capacitacion_id):
    usuario = request.user

    if not usuario.rol or usuario.rol.nombre != 'Docente':
        messages.error(request, "Acceso denegado. Solo para docentes.")
        return redirect('inicio')

    capacitacion = get_object_or_404(
        CapacitacionDocente, id=capacitacion_id, hoja_de_vida__usuario=usuario
    )
    capacitacion.delete()
    messages.success(request, "Capacitación eliminada correctamente.")
    return redirect("docente_capacitacion")
