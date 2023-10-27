from controller import db

#conexão com as tabelas
class Usuario(db.Model):
	__tablename__ = "usuario"
	id = db.Column(db.Integer,primary_key=True, autoincrement=True)
	nome = db.Column(db.String(64),nullable=False)
	dn = db.Column(db.Date,nullable=False)
	cpf = db.Column(db.String(11),unique=True,nullable=False)
	endereco = db.Column(db.String(100),nullable=False)
	email = db.Column(db.String(80),unique=True,nullable=False)
	parentesco = db.Column(db.String(10),nullable=False)
	senha = db.Column(db.String(200),nullable=False)
	profissao = db.Column(db.String(20),nullable=False)
	comochegou = db.Column(db.String(22),nullable=False)

	def __init__(self, nome, dn, cpf, endereco, email, parentesco, senha, profissao, comochegou):
		self.nome = nome 
		self.dn = dn
		self.cpf = cpf
		self.endereco = endereco
		self.email = email
		self.parentesco = parentesco
		self.senha = senha 
		self.profissao = profissao
		self.comochegou = comochegou

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    nome_filho = db.Column(db.Text, nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
	#falta imagem (parte do banco)

	#def __init__(self, autor, titulo, conteudo, imagem):
		#completar (parte do blog)

