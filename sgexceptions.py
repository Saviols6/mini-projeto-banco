#Projeto orientado pela Data Science Academy
#SG-Mini-Projeto2 Aplicação Full-Stack de sistema Bancário em Python com POO
#Módulo para exceções customizadas da aplicação 

#Define a exceção para saldo insuficiente em operações de saque
class SaldoInsuficienteError(Exception):
    #Exceção levantada quando uma operação de saque excede o saldo disponível.

    #Construir da exceção
    def __init__(self, saldo_atual,valor_saque,mensagem = "Saldo insuficiente para realizar o saque."):

        #Saldo atual da conta no número do erro
        self.saldo_atual = saldo_atual

        #Valor solicitado para saque
        self.valor_saque = valor_saque

        #Mensagem detalhada de erro com saldo atual e valor do saque
        self.mensagem = f"{mensagem} Saldo atual: R${saldo_atual:.2f},Tentativa de saque: R${valor_saque:.2f}"

        #Chama o cosntrutor da classe Exception com a mensagem
        super().__init__(self.mensagem)


#Define a exceção para operações em contas inexistentes
class ContaInexistenteError(Exception):

    #Exceção levantada ao tentar operar em uma conta que não existe.

    #construtor da exceção
    def __init__(self, numero_conta, mensagem = "A conta especificada não foi encontrada."):

        #Número da consta que não foi encontrada
        self._numero_conta = numero_conta

        #Mensagem detahada de erro com o numero da conta
        self.mensagem = f"{mensagem} Numero da conta: {numero_conta}"

        #chama o construtor da classe Exception com a mensagem
        super().__init__(self.mensagem)
        