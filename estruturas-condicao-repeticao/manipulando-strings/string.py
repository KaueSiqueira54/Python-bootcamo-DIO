nome = "kaue"
print(nome.upper()) #Todas as letras MAIUSCULAS
print(nome.lower()) #Todas as letras MINUSCULAS
print(nome.title()) #Apenas a primeira letra Maiuscula e o restante minusculo

texto = "  olá mundo!   "
print(texto + ".")
print(texto.strip() + ".") #Elimina espaços vazios
print(texto.lstrip() + ".") #Remover espaços da esquerda para a direita
print(texto.rstrip() + ".") #Remover espaços da direita para a esquerda

menu = "python"
print("####" + menu + "####")
print(menu.center(12, "$"))
print("-".join(menu))

