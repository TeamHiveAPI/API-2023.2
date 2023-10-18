from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask("__name__")
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'bdAPI'
mysql.init_app(app)

@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog")

@app.route('/dados')
def dados():
    return render_template('dados.html', title="Dados")