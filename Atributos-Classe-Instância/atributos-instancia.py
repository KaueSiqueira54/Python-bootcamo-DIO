class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Kaue", 1)
aluno_2 = Estudante("Gustavo", 2)
aluno_3 = Estudante("Irineu", 5)

mostrar_valores(aluno_1)
mostrar_valores(aluno_2)
mostrar_valores(aluno_3)

Estudante.escola = "Python"
aluno_1.matricula = 3

mostrar_valores(aluno_1)
mostrar_valores(aluno_2)
mostrar_valores(aluno_3)
