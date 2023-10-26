from flask import Flask, render_template, url_for, Blueprint,redirect
from flask_login import current_user, login_required, logout_user
from flask import current_app as app

app.config.from_object('config.Config')

#Rota pagina inicial
@app.route('/')
def index():
    return render_template('index.html', nav='active')

#Rota pagina blog 
@app.route('/blog')
def blog():
    return render_template('blog.html', nav='active')

#Rota pagina dados 
@app.route('/dados')
def dados():
    return render_template('dados.html', nav='active')

@app.route('/minhaconta', methods=['GET'])
@login_required
def conta():
    return render_template('minhaconta.html', nav='active')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

