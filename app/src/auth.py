from flask import Blueprint, render_template, redirect, url_for
from .forms import CadastroForm, LoginForm
from .models import db, Usuario

auth_bp = Blueprint('auth_bp', __name__,template_folder='templates',static_folder='static')

#rotas relativas
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validade_on_submit():

	return render_template('login.html', nav='active')

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
	form = CadastroForm()
	if form.validade_on_submit():
		existing_user = Usuario.query.filter_by(email=form.email.data).first()
		if existing_user is None:
			usuario = Usuario()
			usuario.__init__(usuario, form.nome.data, form.dn.data, form.cpf.data, form.endereco.data, form.email.data, form.parentesco.data, form.profissao.data, form.comochegou.data, form.senha.data)
			db.session.add(usuario)
			db.session.commit()
			login_user(usuario)
			return redirect(url_for('index'))
	return render_template('cadastro.html')