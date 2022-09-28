from flask import Flask, render_template, request
from model import model
import this

this.dados = ""
this.modelo = model()
this.msg = ""
this.campo = ""
this.dado = ""
#espaço cliente
this.cod = 0
this.email = ""
this.telefone = ""
this.cpf = ""
this.sexo = ""
this.rg = ""
this.user = ""
this.pswd = ""
#espaço cuidador
this.cod1 = 0
this.nome = ""
this.apelido = ""
this.sus = ""
this.rg1 = ""
this.cpf1 = ""
this.data = ""
this.sexo1 = ""
this.endereco = ""
this.data = ""
this.uf = ""
this.nacionalidade = ""
this.paisNascimento = ""
this.alfabetizado = ""
this.escolaridade = ""
this.etnia = ""
this.religiao = ""
this.email1 = ""
this.user1 = ""
this.pswd1 = ""
#espaço monitoramento
this.pressao = ""
this.diabete = 0
this.dieta = ""
this.kilo = 0
this.altura = 0
this.cod1 = 0
#espaço agenda
this.cod2 = 0
this.exame = ""
this.consulta = ""
pessoa = Flask(__name__)

@pessoa.route('/', methods=['GET','POST'])
def cadastrar():
    if request.method == 'POST':
        this.nome     = request.form['tNovoNome']
        this.telefone = request.form['tNovoTelefone']
        this.endereco = request.form['tNovoEndereco']
        this.data     = request.form['tNovaData']
        this.dados    = this.modelo.inserir(this.nome, this.telefone, this.endereco, this.data)
    return render_template('index.html', titulo="Página Principal", resultado=this.dados)

@pessoa.route('/consultar.html', methods=['GET','POST'])
def consultarTudo():
    if request.method == 'POST':
        this.codigo   = request.form['tNovoCodigo']
        this.msg = this.modelo.consultar(this.codigo)
    return render_template('consultar.html', titulo="Consultar", dados=this.msg)

@pessoa.route('/atualizar.html', methods=['GET','POST'])
def atualizarDado():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.campo = request.form['tCampo']
        this.dado = request.form['tDado']
        this.msg = this.modelo.atualizar(this.codigo, this.campo, this.dado)
    return render_template('atualizar.html', titulo="Atualizar", dados=this.msg)

@pessoa.route('/excluir.html', methods=['GET','POST'])
def excluirDado():
    if request.method == 'POST':
        this.codigo = request.form['tCodigo']
        this.msg = this.modelo.excluir(this.codigo)
    return render_template('excluir.html', titulo="Excluir", dados=this.msg)


if __name__ == '__main__':
    pessoa.run(debug=True, port=5000)

