def principal():
    print("Executando função principal")

    def funcao_interna():
        print("Executando função interna")

    def funcao_2():
        print("Executando função interna 2")

    funcao_interna()
    funcao_2()
principal()
