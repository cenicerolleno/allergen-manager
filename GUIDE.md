\# 📚 Guía de Referencia - Allergen Manager



\---



\## 1. Entornos Virtuales en Python



\### ¿Qué es?

Una burbuja aislada que contiene las dependencias (librerías)

específicas de un proyecto, sin interferir con otros proyectos

ni con el Python global de tu máquina.

Equivalente a `node\_modules` en proyectos JavaScript/React.



\### Comandos esenciales



\*\*Crear el entorno virtual:\*\*

```bash

python -m venv venv

```

\*\*Activarlo en Mac/Linux:\*\*

```bash

source venv/bin/activate

```

\*\*Activarlo en Windows:\*\*

```bash

venv\\Scripts\\activate

```

\*\*Desactivarlo:\*\*

```bash

deactivate

```

\*\*Guardar dependencias:\*\*

```bash

pip freeze > requirements.txt

```

\*\*Instalar dependencias desde archivo:\*\*

```bash

pip install -r requirements.txt

```

\### ⚠️ Importante

`venv/` nunca se sube a GitHub — está en `.gitignore`.

Cada máquina genera el suyo propio con `pip install -r requirements.txt`.



\---



\## 2. Librerías del proyecto



| Librería | Para qué sirve |

|---|---|

| `flask` | Framework web principal |

| `flask-sqlalchemy` | Integra SQLAlchemy con Flask |

| `flask-migrate` | Gestiona versiones del esquema de BBDD |

| `flask-jwt-extended` | Gestión de tokens JWT para rutas protegidas |

| `psycopg2-binary` | Driver que conecta Python con PostgreSQL |

| `python-dotenv` | Lee variables de entorno del archivo `.env` |

| `flask-cors` | Permite peticiones desde el frontend React |



\---

