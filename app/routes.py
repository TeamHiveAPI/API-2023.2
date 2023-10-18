@app.route('/')
def home():
    return render_template('index.html', title='Home')

@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog")

@app.route('/dados')
def dados():
    return render_template('dados.html', title="Dados")