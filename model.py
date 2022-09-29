import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()#Criei o vinculo com a classe conexão
        self.db_connection = self.db_connection.conectar()#Conecto ao banco de dados
        self.con = self.db_connection.cursor()#Navega no meu banco
        
#Cliente       

    def inserirFormulario(self, nome, apelido, sus, rg, cpf, dataDeNascimento, sexo, uf, nacionalidade, alfabetizado, escolaridade, etnia, religiao, endereco):
        try:
            sql = "Insert into cliente(cod, nome, apelido, sus, rg, cpf, dataDeNascimento, sexo, uf, nacionalidade, alfabetizado, escolaridade, etnia, religiao, endereco) values('','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(nome, apelido, sus, rg, cpf, dataDeNascimento, sexo, uf, nacionalidade, alfabetizado, escolaridade, etnia, religiao, endereco)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def consultarFormulario(self, cod):
        try:
            sql = "select * from cliente where cod ='{}'".format(cod)
            self.con.execute(sql)
            msg = ""
            
            for(nome, apelido, sus, rg, cpf, dataDeNascimento, sexo, uf, nacionalidade, alfabetizado, escolaridade, etnia, religiao, endereco) in self.con:
                msg = msg + "\nCódigo: {}, Nome: {}, Apelido: {}, NºSUS: {}, RG: {}, CPF: {}, Nascimento: {}, Sexo: {}, UF: {}, Nacionalidade: {}, Alfabetizado: {}, Escolaridade: {}, Etnia: {}, Religião: {}, Endereço: {}".format(nome, apelido, sus, rg, cpf, dataDeNascimento, sexo, uf, nacionalidade, alfabetizado, escolaridade, etnia, religiao, endereco)
            return msg
        except Exception as erro:
            return erro
        
    def atualizarFormulario(self, cod, campo, novoDado):
        try:
            sql = "update cliente set {} = '{}' where cod = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def excluirFormulario(self, cod):
        try:
            sql = "delete from cliente where cod = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(cod) 
        except Exception as erro:
            return erro
        
#Metodo Login Cliente

    def cad1(self, usu1, pswd1, email, cpf):
        try:
            sql = "Insert into cliente(cod, usu, pswd, email, cpf) values('','{}','{}','{}','{}')".format(usu1, pswd1, email, cpf)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def loginInsert1(self, usu1, pswd1, usu1Input, pswd1Input):
        try:
            sql = 'select * from cliente'
            self.con.execute(sql)
            for (cod, usu1, pswd1) in self.con:
                if usu1 and pswd1 == usu1Input and pswd1Input:
                    return True
            else:
                print('\nUsuário ou senha incorretos!')
            return False
        except Exception as erro:
            return erro

    def loginValid1(self, usu1, pswd1, usu1Input, pswd1Input):
        try:
            if self.loginInsert1(usu1, pswd1, usu1Input, pswd1Input) == True:
                print('Logado com Sucesso !')
                print('\n')
            else:
                print('Login e Senha incorretos!')
                print('\n')
        except Exception as erro:
            print(erro)
            
#Cuidador

    def cad(self, usu, pswd, email, cpf):
        try:
            sql = "Insert into cuidador(cod, usu, pswd, email, cpf) values('','{}','{}','{}','{}')".format(usu, pswd, email, cpf)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def loginInsert(self, usu, pswd, usuInput, pswdInput):
        try:
            sql = 'select * from cuidador'
            self.con.execute(sql)
            for (cod, usu, pswd) in self.con:
                if usu and pswd == usuInput and pswdInput:
                    return True
            else:
                print('\nUsuário ou senha incorretos!')
            return False
        except Exception as erro:
            return erro
        
    def loginValid(self, usu, pswd, usuInput, pswdInput):
        try:
            if self.loginInsert(usu, pswd, usuInput, pswdInput) == True:
                print('Logado com Sucesso !')
                print('\n')
            else:
                print('Login e Senha incorretos!')
                print('\n')
        except Exception as erro:
            print(erro)
            

    def tratarData(self, texto):
        separado = texto.split("/")
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano, mes, dia)