from flask import Flask, render_template, url_for, Blueprint

from flask import current_app as app

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