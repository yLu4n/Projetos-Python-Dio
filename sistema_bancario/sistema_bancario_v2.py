import textwrap

def menu():
    menu = """\n
    ============ MENU ============
    [1]\tDepósito
    [2]\tSaque
    [3]\tExtrato
    [4]\tCriar Nova Conta
    [5]\tListar Contas
    [6]\tCadastrar Usúario
    [4]\tSair
    -> """
    return input(textwrap.dedent(menu))

def saque(*, saldo, valor, extrato, limite, numero_saques, limites_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Não possui saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limte. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Limite máximo de saques excedido. @@@")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n|||| Operação realizada com sucesso! |||")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato

def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n================== EXTRATO ==================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("================================================")

def localizar_usuario(cpf, usuarios):
    usuarios_localizados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_localizados[0] if usuarios_localizados else None


def cadastrar_usuario(usuarios):
    cpf = input("Informe o seu CPF (Sem . ou -): ")
    usuario = localizar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Este CPF já está cadastrado! @@@")
        return 
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (CEP, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario cadastrado com sucesso")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = localizar_usuario(cpf, usuario)
    
    if usuario:
        print("\n|||| Conta criada com sucesso! ||||")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n@@@ Usuário Não encontrado, criação de conta encerrada! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():