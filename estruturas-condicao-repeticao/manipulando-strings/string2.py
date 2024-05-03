nome = "Kaue"
idade = 18
profissao = "Programador"
linguagem = "Python"
saldo = 45.456
dados = {"nome": "kaue", "idade": 28, "saldo": 45.456}

print("Nome: %s Idade: %d" % (nome, idade))
print("nome: {} Idade: {}".format(nome, idade))
print(f"Nome {nome} Idade {idade}")
print("Nome: {1} Idade: {0}".format(idade, nome))
print("nome: {nome} Idade: {idade} {idade} {nome}".format(idade=idade, nome=nome))
print("nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome {nome} Idade{idade} saldo: {saldo:.2f}")

nome = """Kaue Siqueira Dantas
lkaslksakadkjdaljaljdkjdlakjld,
sllkdlskdl
"""

print(nome[:])
print(nome[0:4])
print(nome[5:])
print(nome[5:13])
print(nome[14:20])
print(nome[::-1])
print(nome[::2])