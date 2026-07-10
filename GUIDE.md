# 📚 Guía de Referencia - Allergen Manager

---

## 1. Entornos Virtuales en Python

### ¿Qué es?
Una burbuja aislada que contiene las dependencias (librerías)
específicas de un proyecto, sin interferir con otros proyectos
ni con el Python global de tu máquina.
Equivalente a `node_modules` en proyectos JavaScript/React.

### Comandos esenciales

**Crear el entorno virtual:**
```bash
python -m venv venv
```
**Activarlo en Mac/Linux:**
```bash
source venv/bin/activate
```
**Activarlo en Windows:**
```bash PowerShell/CMD
venv\Scripts\activate
```
```bash Git Bash
source venv\Scripts\activate
```
**Desactivarlo:**
```bash
deactivate
```
**Guardar dependencias:**
```bash
pip freeze > requirements.txt
```
**Instalar dependencias desde archivo:**
```bash
pip install -r requirements.txt
```
### ⚠️ Importante
`venv/` nunca se sube a GitHub — está en `.gitignore`.
Cada máquina genera el suyo propio con `pip install -r requirements.txt`.

---

## 2. Librerías del proyecto


|
 Librería 
|
 Para qué sirve 
|
|
---
|
---
|
|
`flask`
|
 Framework web principal 
|
|
`flask-sqlalchemy`
|
 Integra SQLAlchemy con Flask 
|
|
`flask-migrate`
|
 Gestiona versiones del esquema de BBDD 
|
|
`flask-jwt-extended`
|
 Gestión de tokens JWT para rutas protegidas 
|
|
`psycopg2-binary`
|
 Driver que conecta Python con PostgreSQL 
|
|
`python-dotenv`
|
 Lee variables de entorno del archivo 
`.env`
|
|
`flask-cors`
|
 Permite peticiones desde el frontend React 
|

---
## 3. CORS (Cross-Origin Resource Sharing)

### ¿Qué es?
Un mecanismo de seguridad del navegador que bloquea 
peticiones HTTP entre dominios distintos por defecto.

### El problema que resuelve
Sin CORS, cuando tu React (localhost:3000) intenta 
hacer un fetch a tu Flask (localhost:5000), el navegador 
lo bloquea porque son orígenes distintos (diferente puerto 
= diferente origen).

### Cómo funciona
El navegador antes de cada petición "real" envía una 
petición previa (OPTIONS) preguntando al servidor:
"¿Aceptas peticiones de este origen?"
Si el servidor responde que sí → deja pasar la petición.
Si no responde o dice no → la bloquea.

### Configuración en Flask

**Permitir todos los orígenes (desarrollo):**
```python
CORS(app)
```

**Permitir solo tu frontend (producción):**
```python
CORS(app, origins=["http://localhost:3000"])
```

### ⚠️ Importante
En desarrollo `CORS(app)` es suficiente.
En producción siempre especifica los orígenes permitidos.
---
## 4. Manejo de errores: try/except vs condicionales

### ¿Cuándo usar cada uno?

**Condicionales (if/else)** → para validar datos del cliente (4xx)
Cuando el error depende de lo que manda el usuario.
```python
if 'username' not in body:
    return jsonify({'error': 'username es obligatorio'}), 400
```

**try/except** → para errores del servidor (5xx)
Cuando el error puede ocurrir independientemente del cliente
(caída de BD, timeout, error de SQLAlchemy...).
```python
try:
    users = db.session.execute(db.select(User)).scalars().all()
except Exception as e:
    return jsonify({'error': 'Error interno del servidor'}), 500
```

### Estructura básica
```python
try:
    # código que puede fallar
    resultado = operacion_riesgosa()
except TipoDeError as e:
    # qué hacer si falla
    return jsonify({'error': str(e)}), 500
finally:
    # opcional: se ejecuta siempre, falle o no
    pass
```

### En endpoints Flask el patrón habitual es:
- **GET lista** → try/except alrededor de la consulta
- **POST** → if/else para validar body + try/except para guardar en BD
- **GET por id** → if/else para verificar que existe el recurso (404)
- **PUT** → ambos combinados
---