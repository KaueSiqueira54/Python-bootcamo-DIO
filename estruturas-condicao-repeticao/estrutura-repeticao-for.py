texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
    else:
        print() #adiciona uma quebra de linha
        print("Executado ao final do laço\n")

for numero in range(0, 71, 7):
    print(numero, end=" ")
