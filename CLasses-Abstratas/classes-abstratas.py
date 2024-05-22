from abc import ABC, abstractmethod, abstractproperty
class ControleRemoto(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        return "LG"

class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando..")
        print("TV ligada.")

    @property
    def marca(self):
        return "LG"


    def desligar(self):
        print("Desligando..")
        print("TV desligada.")

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar..")
        print("Ar ligado")
    def desligar(self):
        print("Desligando..")
        print("Ar Desligado")

    @property
    def marca(self):
        return "Samsumg"
    




controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

