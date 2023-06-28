menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saque = 1
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":

        print("Fazer Depósito")
        valor = float(input("Informe o valor do Depósito:"))

        if valor > 0:
            saldo += valor
            extrato += f"D - R$ {valor:.2f}\n"
        
        else:
            print("Operação FALHOU, valor informado é inválido!")
    
    elif opcao == "s":
        
        print("Fazer Saque")
        valor = float(input("Informe o valor do saque:"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saque > LIMITE_SAQUE

        if excedeu_saldo:
            print("Saldo insuficiente")

        elif excedeu_limite:
            print("Limite por saque de R$500,00")

        elif excedeu_saques:
            print("Máximo de 3 saques por dia!")

        elif valor > 0:
            saldo -= valor
            extrato += f"S - R$ {valor:.2f}\n"
            numero_saque += 1

    
    elif opcao == "e":
        print("EXTRATO")
        print(extrato)
        print(f"Saldo - R$ {saldo}")
    
    elif opcao == "q":
        print("Obrigado por usar nossos serviços!")
        break

    else:
        print("Operação Inválida! Digite uma opção válida!")