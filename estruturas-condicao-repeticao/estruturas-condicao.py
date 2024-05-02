MAIOR_IDADE = 18
IDADE_ESPECIAL = 12 
idade = int(input("informe sua idade? "))
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar sua CNH")
    print("Obrigado por utilizar o programa")
elif idade < 18:
    print("Você ainda não pode tirar sua CNH")
    print("Obrigado por usar o programa")
