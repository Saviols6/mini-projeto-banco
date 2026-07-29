#Projeto orientado pela Data Science Academy
#Mini-Projeto 2 - Aplicação Full-Stack de Sistema Bancário em Python com POO


#define a Classe Cliente
class Cliente:

    #Método construtor que inicializa os atributos da classe
    def __init__(self, nome:str, cpf:str):

        #Atriubuto para armazenar o nome do Cliente
        self.nome = nome

        #Método para armazenar o cpf do cliente
        self.cpf = cpf 

        #Lista vazia para armazenar as contas associadas ao cliente
        self.contas = []


    #Método para adicionar uma conta à lista de contas do cliente
    def adicionar_conta(self,conta):

        #Insere o objeto na lista de contas
        self.contas.append(conta)

    #Método especial que define a representação em string do objeto
    def __str__(self):

        return f"Cliente:{self.nome} | CPF: {self.cpf}"