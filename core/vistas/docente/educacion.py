from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from core.models import EducacionDocente, HojaDeVidaDocente
from core.forms import EducacionDocenteForm

@login_required
def docente_educacion_view(request):
    """
    Vista principal para gestionar la educación del docente.
    Permite listar, crear, editar y eliminar registros de educación.
    """
    usuario = request.user
    
    # Verificar que sea un docente
    if not usuario.rol or usuario.rol.nombre != 'Docente':
        messages.error(request, "❌ Acceso denegado. Solo para docentes.")
        return redirect('inicio')
    
    # Obtener o crear hoja de vida
    try:
        hoja_de_vida = HojaDeVidaDocente.objects.get(usuario=usuario)
    except HojaDeVidaDocente.DoesNotExist:
        messages.error(request, "❌ Primero debes completar tus datos básicos.")
        return redirect('docente_datos_basicos')
    
    # Obtener todas las educaciones del docente
    educaciones = EducacionDocente.objects.filter(hoja_de_vida=hoja_de_vida).order_by('-fecha_fin')
    
    # Procesar formulario
    if request.method == 'POST':
        form = EducacionDocenteForm(request.POST)
        if form.is_valid():
            educacion = form.save(commit=False)
            educacion.hoja_de_vida = hoja_de_vida
            educacion.save()
            messages.success(request, "✅ Educación agregada correctamente.")
            return redirect('docente_educacion')
        else:
            messages.error(request, "❌ Corrige los errores en el formulario.")
    else:
        form = EducacionDocenteForm()
    
    context = {
        'educaciones': educaciones,
        'form': form,
        'hoja_de_vida': hoja_de_vida
    }
    
    return render(request, 'panel_docente/educacion.html', context)

@login_required
def editar_educacion(request, educacion_id):
    """
    Vista para editar un registro de educación específico.
    """
    usuario = request.user
    
    # Verificar que sea un docente
    if not usuario.rol or usuario.rol.nombre != 'Docente':
        messages.error(request, "❌ Acceso denegado. Solo para docentes.")
        return redirect('inicio')
    
    # Obtener la educación o devolver 404
    educacion = get_object_or_404(EducacionDocente, id=educacion_id, hoja_de_vida__usuario=usuario)
    
    if request.method == 'POST':
        form = EducacionDocenteForm(request.POST, instance=educacion)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Educación actualizada correctamente.")
            return redirect('docente_educacion')
        else:
            messages.error(request, "❌ Corrige los errores en el formulario.")
    else:
        form = EducacionDocenteForm(instance=educacion)
    
    context = {
        'form': form,
        'educacion': educacion,
        'modo': 'editar'
    }
    
    return render(request, 'panel_docente/educacion_form.html', context)

@login_required
@require_POST
def eliminar_educacion(request, educacion_id):
    """
    Vista para eliminar un registro de educación.
    """
    usuario = request.user
    
    # Verificar que sea un docente
    if not usuario.rol or usuario.rol.nombre != 'Docente':
        return JsonResponse({'success': False, 'message': 'Acceso denegado'})
    
    try:
        educacion = EducacionDocente.objects.get(id=educacion_id, hoja_de_vida__usuario=usuario)
        educacion.delete()
        return JsonResponse({'success': True, 'message': 'Educación eliminada correctamente'})
    except EducacionDocente.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Educación no encontrada'})