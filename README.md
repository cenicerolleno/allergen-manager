# 🥗 Allergen Manager

Aplicación web fullstack para la gestión de alérgenos en platos de restaurante.
Permite registrar platos con sus ingredientes y obtener automáticamente
los alérgenos asociados consultando la API de Open Food Facts.

---

## 🛠️ Stack

- **Backend**: Python 3.13, Flask 3, SQLAlchemy 2, PostgreSQL 16
- **Frontend**: React (en desarrollo)
- **Auth**: JWT

---

## ⚙️ Instalación y configuración

### Requisitos previos
- Python 3.13+
- PostgreSQL 16
- Node.js (para el frontend)

### 1. Clonar el repositorio
```bash
git clone https://github.com/cenicerolleno/allergen-manager.git
cd allergen-manager
```

### 2. Configurar el backend

#### Mac/Linux
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

#### Windows (Git Bash)
```bash
cd backend
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

### 3. Crear el archivo .env
Crear un archivo `.env` en la raíz del proyecto:
DATABASE_URL=postgresql://postgres:TU_CONTRASEÑA@localhost:5432/allergen_manager
JWT_SECRET_KEY=tu_clave_secreta
FLASK_APP=app:create_app
FLASK_DEBUG=1

### 4. Crear la base de datos
```bash
psql -U postgres
CREATE DATABASE allergen_manager;
\q
```

### 5. Ejecutar migraciones
```bash
flask db upgrade
```

### 6. Arrancar el backend
```bash
flask run
```

El servidor estará disponible en `http://localhost:5000`

---

## 📁 Estructura del proyecto
allergen-manager/
├── backend/
│   ├── api/
│   │   ├── allergen/
│   │   ├── dish/
│   │   ├── ingredient/
│   │   └── user/
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   └── seed.py
├── frontend/
│   └── src/
├── .env (no incluido en el repositorio)
└── README.md

---

## 🚧 Estado del proyecto
En desarrollo activo — Módulo 2 (Desarrollo/Mentoría)