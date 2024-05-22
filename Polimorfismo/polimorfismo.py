class Passaro:
    def voar(self):
        print("Voando..")

class Pardal(Passaro):
    def voar(self):
        print("Pardal Voaa")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar")

#Exemplo não convencional para uso de herança para ganhar o método voar
class Avião(Passaro):
    def voar(self):
        print("Avião está indo para as nuvens..")

#voar seria o poliformismmo, pois se comporta de maneira diferente para cada "animal"
def plano_voo(obj):
    obj.voar()

plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Avião())
  
  