from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods = ['POST'])
def login():
    datos = request.get_json()

    # extraer las variablews username y password
    username = datos.get('username')
    password = datos.get('password')

    if username == "admin" and password == "admin123":
        token_generado = create_access_token(identity=username)
        return jsonify({"token": token_generado}), 200
    else:
        return jsonify ({"error":"credenciales invalidas"}), 401