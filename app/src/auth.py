from flask import Blueprint, render_template, redirect, url_for
from app.models import User

auth_bp = Blueprint('auth_bp', __name__,template_folder='templates',static_folder='static')

#rotas relativas
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', nav='active')

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return render_template('cadastro.html')