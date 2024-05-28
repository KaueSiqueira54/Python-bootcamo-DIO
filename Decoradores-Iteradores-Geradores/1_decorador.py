def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar")
        funcao()
        print("Faz algo depois da função")


    return envelope

def ola_mundo():
    print("Olá Mundo!")
    
ola_mundo = meu_decorador(ola_mundo)
ola_mundo()

