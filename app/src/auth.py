from flask import Blueprints, render_template

auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', title="Login")

@auth_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    return render_template('cadastro.html', title="Cadastro")