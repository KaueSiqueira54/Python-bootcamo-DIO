from time import sleep

cont = 0
cont_saque = 0
total_deposito = 0
deposito = 0
saque = 3
limite_saque = 1500
extrato = ""
valor_depositado = 0
valor_sacado = 0
total_sacado = 0
saldo = valor_depositado - valor_sacado

while True: 
    menu = int(input(print(

    ''' ---------SISTEMA-BANCÁRIO-V1---------

    DIGITE UMA DAS OPÇÕES ABAIXO PARA PROSSEGUIR:
    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [4] SAIR
    '''
    )))
    sleep(0.5)

    if menu == 1:
        while True:
            valor_depositado = float(input(print("DIGITE O VALOR A SER DEPOSITADO: ")))
            sleep(0.5)
            if valor_depositado <= 0:
                print("VALOR INVÁLIDO! TENTE DIGITAR OUTRO VALOR!")
                break
                sleep(0.5)
            else: 
                validar = int(input(f"""
                    O VALOR A SER DEPOSITADO É R${valor_depositado:.2f} DESEJA CONFIRMAR?
                    [1] CONFIRMAR
                    [2] CANCELAR
                    [3] DIGITAR OUTRO VALOR
                """))
                sleep(0.5)
                if validar == 1:
                    saldo = saldo + valor_depositado
                    total_deposito += valor_depositado
                    cont = cont + 1
                    deposito = deposito + 1
                    extrato += f"DEPOSITO: R${valor_depositado:.2f}\n"
                    print("DEPOSITO REALIZADO COM SUCESSO!")
                    sleep(0.5)
                    break
                elif validar == 2:
                    print("OPERAÇÃO CANCELADA PELO USUÁRIO!")
                    sleep(0.5)
                    break
                elif validar == 3:
                    print("TENTE DIGITAR NOVAMENTE!")
                    sleep(0.5)
                else:
                    print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE")
                    sleep(0.5)
    elif menu == 2:
        while True:
            valor_sacado = float(input("""
            VOCÊ PODERÁ REALIZAR ATÉ {} SAQUES DIÁRIOS
                COM LIMITE DE R$500 POR SAQUE.
                DIGITE O VALOR A SER SACADO: 
            """.format(saque)))
            sleep(0.5)
            if valor_sacado > valor_depositado or saldo < valor_sacado:
                print("SALDO INSUFICIENTE NA CONTA!")
                break
            else:
                validar = int(input("""
                    O VALOR A SER SACADO É {}
                    DESEJA CONFIRMAR?
                    [1] CONFIRMAR
                    [2] DIGITAR OUTRO VALOR
                    [3] CANCELAR
                """.format(valor_sacado)))
                sleep(0.5)
                if validar == 1:
                    if valor_sacado <= limite_saque:
                        if saque > 0 and valor_sacado <= 500:
                            cont = cont + 1
                            cont_saque = cont_saque + 1
                            saque = saque - 1
                            limite_saque = limite_saque - valor_sacado
                            total_sacado = total_sacado + valor_sacado
                            saldo = saldo - valor_sacado
                            extrato += f"SAQUE: R${valor_sacado:.2f}\n"
                            print("VALOR SACADO COM SUCESSO!")
                            print("VOCÊ TEM {} SAQUES DIÁRIOS".format(saque))
                            sleep(0.5)
                            break
                    elif saque <= 0:
                        print("VOCÊ EXCEDEU O NÚMERO DE SAQUES DIÁRIOS!")
                        sleep(0.5)
                        break
                    elif valor_sacado > limite_saque:
                        print("O VALOR A SER SACADO EXCEDE O SEU LIMITE DE SAQUE!")
                        sleep(0.5)
                        break
                elif validar == 3:
                    print("OPERAÇÃO CANCELADA PELO USUÁRIO!")
                    sleep(0.5)
                    break
                elif validar != 1 and 3:
                    print("TENTE NOVAMENTE!")
                    sleep(0.5)
    elif menu ==3:
        if cont == 0:
            print('NÃO FORAM REALIZADAS MOVIMENTAÇÕES!')
            print(f"SALDO: R$:{saldo:.2f}")
            sleep(0.5)
        else:
            print("------EXTRATO DE TRANSAÇÕES------")
            print(f"TOTAL DE TRANSAÇÕES FEITAS: {cont}")
            print(f"SALDO ATUAL DA CONTA: {saldo}")
            print("EXTRATO:")
            print(f"{extrato}")
            print("--------DEPOSITOS--------")
            print(f"TOTAL DE TRANSAÇÕES: {deposito}")
            print(f"VALOR DEPOSITADO: R${total_deposito:.2f}")
            print("---------SAQUES---------")
            print(f"TOTAL DE TRANSAÇÕES: {cont_saque}")
            print(f"VALOR SACADO: R${total_sacado:.2f}")
            sleep(0.5)
    elif menu == 4:
        sleep(0.5)
        print("OBRIGADO POR UTILIZAR O NOSSO PROGRAMA!")
        sleep(0.8)
        print("ENCERRANDO PROGRAMA...")
        sleep(0.10)
        break
    else:
        print("OPERAÇÃO INVÁLIDA!")
        sleep(0.8)
        print("TENTE NOVAMENTE!")
        sleep(0.8)
