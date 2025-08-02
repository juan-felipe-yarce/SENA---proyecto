from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import IdiomaDocente, HojaDeVidaDocente
from core.forms import IdiomaDocenteForm

@login_required
def docente_idiomas_view(request):
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

    # Listar idiomas
    idiomas = IdiomaDocente.objects.filter(hoja_de_vida=hoja_de_vida)

    # Procesar formulario
    if request.method == 'POST':
        form = IdiomaDocenteForm(request.POST, request.FILES)
        if form.is_valid():
            idioma = form.save(commit=False)
            idioma.hoja_de_vida = hoja_de_vida  # ¡Esto es clave!
            idioma.save()
            messages.success(request, "Idioma agregado correctamente.")
            return redirect('docente_idiomas')
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = IdiomaDocenteForm()

    context = {
        'idiomas': idiomas,
        'form': form,
    }
    return render(request, 'panel_docente/idiomas.html', context)
