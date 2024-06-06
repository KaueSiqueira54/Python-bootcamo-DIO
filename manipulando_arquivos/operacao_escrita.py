arquivo = open("manipulando_arquivos/teste.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n","Escrevendo", "\n", "Um", "\n", "texto"])
arquivo.close()