import mysql.connector
from conexao import conexao

class model:
    def __init__(self):
        self.db_connection = conexao()#Criei o vinculo com a classe conexão
        self.db_connection = self.db_connection.conectar()#Conecto ao banco de dados
        self.con = self.db_connection.cursor()#Navega no meu banco
        
    def inserir(self, nome, apelido, telefone, endereco, dataDeNascimento):
        try:
            sql = "Insert into person(codigo, nome, apelido, telefone, endereco, dataDeNascimento) values('','{}','{}','{}','{}')".format(nome, telefone, endereco, dataDeNascimento)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def consultar(self, cod):
        try:
            sql = "select * from person where codigo ='{}'".format(codigo)
            self.con.execute(sql)
            msg = ""
            
            for(cod, nome, telefone, endereco, dataDeNascimento) in self.con:
                msg = msg + "\nCódigo: {}, Nome: {}, Telefone: {}, Endereço: {}, Nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
            return msg
        except Exception as erro:
            return erro
        
    def atualizar(self, cod, campo, novoDado):
        try:
            sql = "update person set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha atualizada!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def excluir(self, cod):
        try:
            sql = "delete from person where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha excluida!".format(cod) 
        except Exception as erro:
            return erro

    def cad(self, user, pswd, email, cpf):
        try:
            sql = "Insert into cuidador(codigo, user, pswd, email, cpf) values('','{}','{}','{}','{}')".format(user, pswd, email, cpf)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} Inserido!".format(self.con.rowcount)
        except Exception as erro:
            return erro
        
    def loginInsert(self,user, pswd, userInput, pswdInput):
        try:
            sql = 'select * from login'
            self.con.execute(sql)
            for (codigo, user, pswd) in con:
                if user and pswd == userInput and pswdInput:
                    return True
            else:
                print('\nUsuário ou senha incorretos!')
            return False
        except Exception as erro:
            return erro
    def loginValid(user, pswd, userInput, pswdInput):
        try:
            if loginInsert(user, pswd, userInput, pswdInput) == True:
                print('Logado com Sucesso !')
                print('\n')
                menu.operacao()
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