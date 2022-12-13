# Sistema bancário com 3 operações: Depósito, Saque e extrato
# Todos os depósitos deve ser armazenados em uma variável e ser exibido na operação de extrato
# 3 saques diários com limite de R$500 cada
# Se n houver saldo, exibir mensagem
# Todos os saques deve ser armazenados em uma variável e ser exibido na operação de extrato

print("Opções")
menu = """
==================================
[d] Depositar
[s] Sacar
[e] Extrato
[q] sair
==================================
Escolha a opção desejada
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    # Operação de Depósito
    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("O valor informado é inválido.")

    # Operação de Saque
    elif opcao == "s":
        valor = float(input("Digite o valor de saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou, você não tem saldo suficiente!")

        elif excedeu_limite:
            print("Operação falhou, você excedeu limite de saque!")

        elif excedeu_saques:
            print("Operação falhou, você excedeu limite de saque diário")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou, o número informado é inválido!")

    # Operação de Extrato
    elif opcao == "e":
        print("\n ================ EXTRATO ==================")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n ===========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor, selecione a operação desejada")
