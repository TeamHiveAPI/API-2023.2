from controller import db
from sqlalchemy import BINARY

# Conexão com as tabelas
class Usuario(db.Model):
    __tablename__ = "usuario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(64), nullable=False)
    dn = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    endereco = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    parentesco = db.Column(db.String(10), nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    profissao = db.Column(db.String(20), nullable=False)
    comochegou = db.Column(db.String(22), nullable=False)
    imagem_perfil = db.Column(db.String(255), nullable=True)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, nome, dn, cpf, endereco, email, parentesco, senha, profissao, comochegou, is_admin=False):
        self.nome = nome
        self.dn = dn
        self.cpf = cpf
        self.endereco = endereco
        self.email = email
        self.parentesco = parentesco
        self.senha = senha
        self.profissao = profissao
        self.comochegou = comochegou
        self.is_admin = is_admin



class Esquecisenha(db.Model):
    __tablename__ = "esquecisenha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), unique=False, nullable=False)
    chave = db.Column(db.String(200), nullable=False)
    utilizado = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, chave, utilizado=False):
        self.email = email
        self.chave = chave
        self.utilizado = utilizado













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
    status = db.Column(db.String(10), nullable=False, default='pendente')
    
    # Estabelecendo a relação entre Post e Imagem
    imagens = db.relationship('Imagem', backref='post', lazy='dynamic')

    def __init__(self, autor_id, nome_filho, conteudo, data_postagem, status='pendente'):
        self.autor_id = autor_id 
        self.nome_filho = nome_filho
        self.conteudo = conteudo
        self.data_postagem = data_postagem
        self.status = status
