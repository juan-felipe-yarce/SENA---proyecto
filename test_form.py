#!/usr/bin/env python
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from core.models import Usuario, HojaDeVidaDocente, EstadoCivil, Genero, Estrato, Pais, Departamento, Ciudad
from core.forms import DatosBasicosDocenteForm
from datetime import date

def test_datos_basicos_form():
    print("🧪 Probando formulario de datos básicos del docente...")
    
    # Verificar que existen datos de referencia
    print("\n📊 Verificando datos de referencia:")
    print(f"Estados civiles: {EstadoCivil.objects.count()}")
    print(f"Géneros: {Genero.objects.count()}")
    print(f"Estratos: {Estrato.objects.count()}")
    print(f"Países: {Pais.objects.count()}")
    print(f"Departamentos: {Departamento.objects.count()}")
    print(f"Ciudades: {Ciudad.objects.count()}")
    
    # Crear datos de prueba
    test_data = {
        'fecha_nacimiento': '1990-01-01',
        'direccion_linea1': 'Calle 123 # 45-67',
        'telefono_celular': '3001234567',
        'resumen': 'Docente con experiencia en educación básica y media.',
    }
    
    print("\n🔍 Probando formulario con datos mínimos:")
    form = DatosBasicosDocenteForm(data=test_data)
    
    if form.is_valid():
        print("✅ Formulario válido con datos mínimos")
        print("Campos válidos:", list(form.cleaned_data.keys()))
    else:
        print("❌ Formulario inválido:")
        for field, errors in form.errors.items():
            print(f"  - {field}: {errors}")
    
    # Probar con datos completos
    print("\n🔍 Probando formulario con datos completos:")
    complete_data = {
        'fecha_nacimiento': '1985-05-15',
        'genero': Genero.objects.first().id if Genero.objects.exists() else None,
        'estado_civil': EstadoCivil.objects.first().id if EstadoCivil.objects.exists() else None,
        'pais_residencia': Pais.objects.first().id if Pais.objects.exists() else None,
        'departamento_residencia': Departamento.objects.first().id if Departamento.objects.exists() else None,
        'municipio_residencia': Ciudad.objects.first().id if Ciudad.objects.exists() else None,
        'direccion_linea1': 'Carrera 78 # 90-12',
        'direccion_linea2': 'Apartamento 502',
        'estrato': Estrato.objects.first().id if Estrato.objects.exists() else None,
        'telefono_celular': '3109876543',
        'telefono_celular_alterno': '3151234567',
        'telefono_fijo': '6012345678',
        'telefono_fijo_ext': '123',
        'correo_alterno': 'docente.alternativo@gmail.com',
        'resumen': 'Docente con más de 10 años de experiencia en educación básica y media, especializado en matemáticas y ciencias.',
    }
    
    form_complete = DatosBasicosDocenteForm(data=complete_data)
    
    if form_complete.is_valid():
        print("✅ Formulario válido con datos completos")
        print("Campos válidos:", list(form_complete.cleaned_data.keys()))
    else:
        print("❌ Formulario inválido:")
        for field, errors in form_complete.errors.items():
            print(f"  - {field}: {errors}")
    
    # Probar validaciones específicas
    print("\n🔍 Probando validaciones:")
    
    # Test 1: Fecha de nacimiento muy joven
    test_young = test_data.copy()
    test_young['fecha_nacimiento'] = '2010-01-01'
    form_young = DatosBasicosDocenteForm(data=test_young)
    if not form_young.is_valid():
        print("✅ Validación de edad mínima funciona")
    
    # Test 2: Dirección muy corta
    test_short_address = test_data.copy()
    test_short_address['direccion_linea1'] = 'Calle 1'
    form_short = DatosBasicosDocenteForm(data=test_short_address)
    if not form_short.is_valid():
        print("✅ Validación de dirección funciona")
    
    # Test 3: Teléfono muy corto
    test_short_phone = test_data.copy()
    test_short_phone['telefono_celular'] = '123'
    form_phone = DatosBasicosDocenteForm(data=test_short_phone)
    if not form_phone.is_valid():
        print("✅ Validación de teléfono funciona")
    
    # Test 4: Resumen muy corto
    test_short_summary = test_data.copy()
    test_short_summary['resumen'] = 'Corto'
    form_summary = DatosBasicosDocenteForm(data=test_short_summary)
    if not form_summary.is_valid():
        print("✅ Validación de resumen funciona")
    
    print("\n🎉 Pruebas completadas!")

if __name__ == '__main__':
    test_datos_basicos_form() 