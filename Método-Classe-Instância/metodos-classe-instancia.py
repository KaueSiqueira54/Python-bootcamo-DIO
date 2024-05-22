class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    #Método de classe / método da classe Pessoa
    @classmethod
    def criar_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
    

#p = Pessoa("Kaue", 19)
#print(p.nome, p.idade)

#Utilizando método de classe
p2 = Pessoa.criar_data_nascimento(2004, 9, 21, "Kaue")
print(p2.nome, p2.idade)

#Chamando método estático
print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(20))
 
