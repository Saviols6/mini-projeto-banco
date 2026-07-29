#Projeo orientado pela Data Science Academy
#SG-Mini-Projeto2 - Aplicação Full-Stack de Sistema Bancário em Pyhton com POO

#importa a classe Cliente
from sgentidades.sgcliente import Cliente

#Importa a classe base Conta e suas subclasses (Corrente e Poupança)
from sgentidades.sgconta import Conta, ContaCorrente, ContaPoupanca

#Importa exceção personalizada para conta inexistente
from sgutilitarios.sgexceptions import ContaInexistenteError


#Define a classe Banco
class Banco:
    #Classe que gerencia as operações do banco.
    #Demonsra Composição, pois "tem" clientes e conta

    #Construtor da classe Banco
    def __init__(self, nome:str):

        #Nome do banco
        self.nome = nome

        #Dicionário de clientes (chave: CPF, valor: objeto Conta)
        self._clientes = {}

        #Dicionário de contas (chave: Número da conta, valor: objeto Cliente)
        self._conta = {}

    def adicionar_cliente(self,nome: str, cpf: str)->Cliente:
        #Cria e adiciona um novo cliente ao banco

        #Verifica se já existe cliente com o mesmo CPF
        if cpf in self._clientes:
            print("Erro: Cliente com este CPF já cadastrado.")
            return self._clientes[cpf]

        #Cria novo objeto Cliente e adiciona ao dicionário
        novo_cliente = Cliente(nome, cpf)
        self._clientes[cpf] = novo_cliente

        print(f"Cliente {nome} adicionado com sucesso!")

        return novo_cliente


    #Método para criar uma conta para uma conta para um cliente
    def criar_conta(self, cliente: Cliente, tipo:str)->Conta:
        #Cria uma nova conta para um cliente existente

        #Número da nova conta será baseado no total de contas +1
        numero_conta = Conta.get_total_contas() + 1

        #Cria conta corrente se o tipo informado for "corrente"
        if tipo.lower() == 'corrente':
            nova_conta = ContaCorrente(numero_conta,cliente)
        elif tipo.lower() == 'poupanca':
            nova_conta = ContaPoupanca(numero_conta, cliente)

        else:
            print("Tipo de conta inválido. Escolha 'corrente' ou 'Poupanca'.")
            return None

        #Adiciona a conta ao dicionário ao cliente
        self._conta[numero_conta] = nova_conta

        #Associa a conta ao cliente
        cliente.adicionar_conta(nova_conta)
        print(f"Conta{tipo} n⁰ {numero_conta} criada para o cliente {cliente.nome}")

        return nova_conta


    #Método para buscar uma conta pelo número
    def buscar_conta(self,numero_conta: int)->Conta:

        #Busca uma conta pelo seu numero.

        #Tenta recuperar a conta do dicionario
        conta = self._conta.get(numero_conta)

        #Se não encontrar, lança exceção personalizada
        if not conta:
            raise ContaInexistenteError(numero_conta)
        return conta