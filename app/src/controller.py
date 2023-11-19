#aplicação principal
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_pyfile('config.py') 
app.config['upload_path'] = '../src/static/img/uploads/'
app.config['upload_perfil'] = os.path.abspath('static/img/uploads_perfil')

db = SQLAlchemy(app)

from routes import *

def inicializando_app():
    with app.app_context():
        db.create_all()
        # Verifica se o usuário administrador já existe antes de adicioná-lo
        admin_user = Usuario.query.filter_by(email='admin@teamhive.com').first()
        if admin_user is None:
            adm = Usuario(nome='Admin', dn='2023-09-01', cpf='00000000011', endereco='@rimdoamor', email='admin@teamhive.com', parentesco='outro', senha='rim#doamor570', profissao='Administrador', comochegou='outro', is_admin=1)
            db.session.add(adm)
            db.session.commit()

# Para fazer rodar a aplicação sem precisar ficar reinicializar toda vez
if __name__ == '__main__':
    inicializando_app()
    app.run(debug=True)