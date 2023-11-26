menu = """
[1] depositar
[2] sacar
[3] extrato
[4] sair
=>
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    # DEPOSITO:
    entrada = int(input(menu))
    if entrada == 1:
        ent1 = int(input("digite o valor a ser depositado: "))
        if ent1 <= 0:
            print("permitido apenas valores positivos!")
        else:
            saldo += ent1
            extrato += f"[+] deposito identificado no valor de: R$ {ent1}, \n"
            print(f"saldo atual: R$", "%.2f" % saldo)

    # SAQUE:
    elif entrada == 2:
        ent2 = int(input("digite o valor a ser sacado: "))
        while numero_saques <= LIMITE_SAQUES:

            if ent2 > limite:
                print("o limite maximo é apenas R$ 500.00 por saque!")
                break

            elif ent2 <= 0:
                print("apenas valores positivos sao permitidos!")
                break

            elif ent2 > saldo:
                print("voce nao tem saldo o suficiente para sacar essa quantia!")
                print(f"saldo atual:", "%.2f" % saldo)
                break

            elif numero_saques == LIMITE_SAQUES:
                print("voce atingiu o limite de 3 saques diarios")
                break

            else:
                saldo -= ent2
                extrato += f"[-] saque identificado no valor de: R$ {ent2}\n"
                print(f"saldo atual: R$", "%.2f" % saldo)
                numero_saques += 1
                break

    # EXTRATO:
    elif entrada == 3:
        print("abaixo uma listagem dos ultimos extratos da conta:")
        print(extrato)

    # SAIR:
    elif entrada == 4:
        print("saindo do sistema bancario, ate mais!")
        break

    # OPÇAO INVALIDA:
    else:
        print("entrada invalida, tente novamente!")
