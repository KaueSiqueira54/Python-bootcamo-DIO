arquivo = open("manipulando_arquivos\lorem.txt", "r")
#Mostra todo o arquivo
print(arquivo.read())

#mostra somente a primeira linha
print(arquivo.readline())

#Mostra todas as linhas em uma lista
print(arquivo.readlines())

#flip dica para ler usando readline linha a linha
#while len(linha := arquivo.readline()):
 #   print(linha)
arquivo.close()