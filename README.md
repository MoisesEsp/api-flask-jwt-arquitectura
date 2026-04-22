# 🏢 API REST - Gestión de Empleados (Flask + JWT)

Una API RESTful desarrollada en Python para la gestión de empleados. Este proyecto está diseñado con un enfoque en la arquitectura limpia y la seguridad, implementando el patrón **App Factory**, modularización a través de **Blueprints** y un sistema de autenticación seguro utilizando **JSON Web Tokens (JWT)**.

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **Framework:** Flask
* **Base de Datos:** SQLite3
* **Seguridad:** Flask-JWT-Extended (Autenticación basada en tokens)
* **Entorno:** python-dotenv (Gestión de variables de entorno seguras)

## 🏗️ Arquitectura del Proyecto

El código está estructurado para ser escalable y mantenible:

```Proyecto11_API_Avanzada
├── app/
│   ├── __init__.py          # App Factory: Inicialización y configuración del servidor
│   └── rutas/
│       ├── auth.py          # Blueprint: Lógica de inicio de sesión y generación de tokens
│       └── empleados.py     # Blueprint: Endpoints CRUD protegidos
├── .env.example             # Plantilla de variables de entorno
├── .gitignore               # Exclusión de archivos sensibles e inútiles en el repositorio
├── empresa.db               # Base de datos local
└── run.py                   # Archivo de arranque principal

🚀 Instalación y Ejecución Local
Sigue estos pasos para levantar el servidor en tu propia máquina:

1. Clonar el repositorio:
git clone [https://github.com/MoisesEsp/api-flask-jwt-arquitectura.git](https://github.com/tu-usuario/api-flask-jwt-arquitectura.git)
cd api-flask-jwt-arquitectura

2. Crear y activar el entorno virtual:
python -m venv .venv
# En Windows:
.\.venv\Scripts\activate

3. Instalar las dependencias:
    (Asegúrate de tener un archivo requirements.txt, o instala manualmente Flask, Flask-JWT-Extended y python-dotenv)

(Asegúrate de tener un archivo requirements.txt, o instala manualmente Flask, Flask-JWT-Extended y python-dotenv)

4. Configurar las variables de entorno:
Crea un archivo llamado .env en la raíz del proyecto y define tu clave secreta:

JWT_SECRET_KEY=tu_clave_secreta_super_segura_de_32_bytes

5. Inicia el servidor:
python run.py
El servidor estará disponible en http://127.0.0.1:5000


📡 Endpoints de la API
Método	Ruta	            Descripción	Requiere Auth	                        Body (JSON)
POST	/api/auth/login	    Iniciar sesión y obtener token	❌	               {"username": "admin", "password": "..."}
GET	    /api/empleados	    Obtener lista de todos los empleados	✅          Ninguno