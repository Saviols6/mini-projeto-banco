#Projeto orientado pela Data Science Academy
#SG-Mini-Projeto2 - Aplicação Full-Stack de Sistema Bancário em Python com POO
#Módulo principal da Aplicação

from sgoperacoes.banco import Banco

from sgutilitarios.sgexceptions import SaldoInsuficienteError,ContaInexistenteError

#função que exibe o menu principal da aplicação
def menu_principal():

    print("\n--- SG Mini-Projeto 2 - Sistema Bancário Digital ---\n")
    print("1. Adicionar Cliente")
    print("2. Criar Conta")
    print("3. Acessar Conta")
    print("4. Sair\n")
  #Retorna a opção digitada pelo usuário
    return input("Escolha uma opção:")

#Função que exibe o menu de operações de uma conta específica
def menu_conta(banco):
    try:
        #solicita ao usário o numero da conta
        num_conta = int(input("Digite o número da conta: "))

        #busca a conta no banco; pode gerar exceção se não existir
        conta = banco.buscar_conta(num_conta)

        #loop de operações dentro da conta
        while True:
            print(f"\n--- Operações para Conta Nº {conta._numero} ---")
            print(f"Cliente: {conta._cliente.nome} | Saldo: R${conta.saldo:.2f}")
            print("1. Depositar")
            print("2. Sacar")
            print("3. Ver Extrato")
            print("4. Voltar ao Menu Principal")

            #Lê a opção do usuário
            opcao = input("Escolha uma opção:")

            if opcao == '1':
                valor = float(input("Digite o valor para o depósito:"))
                conta.depositar(valor)

            elif opcao == '2':
                try:
                    valor = float(input("Digite um valor para saque: "))
                    conta.sacar(valor)

                except SaldoInsuficienteError as e:
                    print(f"Erro na operação {e}")

            elif opcao == '3':
                conta.extrato()

            elif opcao == '4':
                break
            else:
                print("Opção inválida. Tente novamente.")

    except ContaInexistenteError as e:
        print(f"Erro:{e}")


    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número.")

def main():
    # Cria o objeto Banco
        banco = Banco("Banco Digital SG")
    
        # Loop principal do sistema
        while True:
    
            opcao = menu_principal()
    
            if opcao == '1':
                
                # Adiciona um novo cliente
                nome = input("Digite o nome do cliente: ")
                cpf = input("Digite o CPF do cliente: ")
                banco.adicionar_cliente(nome, cpf)
            
            elif opcao == '2':
                
                # Cria uma nova conta vinculada a um cliente existente
                cpf = input("Digite o CPF do cliente para vincular a conta: ")
                cliente = banco._clientes.get(cpf)
                
                if cliente:
    
                    tipo = input("Digite o tipo da conta (corrente/poupanca): ")
                    banco.criar_conta(cliente, tipo)
                
                else:
                    print("Cliente não encontrado. Cadastre o cliente primeiro.")
    
            elif opcao == '3':
    
                # Abre o menu de operações de uma conta
                menu_conta(banco)
                
            elif opcao == '4':
    
                # Encerra o programa
                print("\nObrigado por usar o nosso sistema. Até logo!\n")
                break
            
            else:
    
                print("\nOpção inválida. Por favor, tente novamente.\n")
    
    # Ponto de entrada da aplicação
if __name__ == "__main__":
    main()
    