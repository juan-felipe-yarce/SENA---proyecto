#!/usr/bin/env python
import subprocess
import sys
import os

def install_and_start():
    """Instalar dependencias y iniciar servidor"""
    print("🚀 Iniciando sistema escolar...")
    
    # Paso 1: Instalar dependencias
    print("📦 Instalando dependencias...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Dependencias instaladas")
    except subprocess.CalledProcessError:
        print("❌ Error instalando dependencias")
        return False
    
    # Paso 2: Verificar debug_toolbar
    try:
        import debug_toolbar
        print("✅ django-debug-toolbar disponible")
    except ImportError:
        print("⚠️ Instalando django-debug-toolbar...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "django-debug-toolbar==4.4.0"])
    
    # Paso 3: Ejecutar migraciones
    print("🔄 Ejecutando migraciones...")
    try:
        subprocess.check_call([sys.executable, "manage.py", "migrate"])
        print("✅ Migraciones completadas")
    except subprocess.CalledProcessError:
        print("❌ Error en migraciones")
        return False
    
    # Paso 4: Iniciar servidor
    print("🌐 Iniciando servidor de desarrollo...")
    print("💡 Accede a: http://127.0.0.1:8000")
    print("💡 Admin: http://127.0.0.1:8000/admin/")
    print("🛑 Presiona Ctrl+C para detener el servidor")
    
    try:
        subprocess.call([sys.executable, "manage.py", "runserver"])
    except KeyboardInterrupt:
        print("\n👋 Servidor detenido")
    
    return True

if __name__ == "__main__":
    install_and_start()