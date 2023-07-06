import textwrap

def menu():
    menu = """
    __________MENU__________

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [n]\tNova Conta
    [l]\tListar Consta
    [u]\tNovo Usuário
    [q]\tSair
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"D - R$ {valor:.2f}\n"
        print("\n=== Depósito Realizado Com SUCESSO! ===")
        
    else:
        print("\n@@@ Operação FALHOU, valor informado é inválido! @@@")

    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite_diario, numero_saques, limite_saques):
    print("Fazer Saque")

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_diario
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Saldo insuficiente @@@")

    elif excedeu_limite:
        print("\n@@@ Limite por saque de R$500,00 @@@")

    elif excedeu_saques:
        print("\n@@@ Máximo de 3 saques por dia! @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"S - \t\tR$ {valor:.2f}\n"
        numero_saque += 1
        print("\n=== Saque Realizado Com SUCESSO! ===")
    
    else:
        print("\n@@@ Operação FALHOU, valor informado é inválido! @@@")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("==========EXTRATO==========")
    print("Não foram realizadas Movimentações" if not extrato else extrato)
    print(f"Saldo - \t\tR$ {saldo}")
    print("===========================")

def criar_usuarios(usuarios): ...

def filtrar_usuarios(cpf, usuarios):...

def criar_conta(agencia, numero_conta, usuarios):...

def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            titular:\t{conta['usuario']['nome']}
        """
        print("=" *100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite_diario = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":

            print("Fazer Depósito")
            valor = float(input("Informe o valor do Depósito:"))

            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            
            print("Fazer Saque")
            valor = float(input("Informe o valor do saque:"))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite_diario=limite_diario,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
        
        elif opcao == "e":
            print("EXTRATO")
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "u":
            print("NOVO USUÁRIO")
            criar_usuarios(usuarios)

        elif opcao == "n":
            print("NOVA CONTA")
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "l":
            print("LISTAR CONTAS")
            listar_contas(contas)
        
        elif opcao == "q":
            print("Obrigado por usar nossos serviços!")
            break

        else:
            print("Operação Inválida! Digite uma opção válida!")
    
main()