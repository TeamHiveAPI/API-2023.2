from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
	FLASK_APP = "wsgi.py"

	SESSION_TYPE = 'filesystem'
	SECRET_KEY = environ.get("SECRET_KEY")

	SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI") # Caminho para o banco de dados mysql
	SQLALCHEMY_ECHO = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False