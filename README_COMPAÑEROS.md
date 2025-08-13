# 🚀 Sistema Escolar - Guía Rápida para Compañeros

## 📋 Información del Proyecto
- **Repositorio**: https://github.com/jdcarvajalMontoya/SistemaEscolarBootstrap
- **Rama**: `jhans_11`
- **Desarrollador**: Juan David Carvajal Montoya
- **Tecnologías**: Django 5.x, Python 3.10+, PostgreSQL, Tailwind CSS

---

## ⚡ Instalación Rápida (Método Automático)

### 1. Clonar el repositorio
```bash
git clone https://github.com/jdcarvajalMontoya/SistemaEscolarBootstrap.git
cd SistemaEscolarBootstrap
git checkout jhans_11
```

### 2. Ejecutar instalador automático
```bash
python setup_companeros.py
```

### 3. Configurar base de datos
1. Instala PostgreSQL
2. Crea base de datos `sistema_escolar`
3. Edita el archivo `.env` con tus credenciales

### 4. Activar entorno y ejecutar
```bash
# Windows
env\Scripts\activate

# Linux/Mac
source env/bin/activate

# Ejecutar migraciones
python manage.py migrate

# Iniciar servidor
python manage.py runserver
```

### 5. Acceder al sistema
- URL: http://localhost:8000
- ¡Listo! 🎉

---

## 📖 Instalación Manual (Si el automático falla)

Consulta el archivo `GUIA_IMPLEMENTACION_COMPAÑEROS.md` para instrucciones detalladas paso a paso.

---

## 🔧 Requisitos Previos

- **Python 3.10+** - [Descargar](https://www.python.org/downloads/)
- **Git** - [Descargar](https://git-scm.com/downloads)
- **PostgreSQL 15-17** - [Descargar](https://www.postgresql.org/download/)
- **Node.js 18+** - [Descargar](https://nodejs.org/)

---

## 🚨 Problemas Comunes

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

---

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs del servidor
2. Consulta `GUIA_IMPLEMENTACION_COMPAÑEROS.md`
3. Contacta al desarrollador con el error específico

---

## ✅ Checklist de Verificación

- [ ] Repositorio clonado desde rama `jhans_11`
- [ ] Entorno virtual activado
- [ ] Dependencias instaladas
- [ ] Base de datos configurada
- [ ] Migraciones aplicadas
- [ ] Servidor ejecutándose
- [ ] Sistema accesible en navegador

---

## 🎯 Comandos Útiles

```bash
# Activar entorno virtual
env\Scripts\activate  # Windows
source env/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
npm install

# Compilar CSS
npm run build

# Ejecutar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Iniciar servidor
python manage.py runserver

# Recolectar archivos estáticos
python manage.py collectstatic
```

---

## 📚 Archivos Importantes

- `setup_companeros.py` - Instalador automático
- `GUIA_IMPLEMENTACION_COMPAÑEROS.md` - Guía detallada
- `requirements.txt` - Dependencias Python
- `package.json` - Dependencias Node.js
- `.env` - Configuración (crear manualmente)

---

## 🎉 ¡Listo para Desarrollar!

Una vez que el sistema esté funcionando, puedes:
- Crear usuarios y probar funcionalidades
- Modificar código según necesidades
- Hacer commits a tu rama
- Colaborar con el equipo

¡Feliz desarrollo! 🚀

