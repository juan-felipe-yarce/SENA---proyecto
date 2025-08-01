# 📚 Instrucciones para Insertar Datos de Educación en pgAdmin4

## 🎯 Objetivo
Insertar datos de educación docente en la tabla `core_educaciondocente` usando pgAdmin4.

## 📋 Pasos a seguir:

### **Paso 1: Abrir pgAdmin4**
1. Abre pgAdmin4
2. Conéctate a tu base de datos `sistema_escolar`
3. Ve a la pestaña "Query Tool"

### **Paso 2: Verificar hojas de vida existentes**
1. Copia y pega el contenido del archivo `verificar_hoja_vida.sql`
2. Ejecuta la consulta
3. Anota el `hoja_vida_id` que necesitas usar

### **Paso 3: Insertar datos de educación**
1. Abre el archivo `insert_educacion_colombia.sql`
2. **IMPORTANTE**: Reemplaza todos los `1` con el ID real de la hoja de vida
3. Copia y pega el script en pgAdmin4
4. Ejecuta el script

### **Paso 4: Verificar la inserción**
1. Ejecuta las consultas de verificación al final del script
2. Verifica que los datos se insertaron correctamente

## 📊 Estructura de la tabla:

```sql
core_educaciondocente:
- id (autoincremental)
- hoja_de_vida_id (FK a core_hojadevidadocente)
- nivel (varchar) - Primaria, Secundaria, Superior, etc.
- institucion (varchar) - Nombre de la institución
- titulo_obtenido (varchar) - Título obtenido
- fecha_inicio (date) - Fecha de inicio
- fecha_fin (date) - Fecha de finalización
```

## 🎓 Niveles de educación incluidos:

1. **Primaria** - Educación básica primaria
2. **Secundaria** - Educación media (bachillerato)
3. **Superior** - Pregrado universitario
4. **Posgrado** - Maestría
5. **Técnica** - Educación técnica (SENA)
6. **Tecnológica** - Tecnólogo
7. **Especialización** - Especialización
8. **Doctorado** - Doctorado

## 🏫 Instituciones incluidas:

- Universidad de Antioquia
- Universidad Nacional de Colombia
- Universidad EAFIT
- Universidad de los Andes
- SENA
- Instituto Tecnológico Metropolitano
- Colegios e instituciones educativas

## ⚠️ Notas importantes:

1. **Siempre verifica el ID de la hoja de vida** antes de insertar
2. **Las fechas deben estar en formato YYYY-MM-DD**
3. **Los niveles deben coincidir con los del formulario**
4. **Una hoja de vida puede tener múltiples registros de educación**

## 🔍 Consultas útiles:

```sql
-- Ver todas las hojas de vida
SELECT id, usuario_id FROM core_hojadevidadocente;

-- Ver educación por docente
SELECT 
    u.correo,
    ed.nivel,
    ed.institucion,
    ed.titulo_obtenido
FROM core_educaciondocente ed
JOIN core_hojadevidadocente hvd ON ed.hoja_de_vida_id = hvd.id
JOIN core_usuario u ON hvd.usuario_id = u.id
ORDER BY u.correo, ed.fecha_inicio;
```

## 🚀 Después de insertar:

1. Ve a tu aplicación Django
2. Inicia sesión como docente
3. Ve a la sección "Educación"
4. Verifica que los datos aparecen correctamente
5. Prueba agregar nuevos registros desde el formulario

¡Listo! 🎉 