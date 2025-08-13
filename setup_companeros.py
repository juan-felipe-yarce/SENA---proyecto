#!/usr/bin/env python3
"""
Script de instalación automática para compañeros del proyecto Sistema Escolar
Desarrollado por: Juan David Carvajal Montoya
"""

import os
import sys
import subprocess
import platform
import json
from pathlib import Path

class Colors:
    """Colores para la terminal"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_header(text):
    """Imprimir encabezado con formato"""
    print(f"\n{Colors.HEADER}{Colors.BOLD}{'='*60}")
    print(f"  {text}")
    print(f"{'='*60}{Colors.ENDC}\n")

def print_step(text):
    """Imprimir paso del proceso"""
    print(f"{Colors.OKBLUE}➤ {text}{Colors.ENDC}")

def print_success(text):
    """Imprimir mensaje de éxito"""
    print(f"{Colors.OKGREEN}✅ {text}{Colors.ENDC}")

def print_warning(text):
    """Imprimir advertencia"""
    print(f"{Colors.WARNING}⚠️  {text}{Colors.ENDC}")

def print_error(text):
    """Imprimir error"""
    print(f"{Colors.FAIL}❌ {text}{Colors.ENDC}")

def run_command(command, check=True, capture_output=False):
    """Ejecutar comando del sistema"""
    try:
        if capture_output:
            result = subprocess.run(command, shell=True, check=check, 
                                  capture_output=True, text=True)
            return result.stdout.strip()
        else:
            subprocess.run(command, shell=True, check=check)
            return True
    except subprocess.CalledProcessError as e:
        if not capture_output:
            print_error(f"Error ejecutando: {command}")
            print_error(f"Error: {e}")
        return False

def check_python_version():
    """Verificar versión de Python"""
    print_step("Verificando versión de Python...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        print_success(f"Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print_error(f"Python {version.major}.{version.minor}.{version.micro} - Se requiere Python 3.10+")
        return False

def check_git():
    """Verificar si Git está instalado"""
    print_step("Verificando Git...")
    if run_command("git --version", capture_output=True):
        print_success("Git está instalado")
        return True
    else:
        print_error("Git no está instalado. Por favor instala Git primero.")
        return False

def check_node():
    """Verificar si Node.js está instalado"""
    print_step("Verificando Node.js...")
    if run_command("node --version", capture_output=True):
        print_success("Node.js está instalado")
        return True
    else:
        print_error("Node.js no está instalado. Por favor instala Node.js primero.")
        return False

def create_virtual_environment():
    """Crear entorno virtual"""
    print_step("Creando entorno virtual...")
    if os.path.exists("env"):
        print_warning("El entorno virtual ya existe")
        return True
    
    if run_command("python -m venv env"):
        print_success("Entorno virtual creado")
        return True
    else:
        print_error("Error creando entorno virtual")
        return False

def activate_virtual_environment():
    """Activar entorno virtual"""
    print_step("Activando entorno virtual...")
    if platform.system() == "Windows":
        activate_script = "env\\Scripts\\activate"
    else:
        activate_script = "source env/bin/activate"
    
    print_warning("Por favor activa manualmente el entorno virtual:")
    print(f"  {activate_script}")
    return True

def install_python_dependencies():
    """Instalar dependencias de Python"""
    print_step("Instalando dependencias de Python...")
    if run_command("pip install -r requirements.txt"):
        print_success("Dependencias de Python instaladas")
        return True
    else:
        print_error("Error instalando dependencias de Python")
        return False

def install_node_dependencies():
    """Instalar dependencias de Node.js"""
    print_step("Instalando dependencias de Node.js...")
    if run_command("npm install"):
        print_success("Dependencias de Node.js instaladas")
        return True
    else:
        print_error("Error instalando dependencias de Node.js")
        return False

def build_tailwind():
    """Compilar Tailwind CSS"""
    print_step("Compilando Tailwind CSS...")
    if run_command("npm run build"):
        print_success("Tailwind CSS compilado")
        return True
    else:
        print_error("Error compilando Tailwind CSS")
        return False

def create_env_file():
    """Crear archivo .env"""
    print_step("Creando archivo .env...")
    env_content = """DEBUG=True
SECRET_KEY=django-insecure-cambia-esta-clave-en-produccion
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/sistema_escolar

# Configuración de base de datos
DB_NAME=sistema_escolar
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
"""
    
    with open(".env", "w", encoding="utf-8") as f:
        f.write(env_content)
    
    print_success("Archivo .env creado")
    print_warning("IMPORTANTE: Edita el archivo .env con tus credenciales de PostgreSQL")
    return True

def run_migrations():
    """Ejecutar migraciones"""
    print_step("Ejecutando migraciones...")
    if run_command("python manage.py migrate"):
        print_success("Migraciones aplicadas")
        return True
    else:
        print_error("Error ejecutando migraciones")
        return False

def collect_static():
    """Recolectar archivos estáticos"""
    print_step("Recolectando archivos estáticos...")
    if run_command("python manage.py collectstatic --noinput"):
        print_success("Archivos estáticos recolectados")
        return True
    else:
        print_error("Error recolectando archivos estáticos")
        return False

def create_superuser():
    """Crear superusuario"""
    print_step("¿Deseas crear un superusuario? (s/n): ", end="")
    response = input().lower().strip()
    
    if response in ['s', 'si', 'sí', 'y', 'yes']:
        print_step("Creando superusuario...")
        print_warning("Sigue las instrucciones en pantalla")
        run_command("python manage.py createsuperuser", check=False)
        print_success("Superusuario creado (si no hubo errores)")
    else:
        print_warning("Saltando creación de superusuario")
    
    return True

def show_next_steps():
    """Mostrar próximos pasos"""
    print_header("PRÓXIMOS PASOS")
    
    steps = [
        "1. Configura PostgreSQL y crea la base de datos 'sistema_escolar'",
        "2. Edita el archivo .env con tus credenciales de PostgreSQL",
        "3. Activa el entorno virtual: env\\Scripts\\activate (Windows) o source env/bin/activate (Linux/Mac)",
        "4. Ejecuta las migraciones: python manage.py migrate",
        "5. Inicia el servidor: python manage.py runserver",
        "6. Abre http://localhost:8000 en tu navegador"
    ]
    
    for step in steps:
        print(f"{Colors.OKCYAN}{step}{Colors.ENDC}")
    
    print(f"\n{Colors.BOLD}¡El proyecto está listo para configurar!{Colors.ENDC}")

def main():
    """Función principal"""
    print_header("INSTALADOR AUTOMÁTICO - SISTEMA ESCOLAR")
    print(f"{Colors.OKCYAN}Desarrollado por: Juan David Carvajal Montoya{Colors.ENDC}")
    print(f"{Colors.OKCYAN}Rama: jhans_11{Colors.ENDC}\n")
    
    # Verificaciones previas
    checks = [
        ("Python 3.10+", check_python_version),
        ("Git", check_git),
        ("Node.js", check_node),
    ]
    
    for check_name, check_func in checks:
        if not check_func():
            print_error(f"Verificación fallida: {check_name}")
            print_error("Por favor instala los requisitos previos y ejecuta el script nuevamente")
            sys.exit(1)
    
    # Proceso de instalación
    installation_steps = [
        ("Entorno virtual", create_virtual_environment),
        ("Activación de entorno", activate_virtual_environment),
        ("Dependencias Python", install_python_dependencies),
        ("Dependencias Node.js", install_node_dependencies),
        ("Compilación Tailwind", build_tailwind),
        ("Archivo .env", create_env_file),
        ("Migraciones", run_migrations),
        ("Archivos estáticos", collect_static),
        ("Superusuario", create_superuser),
    ]
    
    for step_name, step_func in installation_steps:
        print(f"\n{Colors.BOLD}--- {step_name.upper()} ---{Colors.ENDC}")
        if not step_func():
            print_error(f"Error en: {step_name}")
            print_error("Revisa los errores anteriores y ejecuta el script nuevamente")
            sys.exit(1)
    
    # Mostrar próximos pasos
    show_next_steps()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.WARNING}Instalación cancelada por el usuario{Colors.ENDC}")
        sys.exit(1)
    except Exception as e:
        print_error(f"Error inesperado: {e}")
        sys.exit(1)

