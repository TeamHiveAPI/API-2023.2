from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))

class Config:
	MYSQL_DATABASE_HOST = 'localhost'
	MYSQL_DATABASE_USER = 'root'
	MYSQL_DATABASE_DB = 'bdAPI'