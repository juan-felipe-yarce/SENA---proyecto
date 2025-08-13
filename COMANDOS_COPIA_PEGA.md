# 📋 Comandos Listos para Copiar y Pegar

## 🚀 Instalación Rápida (Copia y Pega)

### 1. Clonar Repositorio
```bash
cd C:\xampp\htdocs
git clone https://github.com/jdcarvajalMontoya/SistemaEscolarBootstrap.git
cd SistemaEscolarBootstrap
git checkout jhans_11
```

### 2. Ejecutar Instalador Automático
```bash
python setup_companeros.py
```

### 3. Activar Entorno y Ejecutar
```bash
env\Scripts\activate
python manage.py migrate
python manage.py runserver
```

---

## 📖 Instalación Manual (Copia y Pega)

### 1. Clonar y Configurar
```bash
cd C:\xampp\htdocs
git clone https://github.com/jdcarvajalMontoya/SistemaEscolarBootstrap.git
cd SistemaEscolarBootstrap
git checkout jhans_11
```

### 2. Entorno Virtual
```bash
python -m venv env
env\Scripts\activate
```

### 3. Dependencias
```bash
pip install -r requirements.txt
npm install
```

### 4. Compilar CSS
```bash
npm run build
```

### 5. Migraciones
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Servidor
```bash
python manage.py runserver
```

---

## 🔧 Comandos de Solución de Problemas

### Error de psycopg2
```bash
pip install psycopg2-binary
```

### Error de puerto ocupado
```bash
python manage.py runserver 8001
```

### Error de archivos estáticos
```bash
python manage.py collectstatic
npm run build
```

### Reinstalar dependencias Node.js
```bash
rm -rf node_modules package-lock.json
npm install
```

---

## 📝 Crear Archivo .env

Crea un archivo llamado `.env` en la raíz del proyecto con este contenido:

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

**Recuerda cambiar:**
- `tu_usuario` por tu usuario de PostgreSQL
- `tu_contraseña` por tu contraseña de PostgreSQL

---

## ✅ Verificación Rápida

### Verificar instalaciones
```bash
python --version
git --version
node --version
npm --version
```

### Verificar rama
```bash
git branch
```

### Verificar entorno virtual
```bash
echo $VIRTUAL_ENV
```

### Verificar dependencias
```bash
pip list
npm list
```

---

## 🎯 Comandos de Desarrollo

### Activar entorno
```bash
env\Scripts\activate
```

### Instalar nueva dependencia Python
```bash
pip install nombre_paquete
pip freeze > requirements.txt
```

### Instalar nueva dependencia Node.js
```bash
npm install nombre_paquete
```

### Compilar CSS en modo desarrollo
```bash
npm run watch
```

### Crear superusuario
```bash
python manage.py createsuperuser
```

### Ejecutar tests
```bash
python manage.py test
```

---

## 📞 Comandos de Diagnóstico

### Verificar configuración Django
```bash
python manage.py check
```

### Verificar migraciones
```bash
python manage.py showmigrations
```

### Verificar archivos estáticos
```bash
python manage.py collectstatic --dry-run
```

### Verificar base de datos
```bash
python manage.py dbshell
```

---

## 🚀 Comandos de Producción

### Recolectar archivos estáticos
```bash
python manage.py collectstatic --noinput
```

### Compilar CSS para producción
```bash
npm run build
```

### Ejecutar en puerto específico
```bash
python manage.py runserver 0.0.0.0:8000
```

### Ejecutar con configuración de producción
```bash
python manage.py runserver --settings=core.settings.production
```

---

## 📋 Checklist de Comandos

```bash
# 1. Clonar
cd C:\xampp\htdocs
git clone https://github.com/jdcarvajalMontoya/SistemaEscolarBootstrap.git
cd SistemaEscolarBootstrap
git checkout jhans_11

# 2. Entorno
python -m venv env
env\Scripts\activate

# 3. Dependencias
pip install -r requirements.txt
npm install

# 4. CSS
npm run build

# 5. Migraciones
python manage.py makemigrations
python manage.py migrate

# 6. Servidor
python manage.py runserver
```

---

## 🎉 ¡Listo!

Después de ejecutar estos comandos:
1. Abre http://localhost:8000
2. ¡El sistema debería estar funcionando!
3. Si hay errores, revisa la consola del servidor

¡Feliz desarrollo! 🚀
