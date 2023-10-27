from controller import app
from flask import render_template, redirect, url_for, request, session, flash
from models import Usuario, Post, db

#Rota pagina inicial
@app.route('/')
def index():
    if session.get('user_logado'):
        return render_template('index.html', title='MINHA CONTA', nav='active', )
    return render_template('index.html', nav='active', title='LOGIN')

#Rota pagina blog 
@app.route('/blog', methods=['GET', 'POST'])
def blog():
    if request.method == 'POST':
        autor = session['user_id']
        nomefilho = request.form['nomefilho']
        conteudo = request.form['conteudo']
        novo_post = Post(autor_id=autor, nome_filho=nomefilho, conteudo=conteudo)
        db.session.add(novo_post)

        try:
            db.session.commit()
            flash('Post adicionado com sucesso!')
            return redirect(url_for('blog'))
        except Exception as e:
            db.session.rollback()  # Desfaz a transação
            flash(f'Erro ao adicionar o post: {str(e)}')

    if session.get('user_logado'):
        return render_template('blog.html', title='MINHA CONTA', nav='active')

    return render_template('blog.html', nav='active', title='LOGIN')


#Rota pagina dados 
@app.route('/dados')
def dados():
    if session.get('user_logado'):
        return render_template('dados.html', title='MINHA CONTA', nav='active')
    return render_template('dados.html', title='LOGIN', nav='active')

@app.route('/minhaconta', methods=['GET'])
def conta():
    if session.get('user_logado'):
        return render_template('minhaconta.html', title='MINHA CONTA', nav='active')
    return redirect(url_for('login'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    #no metodo post, ele coleta as informações, verifica se o usuario já existe 
    #e insere um novo usuario.
    if request.method =='POST':
        nome = request.form['nome']
        dn = request.form['dn']
        cpf = request.form['cpf']
        endereco = request.form['endereco']
        email = request.form['email']
        parentesco = request.form['parentesco']
        senha = request.form['senha']
        profissao = request.form['profissao']
        comochegou = request.form['como-chegou']

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            flash('Usuario existente!')
            return redirect(url_for('login') )
        
        novo_user = Usuario(nome=nome, dn=dn, cpf=cpf,endereco=endereco, email=email, parentesco=parentesco, senha=senha, profissao=profissao, comochegou=comochegou)
        db.session.add(novo_user)
        db.session.commit()
        return redirect(url_for('conta'))
    #no metodo get ele vai renderizar a pagina
    return render_template('cadastro.html',title='CADASTRO', nav='active')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('user_logado'):
        return redirect(url_for('conta'))
    
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        usuario = Usuario.query.filter_by(email = email).first()
        if usuario:
            if senha == usuario.senha:
                session['user_id'] = usuario.id
                session['user_logado'] = usuario.nome
                session['user_email'] = usuario.email
                return redirect(url_for('conta'))
            return redirect(url_for('login'))
    return render_template('login.html', nav='active', title='LOGIN')    
    
@app.route('/logout', methods=['POST'])
def logout():
    if request.method == 'POST':
        session['user_id'] = None
        session['user_logado'] = None
        session['user_email'] = None
        flash('Logout realizado com sucesso!')
        return redirect(url_for('login'))

