# config.py
from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev'
    SQLALCHEMY_DATABASE_URI = 'mariadb+mariadbconnector://root:pandur%40tE01@localhost:3307/biblioteca'
    SQLALCHEMY_TRACK_MODIFICATIONS = False