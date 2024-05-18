#Herança simples

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_roda = numero_rodas
    
    def ligar_motor(self):
        print("Ligando o motor...")

    def __str__(self):
        return self.cor
    

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, carregado, cor, placa, numero_rodas):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"sim" if self.carregado else "não estou carregado")

moto = Motocicleta("Azul", "Abc-1234", 2)
moto.ligar_motor()

carro = Carro("preto", "mbs-6547", 4)
carro.ligar_motor()

caminhao = Caminhao("Cinza", "lkj-9875", 8, False)
caminhao.ligar_motor()
print(moto)
print(carro)
print(caminhao)
