menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
[r] Registar Usuario

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
Usuarios = []
numero_usuario = []
Id = 0
Contas = []

# Registar usuario
def registar():
    global Usuarios
    global Id
    global numero_usuario
    nome_usuario = str(input("Insira o nome: "))
    data_nascimento = str(input("Insira a data de nascimento do usuario: "))
    cpf_usuario = str(input("Insira o CPF: "))
    endereco = {}
    logradouro = str(input("Logradouro: "))
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    endereco.update({'Logradouro': logradouro, 'Bairro': bairro, 'Cidade': cidade, 'Estado': estado})
    Usuarios.append({Id: {'Nome': nome_usuario, 'Data de nascimento': data_nascimento, 'CPF': cpf_usuario, 'Endereco': endereco}})
    numero_usuario.append(Id)
    Id += 1

# Criar conta corrente
def criar_conta():
    global Contas
    global Usuarios
    conta = 0
    usuario = int(input("Insira Id do cliente: "))
    conta += 1
    nome_conta = f"Conta N{conta}"
    Contas.append(conta)
    for i in Usuarios:
         for 


# Saque
def saque(valor):
                global saldo
                saldo -= valor
                global extrato
                extrato += f"Saque: R$ {valor:.2f}\n"
                global numero_saquesj
                numero_saques += 1

# Deposito
def deposito(valor):
                global saldo
                saldo += valor
                global extrato
                extrato += f"Depósito: R$ {valor:.2f}\n"

# Extrato
def extrato_(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0 and valor < limite:
            deposito(valor)
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif saldo > 0:
             saque(valor= valor)

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        
        extrato_(saldo, extrato)

    elif opcao == "q":
        break

    elif opcao == "r":
        registar()

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")