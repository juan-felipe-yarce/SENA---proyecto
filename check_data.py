#!/usr/bin/env python
import os
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from core.models import Genero, EstadoCivil, Estrato, Pais, Departamento, Ciudad

def verificar_datos_referencia():
    print("🔍 Verificando datos de referencia...")
    
    # Verificar géneros
    generos = ['Masculino', 'Femenino']
    for nombre in generos:
        genero, created = Genero.objects.get_or_create(nombre=nombre)
        if created:
            print(f"✅ Género creado: {nombre}")
        else:
            print(f"ℹ️ Género ya existe: {nombre}")
    
    # Verificar estados civiles
    estados = ['Soltero/a', 'Casado/a', 'Unión Libre', 'Divorciado/a', 'Viudo/a']
    for nombre in estados:
        estado, created = EstadoCivil.objects.get_or_create(nombre=nombre)
        if created:
            print(f"✅ Estado civil creado: {nombre}")
        else:
            print(f"ℹ️ Estado civil ya existe: {nombre}")
    
    # Verificar estratos
    estratos = ['1', '2', '3', '4', '5', '6']
    for nombre in estratos:
        estrato, created = Estrato.objects.get_or_create(nombre=nombre)
        if created:
            print(f"✅ Estrato creado: {nombre}")
        else:
            print(f"ℹ️ Estrato ya existe: {nombre}")
    
    # Verificar país Colombia
    colombia, created = Pais.objects.get_or_create(
        nombre='Colombia',
        defaults={'codigo_iso': 'COL'}
    )
    if created:
        print("✅ País creado: Colombia")
    else:
        print("ℹ️ País ya existe: Colombia")
    
    # Verificar departamentos principales
    departamentos = [
        'Antioquia', 'Atlántico', 'Bolívar', 'Boyacá', 'Caldas',
        'Caquetá', 'Cauca', 'Cesar', 'Córdoba', 'Cundinamarca',
        'Chocó', 'Huila', 'La Guajira', 'Magdalena', 'Meta',
        'Nariño', 'Norte de Santander', 'Putumayo', 'Quindío',
        'Risaralda', 'Santander', 'Sucre', 'Tolima', 'Valle del Cauca'
    ]
    
    for nombre in departamentos:
        depto, created = Departamento.objects.get_or_create(
            nombre=nombre,
            defaults={'pais': colombia}
        )
        if created:
            print(f"✅ Departamento creado: {nombre}")
        else:
            print(f"ℹ️ Departamento ya existe: {nombre}")
    
    # Verificar ciudades principales
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
            ciudad, created = Ciudad.objects.get_or_create(
                nombre=ciudad_nombre,
                defaults={'departamento': depto}
            )
            if created:
                print(f"✅ Ciudad creada: {ciudad_nombre}")
            else:
                print(f"ℹ️ Ciudad ya existe: {ciudad_nombre}")
        except Departamento.DoesNotExist:
            print(f"❌ Departamento {depto_nombre} no encontrado")
    
    print("\n📊 Resumen de datos:")
    print(f"Géneros: {Genero.objects.count()}")
    print(f"Estados civiles: {EstadoCivil.objects.count()}")
    print(f"Estratos: {Estrato.objects.count()}")
    print(f"Países: {Pais.objects.count()}")
    print(f"Departamentos: {Departamento.objects.count()}")
    print(f"Ciudades: {Ciudad.objects.count()}")
    
    print("\n✅ Verificación completada!")

if __name__ == '__main__':
    verificar_datos_referencia() 