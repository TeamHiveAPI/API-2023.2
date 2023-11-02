from controller import app
from datetime import datetime
from flask import render_template, redirect, url_for, request, session, flash, jsonify
from werkzeug.utils import secure_filename
from models import Imagem, Usuario, Post, db
import os
from os.path import join

#Rota pagina inicial
@app.route('/')
def index():
    if session.get('user_logado'):
        return render_template('index.html', title='MINHA CONTA', nav='active', )
    return render_template('index.html', nav='active', title='LOGIN')

# Rota blog
@app.route('/blog', methods=['GET', 'POST'])
def blog():
    if request.method == 'POST':
        if 'user_id' in session:
            autor = session['user_id']
            nomefilho = request.form['nomefilho']
            conteudo = request.form['conteudo']
            data_postagem = datetime.now()
            imagens = request.files.getlist('imagem')  # Obter várias imagens

            novo_post = Post(autor_id=autor, nome_filho=nomefilho, conteudo=conteudo, data_postagem=data_postagem)
            db.session.add(novo_post)

            try:
                db.session.commit()
                novo_post_id = novo_post.id

                for imagem in imagens:  # Iterar sobre várias imagens
                    if imagem:
                        nome_arquivo = secure_filename(imagem.filename)
                        caminho_completo = join(app.config['upload_path'], nome_arquivo)
                        
                        # Verifica se o arquivo já existe e, se existir, gera um novo nome
                        contador = 1
                        while os.path.exists(caminho_completo):
                            nome_arquivo = f"{os.path.splitext(nome_arquivo)[0]} ({contador}){os.path.splitext(nome_arquivo)[1]}"
                            caminho_completo = join(app.config['upload_path'], nome_arquivo)
                            contador += 1
                        
                        imagem.save(caminho_completo)
                        nova_imagem = Imagem(post_id=novo_post_id, caminho_arquivo=nome_arquivo)
                        db.session.add(nova_imagem)
                
                db.session.commit()  # Realizar o commit fora do loop, após processar todas as imagens
                flash('Post adicionado com sucesso!')
                return redirect(url_for('blog'))

            except Exception as e:
                db.session.rollback()
                flash(f'Erro ao adicionar o post: {str(e)}')

        else:
            flash('Faça login para postar!')
    else:
        page = request.args.get('page', default=1, type=int)
        posts_per_page = 5
        Post.query.order_by(Post.id.desc()).paginate(page=page, per_page=posts_per_page, error_out=False)


    posts = Post.query.order_by(Post.id.desc()).all()
    posts_info = []

    imagem_perfil_url = url_for('static', filename='img/perfil.png')

    for post in posts:
        autor_id = post.autor_id
        usuario = Usuario.query.filter_by(id=autor_id).first()
        caminhos_das_imagens = Imagem.query.filter_by(post_id=post.id).with_entities(Imagem.caminho_arquivo).all()
        if usuario:
            if usuario.imagem_perfil:
                imagem_perfil_url = url_for('static', filename='img/uploads_perfil/' + usuario.imagem_perfil)
                                    
        if usuario:
            data_formatada = post.data_postagem.strftime("%d-%m-%Y")
            post_info = {
                'nome_parente': usuario.nome,
                'parentesco': usuario.parentesco,
                'nome_filho': post.nome_filho,
                'data_postagem': data_formatada,
                'conteudo': post.conteudo,
                'caminho_das_imagens': caminhos_das_imagens,
                'imagem_perfil_url': imagem_perfil_url
            }
            posts_info.append(post_info)
        else:
            print(f"Usuário não encontrado para o post com ID: {post.id}")



    if 'application/json' in request.headers.get('Accept'):
                return jsonify(posts_info)
    
    if session.get('user_logado'):
        return render_template('blog.html', title='MINHA CONTA', nav='active', posts=posts_info, imagem_perfil_url=imagem_perfil_url)

    return render_template('blog.html', nav='active', title='LOGIN', posts=posts_info, imagem_perfil_url=imagem_perfil_url)


@app.route('/salvar_imagem', methods=['POST'])
def salvar_imagem():
    imagem = request.files['imagem']
    nome_arquivo = imagem.filename
    caminho_arquivo = os.path.join(app.root_path, 'uploads', nome_arquivo)
    imagem.save(caminho_arquivo)

    with open(caminho_arquivo, 'rb') as file:
        dados_imagem = file.read()

    nova_imagem = Imagem(nome=nome_arquivo, dados_imagem=dados_imagem)
    db.session.add(nova_imagem)
    db.session.commit()


#Rota pagina dados 
@app.route('/dados')
def dados():
    if session.get('user_logado'):
        return render_template('dados.html', title='MINHA CONTA', nav='active')
    return render_template('dados.html', title='LOGIN', nav='active')

#Rota de perfil
@app.route('/minhaconta', methods=['GET', 'POST'])
def conta():
    if session.get('user_logado'):
        user_id = session['user_id']
        user = Usuario.query.get(user_id)
        if user:
            if user.imagem_perfil:
                imagem_perfil_url = url_for('static', filename='img/uploads_perfil/' + user.imagem_perfil)
            else:
                imagem_perfil_url = url_for('static', filename='img/perfil.png')
            
            return render_template('minhaconta.html', title='MINHA CONTA', nav='active', user=user, imagem_perfil_url=imagem_perfil_url)
    return redirect(url_for('login'))

@app.route('/upload_perfil', methods=['POST'])
def upload_perfil():
    if 'imagem_perfil' in request.files:
        file = request.files['imagem_perfil']
        if file:
            # Verifique se o arquivo tem uma extensão permitida (por exemplo, .png, .jpg, .jpeg)
            if '.' in file.filename and file.filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg'}:
                filename = secure_filename(file.filename)
                caminho_arquivo = os.path.join(app.config['upload_perfil'], filename)
                # Salve a imagem no caminho especificado
                file.save(caminho_arquivo)
                # Atualize o caminho da imagem de perfil do usuário no banco de dados
                if 'user_id' in session:
                    user_id = session['user_id']
                    user = Usuario.query.get(user_id)
                    if user:
                        user.imagem_perfil = filename
                        db.session.commit()
                        flash('Imagem de perfil atualizada com sucesso')
                    else:
                        flash('Usuário não encontrado')
                else:
                    flash('Você deve estar logado para atualizar a imagem de perfil')
            else:
                flash('Apenas arquivos PNG, JPG e JPEG são permitidos')
        else:
            flash('Nenhum arquivo de imagem foi selecionado')
    else:
        flash('Campo de imagem de perfil não encontrado na solicitação')

    return redirect(url_for('conta'))
    
#Rota de cadastro 
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

# Rota para deletar conta do usuário
@app.route('/deletar-conta', methods=['POST'])
def deletar_conta():
    if request.method == 'POST':
        if 'user_id' in session:
            user_id = session['user_id']
            user = Usuario.query.get(user_id)
            if user:
                posts = Post.query.filter_by(autor_id=user_id).all()
                for post in posts:
                    images = Imagem.query.filter_by(post_id=post.id).all()
                    for image in images:
                        db.session.delete(image)
                    db.session.delete(post)
                # Agora você pode excluir o usuário
                db.session.delete(user)
                db.session.commit()
                flash('Conta excluída com sucesso!')
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

