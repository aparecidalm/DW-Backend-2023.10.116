from app import app, db, bcrypt
from flask import render_template, request, flash, redirect
from app.forms import FormCadastro
from app.models import TblCadastro

@app.route('/')
def index():
    return render_template('index.html', titulo = 'Home Page')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo = 'Sobre')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro(): 
    cadastro = FormCadastro()  
    if request.method == 'GET':
        return render_template('cadastro.html', titulo = 'Cadastra-se', cadastro = cadastro)
    if request.method == 'POST':
        if cadastro.validate_on_submit():
            nome = cadastro.nome.data
            email = cadastro.email.data
            senha = cadastro.senha.data
            senha_crypt = bcrypt.generate_password_hash(senha).decode('utf-8')
            flash("Dados Enviados com Sucesso!")
            novo_usuario = TblCadastro(nome = nome, email = email, senha = senha_crypt)
            db.session.add(novo_usuario)
            db.session.commit()
            return redirect('/dados')
    

@app.route('/dados')
def dados():
    usuario = TblCadastro.query.all()
    return render_template('dados.html', usuario = usuario)


@app.route('/dados/<nome>')
def dados_id(nome):
    
    usuario = TblCadastro.query.filter_by(nome = nome).all()#first() - get(id)
    if usuario:
        return render_template('dados.html', usuario = usuario)
    return f"Usuário com o id = {id} não existe!"


@app.route('/dados/atualizar/<int:id>', methods = ['GET','POST'])
def atualizar(id):
    # cadastro = FormCadastro() 
    usuario = TblCadastro.query.get(id)
    if request.method == 'POST':
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']
            # nome = cadastro.nome.data
            # email = cadastro.email.data
            # senha = cadastro.senha.data
            usuario = TblCadastro(nome=nome, email=email, senha=senha)
            db.session.add(usuario)
            db.session.commit()
            return redirect(f'/dados')      
        return f"Usuário com o id = {id} não existe!"
    return render_template('atualizar.html', usuario = usuario)
 

@app.route('/dados/remover/<int:id>', methods=['GET','POST'])
def remover(id):
    usuario = TblCadastro.query.filter_by(id=id).first()
    if request.method == 'POST':
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return redirect('/dados')
 
    return render_template('remover.html')

# @app.route('/cadastro_dados', methods = ['GET'])
# def cadastro_dados():
#     nome = request.args.get('nome')
#     email = request.args.get('email')
#     senha = request.args.get('senha')
#     return f"Dados: {nome}  {email} {senha}"

@app.route('/cadastro_dados', methods = ['POST'])
def cadastro_dados():
    nome = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')
    if (len(nome) == 0) or (len(email) == 0) or (len(senha) == 0): 
        flash("faltou campo a ser preenchido!")
        return redirect('/cadastro')
    else:
        return f"Dados: {nome}  {email} {senha}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', titulo = 'Login')
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        u = TblCadastro.query.filter_by(email=email).first()
        # for u in usuario:
        print(f" {u.email} - {email}")
        print(f" {u.senha} - {senha}")            
        if email == u.email and bcrypt.check_password_hash(u.senha, senha):
            return render_template('autenticado.html', titulo = 'Autenticação', usuario = u.nome)
        else:
            flash("E-mail ou senha incorretos!")
            return redirect('/login') 
    
@app.route('/blog')
def blog():
    return render_template('blog.html', titulo = 'BLOG')

@app.route('/projeto')
def projeto():
    return render_template('projeto.html', titulo = 'Projeto')