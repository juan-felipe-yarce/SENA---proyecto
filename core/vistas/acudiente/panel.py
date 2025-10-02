from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from django import forms
from core.models import PerfilDeUsuario


@login_required
def panel_acudiente(request):
    usuario = request.user
    try:
        perfil = usuario.perfil
    except PerfilDeUsuario.DoesNotExist:
        perfil = None

    # Obtener los perfiles de los estudiantes asociados a este acudiente
    acudidos = []
    if perfil:
        relaciones = perfil.acudidos_asociados.all()
        acudidos = [relacion.estudiante for relacion in relaciones]

    nombre_completo = ""
    if perfil:
        nombre_completo = f"{perfil.primer_nombre} {perfil.segundo_nombre or ''} {perfil.primer_apellido} {perfil.segundo_apellido or ''}".strip()

    context = {
        'usuario': usuario,
        'perfil': perfil,
        'nombre_completo': nombre_completo,
        'acudidos': acudidos,
    }
    return render(request, 'acudiente/panel_inicio.html', context)


# ---------------------------
#   NUEVO: Asignar estudiante
# ---------------------------

class AsignarEstudianteForm(forms.Form):
    estudiante = forms.ModelChoiceField(
        queryset=PerfilDeUsuario.objects.filter(usuario__rol__nombre__icontains='Estudiante'),
        label="Selecciona un estudiante",
        widget=forms.Select(attrs={'class': 'form-select'})
    )


@login_required
def asignar_estudiante(request):
    # Validar que sea acudiente (más flexible con lower)
    rol_nombre = str(getattr(request.user.rol, "nombre", "")).lower()
    if "acudiente" not in rol_nombre:
        return HttpResponse("Acceso denegado. Solo para acudientes.", status=403)

    try:
        perfil_acudiente = request.user.perfil
    except PerfilDeUsuario.DoesNotExist:
        messages.error(request, "Tu usuario no tiene perfil asociado.")
        return redirect('panel_acudiente')

    if request.method == 'POST':
        form = AsignarEstudianteForm(request.POST)
        if form.is_valid():
            estudiante = form.cleaned_data['estudiante']
            # Evitar duplicados
            if perfil_acudiente.acudidos_asociados.filter(estudiante=estudiante).exists():
                messages.info(request, "Ese estudiante ya está asignado.")
            else:
                perfil_acudiente.acudidos_asociados.create(estudiante=estudiante)
                messages.success(request, "Estudiante asignado correctamente.")
            return redirect('ver_estudiantes')
    else:
        form = AsignarEstudianteForm()

    return render(request, 'acudiente/asignar_estudiante.html', {'form': form})


# ---------------------------
#   NUEVO: Ver estudiantes
# ---------------------------

@login_required
def ver_estudiantes(request):
    # Validar que sea acudiente (más flexible con lower)
    rol_nombre = str(getattr(request.user.rol, "nombre", "")).lower()
    if "acudiente" not in rol_nombre:
        return HttpResponse("Acceso denegado. Solo para acudientes.", status=403)

    try:
        perfil = request.user.perfil
    except PerfilDeUsuario.DoesNotExist:
        perfil = None

    acudidos = []
    if perfil:
        relaciones = perfil.acudidos_asociados.all()
        acudidos = [relacion.estudiante for relacion in relaciones]

    context = {
        'perfil': perfil,
        'acudidos': acudidos,
    }
    return render(request, 'acudiente/lista_estudiantes.html', context)
