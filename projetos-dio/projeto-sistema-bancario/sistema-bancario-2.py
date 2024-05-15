
limite_saques = 500
numero_saques = 3
saldo = 0
extrato = " "
valor = 0
cont = 0
usuarios = []
contas = []
AGENCIA = "0001"
#lista_usuarios = []
while True:
    menu = int(input('''
        
        ----------SISTEMA-BANCÁRIO-V2----------
        
        DIGITE UMA DAS OPÇÕES ABAIXO PARA PROSSEGUIR
        [1] SAQUE
        [2] DEPOSITO
        [3] EXTRATO
        [4] NOVO USUÁRIO
        [5] NOVA CONTA
        [6] LISTAR CONTAS
        [7] SAIR
        
        '''))

    def saque(*, saldo, valor, extrato, numero_saques, limite_saques, cont):
        if valor <= 0:
            print("ALGO DEU ERRADO!")
            print("TENTE NOVAMENTE!")
        elif saldo <= 0:
            print("SALDO INSUFICIENTE PARA SAQUE!")
        elif numero_saques <= 0:
            print("VOCE EXCEDEU O NÚMERO DE SAQUES DIÁRIOS!")
        elif valor > limite_saques:
            print("VALOR EXCEDE O LIMITE DIÁRIO DE SAQUE!")
            print("TENTE NOVAMENTE!")
        elif valor <= limite_saques and valor <= saldo:
            saldo = saldo - valor
            numero_saques -= 1
            cont += 1
            extrato += f"SAQUE R$:{valor:.2f}\n"
            print("SAQUE REALIZADO COM SUCESSO!")
        return saldo, extrato, cont, numero_saques

    def deposito(saldo, valor, extrato, cont, /):
        if valor > 0:
            saldo += valor
            cont += 1
            extrato += f"DEPÓSITO: R${valor:.2f}\n"
            print("DEPOSITO REALIZADO COM SUCESSO!")
        else:
            print("ALGO DEU ERRADO! VALOR INVÁLIDO!")
        return saldo, extrato, cont

    def exibir_extrato(saldo, /, *, extrato, cont):
        if cont == 0:
            print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES")
        print("----------EXTRATO----------")
        print(f"SALDO: R$:{saldo:.2f}")
        print(f"Total de transações: {cont}")
        print(extrato,"\n")
        
        return saldo, extrato, cont

    def criar_usuario(usuarios):
        cpf = input("DIGITE SEU CPF: \n")
        usuario = lista_usuarios(cpf, usuarios)

        if usuario:
            print("CPF JÁ CADASTRADO!")
            return
        
        nome = input("DIGITE SEU NOME COMPLETO: \n".title())
        data_nascimento = input("DIGITE SUA DATA DE NASCIMENTO: \n")
        endereco = input("DIGITE SEU ENDEREÇO (LOGRADOURO,  NUMERO,  BAIRRO - CIDADE/SIGLA ESTRADO)\n")
        usuarios.append({"nome":nome, "data_nascimento": data_nascimento, "endereco": endereco}) 
        print("USUÁRIO CADASTRADO COM SUCESSO!")


    def lista_usuarios(cpf, usuarios):
        usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

    def criar_conta(agencia, numero_conta, usuarios):
        cpf = str(input("DIGITE SEU CPF: \n"))
        usuario = lista_usuarios(cpf, usuarios)

        if usuario:
            print("CONTA CRIADA COM SUCESSO!")
            return agencia, numero_conta, usuarios
        print("USUÁRIO NÃO ENCONTRADO!")

    def listar_contas(contas):
        for conta in contas:
            linha = f"""/
            Agência: {conta['agencia']}
            C/C: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
            """


    if menu ==1:
        print(f"""
            VOCÊ TEM {numero_saques} SAQUES DIÁRIOS
            COM LIMITE DE R$:{limite_saques} POR SAQUE
            """)
        valor = float(input("DIGITE UM VALOR PARA SAQUE:"))
        saldo, extrato, cont, numero_saques= saque(
            saldo=saldo, 
            valor=valor, 
            extrato=extrato, 
            numero_saques=numero_saques, 
            limite_saques=limite_saques,
            cont=cont,
        )
    elif menu == 2:
        valor = float(input("DIGITE UM VALOR PARA DEPOSITO: \n"))
        saldo, extrato, cont = deposito(saldo, valor, extrato, cont)

    elif menu == 3:
        saldo, extrato, cont = exibir_extrato(saldo, extrato=extrato, cont=cont)

    elif menu == 4:
        criar_usuario(usuarios)

    elif menu == 5:
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif menu == 6:
        listar_contas(contas)

    elif menu == 7:
        print("ENCERRANDO PROGRAMA...")
        break
    else:
        print("OPERAÇÃO INVÁLIDA!")
    
