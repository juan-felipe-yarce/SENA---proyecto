# core/vistas/acudiente/perfil.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.forms import PerfilUsuarioForm
from core.models import PerfilDeUsuario, Ciudad


# ---------------------------
# Ver perfil de Acudiente
# ---------------------------
@login_required
def perfil_acudiente(request):
    try:
        perfil = request.user.perfil
    except PerfilDeUsuario.DoesNotExist:
        perfil = None

    # ✅ Traemos los estudiantes asignados si existen
    acudidos = perfil.acudidos.all() if perfil else []

    return render(request, "acudiente/perfil_usuario.html", {   # usa el template de acudiente
        "usuario": request.user,
        "perfil": perfil,
        "acudidos": acudidos,   # 👈 lo mandamos al HTML
    })


# ---------------------------
# Editar perfil de Acudiente
# ---------------------------
@login_required
def editar_perfil_acudiente(request):
    try:
        perfil = request.user.perfil
    except PerfilDeUsuario.DoesNotExist:
        # Si no existe, lo creamos con ciudad por defecto
        ciudad_default = Ciudad.objects.first()
        perfil = PerfilDeUsuario.objects.create(
            usuario=request.user,
            ciudad=ciudad_default,
            primer_nombre="",
            primer_apellido="",
            direccion_linea1=""
        )

    if request.method == "POST":
        form = PerfilUsuarioForm(request.POST, request.FILES, instance=perfil, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Perfil actualizado correctamente.")
            return redirect("perfil_acudiente")
        else:
            messages.error(request, "❌ Corrige los errores del formulario.")
    else:
        form = PerfilUsuarioForm(instance=perfil, user=request.user)

    return render(request, "acudiente/editar_perfil.html", {   # usa el template de acudiente
        "usuario": request.user,
        "form": form,
    })
