# Importamos la fábrica desde nuestra carpeta app
from app import create_app

# Fabricamos la aplicación
app = create_app()

# Encendemos el servidor
if __name__ == '__main__':
    app.run(debug=True)