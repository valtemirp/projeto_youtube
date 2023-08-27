from app import app, db, bcrypt
from flask import render_template, flash, session
from app.forms import FormCadastro
from app.models import TblUsuario

@app.route('/')
def index():
    return render_template('index.html', titulo = 'Home')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo = 'Sobre')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html', titulo = 'Projetos')

@app.route('/blog')
def blog():
    return render_template('blog.html', titulo = 'Blog')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    cadastro = FormCadastro()
    dicionario_cadastro = {}
    if cadastro.validate_on_submit():
        nome = cadastro.nome.data
        email = cadastro.email.data
        telefone = cadastro.telefone.data
        senha = cadastro.senha.data
        senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')
        flash('Seu cadastro foi realizado com sucesso!')
        novo_usurio = TblUsuario(
            nome=nome,
            email = email,
            telefone = telefone,
            senha = senha_hash
            )
        db.session.add(novo_usurio)
        db.session.commit()
    return render_template('cadastro.html', titulo = 'Cadastre-se', dicionario_cadastro = dicionario_cadastro, cadastro = cadastro)

@app.route('/login')
def login():
    return render_template('login.html', titulo = 'Login')

@app.route('/teste')
def teste():
    return 'teste'