class cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Iniciando a classe...")
        self.nome=nome
        self.cor=cor
        self.acordado=acordado
    
    def falar(self):
        print("AUAUAU")

    def __del__(self):
        print("Removendo classe;;")
    

def criar_cachorro():
    c = cachorro("Zeeus", "laranja", False)
    print(c.nome)

c = cachorro("Pitico", "Amarelinho")
c.falar()

del c

criar_cachorro()
