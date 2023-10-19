from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
	FLASK_APP = "wsgi.py"

	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://fatec:senha@localhost:3306/usuarios' # Caminho para o banco de dados mysql
	SQLALCHEMY_ECHO = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
