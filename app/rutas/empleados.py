from flask import Blueprint, jsonify
import sqlite3
from flask_jwt_extended import jwt_required

# Creamos el Blueprint llamado 'empleados'
empleados_bp = Blueprint('empleados', __name__)

# Ruta GET encapsulada en el Blueprint
@empleados_bp.route('/empleados', methods=['GET'])
@jwt_required() # candado, verifica el usuario y contrasena 
def obtener_empleados():
    # Usamos una ruta absoluta temporal para asegurar que encuentre la BD copiada
    conexion = sqlite3.connect("empresa.db") 
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM empleados")
    lista_empleados = cursor.fetchall()
    conexion.close()

    empleados_json = []
    for empleado in lista_empleados:
        empleados_json.append({
            "id": empleado[0],
            "nombre": empleado[1],
            "departamento": empleado[2]
        })
        
    return jsonify(empleados_json)