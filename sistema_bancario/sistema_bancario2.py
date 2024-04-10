menu = """
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

-> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    op = input(menu)

    match op:
        case "1":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"
            else:
                print("Operação falhou! O valor informado é inválido.")
        case "2":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Não possui saldo suficiente.")
            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limte.")
            elif excedeu_saques:
                print("Operação falhou! Limite máximo de saques excedido.")
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1
            else:
                print("Operação falhou! O valor informado é inválido.")
        case "3":
            if extrato == "":
                print("\n================== EXTRATO ==================")
                print("Não foram realizadas movimentações." )
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("================================================")
            else:
                print("\n================== EXTRATO ==================")
                print(extrato)
                print(f"\nSaldo: R$ {saldo:.2f}")
                print("================================================")