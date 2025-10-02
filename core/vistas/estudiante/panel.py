from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from core.models import Usuario, PerfilDeUsuario, AsignaturaEstudiante
from core.forms import SeleccionAsignaturasForm


@login_required
def panel_estudiante_inicio(request):
    """
    Vista del panel de inicio para estudiantes.
    Muestra información básica del estudiante logueado.
    Ahora usa las asignaturas seleccionadas por el propio estudiante (Opción 1).
    """
    usuario = request.user
    
    # Verificar que sea un estudiante
    if not usuario.rol or usuario.rol.nombre.lower() != 'estudiante':
        return HttpResponse("Acceso denegado. Solo para estudiantes.", status=403)
    
    # Obtener el perfil del estudiante
    try:
        perfil = usuario.perfil
    except PerfilDeUsuario.DoesNotExist:
        perfil = None
    
    # ✅ Asignaturas que el estudiante ya seleccionó (ManyToMany PerfilDeUsuario)
    asignaturas = perfil.asignaturas.all() if perfil else []
    
    # Preparar el nombre completo
    nombre_completo = ""
    if perfil:
        nombre_completo = f"{perfil.primer_nombre} {perfil.segundo_nombre or ''} {perfil.primer_apellido} {perfil.segundo_apellido or ''}".strip()
    
    context = {
        'usuario': usuario,
        'perfil': perfil,
        'nombre_completo': nombre_completo,
        'grupo': perfil.grupo if perfil else None,
        'asignaturas': asignaturas,   # ← ahora es lo que selecciona el estudiante
    }
    
    return render(request, 'estudiante/panel_inicio.html', context)


@login_required
def estudiante_asignaturas(request):
    """
    Vista para mostrar y gestionar las asignaturas del estudiante.
    Permite seleccionar asignaturas creadas por el coordinador.
    """
    usuario = request.user

    # Verificar que sea estudiante
    if not usuario.rol or usuario.rol.nombre.lower() != 'estudiante':
        messages.error(request, "Acceso denegado. Solo para estudiantes.")
        return redirect('inicio')

    perfil = getattr(usuario, "perfil", None)
    if not perfil:
        messages.error(request, "No se encontró un perfil de estudiante asociado.")
        return redirect('inicio')

    # Asignaturas que el estudiante ya tiene inscritas
    asignaturas_actuales = perfil.asignaturas.all()

    if request.method == "POST":
        form = SeleccionAsignaturasForm(request.POST)
        if form.is_valid():
            # Limpia las asignaturas anteriores
            AsignaturaEstudiante.objects.filter(estudiante=perfil).delete()

            # Asigna las nuevas
            seleccionadas = form.cleaned_data['asignaturas']
            for asignatura in seleccionadas:
                AsignaturaEstudiante.objects.create(estudiante=perfil, asignatura=asignatura)

            messages.success(request, "✅ Tus asignaturas han sido actualizadas correctamente.")
            return redirect('mis_asignaturas')
    else:
        form = SeleccionAsignaturasForm(
            initial={'asignaturas': asignaturas_actuales}
        )

    context = {
        "form": form,
        "asignaturas_actuales": asignaturas_actuales
    }
    return render(request, "estudiante/asignaturas.html", context)


@login_required
def panel_estudiante(request):
    return HttpResponse("Panel del Estudiante")
