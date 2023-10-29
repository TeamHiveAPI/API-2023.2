from controller import app
from datetime import datetime
from flask import render_template, redirect, url_for, request, session, flash
from models import Imagem, Usuario, Post, db

#Rota pagina inicial
@app.route('/')
def index():
    if session.get('user_logado'):
        return render_template('index.html', title='MINHA CONTA', nav='active', )
    return render_template('index.html', nav='active', title='LOGIN')

# Rota do Blog
@app.route('/blog', methods=['GET', 'POST'])
def blog():
    if request.method == 'POST':
            if 'user_id' in session:
                autor = session['user_id']
                nomefilho = request.form['nomefilho']
                conteudo = request.form['conteudo']
                data_postagem = datetime.now()
                #imagens = request.files.getlist('imagem') 

                novo_post = Post(autor_id=autor, nome_filho=nomefilho, conteudo=conteudo, data_postagem=data_postagem)
                db.session.add(novo_post)

                try:
                    db.session.commit()
                    #novo_post_id = novo_post.id 
                    #if imagens:
                        #for imagem in imagens:
                            #nova_imagem = Imagem(novo_post_id, imagem)
                            #db.session.add(nova_imagem)
                            #db.session.commit()
                            #pass
                    flash('Post adicionado com sucesso!')
                    return redirect(url_for('blog'))
                except Exception as e:
                    db.session.rollback()
                    flash(f'Erro ao adicionar o post: {str(e)}')
            else:
                flash('Faça login para postar!')

    posts = Post.query.order_by(Post.id.desc()).all()
    posts_info = []

    for post in posts:
        autor_id = post.autor_id
        usuario = Usuario.query.filter_by(id=autor_id).first()
        
        if usuario:
            data_formatada = post.data_postagem.strftime("%d-%m-%Y")
            post_info = {
                'nome_parente': usuario.nome,
                'parentesco': usuario.parentesco,
                'nome_filho': post.nome_filho,
                'data_postagem': data_formatada,
                'conteudo': post.conteudo
            }
            posts_info.append(post_info)
        else:
            print(f"Usuário não encontrado para o post com ID: {post.id}")

    if 'user_logado' in session: 
        return render_template('blog.html', title='MINHA CONTA', nav='active', posts=posts_info)

    return render_template('blog.html', nav='active', title='LOGIN', posts=posts_info)


#Rota pagina dados 
@app.route('/dados')
def dados():
    if session.get('user_logado'):
        return render_template('dados.html', title='MINHA CONTA', nav='active')
    return render_template('dados.html', title='LOGIN', nav='active')

@app.route('/minhaconta', methods=['GET', 'POST'])
def conta():
    if session.get('user_logado'):
        user_id = session['user_id'] 
        user = Usuario.query.get(user_id)#coloquei 
        if user:  # Verifique se o usuário existe
            return render_template('minhaconta.html', title='MINHA CONTA', nav='active', user=user)
    
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
        flash ('Usuário criado com sucesso. Realize o login.')
        return redirect(url_for('conta'))
    #no metodo get ele vai renderizar a pagina
    return render_template('cadastro.html',title='CADASTRO', nav='active')

#Rota para logar com o usuario
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
                flash('Login realizado com sucesso!')
                return redirect(url_for('conta'))
        flash('Verifique suas credenciais!')
    return render_template('login.html', nav='active', title='LOGIN')  

#Rota para deletar conta do usuario
@app.route('/deletar-conta', methods=['POST'])
def deletar_conta():
    if request.method == 'POST':
        if session.get('user_logado'):
            user_id = session['user_id']
            user = Usuario.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                flash('Conta excluida com sucesso!')
                return redirect(url_for('logout'))
    return "Acesso inválido a esta página."

#Rota para sair da conta do usuario
@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if request.method == 'POST':
        # Lógica de logout
        session['user_id'] = None
        session['user_logado'] = None
        session['user_email'] = None
        flash('Logout realizado com sucesso!')
        return redirect(url_for('login'))
    # Lógica de logout para solicitações GET
    session['user_id'] = None
    session['user_logado'] = None
    session['user_email'] = None
    return redirect(url_for('login'))

