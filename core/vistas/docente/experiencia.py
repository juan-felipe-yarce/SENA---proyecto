from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import ExperienciaDocente, HojaDeVidaDocente
from core.forms import ExperienciaDocenteForm

@login_required
def docente_experiencia_view(request):
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

    # Listar experiencias
    experiencias = ExperienciaDocente.objects.filter(hoja_de_vida=hoja_de_vida).order_by('-fecha_inicio')

    # Procesar formulario
    if request.method == 'POST':
        form = ExperienciaDocenteForm(request.POST)
        if form.is_valid():
            experiencia = form.save(commit=False)
            experiencia.hoja_de_vida = hoja_de_vida
            experiencia.save()
            messages.success(request, "Experiencia agregada correctamente.")
            return redirect('docente_experiencia')
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = ExperienciaDocenteForm()

    context = {
        'experiencias': experiencias,
        'form': form,
    }
    return render(request, 'panel_docente/experiencia.html', context)