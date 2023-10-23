from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(UserMixin, db.Model):
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

	parentesco = db.Column(
		db.String(10),
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

	comochegou = db.Column(
		db.String(22),
		nullable=False
	)

	def __init__(self, nome, dn, cpf, endereco, email, parentesco, senha, profissao, comochegou):
		self.nome = nome 
		self.dn = dn
		self.cpf = cpf
		self.endereco = endereco
		self.email = email
		self.parentesco = parentesco
		self.senha = generate_password_hash(senha, method='sha256')#faz a criptografia da senha, e armazena com segurança no banco de dados
		self.profissao = profissao
		self.comochegou = comochegou

	#confere se a senha é igual ao do usuario.
	def check_password(self, senha):
		return check_password_hash(self.senha, senha)

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

