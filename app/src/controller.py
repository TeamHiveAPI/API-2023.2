#aplicação principal
from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config['upload_path'] = '../src/static/img/uploads/'

db = SQLAlchemy(app)


from  routes import  *

# Para fazer rodar a aplicação sem precisar ficar reinicializar toda vez
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)