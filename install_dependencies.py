#!/usr/bin/env python
import subprocess
import sys
import os

def install_dependencies():
    """Instalar dependencias del proyecto"""
    print("🔧 Instalando dependencias...")
    
    try:
        # Instalar desde requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencias instaladas correctamente")
        
        # Verificar instalación de debug_toolbar
        try:
            import debug_toolbar
            print("✅ django-debug-toolbar instalado correctamente")
        except ImportError:
            print("❌ Error: django-debug-toolbar no se pudo importar")
            print("💡 Ejecutando instalación manual...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "django-debug-toolbar==4.4.0"])
            print("✅ django-debug-toolbar instalado manualmente")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error instalando dependencias: {e}")
        return False
    
    return True

def check_virtual_environment():
    """Verificar si estamos en un entorno virtual"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Entorno virtual activado")
        return True
    else:
        print("⚠️ No se detectó entorno virtual activado")
        print("💡 Recomendación: Activar el entorno virtual antes de ejecutar")
        return False

if __name__ == "__main__":
    print("🚀 Iniciando instalación de dependencias...")
    
    if check_virtual_environment():
        if install_dependencies():
            print("🎉 Instalación completada exitosamente!")
            print("💡 Ahora puedes ejecutar: python manage.py runserver")
        else:
            print("❌ Error en la instalación")
    else:
        print("💡 Para activar el entorno virtual:")
        print("   Windows: env\\Scripts\\activate")
        print("   Linux/Mac: source env/bin/activate") 