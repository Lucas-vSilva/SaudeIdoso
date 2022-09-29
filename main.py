from crypt import methods
from flask import Flask, render_template, request
from model import model
import this

this.dados = ""
this.modelo = model()
this.msg = ""
this.campo = ""
this.dado = ""
#espaço cuidador
this.cod = 0
this.nome = ""
this.email = ""
this.telefone = ""
this.cpf = ""
this.sexo = ""
this.rg = ""
this.usu = ""
this.pswd = ""
this.endereco = ""
#espaço cliente
this.cod1 = 0
this.nome1 = ""
this.apelido = ""
this.sus = ""
this.rg1 = ""
this.cpf1 = ""
this.data = ""
this.sexo1 = ""
this.endereco1 = ""
this.data = ""
this.uf = ""
this.nacionalidade = ""
this.paisNascimento = ""
this.alfabetizado = ""
this.escolaridade = ""
this.etnia = ""
this.religiao = ""
this.email1 = ""
this.usu1 = ""
this.pswd1 = ""
#espaço monitoramento
this.pressao = ""
this.diabete = 0
this.dieta = ""
this.kilo = 0
this.altura = 0
this.cod2 = 0
#espaço agenda
this.cod3 = 0
this.exame = ""
this.consulta = ""
pessoa = Flask(__name__)

#Cliente abaixo

@pessoa.route('/', methods=['GET','POST'])
def cadastrarCliente():
    if request.method == 'POST':
        this.nome1     =      request.form['tNewNome']
        this.apelido  =   request.form['tNewApelido'] 
        this.sus      =       request.form['tNewSus']
        this.rg1       =        request.form['tNewRg']
        this.cpf1      =       request.form['tNewCpf']
        this.data     =      request.form['tNewData'] 
        this.sexo1    =      request.form['tNewSexo']
        this.uf       =        request.form['tNewUf']
        this.nacionalidade = request.form['tNewNacionalidade']
        this.alfabetizado  = request.form['tNewAlfabetizado'] 
        this.escolaridade  = request.form['tNewEscolaridade']
        this.etnia     =         request.form['tNewEtnia']
        this.religiao  =      request.form['tNewReligiao']
        this.email1     =     request.form['tNewEmail']
        this.usu1      =      request.form['tNewUsu']
        this.pswd1     =      request.form['tNewPswd']
        this.endereco1  =      request.form['tNewEndereco1']
        this.dados     = this.modelo.inserir(this.nome1, this.apelido, this.sus, this.rg, this.cpf1, this.data, this.sexo1, this.uf, this.nacionalidade, this.alfabetizado, this.escolaridade, this.etnia, this.religiao, this.email1, this.usu1, this.pswd1, this.endereco1)
    return render_template('index.html', titulo="Página Principal", resultado=this.dados)

@pessoa.route('/', methods=['GET','POST'])
def consultarCliente():
    if request.method == 'POST':
        this.cod1   = request.form['tNewCod1']
        this.msg = this.modelo.consultar(this.cod1)
    return render_template('consultar.html', titulo="Consultar", dados=this.msg)

@pessoa.route('/', methods=['GET','POST'])
def atualizarCliente():
    if request.method == 'POST':
        this.cod1 = request.form['tCod1']
        this.campo = request.form['tCampo']
        this.dado = request.form['tDado']
        this.msg = this.modelo.atualizar(this.cod1, this.campo, this.dado)
    return render_template('atualizar.html', titulo="Atualizar", dados=this.msg)

@pessoa.route('/', methods=['GET','POST'])
def excluirCliente():
    if request.method == 'POST':
        this.cod1 = request.form['tCod1']
        this.msg = this.modelo.excluir(this.cod1)
    return render_template('excluir.html', titulo="Excluir", dados=this.msg)

#Cuidador  abaixo

@pessoa.route('/', methods=['GET', 'POST'])
def cadastrarCuidador():
    if request.method == 'POST':
        this.email = request.form['tNewEmail']
        this.telefone = request.form['tNewTelefone']
        this.cpf = request.form['tNewCpf']
        this.sexo = request.form['tNewSexo']
        this.rg = request.form['tNewRg']
        this.usu = request.form['tNewUsu']
        this.pswd = request.form['tNewPswd']
        this.endereco  =      request.form['tNewEndereco']
        this.dados     = this.modelo.inserir(this.email, this.telefone,this.cpf,this.sexo,this.rg,this.usu,this.pswd)
    return render_template('index.html', titulo="Página Principal", resultado=this.dados)

@pessoa.route('/', methods=['GET','POST'])
def consultarCuidador():
    if request.method == 'POST':
        this.cod   = request.form['tNovoCod']
        this.msg = this.modelo.consultar(this.cod)
    return render_template('consultar.html', titulo="Consultar", dados=this.msg)

@pessoa.route('/', methods=['GET','POST'])
def atualizarCuidador():
    if request.method == 'POST':
        this.cod = request.form['tCod']
        this.campo = request.form['tCampo']
        this.dado = request.form['tDado']
        this.msg = this.modelo.atualizar(this.cod, this.campo, this.dado)
    return render_template('atualizar.html', titulo="Atualizar", dados=this.msg)

@pessoa.route('/', methods=['GET','POST'])
def excluirCuidador():
    if request.method == 'POST':
        this.cod = request.form['tCod']
        this.msg = this.modelo.excluir(this.cod)
    return render_template('excluir.html', titulo="Excluir", dados=this.msg)

if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)

