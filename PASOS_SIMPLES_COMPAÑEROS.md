# 🚀 Guía Simple para Compañeros - Sistema Escolar

## 📋 Información del Proyecto
- **Repositorio**: https://github.com/jdcarvajalMontoya/SistemaEscolarBootstrap
- **Rama**: `jhans_11`
- **Desarrollador**: Juan David Carvajal Montoya

---

## ⚡ Método Rápido (Recomendado)

### Paso 1: Instalar Software Necesario
1. **Python 3.10+** - [Descargar aquí](https://www.python.org/downloads/)
2. **Git** - [Descargar aquí](https://git-scm.com/downloads)
3. **PostgreSQL 15-17** - [Descargar aquí](https://www.postgresql.org/download/)
4. **Node.js 18+** - [Descargar aquí](https://nodejs.org/)

### Paso 2: Clonar el Proyecto
```bash
# Abrir CMD o PowerShell y navegar a tu carpeta de proyectos
cd C:\xampp\htdocs

# Clonar el repositorio
git clone https://github.com/jdcarvajalMontoya/SistemaEscolarBootstrap.git

# Entrar al proyecto
cd SistemaEscolarBootstrap

# Cambiar a la rama correcta
git checkout jhans_11
```

### Paso 3: Ejecutar Instalador Automático
```bash
# Ejecutar el script de instalación
python setup_companeros.py
```

### Paso 4: Configurar Base de Datos
1. **Abrir pgAdmin4**
2. **Crear base de datos** llamada `sistema_escolar`
3. **Editar archivo `.env`** con tus credenciales de PostgreSQL

### Paso 5: Activar y Ejecutar
```bash
# Activar entorno virtual
env\Scripts\activate

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

### Paso 6: Acceder al Sistema
- Abrir navegador
- Ir a: http://localhost:8000
- ¡Listo! 🎉

---

## 📖 Método Manual (Si el automático falla)

### Paso 1: Clonar Repositorio
```bash
cd C:\xampp\htdocs
git clone https://github.com/jdcarvajalMontoya/SistemaEscolarBootstrap.git
cd SistemaEscolarBootstrap
git checkout jhans_11
```

### Paso 2: Crear Entorno Virtual
```bash
python -m venv env
env\Scripts\activate
```

### Paso 3: Instalar Dependencias
```bash
pip install -r requirements.txt
npm install
```

### Paso 4: Compilar CSS
```bash
npm run build
```

### Paso 5: Configurar Base de Datos
1. **Instalar PostgreSQL** si no lo tienes
2. **Crear base de datos** `sistema_escolar` en pgAdmin4
3. **Crear archivo `.env`** en la raíz del proyecto:

```env
DEBUG=True
SECRET_KEY=django-insecure-cambia-esta-clave-en-produccion
DATABASE_URL=postgresql://tu_usuario:tu_contraseña@localhost:5432/sistema_escolar
DB_NAME=sistema_escolar
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

**Reemplaza:**
- `tu_usuario`: Tu usuario de PostgreSQL
- `tu_contraseña`: Tu contraseña de PostgreSQL

### Paso 6: Ejecutar Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### Paso 7: Crear Superusuario (Opcional)
```bash
python manage.py createsuperuser
```

### Paso 8: Iniciar Servidor
```bash
python manage.py runserver
```

---

## 🔧 Solución de Problemas

### Error: "psycopg2 not found"
```bash
pip install psycopg2-binary
```

### Error: "Database connection failed"
- Verifica que PostgreSQL esté ejecutándose
- Revisa credenciales en `.env`
- Verifica que la base de datos existe

### Error: "Port already in use"
```bash
python manage.py runserver 8001
```

### Error: "Static files not found"
```bash
python manage.py collectstatic
npm run build
```

---

## ✅ Checklist de Verificación

- [ ] Python 3.10+ instalado
- [ ] Git instalado
- [ ] PostgreSQL instalado
- [ ] Node.js instalado
- [ ] Repositorio clonado
- [ ] Rama `jhans_11` seleccionada
- [ ] Entorno virtual activado
- [ ] Dependencias instaladas
- [ ] CSS compilado
- [ ] Base de datos creada
- [ ] Archivo `.env` configurado
- [ ] Migraciones aplicadas
- [ ] Servidor ejecutándose
- [ ] Sistema accesible en navegador

---

## 🎯 Comandos Útiles

```bash
# Activar entorno virtual
env\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
npm install

# Compilar CSS
npm run build

# Migraciones
python manage.py makemigrations
python manage.py migrate

# Superusuario
python manage.py createsuperuser

# Servidor
python manage.py runserver

# Archivos estáticos
python manage.py collectstatic
```

---

## 📞 Si Tienes Problemas

1. **Revisa los logs** del servidor Django
2. **Verifica la consola** del navegador
3. **Consulta** `GUIA_IMPLEMENTACION_COMPAÑEROS.md`
4. **Contacta al desarrollador** con el error específico

---

## 🎉 ¡Listo para Trabajar!

Una vez que el sistema esté funcionando:
- Crea usuarios y prueba funcionalidades
- Modifica código según necesidades
- Haz commits a tu rama
- Colabora con el equipo

¡Feliz desarrollo! 🚀
