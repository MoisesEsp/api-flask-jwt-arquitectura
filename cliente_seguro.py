import requests

# PASO 1: login
url_login = "http://127.0.0.1:5000/api/auth/login"

credenciales = {"username":"admin", "password":"admin123"}
respuesta_login= requests.post(url_login, json=credenciales)

# Extraemos el token del JSON que nos devolvió el servidor
token = respuesta_login.json().get("token")
print("Código de estado:", respuesta_login.status_code)


# PASO 2: Ir a la zona VIP y mostrar el pase en la puerta (Empleados)
url_empleados = "http://127.0.0.1:5000/api/empleados"

# Preparamos nuestra cabecera con el token (La pulsera VIP)
cabeceras={
    "Authorization":f"Bearer {token}"
}

# Hacemos la petición GET, pero esta vez le adjuntamos las cabeceras
respuesta_empleados = requests.get(url_empleados,headers=cabeceras)
print("\n2. Reswpuesta del servidor protegido:")
print(respuesta_empleados.json())