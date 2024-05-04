from time import sleep

cont = 0
total_deposito = 0
deposito = 0
saque = 3
limite_saque = 1500
extrato = ""
valor_depositado = 0
valor_sacado = 0
total_sacado = 0

while True: 
    menu = int(input(print(
    ''' #####SISTEMA-BANCÁRIO-V1#####

    DIGITE UMA DAS OPÇÕES ABAIXO PARA PROSSEGUIR:
    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [4] SAIR
    '''
    )))

    if menu == 1:
        while True:
            valor_depositado = float(input(print("DIGITE O VALOR A SER DEPOSITADO: ")))
            validar = int(input(f"""
                O VALOR A SER DEPOSITADO É R${valor_depositado:.2f} DESEJA CONFIRMAR?
                [1] CONFIRMAR
                [2] CANCELAR
                [3] DIGITAR OUTRO VALOR
            """))
            if validar == 1:
                #valor_depositado += valor_depositado
                total_deposito += valor_depositado
                cont = cont + 1
                print("DEPOSITO REALIZADO COM SUCESSO!")
                break
            elif validar == 2:
                print("OPERAÇÃO CANCELADA PELO USUÁRIO!")
                break
            else:
                print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE")
    elif menu == 2:
        while True:
            valor_sacado = float(input("""
            VOCÊ PODERÁ REALIZAR ATÉ {} SAQUES DIÁRIOS
                COM LIMITE DE R$500 POR SAQUE.
                DIGITE O VALOR A SER SACADO: 
            """.format(saque)))
            validar = int(input("""
                O VALOR A SER SACADO É {}
                DESEJA CONFIRMAR?
                [1] CONFIRMAR
                [2] DIGITAR OUTRO VALOR
                [3] CANCELAR
            """.format(valor_sacado)))
            if validar == 1:
                if valor_sacado <= limite_saque:
                    if saque > 0:
                        cont = cont + 1
                        saque = saque - 1
                        limite_saque = limite_saque - valor_sacado
                        total_sacado = total_sacado + valor_sacado
                        print("VALOR SACADO COM SUCESSO!")
                        print("VOCÊ TEM {} SAQUES DIÁRIOS".format(saque))
                        break
                elif saque <= 0:
                    print("VOCÊ EXCEDEU O NÚMERO DE SAQUES DIÁRIOS!")
                    break
                elif valor_sacado > limite_saque:
                    print("O VALOR A SER SACADO EXCEDE O SEU LIMITE DE SAQUE!")
                    break
            elif validar == 3:
                print("OPERAÇÃO CANCELADA PELO USUÁRIO!")
                break
            elif validar != 1 and 3:
                print("OPÇÃO INVÁLIDA!")
    elif menu ==3: 
        if cont > 1:          
            print(f"valor sacado: {total_sacado}")
            print(f"Valor depositado: {total_deposito}")


            


