nomes = []
saldos = []

def criar_conta(nome, saldo=0):
    nomes.append(nome)
    saldos.append(saldo)

def depositar(indice, valor):
    saldos[indice] = saldos[indice] + valor
    print(f"Depósito de R${valor} realizado com sucesso.")

def sacar(indice, valor):
    if saldos[indice] >= valor:
        saldos[indice] = saldos[indice] - valor
        print(f"Saque de R${valor} realizado com sucesso.")
    else:
        print("Saldo insuficiente.")

def consultar_saldo(indice):
    print(f"O saldo da conta de {nomes[indice]} é R${saldos[indice]}.")

while True:
    nome = input("Digite o nome do titular da conta: ")
    saldo = float(input("Digite o saldo inicial: "))
    
    criar_conta(nome, saldo)

    while True:
        print("\nEscolha uma operação:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Saldo")
        print("4 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        indice = nomes.index(nome)

        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            depositar(indice, valor)
            consultar_saldo(indice)
        elif opcao == 2:
            consultar_saldo(indice)
            valor = float(input("Digite o valor do saque: "))
            sacar(indice, valor)
            consultar_saldo(indice)
        elif opcao == 3:
            consultar_saldo(indice)
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")


    print("\nDeseja criar outra conta? (s/n)")
    resposta = input().lower()
    if resposta != 's':
        break