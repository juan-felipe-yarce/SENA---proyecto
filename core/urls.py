from django.conf import settings
from core.forms import CustomPasswordResetForm
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from core.vistas.autenticacion.autenticacion import (
    login_usuario, logout_usuario, registro_usuario
)
from core.vistas.docente.panel import panel_docente_view
from core.vistas.navegacion.inicio import bienvenida, inicio
from core.vistas.perfil.perfil_usuario import perfil_usuario, editar_perfil
from core.vistas.estudiante.panel import (
    panel_estudiante_inicio,
    estudiante_asignaturas,   # 👈 import nuevo
)
from core.vistas.acudiente.panel import (
    panel_acudiente,
    asignar_estudiante,
    ver_estudiantes
)
from core.vistas.acudiente.perfil import (
    perfil_acudiente,
    editar_perfil_acudiente,
)
from core.vistas.docente.capacitacion import (
    docente_capacitacion_view,
    editar_capacitacion,
    eliminar_capacitacion,
)
from core.vistas.docente.docente_hoja_vida import docente_datos_basicos_view
from core.vistas.docente.educacion import (
    docente_educacion_view, editar_educacion, eliminar_educacion
)
from core.vistas.docente.idiomas import docente_idiomas_view
from core.vistas.docente.experiencia import docente_experiencia_view
from core.vistas.coordinador.panel import (
    panel_coordinador,
    usuarios_pendientes,
    activar_usuario
)
from core.vistas.coordinador.gestion_academica import (
    lista_niveles, crear_nivel, editar_nivel, eliminar_nivel,
    lista_grados, crear_grado, editar_grado, eliminar_grado,
    lista_areas, crear_area, editar_area, eliminar_area,
    lista_asignaturas, crear_asignatura, editar_asignatura, eliminar_asignatura,
    lista_temas, crear_tema, editar_tema, eliminar_tema,
    lista_logros, crear_logro, editar_logro, eliminar_logro,
    lista_aulas, crear_aula, editar_aula, eliminar_aula,
    lista_grupos, crear_grupo, editar_grupo, eliminar_grupo,
    lista_asignaciones, crear_asignacion, editar_asignacion, eliminar_asignacion
)
from django.contrib.auth import views as auth_views
from core.vistas.ajax.ubicaciones import obtener_departamentos, obtener_ciudades


urlpatterns = [
    # Autenticación
    path('login/', login_usuario, name='login'),
    path('logout/', logout_usuario, name='logout'),
    path('registro/', registro_usuario, name='registro'),

    # Página de bienvenida (pública) y página de inicio
    path('', bienvenida, name='bienvenida'),
    path('inicio/', inicio, name='inicio'),

    # Perfil del usuario autenticado (genérico)
    path('perfil/', perfil_usuario, name='perfil_usuario'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),

    # Paneles por rol
    path('panel-docente/', panel_docente_view, name='panel_docente'),

    path('panel-estudiante/', panel_estudiante_inicio, name='panel_estudiante'),
    path('panel-estudiante/asignaturas/', estudiante_asignaturas, name='mis_asignaturas'),# 👈 nueva ruta

    path('panel-coordinador/', panel_coordinador, name='panel_coordinador'),
    path('panel-acudiente/', panel_acudiente, name='panel_acudiente'),
    path('panel-acudiente/asignar/', asignar_estudiante, name='asignar_estudiante'),
    path('panel-acudiente/estudiantes/', ver_estudiantes, name='ver_estudiantes'),
    path('panel-acudiente/perfil/', perfil_acudiente, name='perfil_acudiente'),
    path('panel-acudiente/perfil/editar/', editar_perfil_acudiente, name='editar_perfil_acudiente'),

    # Coordinador - Gestión académica
    path('coordinador/niveles/', lista_niveles, name='lista_niveles'),
    path('coordinador/niveles/nuevo/', crear_nivel, name='crear_nivel'),
    path('coordinador/niveles/editar/<int:pk>/', editar_nivel, name='editar_nivel'),
    path('coordinador/niveles/eliminar/<int:pk>/', eliminar_nivel, name='eliminar_nivel'),

    path('coordinador/grados/', lista_grados, name='lista_grados'),
    path('coordinador/grados/nuevo/', crear_grado, name='crear_grado'),
    path('coordinador/grados/editar/<int:pk>/', editar_grado, name='editar_grado'),
    path('coordinador/grados/eliminar/<int:pk>/', eliminar_grado, name='eliminar_grado'),

    path('coordinador/aulas/', lista_aulas, name='lista_aulas'),
    path('coordinador/aulas/nuevo/', crear_aula, name='crear_aula'),
    path('coordinador/aulas/editar/<int:pk>/', editar_aula, name='editar_aula'),
    path('coordinador/aulas/eliminar/<int:pk>/', eliminar_aula, name='eliminar_aula'),

    path('coordinador/grupos/', lista_grupos, name='lista_grupos'),
    path('coordinador/grupos/nuevo/', crear_grupo, name='crear_grupo'),
    path('coordinador/grupos/editar/<int:pk>/', editar_grupo, name='editar_grupo'),
    path('coordinador/grupos/eliminar/<int:pk>/', eliminar_grupo, name='eliminar_grupo'),

    path('coordinador/asignaciones/', lista_asignaciones, name='lista_asignaciones'),
    path('coordinador/asignaciones/nuevo/', crear_asignacion, name='crear_asignacion'),
    path('coordinador/asignaciones/editar/<int:pk>/', editar_asignacion, name='editar_asignacion'),
    path('coordinador/asignaciones/eliminar/<int:pk>/', eliminar_asignacion, name='eliminar_asignacion'),

    path('coordinador/usuarios-pendientes/', usuarios_pendientes, name='usuarios_pendientes'),
    path('coordinador/activar-usuario/<int:usuario_id>/', activar_usuario, name='activar_usuario'),

    path('coordinador/areas/', lista_areas, name='lista_areas'),
    path('coordinador/areas/nuevo/', crear_area, name='crear_area'),
    path('coordinador/areas/editar/<int:pk>/', editar_area, name='editar_area'),
    path('coordinador/areas/eliminar/<int:pk>/', eliminar_area, name='eliminar_area'),

    path('coordinador/asignaturas/', lista_asignaturas, name='lista_asignaturas'),
    path('coordinador/asignaturas/nuevo/', crear_asignatura, name='crear_asignatura'),
    path('coordinador/asignaturas/editar/<int:pk>/', editar_asignatura, name='editar_asignatura'),
    path('coordinador/asignaturas/eliminar/<int:pk>/', eliminar_asignatura, name='eliminar_asignatura'),

    path('coordinador/temas/', lista_temas, name='lista_temas'),
    path('coordinador/temas/nuevo/', crear_tema, name='crear_tema'),
    path('coordinador/temas/editar/<int:pk>/', editar_tema, name='editar_tema'),
    path('coordinador/temas/eliminar/<int:pk>/', eliminar_tema, name='eliminar_tema'),

    path('coordinador/logros/', lista_logros, name='lista_logros'),
    path('coordinador/logros/nuevo/', crear_logro, name='crear_logro'),
    path('coordinador/logros/editar/<int:pk>/', editar_logro, name='editar_logro'),
    path('coordinador/logros/eliminar/<int:pk>/', eliminar_logro, name='eliminar_logro'),

    # Docentes - Hoja de Vida
    path('docente/hoja-vida/datos-basicos/', docente_datos_basicos_view, name='docente_datos_basicos'),

    # Educación
    path('docente/hoja-vida/educacion/', docente_educacion_view, name='docente_educacion'),
    path('docente/hoja-vida/educacion/editar/<int:educacion_id>/', editar_educacion, name='editar_educacion'),
    path('docente/hoja-vida/educacion/eliminar/<int:educacion_id>/', eliminar_educacion, name='eliminar_educacion'),

    # Capacitaciones
    path('docente/hoja-vida/capacitacion/', docente_capacitacion_view, name='docente_capacitacion'),
    path('docente/hoja-vida/capacitacion/editar/<int:capacitacion_id>/', editar_capacitacion, name='editar_capacitacion'),
    path('docente/hoja-vida/capacitacion/eliminar/<int:capacitacion_id>/', eliminar_capacitacion, name='eliminar_capacitacion'),

    # Idiomas
    path('docente/hoja-vida/idiomas/', docente_idiomas_view, name='docente_idiomas'),

    # Experiencia
    path('docente/hoja-vida/experiencia/', docente_experiencia_view, name='docente_experiencia'),

    # AJAX
    path('ajax/departamentos/', obtener_departamentos, name='ajax_departamentos'),
    path('ajax/ciudades/', obtener_ciudades, name='ajax_ciudades'),

    # Password Reset con formulario personalizado
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form.html',
            form_class=CustomPasswordResetForm
        ),
        name='password_reset'
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done.html'
        ),
        name='password_reset_done'
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='registration/password_reset_confirm.html'
        ),
        name='password_reset_confirm'
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='registration/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]

# Solo en modo desarrollo
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
