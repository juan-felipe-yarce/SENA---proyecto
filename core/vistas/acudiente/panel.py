from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
        # TODO: Mover el formateo de nombre completo a un método en el modelo PerfilDeUsuario
        nombre_completo = f"{perfil.primer_nombre} {perfil.segundo_nombre or ''} {perfil.primer_apellido} {perfil.segundo_apellido or ''}".strip()
        # TODO: Modularizar la obtención de acudidos en un método del modelo o manager

    context = {
        'usuario': usuario,
        'perfil': perfil,
        'nombre_completo': nombre_completo,
        'acudidos': acudidos,
    }
    return render(request, 'acudiente/panel_inicio.html', context)
