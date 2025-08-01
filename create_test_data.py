#!/usr/bin/env python
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from core.models import Genero, EstadoCivil, Estrato, Pais, Departamento, Ciudad

def crear_datos_prueba():
    print("Creando datos de prueba...")
    
    # Crear géneros
    generos = ['Masculino', 'Femenino', 'Otro']
    for nombre in generos:
        Genero.objects.get_or_create(nombre=nombre)
    
    # Crear estados civiles
    estados = ['Soltero/a', 'Casado/a', 'Unión Libre', 'Divorciado/a', 'Viudo/a']
    for nombre in estados:
        EstadoCivil.objects.get_or_create(nombre=nombre)
    
    # Crear estratos
    estratos = ['1', '2', '3', '4', '5', '6']
    for nombre in estratos:
        Estrato.objects.get_or_create(nombre=nombre)
    
    # Crear país Colombia
    colombia, created = Pais.objects.get_or_create(
        nombre='Colombia',
        defaults={'codigo_iso': 'COL'}
    )
    
    # Crear departamentos de Colombia
    departamentos = [
        'Antioquia', 'Atlántico', 'Bolívar', 'Boyacá', 'Caldas',
        'Caquetá', 'Cauca', 'Cesar', 'Córdoba', 'Cundinamarca',
        'Chocó', 'Huila', 'La Guajira', 'Magdalena', 'Meta',
        'Nariño', 'Norte de Santander', 'Putumayo', 'Quindío',
        'Risaralda', 'Santander', 'Sucre', 'Tolima', 'Valle del Cauca',
        'Arauca', 'Casanare', 'Guainía', 'Guaviare', 'Vaupés', 'Vichada'
    ]
    
    for nombre in departamentos:
        Departamento.objects.get_or_create(
            nombre=nombre,
            pais=colombia
        )
    
    # Crear algunas ciudades principales
    ciudades_data = [
        ('Medellín', 'Antioquia'),
        ('Barranquilla', 'Atlántico'),
        ('Cartagena', 'Bolívar'),
        ('Tunja', 'Boyacá'),
        ('Manizales', 'Caldas'),
        ('Bogotá', 'Cundinamarca'),
        ('Cali', 'Valle del Cauca'),
        ('Bucaramanga', 'Santander'),
        ('Pereira', 'Risaralda'),
        ('Ibagué', 'Tolima'),
    ]
    
    for ciudad_nombre, depto_nombre in ciudades_data:
        try:
            depto = Departamento.objects.get(nombre=depto_nombre)
            Ciudad.objects.get_or_create(
                nombre=ciudad_nombre,
                departamento=depto
            )
        except Departamento.DoesNotExist:
            print(f"Departamento {depto_nombre} no encontrado")
    
    print("✅ Datos de prueba creados exitosamente!")
    print(f"Géneros: {Genero.objects.count()}")
    print(f"Estados civiles: {EstadoCivil.objects.count()}")
    print(f"Estratos: {Estrato.objects.count()}")
    print(f"Países: {Pais.objects.count()}")
    print(f"Departamentos: {Departamento.objects.count()}")
    print(f"Ciudades: {Ciudad.objects.count()}")

if __name__ == '__main__':
    crear_datos_prueba() 