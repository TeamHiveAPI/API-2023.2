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

# Criação de uma tabela para as imagens, associada aos posts
class Imagem(db.Model):
    __tablename__ = 'imagem'

    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete='CASCADE'))
    caminho_arquivo = db.Column(db.String(255))  # Adicionando o campo para o caminho do arquivo

    def __init__(self, post_id, caminho_arquivo):  # Ajuste no construtor
        self.post_id = post_id
        self.caminho_arquivo = caminho_arquivo

class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    autor_id = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'))
    nome_filho = db.Column(db.Text, nullable=False)
    conteudo = db.Column(db.Text, nullable=False)
    data_postagem = db.Column(db.Date, nullable=False)
    
    # Estabelecendo a relação entre Post e Imagem
    imagens = db.relationship('Imagem', backref='post', lazy='dynamic')

    def __init__(self, autor_id, nome_filho, conteudo, data_postagem):
        self.autor_id = autor_id 
        self.nome_filho = nome_filho
        self.conteudo = conteudo
        self.data_postagem = data_postagem