import os
from flask import Flask
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

# Carga las variables definidas en el archivo .env a la memoria del sistema
load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
    jwt = JWTManager(app)

    from .rutas.empleados import empleados_bp # Importacion del Blueprint
    from .rutas.auth import auth_bp #Importacion del Blueprint autenticvacion
    
    app.register_blueprint(empleados_bp, url_prefix='/api') # registro del Blueprint
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    return app
