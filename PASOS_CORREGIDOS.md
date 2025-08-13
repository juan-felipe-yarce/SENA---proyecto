# 🚀 Pasos Corregidos para Ejecutar el Proyecto en Cualquier PC

## 📋 Requisitos Previos (OBLIGATORIOS)
- Python 3.10+
- Git
- PostgreSQL 15-17
- Node.js 18+

---

## 🔄 Paso 1: Clonar el Repositorio (CORREGIDO)

```bash
# ✅ CORRECTO - Clonar el repositorio completo
git clone https://github.com/jdcarvajalMontoya/SistemaEscolarBootstrap.git

# Entrar al directorio
cd SistemaEscolarBootstrap

# ✅ IMPORTANTE - Cambiar a la rama específica
git checkout jhans_11

# Verificar que estás en la rama correcta
git branch
```

---

## 🐍 Paso 2: Configurar Entorno Virtual

```bash
# Crear entorno virtual
python -m venv env

# Activar entorno virtual (Windows)
env\Scripts\activate

# Verificar que está activado (debe aparecer (env) al inicio)
```

---

## 📦 Paso 3: Instalar Dependencias

```bash
# Instalar dependencias de Python
pip install -r requirements.txt

# Instalar dependencias de Node.js
npm install
```

---

## 🗄️ Paso 4: Configurar Base de Datos (OBLIGATORIO)

### 4.1 Instalar y configurar PostgreSQL
1. Descarga e instala PostgreSQL desde: https://www.postgresql.org/download/
2. Durante la instalación, anota el usuario y contraseña que configures
3. Abre pgAdmin4 y crea una base de datos llamada `sistema_escolar`

### 4.2 Crear archivo de configuración
Crea un archivo `.env` en la raíz del proyecto:

```env
DEBUG=True
SECRET_KEY=django-insecure-cambia-esta-clave-en-produccion
DATABASE_URL=postgresql://tu_usuario:tu_contraseña@localhost:5432/sistema_escolar

# Configuración de base de datos
DB_NAME=sistema_escolar
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
```

**Reemplaza:**
- `tu_usuario`: Tu usuario de PostgreSQL
- `tu_contraseña`: Tu contraseña de PostgreSQL

---

## 🎨 Paso 5: Compilar Frontend (OBLIGATORIO)

```bash
# Compilar Tailwind CSS
npm run build
```

---

## ⚙️ Paso 6: Configurar Django

### 6.1 Verificar configuración de base de datos
Abre `core/settings.py` y asegúrate de que tenga:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sistema_escolar',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 6.2 Ejecutar migraciones
```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate
```

---

## 👤 Paso 7: Crear Superusuario (Opcional)

```bash
# Crear superusuario
python manage.py createsuperuser
```

---

## 🚀 Paso 8: Ejecutar el Proyecto

```bash
# Iniciar servidor
python manage.py runserver
```

### Acceder al sistema:
- URL: http://localhost:8000
- ¡Listo! 🎉

---

## 🔧 Solución de Problemas Comunes

### Error: "psycopg2 not found"
```bash
pip install psycopg2-binary
```

### Error: "Database connection failed"
1. Verifica que PostgreSQL esté ejecutándose
2. Revisa credenciales en `.env` y `settings.py`
3. Verifica que la base de datos existe

### Error: "Static files not found"
```bash
python manage.py collectstatic
npm run build
```

### Error: "Port already in use"
```bash
python manage.py runserver 8001
```

---

## ✅ Checklist de Verificación

- [ ] Repositorio clonado correctamente
- [ ] Rama `jhans_11` seleccionada
- [ ] Entorno virtual activado
- [ ] Dependencias Python instaladas
- [ ] Dependencias Node.js instaladas
- [ ] PostgreSQL instalado y ejecutándose
- [ ] Base de datos `sistema_escolar` creada
- [ ] Archivo `.env` configurado
- [ ] Tailwind CSS compilado
- [ ] Migraciones aplicadas
- [ ] Servidor ejecutándose sin errores

---

## 🎯 Comandos Completos en Orden

```bash
# 1. Clonar y cambiar rama
git clone https://github.com/jdcarvajalMontoya/SistemaEscolarBootstrap.git
cd SistemaEscolarBootstrap
git checkout jhans_11

# 2. Entorno virtual
python -m venv env
env\Scripts\activate

# 3. Dependencias
pip install -r requirements.txt
npm install

# 4. Compilar CSS
npm run build

# 5. Configurar .env (manual)

# 6. Migraciones
python manage.py makemigrations
python manage.py migrate

# 7. Superusuario (opcional)
python manage.py createsuperuser

# 8. Ejecutar
python manage.py runserver
```

---

## ⚠️ Notas Importantes

1. **PostgreSQL es OBLIGATORIO** - No funciona con SQLite
2. **La rama debe ser `jhans_11`** - No `Jhans_11`
3. **Tailwind CSS debe compilarse** - No funciona sin compilar
4. **Archivo `.env` es necesario** - Para configuración de base de datos

---

## 🎉 ¡Con estos pasos corregidos funcionará en cualquier PC!
