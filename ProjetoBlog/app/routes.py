from app import app, db
from flask import render_template, request, flash, redirect
from app.forms import Cadastro
from app.models import TblCadastro

@app.route('/')
def index():
    return render_template('index.html', titulo = 'Home Page')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo = 'Sobre')

@app.route('/login')
def login():
    return render_template('login.html', titulo = 'Login')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    cadastro = Cadastro()    
    if cadastro.validate_on_submit():
        nome = cadastro.nome.data
        email = cadastro.email.data
        senha = cadastro.senha.data
        flash('Dados enviados com sucesso!')

        novo_cadastro = TblCadastro(nome = nome, email = email, senha = senha)
        db.session.add(novo_cadastro)
        db.session.commit()
        
    return render_template('cadastro.html', titulo = 'Cadastro', cadastro = cadastro)

@app.route('/projeto')
def projeto():
    return render_template('projeto.html', titulo = 'Projeto')

@app.route('/blog')
def blog():
    return render_template('blog.html', titulo = 'Blog')

@app.route('/dados', methods=['POST'])
def dados():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    if len(senha) == 0 or len(senha) == 0 or len(senha) == 0:
        flash('Campo Vazio!')
        return redirect('/cadastro')
    else:
       return f"Nome: {nome}\nEmail: {email}\nSenha: {senha}" 
    

# @app.route('/dados', methods=['GET'])
# def dados():
#     nome = request.args.get('nome')
#     email = request.args.get('email')
#     senha = request.args.get('senha')
#     return f"Nome: {nome}\nEmail: {email}\nSenha: {senha}"