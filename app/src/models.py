from werkzeug.security import generate_password_hash, check_password_hash

from . import db

class Usuario(db.Model):
	__tablename__ = "usuario"

	id = db.Column(
		db.Integer,
		primary_key=True
	)

	nome = db.Column(
		db.String(64),
		nullable=False
	)

	dn = db.Column(
		db.Date,
		nullable=False
	)

	cpf = db.Column(
		db.String(11),
		unique=True,
		nullable=False
	)

	endereco = db.Column(
		db.String(100),
		nullable=False
	)

	email = db.Column(
		db.String(80),
		unique=True,
		nullable=False
	)
	
	senha = db.Column(
		db.String(200),
		nullable=False
	)
	
	profissao = db.Column(
		db.String(20),
		nullable=False
	)

class Post(db.Model):
	__tablename__ = "post"

	id = db.Column(
		db.Integer,
		primary_key=True
	)

	autor =	db.Column(
		db.ForeignKey(Usuario.id),
		primary_key=True
	)

	titulo = db.Column(
		db.String(50),
		nullable=False
	)

	conteudo = db.Column(
		db.Text,
		nullable=False
	)

