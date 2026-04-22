import requests

url  = "http://127.0.0.1:5000/api/auth/login"

login = {
    "username" : "admin",
    "password" : "admin123"
}
    
respuesta = requests.post(url, json=login)