from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import CadastroForm, LoginForm
from .models import db, Usuario
from flask_login import current_user, login_user
from werkzeug.security import  check_password_hash

auth_bp = Blueprint('auth_bp', __name__,template_folder='templates',static_folder='static')

#rotas relativas
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	
	form =LoginForm()
	if form.validate_on_submit():
		usuario= Usuario.query.filter_by(email= form.email.data).first()
		if usuario and check_password_hash(usuario.senha, form.senha.data):
			login_user(usuario)
			return redirect(url_for('index'))
		
	flash('E-mail ou senha invalidos!')
	return render_template('login', form=form, nav='active')

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	form = CadastroForm()
	if form.validade_on_submit():
		existing_user = Usuario.query.filter_by(email=form.email.data).first()
		if existing_user == None:
			usuario = Usuario()
			usuario=(usuario, form.nome.data, form.dn.data, form.cpf.data, form.endereco.data, form.email.data, form.parentesco.data, form.profissao.data, form.comochegou.data, form.senha.data)
			db.session.add(usuario)
			db.session.commit()
			login_user(usuario)
			return redirect(url_for('index'))
	return render_template('cadastro.html')