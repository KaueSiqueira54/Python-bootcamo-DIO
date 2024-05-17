class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self. ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("BIBIIIIIII")

    def parar(self):
        print("Parando biciclete")
        print("Parooou, bicicleta parada")

    def correr(self):
        print("ZOOOOOOOOOOM")
    
    def trocar_marcha(self):
        print("Marcha alterada")

    def get_cor(self):
        return self.cor
    
    #def __str__(self):
        #return f"Bicicleta: {self.cor, self.modelo, self.ano, self.valor}"
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f"{chave}={valor}" for chave, valor in self.__dict__.items()])}"

b2 = Bicicleta("Verde", "monark", 2000, 120)
Bicicleta.buzinar(b2)
print(b2.get_cor())

print(b2)
b2.trocar_marcha()
