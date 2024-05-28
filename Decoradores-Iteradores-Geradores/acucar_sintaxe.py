def meu_decorador(funcao):
    def envelope():
        print("Faz algo antes de executar")
        funcao()
        print("Faz algo depois da função")


    return envelope

#chamando função decoradora
#açucar sintático
@meu_decorador
def ola_mundo():
    print("Olá Mundo!")
    
ola_mundo()

