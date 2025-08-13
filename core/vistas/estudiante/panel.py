from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from core.models import Usuario, PerfilDeUsuario, AsignacionDocente

@login_required
def panel_estudiante_inicio(request):
    """
    Vista del panel de inicio para estudiantes.
    Muestra información básica del estudiante logueado.
    """
    # Obtener el usuario actual
    usuario = request.user
    
    # Verificar que sea un estudiante
    if not usuario.rol or usuario.rol.nombre != 'Estudiante':
        return HttpResponse("Acceso denegado. Solo para estudiantes.", status=403)
    
    # Obtener el perfil del estudiante
    try:
        perfil = usuario.perfil
    except PerfilDeUsuario.DoesNotExist:
        perfil = None
    
    # Obtener el grupo del estudiante
    grupo = perfil.grupo if perfil else None
    
    # Obtener las asignaturas del grupo (a través de las asignaciones docentes)
    asignaturas = []
    if grupo:
        asignaciones = AsignacionDocente.objects.filter(grupo=grupo).select_related('asignatura', 'asignatura__area')
        asignaturas = [asignacion.asignatura for asignacion in asignaciones]
    
    # Preparar el nombre completo
    nombre_completo = ""
    if perfil:
        # TODO: Mover el formateo de nombre completo a un método en el modelo PerfilDeUsuario
        nombre_completo = f"{perfil.primer_nombre} {perfil.segundo_nombre or ''} {perfil.primer_apellido} {perfil.segundo_apellido or ''}".strip()
    # TODO: Modularizar la obtención de asignaturas en un método del modelo o manager
    
    context = {
        'usuario': usuario,
        'perfil': perfil,
        'nombre_completo': nombre_completo,
        'grupo': grupo,
        'asignaturas': asignaturas,
    }
    
    return render(request, 'estudiante/panel_inicio.html', context)

def panel_estudiante(request):
    return HttpResponse("Panel del Estudiante")
