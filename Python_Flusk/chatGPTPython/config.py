import os

class Config:
    # Configuración de la base de datos en MariaDB
    SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:pandur%40tE01@localhost:3307/biblioteca'

    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desactiva el seguimiento de modificaciones
    SECRET_KEY = os.urandom(24)  # Clave secreta para sesiones, puedes cambiarla por algo más seguro
