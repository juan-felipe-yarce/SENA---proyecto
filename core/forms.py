import re
from django.contrib.auth import authenticate
from django import forms
from django.forms import TextInput, Select, EmailInput, FileInput, PasswordInput
# from django.contrib.auth.hashers import make_password

from .models import (
    Usuario, Rol, TipoDocumento, Ciudad, Pais, Departamento,
    NivelEducativo, Grado, Area, Asignatura, Tema, Logro,
    Aula, Grupo, AsignacionDocente,
    PerfilDeUsuario,
    HojaDeVidaDocente, EducacionDocente, CapacitacionDocente,
    IdiomaDocente, ExperienciaDocente
)





# Formulario de Registro de Usuario
class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(
        label="Contraseña",
        widget=PasswordInput(attrs={'class': 'w-full p-2 border rounded'}),
        help_text="Debe tener al menos 8 caracteres, incluir una mayúscula, una minúscula, un número y un símbolo (#$%!)."
    )
    confirmar_password = forms.CharField(
        label="Confirmar Contraseña",
        widget=PasswordInput(attrs={'class': 'w-full p-2 border rounded'})
    )

    # Campos auxiliares para ubicación de expedición
    pais_identificacion = forms.ModelChoiceField(
        label="País de expedición",
        queryset=Pais.objects.all(),
        required=False,
        widget=Select(attrs={'class': 'w-full p-2 border rounded'})
    )
    departamento_identificacion = forms.ModelChoiceField(
        label="Departamento de expedición",
        queryset=Departamento.objects.none(),
        required=False,
        widget=Select(attrs={'class': 'w-full p-2 border rounded'})
    )
    municipio_identificacion = forms.ModelChoiceField(
        label="Municipio de expedición",
        queryset=Ciudad.objects.none(),
        required=False,
        widget=Select(attrs={'class': 'w-full p-2 border rounded'})
    )

    class Meta:
        model = Usuario
        fields = ['correo', 'rol', 'tipo_documento', 'numero_documento', 'municipio_identificacion', 'password']
        widgets = {
            'correo': EmailInput(attrs={'class': 'w-full p-2 border rounded'}),
            'rol': Select(attrs={'class': 'w-full p-2 border rounded'}),
            'tipo_documento': Select(attrs={'class': 'w-full p-2 border rounded'}),
            'numero_documento': TextInput(attrs={'class': 'w-full p-2 border rounded'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Ordenar roles por ID
        self.fields['rol'].queryset = Rol.objects.all().order_by('id')

        # Cargar departamentos si hay país en los datos
        if 'pais_identificacion' in self.data:
            try:
                pais_id = int(self.data.get('pais_identificacion'))
                self.fields['departamento_identificacion'].queryset = Departamento.objects.filter(pais_id=pais_id)
            except (ValueError, TypeError):
                self.fields['departamento_identificacion'].queryset = Departamento.objects.none()

        # Cargar ciudades si hay departamento en los datos
        if 'departamento_identificacion' in self.data:
            try:
                departamento_id = int(self.data.get('departamento_identificacion'))
                self.fields['municipio_identificacion'].queryset = Ciudad.objects.filter(departamento_id=departamento_id)
            except (ValueError, TypeError):
                self.fields['municipio_identificacion'].queryset = Ciudad.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirmar = cleaned_data.get("confirmar_password")

        if password != confirmar:
            raise forms.ValidationError("⚠️ Las contraseñas no coinciden.")
        if len(password) < 8:
            raise forms.ValidationError("🔒 La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("🔒 La contraseña debe incluir al menos una letra mayúscula.")
        if not re.search(r'[a-z]', password):
            raise forms.ValidationError("🔒 La contraseña debe incluir al menos una letra minúscula.")
        if not re.search(r'\d', password):
            raise forms.ValidationError("🔒 La contraseña debe incluir al menos un número.")
        if not re.search(r'[#\$%!_]', password):
            raise forms.ValidationError("🔒 La contraseña debe incluir al menos un símbolo especial: # $ % ! _")

        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.set_password(self.cleaned_data["password"])
        usuario.municipio_identificacion = self.cleaned_data.get("municipio_identificacion")
        usuario.is_active = False
        usuario.is_superuser = False
        usuario.is_staff = False

        if commit:
            usuario.save()

        return usuario


    
# Formulario para Perfil de Usuario
class PerfilUsuarioForm(forms.ModelForm):
    correo = forms.EmailField(label="Correo electrónico", required=True, disabled=True)

    tipo_documento = forms.ModelChoiceField(
        queryset=TipoDocumento.objects.all(),
        required=False,
        label="Tipo de Documento"
    )
    numero_documento = forms.CharField(
        required=False,
        label="Número de Documento"
    )
    municipio_identificacion = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        required=False,
        label="Municipio de expedición"
    )

    class Meta:
        model = PerfilDeUsuario
        fields = [
            'foto',
            'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido',
            'direccion_linea1', 'direccion_linea2',
            'especialidad', 'grupo', 'acudidos'
        ]
        widgets = {
            'foto': FileInput(),
            'primer_nombre': TextInput(),
            'segundo_nombre': TextInput(),
            'primer_apellido': TextInput(),
            'segundo_apellido': TextInput(),
            'direccion_linea1': TextInput(),
            'direccion_linea2': TextInput(),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Inicializa datos desde usuario autenticado si existen
        if self.user:
            self.fields['correo'].initial = self.user.correo
            self.fields['tipo_documento'].initial = self.user.tipo_documento
            self.fields['numero_documento'].initial = self.user.numero_documento
            self.fields['municipio_identificacion'].initial = self.user.municipio_identificacion

        # Campos visibles por rol
        campos_visibles = [
            'foto', 'primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido',
            'tipo_documento', 'numero_documento', 'municipio_identificacion',
            'direccion_linea1', 'direccion_linea2'
        ]

        if self.user and self.user.rol:
            rol = self.user.rol.nombre.strip().lower()
            if rol == 'docente':
                campos_visibles.append('especialidad')
                self.fields['especialidad'].required = False
            elif rol == 'estudiante':
                campos_visibles.append('grupo')
                self.fields['grupo'].required = False
            elif rol in ['acudiente', 'padre de familia o acudiente']:
                campos_visibles.append('acudidos')
                self.fields['acudidos'].queryset = PerfilDeUsuario.objects.filter(
                    usuario__rol__nombre__iexact='estudiante'
                )
                self.fields['acudidos'].required = False

        for field in list(self.fields):
            if field not in campos_visibles and field != 'correo':
                del self.fields[field]

        # 🔹 Hacer todos los campos opcionales (menos correo)
        for name, field in self.fields.items():
            if name != 'correo':
                field.required = False

    def save(self, commit=True):
        perfil = super().save(commit=False)

        # Actualiza datos básicos en usuario
        if self.user:
            self.user.tipo_documento = self.cleaned_data.get('tipo_documento')
            self.user.numero_documento = self.cleaned_data.get('numero_documento')
            self.user.municipio_identificacion = self.cleaned_data.get('municipio_identificacion')
            if commit:
                self.user.save()

        if commit:
            perfil.save()
            self.save_m2m()

        return perfil


class LoginForm(forms.Form):
    correo = forms.EmailField(
        label="Correo electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Correo electrónico',
            'autocomplete': 'email'
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Contraseña',
            'autocomplete': 'current-password'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        correo = cleaned_data.get("correo")
        password = cleaned_data.get("password")

        if correo and password:
            try:
                usuario = Usuario.objects.get(correo=correo)
            except Usuario.DoesNotExist:
                raise forms.ValidationError("❌ Usuario o contraseña incorrectos.")

            if not usuario.is_active:
                if usuario.rol and usuario.rol.nombre.lower() == "coordinador académico":
                    raise forms.ValidationError("🕒 Tu cuenta como Coordinador Académico aún no ha sido activada por el superusuario.")
                else:
                    raise forms.ValidationError("🕒 Tu cuenta aún no ha sido activada. Espera la validación.")

            usuario_autenticado = authenticate(correo=correo, password=password)
            if usuario_autenticado is None:
                raise forms.ValidationError("❌ Usuario o contraseña incorrectos.")

            self.cleaned_data["usuario"] = usuario_autenticado

        return self.cleaned_data

# Formulario para Nivel Educativo
class NivelEducativoForm(forms.ModelForm):
    class Meta:
        model = NivelEducativo
        fields = ['nombre']

# Formulario para Grado
class GradoForm(forms.ModelForm):
    class Meta:
        model = Grado
        fields = ['nivel', 'nombre']
        
# Formulario para Aula
class AulaForm(forms.ModelForm):
    class Meta:
        model = Aula
        fields = ['nombre', 'capacidad', 'estado']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-500'
            }),
            'capacidad': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-500'
            }),
            'estado': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border border-gray-300 rounded focus:outline-none focus:ring focus:border-blue-500'
            }),
        }



# Formulario para Grupo
class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ['nombre', 'grado', 'aula']

    def clean(self):
        cleaned_data = super().clean()
        nombre = cleaned_data.get('nombre')
        grado = cleaned_data.get('grado')
        if Grupo.objects.filter(nombre=nombre, grado=grado).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError("Ya existe un grupo con ese nombre en el mismo grado.")
        return cleaned_data


# Formulario para Asignación de Docente
class AsignacionDocenteForm(forms.ModelForm):
    class Meta:
        model = AsignacionDocente
        fields = ['docente', 'asignatura', 'grupo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrar solo usuarios con rol "Docente"
        self.fields['docente'].queryset = Usuario.objects.filter(rol__nombre__iexact='Docente')


# Formulario para Área
class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ['nombre', 'obligatoria']

# Formulario para Asignatura
class AsignaturaForm(forms.ModelForm):
    class Meta:
        model = Asignatura
        fields = ['nombre', 'grado', 'area']

# Formulario para Tema
class TemaForm(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ['nombre', 'asignatura']

# Formulario para Logro
class LogroForm(forms.ModelForm):
    class Meta:
        model = Logro
        fields = ['descripcion', 'asignatura']

# Hoja de Vida Docentes
class DatosBasicosDocenteForm(forms.ModelForm):
    class Meta:
        model = HojaDeVidaDocente
        exclude = ['usuario']  # Usuario se asigna en la vista

        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'genero': forms.Select(attrs={
                'class': 'form-select'
            }),
            'estado_civil': forms.Select(attrs={
                'class': 'form-select'
            }),
            'pais_residencia': forms.Select(attrs={
                'class': 'form-select'
            }),
            'departamento_residencia': forms.Select(attrs={
                'class': 'form-select'
            }),
            'municipio_residencia': forms.Select(attrs={
                'class': 'form-select'
            }),
            'direccion_linea1': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'direccion_linea2': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'estrato': forms.Select(attrs={
                'class': 'form-select'
            }),
            'telefono_celular': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono_celular_alterno': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono_fijo': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'telefono_fijo_ext': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'correo_alterno': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'resumen': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Hacer campos opcionales más claros
        self.fields['estado_civil'].required = False
        self.fields['genero'].required = False
        self.fields['pais_residencia'].required = False
        self.fields['departamento_residencia'].required = False
        self.fields['municipio_residencia'].required = False
        self.fields['estrato'].required = False
        self.fields['telefono_celular_alterno'].required = False
        self.fields['telefono_fijo'].required = False
        self.fields['telefono_fijo_ext'].required = False
        self.fields['correo_alterno'].required = False
        self.fields['direccion_linea2'].required = False
        
        # Agregar placeholders y ayuda
        self.fields['estado_civil'].help_text = "Opcional"
        self.fields['genero'].help_text = "Opcional"
        self.fields['estrato'].help_text = "Opcional"
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_nacimiento = cleaned_data.get('fecha_nacimiento')
        direccion_linea1 = cleaned_data.get('direccion_linea1')
        telefono_celular = cleaned_data.get('telefono_celular')
        resumen = cleaned_data.get('resumen')
        
        # Validar campos requeridos
        if not fecha_nacimiento:
            raise forms.ValidationError("La fecha de nacimiento es obligatoria.")
        
        if not direccion_linea1 or len(direccion_linea1.strip()) < 10:
            raise forms.ValidationError("La dirección debe tener al menos 10 caracteres.")
        
        if not telefono_celular or len(telefono_celular.strip()) < 7:
            raise forms.ValidationError("El teléfono celular debe tener al menos 7 dígitos.")
        
        if not resumen or len(resumen.strip()) < 20:
            raise forms.ValidationError("El resumen debe tener al menos 20 caracteres.")
        
        # Validar edad
        if fecha_nacimiento:
            from datetime import date
            today = date.today()
            age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
            
            if age < 18:
                raise forms.ValidationError("La edad mínima debe ser 18 años.")
            if age > 100:
                raise forms.ValidationError("La edad máxima debe ser 100 años.")
        
        return cleaned_data

# Identificación Formulario
class IdentificacionForm(forms.ModelForm):
    municipio_identificacion = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        label="Municipio de Identificación",
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select'
        })
    )

    class Meta:
        model = Usuario
        fields = ['tipo_documento', 'numero_documento', 'municipio_identificacion']
        widgets = {
            'tipo_documento': forms.Select(attrs={
                'class': 'form-select'
            }),
            'numero_documento': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
    
    def clean_numero_documento(self):
        numero_documento = self.cleaned_data.get('numero_documento')
        if numero_documento:
            # Remover espacios y caracteres especiales
            numero_documento = ''.join(filter(str.isalnum, numero_documento))
            if len(numero_documento) < 8:
                raise forms.ValidationError("El número de documento debe tener al menos 8 caracteres.")
        return numero_documento


        
# Identidad Form
class IdentidadForm(forms.ModelForm):
    class Meta:
        model = PerfilDeUsuario
        fields = ['primer_nombre', 'segundo_nombre', 'primer_apellido', 'segundo_apellido']
        widgets = {
            'primer_nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'segundo_nombre': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'primer_apellido': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'segundo_apellido': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        primer_nombre = cleaned_data.get('primer_nombre')
        primer_apellido = cleaned_data.get('primer_apellido')
        
        if primer_nombre and len(primer_nombre.strip()) < 2:
            raise forms.ValidationError("El primer nombre debe tener al menos 2 caracteres.")
        
        if primer_apellido and len(primer_apellido.strip()) < 2:
            raise forms.ValidationError("El primer apellido debe tener al menos 2 caracteres.")
        
        return cleaned_data

class EducacionDocenteForm(forms.ModelForm):
    class Meta:
        model = EducacionDocente
        fields = ['nivel', 'institucion', 'titulo_obtenido', 'fecha_inicio', 'fecha_fin']
        widgets = {
            'nivel': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Selecciona el nivel educativo'
            }),
            'institucion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre de la institución'
            }),
            'titulo_obtenido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Título obtenido'
            }),
            'fecha_inicio': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'fecha_fin': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_fin = cleaned_data.get('fecha_fin')
        
        if fecha_inicio and fecha_fin and fecha_inicio > fecha_fin:
            raise forms.ValidationError("La fecha de inicio no puede ser posterior a la fecha de fin.")
        
        return cleaned_data

class CapacitacionDocenteForm(forms.ModelForm):
    class Meta:
        model = CapacitacionDocente
        exclude = ['hoja_de_vida']  # Oculta el campo en el formulario
        widgets = {
            'nombre_curso': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del curso'}),
            'institucion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institución'}),
            'duracion_horas': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duración en horas'}),
            'documento_soporte': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            
        }


class IdiomaDocenteForm(forms.ModelForm):
    class Meta:
        model = IdiomaDocente
        exclude = ['hoja_de_vida']
        widgets = {
            'idioma': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Idioma'}),
            'nivel_habla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nivel de habla (ej: Básico, Intermedio, Avanzado)'}),
            'nivel_lee': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nivel de lectura'}),
            'nivel_escribe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nivel de escritura'}),
            'documento_soporte': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class ExperienciaDocenteForm(forms.ModelForm):
    class Meta:
        model = ExperienciaDocente
        exclude = ['hoja_de_vida']
        widgets = {
            'institucion': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Institución'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción', 'rows': 2}),
        }
        
from django import forms
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(  # 👈 mantenemos "email", Django lo espera así
        label="Correo electrónico",
        max_length=254,
        widget=forms.EmailInput(attrs={
            "autocomplete": "email",
            "class": "form-control",
            "placeholder": "Ingresa tu correo"
        })
    )

    def get_users(self, email):
        """Buscar usuarios activos usando el campo 'correo' de tu modelo."""
        active_users = User._default_manager.filter(
            **{
                f"{User.EMAIL_FIELD}__iexact": email,  # 👈 respeta lo definido en el modelo
                "is_active": True,
            }
        )
        return (u for u in active_users if u.has_usable_password())

# ==============================
# FORMULARIO: Selección de Asignaturas (para Estudiantes)
# ==============================

from .models import Asignatura

class SeleccionAsignaturasForm(forms.Form):
    asignaturas = forms.ModelMultipleChoiceField(
        queryset=Asignatura.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Selecciona las asignaturas que deseas cursar"
    )
