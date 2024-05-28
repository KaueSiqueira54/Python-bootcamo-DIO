
#quando o código for mais simples, utilizar geradores, ex: controle de fluxo
#quando for mais complexo, utilizar iteradores

def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)
